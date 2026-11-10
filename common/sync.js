/* VIA 통합 연동: H로드맵과 거기에 묶인 활동(데일리보카·더블보카·데일리어법 등)의 기록을 이름 하나로 모든 기기에 잇는다.
   고등 내신 앱의 rec.js와 같은 방식(같은 구글 시트 서버, 같은 요청 형식). id는 VIA| 로 시작해 다른 기록과 섞이지 않는다.
   이름은 한 번만 넣으면 되고(wn_name), 선생님 확인 링크(?t=1&c=A|B)는 신유정A/B 로 따로 이어진다. 오류가 나도 앱 본체에는 영향이 없도록 모두 try 안에서 돈다. */
(function(){try{
  var W=window,D=document,P=location.pathname;
  if(W.__viaSync)return;W.__viaSync=1;
  if(/\/wn-t\//.test(P))return;
  var URL_=W.REC_URL||'https://script.google.com/macros/s/AKfycbw1YQfKsgAXNk8NYoxOfz4bsCSy66fiim7HoFAUk162ksxrEbmspMs2UifNZ-93sdf05A/exec';
  var LS=null;try{LS=W.localStorage;LS.getItem('x')}catch(e){return}
  var UK='via_uid',MK='via_meta',AK='via_at',MAXV=60000,T0=Date.now();
  function g(k){try{return LS.getItem(k)}catch(e){return null}}
  function s(k,v){try{LS.setItem(k,v)}catch(e){}}
  function d(k){try{LS.removeItem(k)}catch(e){}}
  function jg(k){try{return JSON.parse(g(k)||'null')}catch(e){return null}}
  /* 이 연동이 잇는 기록. 누적복습(wn_rv*)은 로드맵이 따로 잇는다. 데일리어법은 날짜별 점수 연동(EO_)과 함께 문제별 기록까지 잇는다 */
  function mirrored(k){
    if(!k||typeof k!=='string')return false;
    if(k.indexOf('via_')===0||k.indexOf('rec_')===0||k.indexOf('demo_')===0)return false;
    return /^(dv_|dvc_|dvp_|wl_|star_|wn_mm_|wn_star_|wn_fp_|eobeop_daily_v1_)/.test(k);
  }
  function keys(){var o=[],i,k;for(i=0;i<LS.length;i++){k=LS.key(i);if(mirrored(k))o.push(k)}return o}
  function nm(){
    var q=W.location.search;
    if(/[?&]t=1(&|$)/.test(q)){var c=(/[?&]c=([AB])(&|$)/.exec(q)||[])[1]||'';return '신유정'+c}
    return (g('wn_name')||g('recm_name')||g('rec_name')||'').replace(/\s+/g,'');
  }
  function ident(){var n=nm();return n?'VIA|'+n.toLowerCase():''}
  function dm(a,b){
    if(a===b)return a;
    var ta=typeof a,tb=typeof b,o,k;
    if(ta==='number'&&tb==='number')return Math.max(a,b);
    if(ta==='boolean'&&tb==='boolean')return a||b;
    if(Array.isArray(a)&&Array.isArray(b)){var seen={};o=[];a.concat(b).forEach(function(x){var t=JSON.stringify(x);if(!seen[t]){seen[t]=1;o.push(x)}});return o}
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
    return {ch:ch,sent:sent,n:Object.keys(sent).length};
  }
  function push(id,keep){
    var c=pending();if(!c.n)return Promise.resolve(false);
    return post({act:'put',id:id,data:c.ch},keep).then(function(){
      var meta=jg(MK)||{},k;for(k in c.sent)meta[k]=c.sent[k];s(MK,JSON.stringify(meta));return true});
  }
  function sync(id){
    if(busy){again=true;return Promise.resolve(false)}busy=true;
    return post({act:'put',id:id,data:{}}).then(function(r){
      var rem=r.data||{},meta=jg(MK)||{},rl=false,k;
      for(k in rem){
        if(!mirrored(k))continue;
        var rs=unwrap(rem[k]&&rem[k].v);if(rs===null)continue;
        var lv=g(k);
        if(lv===rs){meta[k]=rs;continue}
        if(lv===null){s(k,rs);meta[k]=rs;rl=true;continue}
        if(meta[k]!==lv){
          var mg=merge(lv,rs,k);if(mg!==lv){s(k,mg);rl=true}
        }else{s(k,rs);meta[k]=rs;rl=true}
      }
      s(MK,JSON.stringify(meta));s(AK,String(Date.now()));
      return push(id,false).then(function(){busy=false;if(again){again=false;sched()}return rl},function(){busy=false;return rl});
    },function(e){busy=false;throw e});
  }
  function wipe(){keys().forEach(d);d(MK)}
  function reloadOnce(){
    try{var t=Number(sessionStorage.getItem('via_rl')||0);if(Date.now()-t>20000){sessionStorage.setItem('via_rl',String(Date.now()));location.reload()}}catch(e){}
  }
  var isBoard=/\/wn\/?(index\.html)?$/.test(P);
  function after(rl,early){if(rl&&(early||isBoard))reloadOnce()}
  var timer=null,started=false;
  function sched(){
    if(timer)return;
    timer=setTimeout(function(){timer=null;var id=ident();if(id&&id===g(UK))sync(id).catch(function(){})},4000);
  }
  try{var sp=W.Storage.prototype,os=sp.setItem;sp.setItem=function(k){os.apply(this,arguments);try{if(this===LS){if(mirrored(k))sched();else if(k==='wn_name'&&!started)setTimeout(start,50)}}catch(e){}}}catch(e){}
  function start(){
    if(started)return;var id=ident();if(!id)return;started=true;
    var prev=g(UK);
    var early=function(){return Date.now()-T0<12000};
    var first=function(){s(UK,id);d(MK);return sync(id).then(function(rl){after(rl,true)}).catch(function(){})};
    if(prev&&prev!==id){
      /* 공용 기기에서 다른 학생이 들어옴: 이전 학생 기록을 올리고 지운 뒤 새 학생 기록을 받는다 */
      push(prev,false).catch(function(){}).then(function(){wipe();return first()});
    }else if(!prev){first()}
    else{sync(id).then(function(rl){after(rl,early())}).catch(function(){})}
    setInterval(function(){if(!D.hidden)sync(id).then(function(rl){after(rl,false)}).catch(function(){})},60000);
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
