/* 어법제대로 해설 — 선생님이 연 쪽만 학생에게 보이게 하는 잠금 */
(function(){
  var KV='https://script.google.com/macros/s/AKfycbw1YQfKsgAXNk8NYoxOfz4bsCSy66fiim7HoFAUk162ksxrEbmspMs2UifNZ-93sdf05A/exec',ID='EJCTL';
  var key=(location.pathname.split('/').pop()||'').replace(/\.html$/,'');
  function ls(k){try{return localStorage.getItem(k)}catch(e){return null}}
  function ss(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  var hide=document.getElementById('ej-hide');
  function show(){ if(hide&&hide.parentNode) hide.parentNode.removeChild(hide); var o=document.getElementById('ej-lock'); if(o) o.parentNode.removeChild(o); if(location.hash){ setTimeout(function(){ var t=document.getElementById(decodeURIComponent(location.hash.slice(1))); if(t) t.scrollIntoView(); },60); } }
  if(ls('ej_teacher')==='1'||!key||key==='index'){ show(); return; }
  function read(){
    return fetch(KV,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify({act:'put',id:ID,data:{}})})
      .then(function(r){return r.json()}).then(function(r){
        var d=(r&&r.data)||{},x=d[key],s=(x&&x.v&&typeof x.v.s==='string')?x.v.s:(x&&typeof x.s==='string'?x.s:null),o=0;
        try{ if(s) o=JSON.parse(s).o?1:0; }catch(e){}
        return o;
      });
  }
  var box=null,msg=null,timer=null;
  function lock(text){
    if(!box){
      box=document.createElement('div'); box.id='ej-lock';
      box.setAttribute('style','position:fixed;inset:0;z-index:99999;visibility:visible !important;background:#f6f4ee;color:#1c1f26;display:flex;align-items:center;justify-content:center;padding:24px;font-family:"Malgun Gothic",sans-serif;text-align:center');
      box.innerHTML='<div style="max-width:320px"><div style="font-size:19px;font-weight:700;margin:8px 0 6px">아직 열리지 않았어요</div><div id="ej-msg" style="font-size:15px;line-height:1.7;color:#555"></div><button id="ej-re" style="margin-top:16px;border:1px solid #2b5aa8;color:#2b5aa8;background:#fff;font:inherit;font-size:15px;padding:8px 18px;border-radius:999px">다시 확인</button></div>';
      document.body.appendChild(box); msg=box.querySelector('#ej-msg');
      box.querySelector('#ej-re').onclick=check;
    }
    msg.textContent=text;
  }
  function check(){
    read().then(function(o){
      if(o){ ss('ej_open:'+key,'1'); show(); if(timer) clearInterval(timer); }
      else { ss('ej_open:'+key,'0'); lock('선생님이 이 쪽을 열어 주면 볼 수 있어요.'); }
    },function(){
      if(ls('ej_open:'+key)==='1'){ show(); if(timer) clearInterval(timer); }
      else lock('연결이 안 됐어요. 잠시 뒤 다시 눌러 주세요.');
    });
  }
  function start(){ check(); timer=setInterval(check,15000); }
  if(document.body) start(); else document.addEventListener('DOMContentLoaded',start);
})();
