/* VIA 통합 연동: H로드맵과 거기에 묶인 활동(데일리보카·더블보카·데일리어법 등)의 기록을 이름 하나로 모든 기기에 잇는다.
   고등 내신 앱의 rec.js와 같은 방식(같은 구글 시트 서버, 같은 요청 형식). id는 VIA| 로 시작해 다른 기록과 섞이지 않는다.
   이름은 한 번만 넣으면 되고(wn_name), 선생님 확인 링크(?t=1&c=A|B)는 신유정A/B 로 따로 이어진다. 오류가 나도 앱 본체에는 영향이 없도록 모두 try 안에서 돈다. */
(function(){try{
  var W=window,D=document,P=location.pathname;
  if(W.__viaSync)return;W.__viaSync=1;
  if(/\/wn-t\//.test(P))return;
  var URL_=W.REC_URL||'https://script.google.com/macros/s/AKfycbw1YQfKsgAXNk8NYoxOfz4bsCSy66fiim7HoFAUk162ksxrEbmspMs2UifNZ-93sdf05A/exec';
  var LS=null;try{LS=W.localStorage;LS.getItem('x')}catch(e){return}
  /* 261117g: 기록 서버에 "받기만" 하는 요청(act:'put' 에 data 가 빈 것)은 Firebase 에서 바로 답한다(서버를 거치지 않는다).
     이 파일을 쓰는 화면(로드맵·데일리보카·더블보카·데일리어법)의 받기 요청이 모두 해당된다. 한 기록은 8조각이라 한 번에 받는다.
     조각이 하나도 없거나 실패·2.5초 초과면 원래 요청을 그대로 서버로 보낸다. 쓰기 요청과 내신 기록(REC|·RECM| - 명단 확인이 필요)은 건드리지 않는다 */
  try{(function(){
    if(W.__recFs||!W.fetch||!W.Response)return;W.__recFs=1;
    var of=W.fetch;
    function fsRead(id){
      try{
        var smp=/(^|[|:])샘플\d*([|:]|$)/.test(id),base='projects/h-roadmap/databases/(default)/documents/'+(smp?'rec_s':'rec')+'/'+String(id).replace(/%/g,'%25').replace(/\//g,'%2F')+'~',names=[],i;
        for(i=0;i<8;i++)names.push(base+i);
        var ac=W.AbortController?new AbortController():null,tm=ac?setTimeout(function(){ac.abort()},2500):0;
        return of.call(W,'https://firestore.googleapis.com/v1/projects/h-roadmap/databases/(default)/documents:batchGet',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({documents:names}),signal:ac?ac.signal:undefined})
          .then(function(r){clearTimeout(tm);return r.ok?r.json():null})
          .then(function(a){
            if(!Array.isArray(a)||a.length!==8)return null;
            var data={},found=0,j,o,k,x;
            for(j=0;j<a.length;j++){
              x=a[j];if(x.missing)continue;if(!x.found)return null;found++;
              o=x.found.fields&&x.found.fields.j&&x.found.fields.j.stringValue;if(!o)continue;o=JSON.parse(o);
              for(k in o){try{data[k]={v:JSON.parse(String(o[k][0])),t:Number(o[k][1])}}catch(e){}}
            }
            return found?{ok:1,data:data,fs:1}:null;
          }).catch(function(){clearTimeout(tm);return null});
      }catch(e){return Promise.resolve(null)}
    }
    /* 261123: 올리기(쓰기)도 Firebase 로 바로 보낸다. 서버가 하던 일(조각 정하기·합치기·충돌 확인)을 그대로 한다 —
       한 기록 = 8조각, 키 → 조각은 서버와 같은 해시, 합치기는 키마다 더 나중 시각이 이김, 쓸 때는 읽은 시각(updateTime)을 조건으로 걸어 동시에 쓴 것을 덮지 않는다(어긋나면 다시 읽고 4번까지).
       VIA| 기록만(내신 REC|·RECM| 은 명단 확인이 필요해 서버 그대로). 실패·시간 초과이거나 페이지를 닫는 중(keepalive)이면 원래대로 서버로 보낸다 */
    function rh(k){var h=5381,i;k=String(k);for(i=0;i<k.length;i++)h=((h<<5)+h+k.charCodeAt(i))|0;return (h>>>0)%8}
    var FSB='https://firestore.googleapis.com/v1/',DB='projects/h-roadmap/databases/(default)/documents';
    function enc(id){return String(id).replace(/%/g,'%25').replace(/\//g,'%2F')}
    function fsCall(op,body){
      var ac=W.AbortController?new AbortController():null,tm=ac?setTimeout(function(){ac.abort()},4000):0;
      return of.call(W,FSB+DB+':'+op,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),signal:ac?ac.signal:undefined})
        .then(function(r){clearTimeout(tm);return r.text().then(function(t){return{code:r.status,body:t}})},function(){clearTimeout(tm);return null});
    }
    function fsWrite(id,data){
      var smp=/(^|[|:])샘플\d*([|:]|$)/.test(id),col=smp?'rec_s':'rec',need={},k,c,n=0,own=Object.prototype.hasOwnProperty;
      for(k in data){if(own.call(data,k)&&data[k]){need[rh(k)]=1;n++}}
      if(!n)return Promise.resolve(true);
      var cs=Object.keys(need).map(Number);
      function nmOf(c){return DB+'/'+col+'/'+enc(id)+'~'+c}
      function attempt(left){
        return fsCall('batchGet',{documents:cs.map(nmOf)}).then(function(r){
          if(!r||r.code!==200)return false;
          var a;try{a=JSON.parse(r.body)}catch(e){return false}
          if(!Array.isArray(a)||a.length!==cs.length)return false;
          var g={},i,x,nm,o,j;
          for(i=0;i<a.length;i++){
            x=a[i];
            if(x.found){nm=x.found.name;j=x.found.fields&&x.found.fields.j&&x.found.fields.j.stringValue;try{o=j?JSON.parse(j):{}}catch(e){return false}g[nm.slice(nm.lastIndexOf('~')+1)]={ut:x.found.updateTime,d:o}}
            else if(x.missing){nm=x.missing;g[nm.slice(nm.lastIndexOf('~')+1)]={ut:null,d:{}}}
            else return false;
          }
          var dirty={},d,val;
          for(k in data){
            if(!own.call(data,k))continue;d=data[k];if(!d)continue;
            val=JSON.stringify(d.v);if(val===undefined||val.length>45000)continue;
            c=rh(k);if(!g[c])return false;
            if(!own.call(g[c].d,k)||d.t>Number(g[c].d[k][1])){g[c].d[k]=[val,d.t===undefined?'':d.t];dirty[c]=1}
          }
          var ws=[],s;
          for(c in dirty){
            s=JSON.stringify(g[c].d);if(s.length>900000)return false;
            ws.push({update:{name:nmOf(c),fields:{j:{stringValue:s},t:{integerValue:String(Date.now())},id:{stringValue:String(id)}}},currentDocument:g[c].ut?{updateTime:g[c].ut}:{exists:false}});
          }
          if(!ws.length)return true;
          return fsCall('commit',{writes:ws}).then(function(r2){
            if(!r2)return false;
            if(r2.code===200)return true;
            if(left>0&&(r2.code===409||/FAILED_PRECONDITION|ALREADY_EXISTS|ABORTED/.test(r2.body)))return attempt(left-1);
            return false;
          });
        });
      }
      return attempt(4).catch(function(){return false});
    }
    var SRV_='AKfycbw1YQfKsgAXNk8NYoxOfz4bsCSy66fiim7HoFAUk162ksxrEbmspMs2UifNZ-93sdf05A';
    function okResp(r){return new W.Response(JSON.stringify(r),{status:200,headers:{'Content-Type':'application/json'}})}
    W.fetch=function(u,o){
      try{
        if(typeof u==='string'&&u.indexOf(SRV_)>0&&o&&o.method==='POST'&&typeof o.body==='string'){
          var self=this,args=arguments,b,k,n=0;
          if(o.body.length<600000){
            b=JSON.parse(o.body);
            if(b&&b.act==='put'&&typeof b.id==='string'&&b.id.length>=3&&!/^RECM?\|/.test(b.id)&&b.data&&typeof b.data==='object'){
              for(k in b.data)n++;
              if(!n){if(o.body.length<600)return fsRead(b.id).then(function(r){return r?okResp(r):of.apply(self,args)})}
              else if(b.nr&&!o.keepalive&&b.id.indexOf('VIA|')===0&&b.id.length>=5&&b.id.length<=60){
                return fsWrite(b.id,b.data).then(function(ok){return ok?okResp({ok:1,fs:1}):of.apply(self,args)});
              }
            }
          }
        }
      }catch(e){}
      return of.apply(this,arguments);
    };
  })()}catch(e){}
  var UK='via_uid',MK='via_meta',AK='via_at',LK='via_lt',TK='via_tomb',MAXV=60000,T0=Date.now();
  function g(k){try{return LS.getItem(k)}catch(e){return null}}
  var inS=0;
  function s(k,v){inS++;try{LS.setItem(k,v)}catch(e){}inS--}
  function d(k){inS++;try{LS.removeItem(k)}catch(e){}inS--}
  function jg(k){try{return JSON.parse(g(k)||'null')}catch(e){return null}}
  /* 이 연동이 잇는 기록. 누적복습(wn_rv*)은 로드맵이 따로 잇는다. 데일리어법은 날짜별 점수 연동(EO_)과 함께 문제별 기록까지 잇는다 */
  function mirrored(k){
    if(!k||typeof k!=='string')return false;
    if(k.indexOf('via_')===0||k.indexOf('rec_')===0||k.indexOf('demo_')===0)return false;
    /* 261118: 보드 밖에서 바로 여는 앱의 기록도 같은 방식으로 잇는다(앱마다 저장값 이름을 여기에 더한다). 천일문S: 놓친 문장·본 문장 목록 */
    if(/^(sj_missed|sj_looked2)$/.test(k))return true;
    return /^(dv_|dvc_|dvp_|wl_|star_|wn_mm_|wn_star_|wn_fp_|eobeop_daily_v1_)/.test(k);
  }
  function keys(){var o=[],i,k;for(i=0;i<LS.length;i++){k=LS.key(i);if(mirrored(k))o.push(k)}return o}
  /* 별표·틀린 목록·이어풀기 진행처럼 '지우거나 줄어드는' 기록은 합치지 않고, 더 나중에 바꾼 쪽이 이긴다(지운 것도 기록으로 남긴다) */
  function lww(k){return /^(wn_star_|wn_fp_|dvc_|dvp_|star_|wl_|sj_missed$|sj_looked2$)/.test(k)}
  function stamp(k){var o=jg(LK)||{};o[k]=Date.now();s(LK,JSON.stringify(o));var tb=jg(TK)||{};if(k in tb){delete tb[k];s(TK,JSON.stringify(tb))}}
  function tomb(k){var tb=jg(TK)||{};tb[k]=Date.now();s(TK,JSON.stringify(tb));var o=jg(LK)||{};delete o[k];s(LK,JSON.stringify(o))}
  function nm(){
    var q=W.location.search;
    if(/[?&]t=1(&|$)/.test(q)){var c=(/[?&]c=([AB])(&|$)/.exec(q)||[])[1]||'';return '신유정'+c}
    /* 261118: 보드에서 연 화면이 '지금 보드에 들어온 학생'을 알려 주면 그 이름으로 잇는다 */
    if(W.__bdName)return String(W.__bdName).replace(/\s+/g,'');
    return (g('wn_name')||g('recm_name')||g('rec_name')||'').replace(/\s+/g,'');
  }
  function ident(){var n=nm();return n?'VIA|'+n.toLowerCase():''}
  function dm(a,b){
    if(a===b)return a;
    var ta=typeof a,tb=typeof b,o,k;
    if(ta==='number'&&tb==='number')return Math.max(a,b);
    if(ta==='boolean'&&tb==='boolean')return a||b;
    if(Array.isArray(a)&&Array.isArray(b)){/* 261116: 이 기기 목록은 그대로 두고, 저쪽에만 더 있는 것만 뒤에 붙인다(같은 값이 여러 번 있어도 지우지 않는다) */var cnt={};o=a.slice();a.forEach(function(x){var t=JSON.stringify(x);cnt[t]=(cnt[t]||0)+1});b.forEach(function(x){var t=JSON.stringify(x);if(cnt[t]>0)cnt[t]--;else o.push(x)});return o}
    if(a&&b&&ta==='object'&&tb==='object'&&!Array.isArray(a)&&!Array.isArray(b)){
      o={};for(k in a)o[k]=(k in b)?dm(a[k],b[k]):a[k];for(k in b)if(!(k in a))o[k]=b[k];return o}
    return b;
  }
  function merge(loc,rem,k){try{var a=JSON.parse(loc),b=JSON.parse(rem);
    if(k&&k.indexOf('eobeop_daily_v1_')===0&&a&&b){
      /* 처음부터 다시(rsT)를 누른 쪽이 이긴다. 같은 시점이면 합치되 '전체 열기'는 이 기기 값을 쓴다 */
      var ra=Number(a.rsT||0),rb=Number(b.rsT||0);
      if(ra>rb)return loc;if(rb>ra)return rem;
      var m=dm(a,b);m.open=!!a.open;return JSON.stringify(m)}
    return JSON.stringify(dm(a,b))}catch(e){return rem}}
  function post(body,keep){
    return fetch(URL_,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(body),keepalive:!!keep})
      .then(function(r){return r.json()}).then(function(r){if(!r||!r.ok)throw new Error('via');return r});
  }
  function unwrap(v){return(v&&typeof v==='object'&&typeof v.s==='string')?v.s:null}
  var busy=false,again=false;
  function pending(){
    var meta=jg(MK)||{},ch={},sent={};
    keys().forEach(function(k){var v=g(k);if(v===null||v.length>MAXV)return;if(meta[k]!==v){ch[k]={v:{s:v},t:Date.now()};sent[k]=v}});
    var tb=jg(TK)||{},lt=jg(LK)||{};
    for(var k in tb){if(g(k)===null&&meta[k]!==''){ch[k]={v:{s:''},t:tb[k]};sent[k]=''}}
    for(var k2 in ch){if(ch[k2].v.s!==''&&lww(k2)&&lt[k2])ch[k2].t=lt[k2]}
    return {ch:ch,sent:sent,n:Object.keys(sent).length};
  }
  function push(id,keep){
    var c=pending();if(!c.n)return Promise.resolve(false);
    /* 261116e: 올리기만 할 때는 서버가 기록을 돌려주지 않게 한다(nr:1) */
    return post({act:'put',id:id,nr:1,data:c.ch},keep).then(function(){
      var meta=jg(MK)||{},k;for(k in c.sent)meta[k]=c.sent[k];s(MK,JSON.stringify(meta));return true});
  }
  function sync(id){
    if(busy){again=true;return Promise.resolve(false)}busy=true;
    return post({act:'put',id:id,data:{}}).then(function(r){
      var rem=r.data||{},meta=jg(MK)||{},rl=false,k,ltA=jg(LK)||{};
      for(k in rem){
        if(!mirrored(k))continue;
        var rs=unwrap(rem[k]&&rem[k].v);if(rs===null)continue;
        var lv=g(k);
        if(lww(k)){
          var rt=Number(rem[k].t||0),tbm=jg(TK)||{},ltm=jg(LK)||{};
          if(lv===null){
            if(rs===''){meta[k]='';continue}
            if(tbm[k]&&tbm[k]>=rt)continue; /* 이 기기에서 지운 게 더 나중 → 그대로 지운 채로 두고 올린다 */
            s(k,rs);meta[k]=rs;rl=true;continue}
          if(lv===rs){meta[k]=rs;continue}
          if(rs===''){ /* 다른 기기에서 지움 */
            if(meta[k]!==lv&&ltm[k]&&ltm[k]>rt)continue;
            d(k);meta[k]='';rl=true;continue}
          if(meta[k]!==lv){
            if(ltm[k]){ if(ltm[k]>rt)continue; s(k,rs);meta[k]=rs;rl=true;continue }
            /* 변경 시각을 모르는 예전 값: 예전 방식대로 합친다 */
            var mg0=merge(lv,rs,k);if(mg0!==lv){s(k,mg0);rl=true}continue}
          s(k,rs);meta[k]=rs;rl=true;continue}
        if(lv===rs){meta[k]=rs;continue}
        if(lv===null){s(k,rs);meta[k]=rs;rl=true;continue}
        if(meta[k]!==lv){
          var mg=merge(lv,rs,k);if(mg!==lv){s(k,mg);rl=true}
        }else{
          /* 261116b: 서버 값이 이 기기에서 바꾼 시각보다 옛것이면 받지 않고, 이 기기 값을 다시 올린다(옛 값이 새 값을 덮어쓰지 못하게) */
          var rt2=Number((rem[k]&&rem[k].t)||0);
          if(ltA[k]&&rt2&&rt2<ltA[k]){delete meta[k]}else{s(k,rs);meta[k]=rs;rl=true}
        }
      }
      s(MK,JSON.stringify(meta));s(AK,String(Date.now()));
      return push(id,false).then(function(){busy=false;if(again){again=false;sched()}return rl},function(){busy=false;return rl});
    },function(e){busy=false;throw e});
  }
  function wipe(){keys().forEach(d);d(MK);d(LK);d(TK)}
  function reloadOnce(){
    try{var t=Number(sessionStorage.getItem('via_rl')||0);if(Date.now()-t>20000){sessionStorage.setItem('via_rl',String(Date.now()));location.reload()}}catch(e){}
  }
  var isBoard=/\/wn\/?(index\.html)?$/.test(P);
  function after(rl,early){if(W.__wnBusy)return;/* 복습을 푸는 중에는 새로고침하지 않는다 */if(rl&&(early||isBoard))reloadOnce()}
  var timer=null,started=false;
  /* 261116b: 저장이 일어날 때마다 서버와 맞추지 않는다. 마지막 저장 뒤 5초 조용하면(계속 풀고 있으면 늦어도 15초마다) 바뀐 것만 한 번 올린다.
     받기는 화면을 열 때·돌아올 때 한다. 서버가 한 번에 한 요청씩만 처리하므로 요청 수를 줄이는 것이 곧 속도다 */
  var firstAt=0;
  function pushNow(){
    var id=ident();if(!id||id!==g(UK))return;
    if(busy){again=true;return}
    busy=true;push(id,false).catch(function(){}).then(function(){busy=false;if(again){again=false;sched()}});
  }
  function sched(){
    var now=Date.now();if(!firstAt)firstAt=now;
    if(timer)clearTimeout(timer);
    timer=setTimeout(function(){timer=null;firstAt=0;pushNow()},Math.max(0,Math.min(5000,firstAt+15000-now)));
  }
  try{var sp=W.Storage.prototype,os=sp.setItem;var orm=sp.removeItem;sp.removeItem=function(k){var had=null;try{if(this===LS&&!inS&&lww(k)&&mirrored(k))had=LS.getItem(k)}catch(e){}orm.apply(this,arguments);try{if(had!==null){tomb(k);sched()}}catch(e){}};
  /* 261116b: 합치는 기록도, 앱이 값을 실제로 바꿨을 때 시각을 적는다 */
  sp.setItem=function(k,v){var old,mine=false;try{mine=this===LS&&!inS&&mirrored(k);if(mine&&!lww(k))old=LS.getItem(k)}catch(e){}os.apply(this,arguments);try{if(this===LS){if(mirrored(k)){if(mine&&(lww(k)||old!==String(v)))stamp(k);if(!inS)sched()}else if(k==='wn_name'&&!started)setTimeout(start,50)}}catch(e){}}}catch(e){}
  function start(){
    if(started)return;var id=ident();if(!id)return;started=true;
    var prev=g(UK);
    var early=function(){return Date.now()-T0<12000};
    var first=function(){s(UK,id);d(MK);return sync(id).then(function(rl){after(rl,true)}).catch(function(){})};
    if(prev&&prev!==id){
      /* 공용 기기에서 다른 학생이 들어옴: 이전 학생 기록을 올리고 지운 뒤 새 학생 기록을 받는다 */
      push(prev,false).catch(function(){return new Promise(function(ok){setTimeout(ok,1500)}).then(function(){return push(prev,false)})}).catch(function(){return new Promise(function(ok){setTimeout(ok,3000)}).then(function(){return push(prev,false)})}).catch(function(){}).then(function(){wipe();return first()});
    }else if(!prev){first()}
    /* 261116b: 45초 안에 이미 맞췄으면(앱 사이를 오갈 때) 다시 받지 않고, 올릴 것이 있을 때만 올린다. 1분마다도 올리기만 한다 */
    else if(Date.now()-Number(g(AK)||0)>45000){sync(id).then(function(rl){after(rl,early())}).catch(function(){})}
    else if(pending().n)sched();
    setInterval(function(){if(!D.hidden&&pending().n)pushNow()},60000);
    var hid=0;
    D.addEventListener('visibilitychange',function(){
      if(D.hidden){hid=Date.now();push(id,true).catch(function(){})}
      else if(hid&&Date.now()-hid>30000){sync(id).then(function(rl){after(rl,false)}).catch(function(){})}
    });
    W.addEventListener('pagehide',function(){push(id,true).catch(function(){})});
  }
  start();
  /* 이름이 나중에 입력되는 경우를 위해 잠시 확인 */
  var tries=0,iv=setInterval(function(){if(started||++tries>200){clearInterval(iv);return}start()},1500);
}catch(e){}})();
