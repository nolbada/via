/* attfs 261117a — 출석부 저장소(Firebase 직통). 예전 출석 서버(Apps Script)의 동작을 그대로 옮긴 것.
   문서: <col>/ros (명단), <col>/mk (결석·보강), <col>/v (변경 번호 + 처리한 작업 id), <col>/d_<날짜> (그날 기록)
   각 문서는 j(JSON 문자열) 한 칸. 쓰기는 "읽은 뒤 안 바뀌었을 때만" 조건으로 묶어서 한 번에 한다. */
(function(root){
'use strict';
var TZ='Asia/Seoul';
var MK_SLOTS=['불참','11시','11시30분','12시','12시30분','1시','1시30분','2시','2시30분','3시','3시30분','4시','4시30분','5시','5시30분','6시','6시30분','7시','7시30분'];
var MK_KINDS=['보강기회X','보강/보충 완료','보강연기','보충-결석'];
var MK_AMOUNTS=['30분','1시간','1시간30분','2시간'];
var MK_REASONS=['결석 보충','숙제 70% 미만','학습 미완료','병결','무단','여행/휴가','개인','미완료','학교 행사','부모님연락','보충','가족행사'];
var SEEN_MAX=400;

function hhmm(ms){
  var p=new Intl.DateTimeFormat('en-GB',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date(Number(ms))),h='',m='';
  p.forEach(function(x){if(x.type==='hour')h=x.value;if(x.type==='minute')m=x.value;});
  if(h==='24')h='00';
  return h+':'+m;
}
function chkDate(v){ if(!v) return ''; if(!/^\d{4}-\d{2}-\d{2}$/.test(v)) throw new Error('날짜 형식 오류: '+v); return v; }
function clone(o){ return JSON.parse(JSON.stringify(o)); }

/* ---- 순수 계산부: W = {ros:[], mk:{next,list:[]}, v:{n,seen:[]}, days:{date:{ 'group|name': row }}} ---- */
function dayOf(W,date){ if(!W.days[date]) W.days[date]={}; return W.days[date]; }
function rowFor(W,date,group,name){
  var d=dayOf(W,date),k=group+'|'+name;
  if(!d[k]) d[k]={arrive:'',teacher:'',leave:'',status:'',memo:'',a0:'',l0:'',updated:Date.now()};
  return d[k];
}
function apply(W,date,group,op){
  if(op.op==='add_student'){ W.ros.push({name:op.name,group:group,grade:op.grade||'',active:'Y'}); return; }
  if(op.op==='remove_student'){ W.ros.forEach(function(r){ if(r.name===op.name&&r.group===group) r.active='N'; }); return; }
  if(op.op==='clear_day'){ var d=dayOf(W,date); Object.keys(d).forEach(function(k){ if(k.indexOf(group+'|')===0) delete d[k]; }); return; }
  var cur=rowFor(W,date,group,op.name), v=clone(cur);
  var t=Number(op.t)||Date.now();
  if(op.op==='arrive'){ if(!v.arrive) v.arrive=t; if(v.status!=='left') v.status='in'; }
  else if(op.op==='assign'){ if(!v.arrive) v.arrive=t; v.teacher=op.teacher; if(v.status!=='left') v.status='in'; }
  else if(op.op==='leave'){ if(!v.arrive) v.arrive=t; v.leave=t; v.status='left'; }
  else if(op.op==='absent'){ v.status='absent'; }
  else if(op.op==='back'){
    if(v.status==='left'){ v.leave=''; v.status='in'; }
    else if(v.teacher){ v.teacher=''; }
    else { v.arrive=''; v.status=''; }
  }
  else if(op.op==='edit'){
    if(op.field==='arrive'){ if(!v.a0) v.a0=v.arrive; v.arrive=t; }
    else if(op.field==='leave'){ if(!v.l0) v.l0=v.leave; v.leave=t; }
  }
  else if(op.op==='memo'){ v.memo=op.v||''; }
  if(v.arrive&&v.leave&&Number(v.leave)<Number(v.arrive)) throw new Error('귀가 시각이 등원 시각보다 빠릅니다: '+op.name);
  v.updated=Date.now();
  dayOf(W,date)[group+'|'+op.name]=v;
}
function mkSync(W,date){
  var rows=W.mk.list.filter(function(x){return x.date===date;});
  if(!rows.length) return;
  var d=W.days[date]||{},st={};
  Object.keys(d).forEach(function(k){
    var name=k.slice(k.indexOf('|')+1),s=d[k].status,a=d[k].arrive,cur=st[name];
    if(!cur||s==='in'||s==='left') st[name]={status:s,arrive:a};
  });
  rows.forEach(function(x){
    var r=st[x.name];
    if(r&&(r.status==='in'||r.status==='left')){
      if(!x.done){ x.done=true; x.arr=r.arrive?hhmm(r.arrive):''; }
    } else if(r&&r.status===''&&x.done&&x.arr){ x.done=false; x.arr=''; }
  });
}
function mkForDate(W,date){
  return W.mk.list.filter(function(x){return x.date===date&&x.kind!=='보강기회X';})
    .map(function(x){return {row:x.row,name:x.name,slot:x.slot,done:x.done,reason:x.reason,amt:x.amt,part:x.part};});
}
function state(W,date,group,errs){
  var roster=[];
  W.ros.forEach(function(r){ if(r.group===group&&r.active!=='N') roster.push({name:r.name,grade:r.grade}); });
  var d=W.days[date]||{},r={},pre=group+'|';
  Object.keys(d).forEach(function(k){
    if(k.indexOf(pre)!==0) return;
    var row=d[k];
    r[k.slice(pre.length)]={arrive:row.arrive||null,teacher:row.teacher||'',leave:row.leave||null,status:row.status||'',memo:row.memo||'',a0:row.a0||null,l0:row.l0||null};
  });
  var mk=[]; try{ mk=mkForDate(W,date); }catch(e){}
  return {ok:true,roster:roster,rec:r,mk:mk,now:Date.now(),errs:errs||[]};
}
function mkFind(W,op){
  var row=Number(op.row);
  if(!row||row<2) throw new Error('행 오류');
  for(var i=0;i<W.mk.list.length;i++) if(W.mk.list[i].row===row){
    if(W.mk.list[i].name!==op.name) break;
    return i;
  }
  throw new Error('목록이 바뀌었습니다. 새로고침 후 다시 시도');
}
function mkApply(W,op){
  if(op.op==='mk_add'){
    var name=String(op.name||'').trim();
    if(!name) throw new Error('이름이 없습니다');
    if(op.reason&&MK_REASONS.indexOf(op.reason)<0) throw new Error('사유 오류');
    if(op.slot&&MK_SLOTS.indexOf(op.slot)<0) throw new Error('시간대 오류');
    var cnt=Math.max(1,Math.min(Number(op.count)||1,6));
    if(op.amount&&MK_AMOUNTS.indexOf(op.amount)<0) throw new Error('분량 오류');
    var date=chkDate(op.date),abs=chkDate(op.abs);
    var grp=cnt>1?String(Date.now()):'';
    for(var k=0;k<cnt;k++){
      W.mk.list.push({row:W.mk.next++,done:false,name:name,date:k===0?date:'',slot:op.slot||'',kind:'',arr:'',abs:abs,reason:op.reason||'',memo:op.memo||'',part:cnt>1?(k+1)+'/'+cnt:'',amt:op.amount||'',grp:grp});
    }
    return;
  }
  var i=mkFind(W,op),x=W.mk.list[i];
  if(op.op==='mk_set'){
    var f=op.f||{},n=clone(x);
    if('date' in f) n.date=chkDate(f.date);
    if('slot' in f){ if(f.slot&&MK_SLOTS.indexOf(f.slot)<0) throw new Error('시간대 오류'); n.slot=f.slot||''; }
    if('kind' in f){ if(f.kind&&MK_KINDS.indexOf(f.kind)<0) throw new Error('구분 오류'); n.kind=f.kind||''; }
    if('memo' in f) n.memo=f.memo||'';
    if('done' in f){ n.done=!!f.done; if(!f.done) n.arr=''; }
    W.mk.list[i]=n; return;
  }
  if(op.op==='mk_del'){ W.mk.list.splice(i,1); return; }
  throw new Error('알 수 없는 작업: '+op.op);
}
function seenHas(W,id){ return W.v.seen.indexOf(id)>=0; }
function seenAdd(W,id){ W.v.seen.push(id); if(W.v.seen.length>SEEN_MAX) W.v.seen=W.v.seen.slice(-SEEN_MAX); }

/* q 를 W 에 적용하고 응답을 만든다 (서버 handle_ 와 같은 순서) */
function handle(W,q){
  var errs=[];
  if(q.act==='mk'){
    (q.ops||[]).forEach(function(op){
      if(op.id&&seenHas(W,op.id)) return;
      try{ mkApply(W,op); if(op.id) seenAdd(W,op.id); }catch(er){ errs.push(String(er)); }
    });
    var names={};
    W.ros.forEach(function(r){ if(r.active!=='N'&&r.name) names[r.name]=1; });
    return {ok:true,list:clone(W.mk.list),names:Object.keys(names).sort(),errs:errs,now:Date.now()};
  }
  var date=q.date,group=q.group;
  if(q.act==='ops'&&q.ops){
    q.ops.forEach(function(op){
      if(op.id&&seenHas(W,op.id)) return;
      try{ apply(W,op.date||date,group,op); if(op.id) seenAdd(W,op.id); }catch(er){ errs.push(String(er)); }
    });
    try{ mkSync(W,date); }catch(er2){ errs.push('보강 연동: '+String(er2)); }
  }
  return state(W,date,group,errs);
}
function datesOf(q){
  var s={};
  if(q.act==='mk') return [];
  if(q.date) s[q.date]=1;
  (q.ops||[]).forEach(function(op){ if(op.date) s[op.date]=1; });
  return Object.keys(s);
}

/* ---- 저장소 연결부 ---- */
function make(opt){
  /* opt: {col, token(): Promise<string>, fetch?, vnow?(): 지금 번호표 값 또는 null} */
  var F=opt.fetch||root.fetch.bind(root);
  var DB='projects/h-roadmap/databases/(default)',BASE='https://firestore.googleapis.com/v1/'+DB+'/documents';
  var cache={};
  function nm(id){ return DB+'/documents/'+opt.col+'/'+id; }
  function call(path,body){
    return opt.token().then(function(tok){
      return F(BASE+path,{method:'POST',headers:{'Authorization':'Bearer '+tok,'Content-Type':'application/json'},body:JSON.stringify(body)});
    });
  }
  function get(ids){
    return call(':batchGet',{documents:ids.map(nm)}).then(function(r){
      if(r.status===401||r.status===403) throw {auth:1};
      if(!r.ok) throw new Error('읽기 실패 '+r.status);
      return r.json();
    }).then(function(arr){
      var out={};
      arr.forEach(function(x){
        if(x.found){ var id=x.found.name.split('/').pop(); out[id]={j:x.found.fields&&x.found.fields.j?x.found.fields.j.stringValue:'',ut:x.found.updateTime}; }
      });
      return out;
    });
  }
  function commit(writes){
    return call(':commit',{writes:writes}).then(function(r){
      if(r.status===401||r.status===403) throw {auth:1};
      if(r.status===400||r.status===409||r.status===412) return r.text().then(function(t){ if(/FAILED_PRECONDITION|ALREADY_EXISTS|ABORTED|NOT_FOUND/.test(t)||r.status===409) return false; throw new Error('저장 실패 '+r.status); });
      if(!r.ok) throw new Error('저장 실패 '+r.status);
      return true;
    });
  }
  function load(dates){
    var ids=['ros','mk','v'].concat(dates.map(function(d){return 'd_'+d;}));
    return get(ids).then(function(g){
      var W={ros:g.ros?JSON.parse(g.ros.j):[],mk:g.mk?JSON.parse(g.mk.j):{next:2,list:[]},v:g.v?JSON.parse(g.v.j):{n:0,seen:[]},days:{}};
      dates.forEach(function(d){ W.days[d]=g['d_'+d]?JSON.parse(g['d_'+d].j):{}; });
      return {W:W,g:g};
    });
  }
  function ser(W,id){
    if(id==='ros') return JSON.stringify(W.ros);
    if(id==='mk') return JSON.stringify(W.mk);
    return JSON.stringify(W.days[id.slice(2)]||{});
  }
  function once(q){
    var dates=datesOf(q);
    return load(dates).then(function(L){
      var W=L.W,g=L.g,seen0=W.v.seen.length?W.v.seen[W.v.seen.length-1]:'',seenN=W.v.seen.length;
      var res=handle(W,q);
      var ids=['ros','mk'].concat(Object.keys(W.days).map(function(d){return 'd_'+d;})),writes=[];
      ids.forEach(function(id){
        var s=ser(W,id),old=g[id]?g[id].j:(id==='ros'?'[]':id==='mk'?JSON.stringify({next:2,list:[]}):'{}');
        if(s===old) return;
        writes.push({update:{name:nm(id),fields:{j:{stringValue:s}}},currentDocument:g[id]?{updateTime:g[id].ut}:{exists:false}});
      });
      var seenCh=W.v.seen.length!==seenN||(W.v.seen.length?W.v.seen[W.v.seen.length-1]:'')!==seen0;
      if(!writes.length&&!seenCh){ return {res:res,v:W.v.n}; }
      W.v.n=(W.v.n||0)+1;
      writes.push({update:{name:nm('v'),fields:{j:{stringValue:JSON.stringify(W.v)}}},currentDocument:g.v?{updateTime:g.v.ut}:{exists:false}});
      return commit(writes).then(function(ok){ return ok?{res:res,v:W.v.n}:null; });
    });
  }
  function ckey(q){ return q.act==='mk'?'mk':'ops|'+q.date+'|'+q.group; }
  function post(q){
    var hasOps=q.ops&&q.ops.length,k=ckey(q),n=0;
    function run(){
      return once(q).then(function(r){
        if(r){ cache[k]={v:r.v,res:r.res}; return r.res; }
        if(++n>=8) throw new Error('busy');
        return new Promise(function(z){ setTimeout(z,150+Math.random()*400*n); }).then(run);
      });
    }
    var p;
    if(!hasOps&&cache[k]){
      /* 번호표(v)를 "바뀔 때만" 받는 연결이 살아 있으면(opt.vnow) 다시 읽지 않고 그 값을 쓴다 */
      var live=opt.vnow?opt.vnow():null;
      p=(typeof live==='number'?Promise.resolve(null):get(['v'])).then(function(g){
        var vn=g===null?live:(g.v?JSON.parse(g.v.j).n:0);
        if(vn===cache[k].v){ var c=clone(cache[k].res); c.now=Date.now(); return c; }
        return run();
      });
    } else p=run();
    return p.catch(function(e){
      if(e&&e.auth) return {ok:false,err:'auth'};
      return {ok:false,err:String(e&&e.message||e)};
    });
  }
  return {post:post,_get:get,_commit:commit,_nm:nm};
}

var api={make:make,handle:handle,datesOf:datesOf,hhmm:hhmm};
if(typeof module!=='undefined'&&module.exports) module.exports=api; else root.AttFs=api;
})(typeof window!=='undefined'?window:globalThis);
