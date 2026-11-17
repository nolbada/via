# attend/index.html (비밀번호 방식) -> attend-g/index.html (구글 로그인 + Firebase 직통) 변환기
# 사용: python3 attend-g/build.py   (via 저장소 맨 위에서)
# 원본(비밀번호판)은 attend-g/src-pw.html 에 보관. 결과: attend-g/index.html(시험 겸용), attend/index.html(실사용)
import re,io
s=io.open('attend-g/src-pw.html',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    c=s.count(a)
    assert c==n,(a[:50],c)
    s=s.replace(a,b)
rep('''  <input id="pwin" type="password" placeholder="비밀번호" autocomplete="current-password">
  <button class="p" id="pwok" style="width:100%">확인</button>''','''  <button class="p" id="glog" style="width:100%">구글로 로그인</button>
  <div style="color:#6a7a7d;font-size:13px;margin-top:10px;line-height:1.6">선생님 구글 계정으로만 열립니다.</div>''')
rep('<script>\n(function(){\nvar API=','<script src="attfs.js?v=261118a"></script>\n<script>\n(function(){\nvar TEST=/[?&]t=1/.test(location.search),NS=TEST?\'attt_\':\'attg_\';\nvar AUTHW=[],AUTHR=null;window.__attReady=function(a){AUTHR=a;AUTHW.splice(0).forEach(function(f){f();});};\nfunction authReady(){return new Promise(function(z){if(AUTHR)z();else AUTHW.push(z);});}\nvar STORE=AttFs.make({col:TEST?\'att_t\':\'att\',token:function(){return authReady().then(function(){return AUTHR.token();});},vnow:function(){var w=window.__attV;return (w&&typeof w.n===\'number\')?w.n:null;}});if(TEST)window.__store=STORE;\nvar API=')
rep("'att_q_'","NS+'q_'",2)
rep("'att_s_'","NS+'s_'",2)
rep('''  var c=new AbortController(),tm=setTimeout(function(){c.abort();},40000);
  return fetch(API,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(body),signal:c.signal}).then(function(r){clearTimeout(tm);return r.json();},function(e){clearTimeout(tm);throw e;});''','''  return new Promise(function(ok,no){var tm=setTimeout(function(){no(new Error('timeout'));},40000);STORE.post(body).then(function(r){clearTimeout(tm);ok(r);},function(e){clearTimeout(tm);no(e);});});''')
rep("ls('att_pw',null);pw='';showGate('비밀번호가 맞지 않습니다');return;","authFail();return;",2)
rep('''document.getElementById('pwok').onclick=function(){
  var v=document.getElementById('pwin').value;if(!v)return;
  pw=v;ls('att_pw',v);start();
};
document.getElementById('pwin').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('pwok').click();});''','''var FAILMSG='';
function authFail(){ls(NS+'in',null);pw='';var em='';try{em=AUTHR&&AUTHR.email()||''}catch(e){}FAILMSG=(em?'방금 로그인한 계정('+em+')은 선생님 계정이 아닙니다. ':'이 계정으로는 열 수 없습니다. ')+'아래 버튼을 눌러 선생님 구글 계정을 골라 주세요. 목록에 없으면 "다른 계정 사용"을 누르면 됩니다.';showGate(FAILMSG);if(AUTHR)AUTHR.signOut();}
document.getElementById('glog').onclick=function(){
  var b=this;FAILMSG='';document.getElementById('gerr').textContent='';
  if(!AUTHR){document.getElementById('gerr').textContent='준비 중입니다. 잠시 뒤 다시 눌러 주세요.';return;}
  b.disabled=true;AUTHR.signIn().then(function(){b.disabled=false;},function(e){b.disabled=false;var c=e&&e.code||'';document.getElementById('gerr').textContent=c==='auth/popup-blocked'?'로그인 창이 막혔습니다. 크롬 앱에서 이 주소를 열어 다시 눌러 주세요.':(c==='auth/popup-closed-by-user'||c==='auth/cancelled-popup-request')?'로그인 창이 닫혔습니다. 다시 누르고, 뜨는 창에서 선생님 구글 계정을 골라 주세요.':c==='auth/network-request-failed'?'인터넷 연결이 안 됩니다. 연결을 확인하고 다시 눌러 주세요.':'로그인이 안 됐습니다. 이 글을 그대로 알려 주세요: '+(c||e);});
};
var STARTED=false;
window.__attVchg=function(){if(STARTED&&!document.hidden)syncAll();};
window.__attUser=function(u){
  if(u){ls(NS+'in','1');pw='g';if(!STARTED)start();else syncAll();}
  else{ls(NS+'in',null);pw='';STARTED=false;showGate(FAILMSG);}
};''')
rep('''  document.getElementById('app').style.display='block';
  render();syncAll();''','''  document.getElementById('app').style.display='block';
  STARTED=true;if(TEST)document.title='출석부 (시험)';
  render();syncAll();''')
rep("  try{S.Q=JSON.parse(ls(NS+'q_'+g)||'[]');}catch(e){S.Q=[];}","  try{S.Q=JSON.parse(ls(NS+'q_'+g)||'[]');}catch(e){S.Q=[];}\n  if(!TEST){try{var oq=JSON.parse(ls('att'+'_q_'+g)||'[]');if(oq&&oq.length){S.Q=oq.concat(S.Q);saveQ(g);}ls('att'+'_q_'+g,null);}catch(e){}}")
rep("pw=ls('att_pw')||'';\nif(pw)start();else showGate('');","pw=ls(NS+'in')==='1'?'g':'';\nif(pw)start();else showGate('');")
rep('</body>','''<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, signInWithRedirect, getRedirectResult, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-auth.js";
const auth=getAuth(initializeApp({apiKey:"AIzaSyC88G-OjMJOqVqnIVqunzh7fvk91wtKKnA",authDomain:"nolbada.github.io",projectId:"h-roadmap",appId:"1:575520405083:web:b9f40b64cb0ae3d1a9317e"}));
/* 번호표 문서(v)를 "바뀔 때만" 받는다. 연결되어 있으면 10초마다 다시 읽지 않는다. 주소에 snap=0 을 붙이면 끈다 */
let vUnsub=null;
async function vWatch(u){
  if(/[?&]snap=0/.test(location.search))return;
  if(!u){if(vUnsub){try{vUnsub()}catch(e){}vUnsub=null}window.__attV=null;return}
  if(vUnsub)return;
  vUnsub=()=>{};
  try{
    const {getFirestore,doc,onSnapshot}=await import("https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js");
    const col=/[?&]t=1/.test(location.search)?"att_t":"att";
    vUnsub=onSnapshot(doc(getFirestore(auth.app),col,"v"),s=>{
      if(s.metadata.fromCache)return;
      let n=0;try{n=s.exists()?(JSON.parse(s.data().j).n||0):0}catch(e){}
      const old=window.__attV;window.__attV={n:n};
      if(old&&old.n!==n&&window.__attVchg)window.__attVchg();
    },()=>{window.__attV=null;vUnsub=null});
  }catch(e){window.__attV=null;vUnsub=null}
}
let first=true;
onAuthStateChanged(auth,u=>{
  if(first){first=false;window.__attReady({
    token:()=>auth.currentUser?auth.currentUser.getIdToken():Promise.reject({auth:1}),
    /* 로그인 창(팝업)이 막히는 폰에서는 창을 띄우지 않고 구글 화면으로 갔다가 돌아오는 방식으로 다시 시도한다 */
    signIn:()=>{const p=new GoogleAuthProvider();p.setCustomParameters({prompt:"select_account"});return signInWithPopup(auth,p).catch(e=>{const c=e&&e.code||"";if(c==="auth/popup-blocked"||c==="auth/operation-not-supported-in-this-environment"||c==="auth/web-storage-unsupported"){try{sessionStorage.setItem("att_redir","1")}catch(x){}return signInWithRedirect(auth,p);}throw e;});},
    signOut:()=>signOut(auth),
    email:()=>auth.currentUser?auth.currentUser.email:''
  });}
  window.__attUser(u);
  vWatch(u);
  let rd=null;try{rd=sessionStorage.getItem("att_redir");sessionStorage.removeItem("att_redir")}catch(x){}
  if(rd&&!u){const g=document.getElementById("gerr");if(g)g.textContent="이 브라우저에서는 구글 로그인이 끝까지 되지 않았습니다. 크롬 앱에서 이 주소를 열어 다시 눌러 주세요.";}
});
getRedirectResult(auth).catch(e=>{const g=document.getElementById("gerr");if(g)g.textContent="로그인이 안 됐습니다. 이 글을 그대로 알려 주세요: "+(e&&e.code||e);});
</script>
</body>''')
s=s.replace('<head>','<head>\n<meta name="robots" content="noindex,nofollow">',1) if 'noindex' not in s else s
io.open('attend-g/index.html','w',encoding='utf-8').write(s)
assert s.count('src="attfs.js?v=')==1
io.open('attend/index.html','w',encoding='utf-8').write(s.replace('src="attfs.js?v=','src="../attend-g/attfs.js?v='))
print('ok',len(s))
