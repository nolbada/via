/* wnfs 261117a — REC H(선생님 화면)의 "보는" 요청 4가지를 오답노트 서버 대신 Firebase 에서 바로 읽는다.
   t_students / t_list / t_hw / t_rev. 계산 방식은 서버(route_)와 같다. 선생님 구글 로그인이 되어 있을 때만 쓰고,
   안 되거나 실패하면 null 을 돌려줘서 화면이 예전처럼 서버에 묻게 한다. 고치는 요청은 건드리지 않는다. */
(function(W){
'use strict';
var DB='https://firestore.googleapis.com/v1/projects/h-roadmap/databases/(default)/documents/';
var AUTH=null,WD=['일','월','화','수','목','금','토'];
W.__wnAuthReady=function(a){AUTH=a};
function norm(s){return String(s==null?'':s).replace(/\s+/g,'')}
function today(){return new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Seoul',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date())}
function addDays(d,n){var p=d.split('-');return new Date(Date.UTC(+p[0],+p[1]-1,+p[2]+n)).toISOString().slice(0,10)}
function tok(){if(!AUTH||!AUTH.signedIn())return Promise.reject(new Error('nologin'));return AUTH.token()}
function req(path){return tok().then(function(t){return fetch(DB+path,{headers:{Authorization:'Bearer '+t}})})}
function getDoc(path){return req(path).then(function(r){if(r.status===404)return null;if(!r.ok)throw new Error('http '+r.status);return r.json()})}
function listCol(col){
  var out=[];
  function page(tk){return req(col+'?pageSize=300'+(tk?'&pageToken='+encodeURIComponent(tk):'')).then(function(r){if(!r.ok)throw new Error('http '+r.status);return r.json()}).then(function(j){(j.documents||[]).forEach(function(d){out.push(d)});if(j.nextPageToken)return page(j.nextPageToken)})}
  return page('').then(function(){return out});
}
function J(doc){var j=doc&&doc.fields&&doc.fields.j&&doc.fields.j.stringValue;return j?JSON.parse(j):null}
function idOf(doc){return String(doc.name).split('/').pop()}
function parseWn(name,doc,out){
  (J(doc)||[]).forEach(function(x){out.push({row:0,name:name,w:String(x.w),m:String(x.m||''),src:String(x.src||''),how:String(x.how||''),ask:!!x.ask,first:String(x.first||''),c:Number(x.c)||0,st:Number(x.st)||0,nx:String(x.nx||''),grad:!!x.grad,last:String(x.last||''),qid:String(x.qid||'')})});
}
function pub(r){return {w:r.w,m:r.m,src:r.src,ask:r.ask,c:r.c,st:r.st,nx:r.nx,first:r.first,q:r.qid}}
function byPriority(a,b){return (b.c-a.c)||(a.nx<b.nx?-1:a.nx>b.nx?1:0)}
function roster(){
  return getDoc('ros/wn').then(function(d){
    var o=J(d);if(!o)throw new Error('noroster');
    var v=[o.head].concat(o.rows),m={},i;
    for(i=1;i<v.length;i++){
      var n=norm(v[i][0]);if(!n)continue;
      if(String(v[i][7]||'').indexOf('퇴원')>=0)continue;
      m[n]={name:n,grade:String(v[i][1]||''),school:String(v[i][2]||''),cap:Number(v[i][3])||40,dv:String(v[i][4]||''),dvDate:String(v[i][5]==null?'':v[i][5]),start:String(v[i][6]==null?'':v[i][6])};
    }
    return m;
  });
}
function holdMap(){
  return getDoc('cfgsrc/all').then(function(d){
    var a=J(d)||[],m={};
    a.forEach(function(r){var k=String(r[0]);if(k.indexOf('HOLD|')!==0)return;try{m[k.slice(5)]=JSON.parse(String(r[1]))}catch(e){}});
    return m;
  });
}
function inHold(h,d){
  if(!h)return false;
  if(h.hold&&h.hs&&d>=h.hs&&d<=h.hold)return true;
  var a=h.holds||[],i;for(i=0;i<a.length;i++)if(d>=a[i].a&&d<=a[i].b)return true;
  return false;
}
function shiftNx(rows,hm){
  rows.forEach(function(r){
    var h=hm[r.name];if(!h||!r.nx||!r.last||r.nx<=r.last)return;
    var p1=r.last.split('-'),p2=r.nx.split('-');
    var remain=Math.round((Date.UTC(+p2[0],+p2[1]-1,+p2[2])-Date.UTC(+p1[0],+p1[1]-1,+p1[2]))/86400000);
    var cur=r.last,g=0;
    if(remain>15){cur=addDays(r.nx,-1);remain=1}
    while(remain>0&&g++<400){cur=addDays(cur,1);if(!inHold(h,cur))remain--}
    r.nx=cur;
  });
  return rows;
}
var ACT={
  t_students:function(){
    return Promise.all([roster(),listCol('wnsrc')]).then(function(a){
      var ros=a[0],rows=[],t=today(),list=[];
      a[1].forEach(function(d){parseWn(idOf(d),d,rows)});
      Object.keys(ros).forEach(function(n){
        var mine=rows.filter(function(r){return r.name===n&&!r.grad});
        var due=mine.filter(function(r){return r.nx&&r.nx<=t});
        list.push({name:n,grade:ros[n].grade,school:ros[n].school,total:mine.length,due:due.length,askDue:due.filter(function(r){return r.ask}).length,dv:ros[n].dv,dvDate:ros[n].dvDate});
      });
      return {ok:true,today:t,students:list};
    });
  },
  t_list:function(q){
    var n2=norm(q.name);if(!n2||/^샘플/.test(n2))return null;
    return Promise.all([getDoc('wnsrc/'+encodeURIComponent(n2)),holdMap()]).then(function(a){
      var all=[],t2=today(),lim=Number(q.limit)||10;
      if(a[0])parseWn(n2,a[0],all);
      var rows=shiftNx(all.filter(function(r){return r.name===n2&&!r.grad}),a[1]);
      var dueq=rows.filter(function(r){return r.ask&&r.nx&&r.nx<=t2}).sort(byPriority);
      if(q.all)return {ok:true,today:t2,items:rows.slice().sort(byPriority).slice(0,Number(q.max)||300).map(pub),askDue:dueq.length,total:rows.length,all:true};
      return {ok:true,today:t2,items:dueq.slice(0,lim).map(pub),askDue:dueq.length,total:rows.length};
    });
  },
  t_hw:function(q){
    return listCol('hwsrc').then(function(docs){
      var recs=[],res=[],from=String(q.from||'');
      docs.forEach(function(d){(J(d)||[]).forEach(function(r){recs.push(r)})});
      recs.sort(function(a,b){return a[7]-b[7]});
      recs.forEach(function(v){var d=String(v[5]==null?'':v[5]);if(d>=from)res.push({name:String(v[1]),level:String(v[2]),day:Number(v[3]),score:String(v[4]),date:d,wd:String(v[6])})});
      return {ok:true,items:res};
    });
  },
  t_rev:function(q){
    return listCol('logsrc').then(function(docs){
      var recs=[],fr=String(q.from||''),agg={},out=[];
      docs.forEach(function(d){(J(d)||[]).forEach(function(r){recs.push(r)})});
      recs.sort(function(a,b){return a[7]-b[7]});
      recs.forEach(function(lv){
        if(String(lv[3])!=='학생복습')return;
        var dd=String(lv[0]==null?'':lv[0]).slice(0,10);
        if(dd<fr)return;
        var kk=norm(lv[1])+'|'+dd;
        if(!agg[kk])agg[kk]={name:norm(lv[1]),date:dd,n:0,ok:0};
        agg[kk].n++;if(String(lv[4])==='O')agg[kk].ok++;
      });
      Object.keys(agg).forEach(function(k){var a2=agg[k],pp=a2.date.split('-');a2.wd=WD[new Date(Date.UTC(+pp[0],+pp[1]-1,+pp[2])).getUTCDay()];out.push(a2)});
      return {ok:true,items:out};
    });
  }
};
function authReady(){
  /* 로그인 정보가 확인될 때까지 최대 2초 기다린다 */
  return new Promise(function(z){
    var n=0;(function tick(){
      if(AUTH){Promise.race([AUTH.ready,new Promise(function(y){setTimeout(y,2000)})]).then(function(){z(AUTH.signedIn())});return}
      if(++n>20){z(false);return}
      setTimeout(tick,100);
    })();
  });
}
W.WNFS={
  /* 바로 읽을 수 있는 요청이면 Promise(응답 또는 null), 아니면 null 을 돌려준다. null 이면 화면이 서버에 묻는다 */
  handle:function(b){
    var f=b&&ACT[b.act];if(!f)return null;
    return authReady().then(function(ok){
      if(!ok)return null;
      var p=f(b);if(!p)return null;
      return Promise.race([p,new Promise(function(z,j){setTimeout(function(){j(new Error('slow'))},6000)})]);
    });
  }
};
})(window);
