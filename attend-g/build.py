# attend/index.html (비밀번호 방식) -> attend-g/index.html (구글 로그인 + Firebase 직통) 변환기
# 사용: python3 attend-g/build.py   (via 저장소 맨 위에서)
import re,io
s=io.open('attend/index.html',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    c=s.count(a)
    assert c==n,(a[:50],c)
    s=s.replace(a,b)
rep('''  <input id="pwin" type="password" placeholder="비밀번호" autocomplete="current-password">
  <button class="p" id="pwok" style="width:100%">확인</button>''','''  <button class="p" id="glog" style="width:100%">구글로 로그인</button>''')
rep('<script>\n(function(){\nvar API=','<script src="attfs.js?v=261117a"></script>\n<script>\n(function(){\nvar TEST=/[?&]t=1/.test(location.search),NS=TEST?\'attt_\':\'attg_\';\nvar AUTHW=[],AUTHR=null;window.__attReady=function(a){AUTHR=a;AUTHW.splice(0).forEach(function(f){f();});};\nfunction authReady(){return new Promise(function(z){if(AUTHR)z();else AUTHW.push(z);});}\nvar STORE=AttFs.make({col:TEST?\'att_t\':\'att\',token:function(){return authReady().then(function(){return AUTHR.token();});}});\nvar API=')
rep("'att_q_'","NS+'q_'",2)
rep("'att_s_'","NS+'s_'",2)
rep('''  var c=new AbortController(),tm=setTimeout(function(){c.abort();},40000);
  return fetch(API,{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(body),signal:c.signal}).then(function(r){clearTimeout(tm);return r.json();},function(e){clearTimeout(tm);throw e;});''','''  return new Promise(function(ok,no){var tm=setTimeout(function(){no(new Error('timeout'));},40000);STORE.post(body).then(function(r){clearTimeout(tm);ok(r);},function(e){clearTimeout(tm);no(e);});});''')
rep("ls('att_pw',null);pw='';showGate('비밀번호가 맞지 않습니다');return;","authFail();return;",2)
rep('''document.getElementById('pwok').onclick=function(){
  var v=document.getElementById('pwin').value;if(!v)return;
  pw=v;ls('att_pw',v);start();
};
document.getElementById('pwin').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('pwok').click();});''','''function authFail(){ls(NS+'in',null);pw='';showGate('이 계정으로는 열 수 없습니다. 선생님 계정으로 로그인해 주세요.');if(AUTHR)AUTHR.signOut();}
document.getElementById('glog').onclick=function(){
  var b=this;document.getElementById('gerr').textContent='';
  if(!AUTHR){document.getElementById('gerr').textContent='준비 중입니다. 잠시 뒤 다시 눌러 주세요.';return;}
  b.disabled=true;AUTHR.signIn().then(function(){b.disabled=false;},function(e){b.disabled=false;var c=e&&e.code||'';document.getElementById('gerr').textContent=c==='auth/popup-blocked'?'로그인 창이 막혔습니다. 크롬에서 열어 주세요.':(c==='auth/popup-closed-by-user'||c==='auth/cancelled-popup-request')?'':'로그인 실패: '+(c||e);});
};
var STARTED=false;
window.__attUser=function(u){
  if(u){ls(NS+'in','1');pw='g';if(!STARTED)start();else syncAll();}
  else{ls(NS+'in',null);pw='';STARTED=false;showGate('');}
};''')
rep('''  document.getElementById('app').style.display='block';
  render();syncAll();''','''  document.getElementById('app').style.display='block';
  STARTED=true;if(TEST)document.title='출석부 (시험)';
  render();syncAll();''')
rep("pw=ls('att_pw')||'';\nif(pw)start();else showGate('');","pw=ls(NS+'in')==='1'?'g':'';\nif(pw)start();else showGate('');")
rep('</body>','''<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.14.1/firebase-auth.js";
const auth=getAuth(initializeApp({apiKey:"AIzaSyC88G-OjMJOqVqnIVqunzh7fvk91wtKKnA",authDomain:"h-roadmap.firebaseapp.com",projectId:"h-roadmap",appId:"1:575520405083:web:b9f40b64cb0ae3d1a9317e"}));
let first=true;
onAuthStateChanged(auth,u=>{
  if(first){first=false;window.__attReady({
    token:()=>auth.currentUser?auth.currentUser.getIdToken():Promise.reject({auth:1}),
    signIn:()=>{const p=new GoogleAuthProvider();p.setCustomParameters({prompt:"select_account"});return signInWithPopup(auth,p);},
    signOut:()=>signOut(auth)
  });}
  window.__attUser(u);
});
</script>
</body>''')
s=s.replace('<head>','<head>\n<meta name="robots" content="noindex,nofollow">',1) if 'noindex' not in s else s
io.open('attend-g/index.html','w',encoding='utf-8').write(s)
print('ok',len(s))
