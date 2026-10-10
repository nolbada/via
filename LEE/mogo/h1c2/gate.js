/* 동남비타민영어학원 - 자료 서버 열람 (MOGO_GATE=1 일 때만 작동). 꺼져 있으면 기존처럼 data 폴더 파일을 읽어요. */
(function(){
var W=window,URL=W.MOGO_SYNC||'',ON=!!(URL&&W.MOGO_GATE),K='mogo-cred';
function rd(){try{var j=JSON.parse(localStorage.getItem(K)||'null');return j&&j.n&&j.p?j:null}catch(e){return null}}
W.MOGO={on:ON,cred:rd,
  set:function(n,p){try{localStorage.setItem(K,JSON.stringify({n:n,p:p}))}catch(e){}},
  clear:function(){try{localStorage.removeItem(K)}catch(e){}},
  src:function(kind,id){
    if(!ON)return 'data/'+id+'.js';
    var c=rd()||{n:'',p:''};
    return URL+'?act=data&kind='+kind+'&id='+encodeURIComponent(id)+'&name='+encodeURIComponent(c.n)+'&pin='+encodeURIComponent(c.p);
  },
  login:function(n,p,cb){
    var f='mogo_cb'+Date.now(),s=document.createElement('script'),done=false;
    W[f]=function(r){done=true;try{delete W[f]}catch(e){W[f]=null}if(s.parentNode)s.parentNode.removeChild(s);cb(r)};
    s.onerror=function(){if(!done){done=true;cb({ok:false,err:'net'})}};
    s.src=URL+'?act=login&cb='+f+'&name='+encodeURIComponent(n)+'&pin='+encodeURIComponent(p);
    document.head.appendChild(s);
  }
};
})();
