(function(){
"use strict";
const DAYS=Object.keys(window.VL_DATA).map(Number).sort((a,b)=>a-b);
const hk=s=>{let h=7;for(const c of String(s))h=(h*31+c.charCodeAt(0))%100003;return h%100;};
const D=(()=>{const m={judge:[],broken:[],deriv:[],family:[],conf:[],w24:[],poly:[]};
 DAYS.forEach(n=>{const d=window.VL_DATA[n];Object.keys(m).forEach(k=>{(d[k]||[]).forEach(x=>{x._day=n;m[k].push(x);});});});
 m.judge=m.judge.filter(x=>x.rel!=='관계없음'||hk(x.id)<75);
 m.broken=m.broken.filter(x=>(x.bad&&x.orig)||hk(x.id)<80);
 const d1=window.VL_DATA[DAYS[0]];['tip','tipex','tipq','mention'].forEach(k=>{m[k]=d1[k];});return m;})();
const DAYTXT=DAYS.length>1?'DAY '+DAYS[0]+'~'+DAYS[DAYS.length-1]:'DAY '+DAYS[0];
const $=document.getElementById('app');
const KEY='vl_state_v2';
let S={log:[],weak:{},lv:{},tipSeen:0,sr:{}};
try{const r=localStorage.getItem(KEY);if(r)S=Object.assign(S,JSON.parse(r));}catch(e){}
// 사용시간: 화면을 벗어난 시간, 30초 넘게 아무 동작 없던 시간은 제외
let lastAct=Date.now(),actSec=0;
const IDLE=30000;
const tick=()=>{const n=Date.now();if(!document.hidden){actSec+=Math.min(n-lastAct,IDLE)/1000;}lastAct=n;};
['pointerdown','keydown','touchstart','scroll'].forEach(e=>addEventListener(e,tick,{passive:true}));
document.addEventListener('visibilitychange',()=>{if(document.hidden){actSec+=Math.min(Date.now()-lastAct,IDLE)/1000;lastAct=Date.now();}else{lastAct=Date.now();}});
const fmtT=s=>{s=Math.round(s);return s>=60?Math.floor(s/60)+'분 '+(s%60)+'초':s+'초';};
const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(S));}catch(e){}};
const shuffle=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]];}return a;};
const strip=h=>String(h||'').replace(/<[^>]+>/g,'');
const esc=s=>String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const norm=w=>w.toLowerCase().replace(/[^a-z']/g,'');
const sb=(en,ko,label)=>`<div class="sb"><div>${esc(strip(en))}</div><div class="sub">${esc(strip(ko))}${label?` <span class="tag">${label}</span>`:''}</div></div>`;
const ownerOf={},senseInfo={};D.poly.forEach(p=>p.senses.forEach(s=>{ownerOf[s.sense]=p.word;senseInfo[s.sense]=Object.assign({word:p.word},s);}));
const exBlock=(w,ex,gl)=>`<div class="sb"><b>${w}</b>${gl?' = '+esc(gl):''}${sb(ex.en,ex.ko,ex.src==='book'?'책 문장':ex.src==='cam'?'Cambridge Dictionary':'예문')}</div>`;
const famSent={};D.deriv.forEach(d=>{if(!famSent[d.ans])famSent[d.ans]={en:d.en,ko:d.ko,src:'book'};});

// ---------- 모드 (종이 PART2 순서) ----------
const MODES=[
 ['judge','① 짝 판별','유의어? 반의어? 관계없음?',()=>D.judge.map(x=>({t:'judge',id:x.id,d:x}))],
 ['poly1','② 다의어: 뜻 모두 찾기','단어 하나의 뜻을 전부 눌러요',()=>D.poly.map(p=>({t:'poly1',id:'ST-'+p.word,d:p}))],
 ['poly2','③ 다의어: 뜻 → 문장','이 뜻으로 쓰인 문장은?',()=>D.poly.flatMap(p=>p.senses.map((s,i)=>({t:'poly2',id:'RV-'+p.word+'-'+i,d:{word:p.word,target:i,senses:p.senses}})))],
 ['deriv','④ 파생어 사다리','같은 어근 가족, 자리에 맞는 모양',()=>D.deriv.map(x=>({t:'deriv',id:x.id,d:x}))],
 ['w24','⑤ 오답 24 체크','보기에 나왔던 단어, 뜻 맞히기 (+ 쓰기 몇 개)',()=>D.w24.map(x=>({t:'w24',id:x.id,d:x}))],
 ['broken','⑥ 고장 난 문장','틀린 곳 있음? 없음?',()=>D.broken.map(x=>({t:'broken',id:x.id,d:x}))]
];
const poolOf=k=>MODES.find(m=>m[0]===k)[3]();
const allItems=()=>MODES.filter(m=>m[3]).flatMap(m=>m[3]());
const weakIds=()=>Object.keys(S.weak).filter(k=>S.weak[k]>0);
const NAME={judge:'짝 판별',poly1:'다의어 뜻 찾기',poly2:'다의어 뜻→문장',deriv:'파생어 사다리',w24:'오답 24',broken:'고장 난 문장',};

let Q=[],cur=null,total=0,doneN=0,round=null,answered=false;

function home(){
 const wk=weakIds().length,done=S.doneDay===dayNo(),P=plan(done?1:0);
 const met=Object.keys(S.sr).length,grad=Object.values(S.sr).filter(e=>e.done).length,dn=dueWords().length;
 $.innerHTML=`<h1>보카링크 VOCA LINK</h1><div class="sub">${DAYTXT} · 동남비타민영어학원</div>
 <div class="stats"><div><b>${met}</b><span>지금까지 만난 단어</span></div><div><b>${dn}</b><span>복습할 때가 된 단어</span></div><div><b>${grad}</b><span>완전히 외운 단어</span></div></div>
 <div class="today">${done?'다음 구성':'오늘 구성'} ${[['c-new','오늘부터 1일',P.n],['c-weak','왜 자꾸 날 잊어?',P.w],['c-rev','우리 만났었지?',P.r]].filter(a=>a[2]>0).map(a=>`<b class="${a[0]}">${a[1]} ${a[2]}</b>`).join(' · ')}</div>
 ${done?'<button class="btn" disabled style="opacity:.6">오늘 20문제 끝! 다음에 또 만나요</button>':'<button class="btn pri" data-go="daily">오늘의 20문제</button>'}
 <button class="btn" data-go="stats">내 기록</button>
 <div class="card why"><h2>하루 20문제는 이렇게 짜여요</h2>
 <div class="sub" style="margin-bottom:8px">첫날은 20문제가 모두 새 단어예요. 둘째 날부터 아래 세 가지가 섞여 나와요.</div>
 <div class="wy"><b class="c-new">오늘부터 1일</b>새 단어예요. 처음 하는 날은 20문제, 다음 날부터는 매일 6문제예요.</div>
 <div class="wy"><b class="c-weak">왜 자꾸 날 잊어?</b>틀렸던 단어(오답)가 돌아와요. 3~6문제예요.</div>
 <div class="wy"><b class="c-rev">우리 만났었지?</b>앞에서 본 단어(누적 복습)예요. 복습할 때가 된 단어가 나머지를 채워요. 뒤로 갈수록 이 비중이 커져요.</div></div>
 <div class="card why"><h2>이 앱은 이렇게 설계되었어요</h2>
 <div class="wy"><b>혼자서는 안 하게 되는 복습</b>누적 복습과 틀린 단어 복습을 앱이 알아서 시켜요. 날짜를 기억하거나 고를 필요가 없어요.</div>
 <div class="wy"><b>간격 복습</b>틀린 단어는 내일, 맞힌 단어는 3일 · 7일 · 14일 뒤에 다시 만나요. 잊을 만할 때 다시 보면 오래 남아요.</div>
 <div class="wy"><b>꺼내 쓰기</b>보고 읽는 대신 직접 골라서 기억을 꺼내요. 읽기만 하는 것보다 기억에 더 오래 남는다고 알려져 있어요.</div>
 <div class="wy"><b>검증된 문제만</b>교재에 실린 단어와 문제만 써요. 정답이 하나로 확인된 것만 넣고, 애매한 문제는 뺐어요.</div></div>
 ${/[?&]t=1/.test(location.search)?`<button class="btn" data-go="next" style="color:#999;font-size:14px">내일로 넘기기 (선생님 테스트용)</button>
 <button class="btn" data-go="reset" style="color:#999;font-size:14px">기록 지우기 (선생님 테스트용)</button>`:''}`;
 $.querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>{const g=b.dataset.go;if(g==='next'){S.off=(S.off||0)+1;save();home();return;}if(g==='reset'){if(confirm('이 폰/브라우저의 풀이 기록을 모두 지울까요?')){S={log:[],weak:{},lv:{},tipSeen:0,sr:{}};save();home();}return;}g==='stats'?stats():g==='daily'?startDaily():start(g);});
}
// ---------- 오늘의 20문제: 뷔페식 골라담기 (이미 담은 문제는 제외, 틀린 문제만 다시) ----------
const QUOTA={judge:3,poly1:1,poly2:3,deriv:3,w24:6,broken:3};
const QSUM=Object.values(QUOTA).reduce((a,b)=>a+b,0);
// ---- 간격 복습(라이트너): 틀리면 내일, 맞히면 3일→7일→14일 뒤에 다시. 3번 연속 이어서 맞히면 졸업 ----
let SHIFT=0;
const dayNo=()=>Math.floor((Date.now()+9*36e5)/864e5)+SHIFT+(S.off||0);
const GAP=[1,3,7,14],DUE_MAX=6;
// ---- 단어 단위 간격 복습: 처음 만난 단어는 맞히면 3일 뒤, 틀리면 내일. 복습에서 맞히면 간격 3→7→14일, 틀리면 다시 내일 ----
// 고장 난 문장이 어떤 단어를 공부시키는지 직접 지정
const BW={'S1-1-X':'exist','S1-3-X':'neglect','S1-5-X':'add','C1-1-X':'country','C1-2-X':'country','C1-3-O':'country','C1-4-X':'accept','C1-5-X':'accept','C1-6-O':'accept','D1-2-X':'competition','D1-3-X':'competitive','D1-5-X':'competence','D1-6-X':'competent','D1-1-O':'compete','D1-4-O':'competitor','D1-7-O':'competition','S1-2-Y':'property','S1-4-Y':'deceive','S1-6-Y':'experience','S1-8-Y':'catastrophe','S1-7-O':'induce','S2-7-X':'merge','C2-1-X':'active','C2-2-X':'active','C2-3-X':'actual','C2-5-X':'fall','C2-6-X':'fall','D2-1-X':'create','D2-2-X':'creation','D2-3-X':'creative','D2-4-X':'creativity','D2-5-X':'creator','D2-7-X':'creation','S2-2-Y':'event','S2-4-Y':'describe','S2-5-Y':'choice','S2-8-Y':'diminish','S2-3-O':'tension','S2-6-O':'field','D2-6-O':'creature','P2-4-O':'branch'};
function wordKey(i){const d=i.d;
 if(i.t==='judge')return norm(d.a);
 if(i.t==='w24')return norm(d.w);
 if(i.t==='deriv')return norm(d.ans);
 if(i.t==='poly1'||i.t==='poly2')return norm(d.word);
 if(i.t==='broken')return BW[i.id]||('s:'+i.id); return i.id;}
let _hs=null;function headSet(){if(!_hs){_hs=new Set();D.judge.forEach(x=>_hs.add(norm(x.a)));D.w24.forEach(x=>_hs.add(norm(x.w)));D.deriv.forEach(x=>_hs.add(norm(x.ans)));D.poly.forEach(x=>_hs.add(norm(x.word)));}return _hs;}
const wordPool=()=>{const m={};['judge','poly1','poly2','deriv','w24','broken'].forEach(k=>poolOf(k).forEach(i=>{(m[wordKey(i)]=m[wordKey(i)]||[]).push(i);}));return m;};
function srUpdate(w,ok){const e=S.sr[w],t=dayNo();
 if(!e){S.sr[w]=ok?{b:1,due:t+GAP[1],wrong:0}:{b:0,due:t+1,wrong:1};return;}
 if(!ok){S.sr[w]={b:0,due:t+1,wrong:1};return;}
 if(e.done||e.due>t)return; // 때가 안 된 단어를 연습으로 맞힌 건 간격에 반영하지 않음
 const b=e.b+1;
 if(b>=GAP.length){S.sr[w]={b:4,due:0,done:1,wrong:0};return;}
 S.sr[w]={b,due:t+GAP[b],wrong:0};}
const dueWords=()=>{const t=dayNo();return Object.keys(S.sr).filter(w=>!S.sr[w].done&&S.sr[w].due<=t).sort((x,y)=>S.sr[x].due-S.sr[y].due);};
const dueIds=dueWords;
function nextDue(){const t=dayNo();const d=Object.keys(S.sr).filter(w=>!S.sr[w].done&&S.sr[w].due>t).map(w=>S.sr[w].due);return d.length?Math.min(...d)-t:0;}
function seenSet(){return new Set(Object.keys(S.sr));}
function unseenCount(){const sn=seenSet();return Object.keys(QUOTA).reduce((n,k)=>n+poolOf(k).filter(i=>!sn.has(i.id)).length,0);}
function pastWrong(wp,have){ // 예전에 한 번이라도 틀렸고 아직 졸업 못 한 단어 (많이 틀린 순)
 const id2w={};Object.keys(wp).forEach(w=>wp[w].forEach(i=>id2w[i.id]=w));
 const cnt={};S.log.forEach(l=>{if(!l.ok&&id2w[l.id])cnt[id2w[l.id]]=(cnt[id2w[l.id]]||0)+1;});
 return Object.keys(cnt).filter(w=>S.sr[w]&&!S.sr[w].done&&!(have&&have.has(w))).sort((a,b)=>cnt[b]-cnt[a]);}
function plan(sh){SHIFT=sh||0;try{return planRaw();}finally{SHIFT=0;}}
function planRaw(){ // 홈에 보여 줄 구성 (startDaily와 같은 규칙). plan(1)=내일 기준
 const N=20,wp=wordPool(),due=dueWords().filter(w=>wp[w]);
 if(!Object.keys(S.sr).length)return{n:20,w:0,r:0};
 const wd=due.filter(w=>S.sr[w].wrong),rd=due.length-wd.length;
 let w=Math.min(6,wd.length);
 if(w<3)w=Math.min(3,wd.length+pastWrong(wp,new Set(wd)).length);
 const n=Math.max(3,Math.min(6,N-w-rd));return{n,w,r:N-n-w};}
function startDaily(){
 const N=20,WEAK_MAX=6,WEAK_MIN=3;
 const wp=wordPool(),keys=Object.keys(wp);
 const due=dueWords();
 const weak=shuffle(due.filter(w=>S.sr[w].wrong&&wp[w]));
 const rev=shuffle(due.filter(w=>!S.sr[w].wrong&&wp[w]));
 const dayOf=w=>Math.min(...wp[w].map(i=>i.d._day||1)); // 새 단어는 앞 DAY부터 차례로
 const byDay=a=>shuffle(a).sort((x,y)=>dayOf(x)-dayOf(y));
 const fresh=byDay(keys.filter(w=>!S.sr[w]));
 const logged=new Set(S.log.map(l=>l.id));
 const CAP={judge:4,poly1:2,poly2:3,deriv:3,w24:4,broken:4},used={};
 const out=[],have=new Set();
 // 한 단어에 문제 하나를 배정 (아직 안 푼 유형 우선, 유형별 하루 상한 적용)
 const add=(w,th,force)=>{if(have.has(w))return false;const its=wp[w],lf=its.filter(i=>!logged.has(i.id));
  let cand=shuffle(lf.length?lf:its);if(!force)cand=cand.filter(i=>(used[i.t]||0)<CAP[i.t]);
  if(!cand.length)return false;let it=cand[0];if(it.t==='judge'){const wantNR=Math.random()>=0.7,m=cand.find(i=>i.t==='judge'&&((i.d.rel==='관계없음')===wantNR));if(m)it=m;}used[it.t]=(used[it.t]||0)+1;have.add(w);out.push([it,th]);return true;};
 const take=(arr,n,th,force)=>{let c=0;for(let k=0;k<arr.length&&c<n;k++){if(add(arr[k],th,force)){arr.splice(k,1);k--;c++;}}return c;};
 // 구성: 첫 만남 6(복습이 몰리면 최소 3, 맨 첫날만 20) + 틀린 단어 최대 6 + 나머지는 시기가 된 복습. 다의어 2유형은 첫 만남에 매일 포함
 const first=!Object.keys(S.sr).length,NEWQ=first?N:Math.max(3,Math.min(6,N-Math.min(weak.length,WEAK_MAX)-rev.length));
 const addT=(w,t)=>{if(have.has(w))return false;const its=(wp[w]||[]).filter(i=>i.t===t);if(!its.length)return false;
  const lf=its.filter(i=>!logged.has(i.id)),it=shuffle(lf.length?lf:its)[0];used[t]=(used[t]||0)+1;have.add(w);out.push([it,'new']);
  const k=fresh.indexOf(w);if(k>=0)fresh.splice(k,1);return true;};
 const polyW=byDay(fresh.filter(w=>wp[w].some(i=>i.t==='poly2')&&wp[w].some(i=>i.t==='poly1')));
 if(polyW.length>=1)addT(polyW[0],'poly2');
 if(polyW.length>=2)addT(polyW[1],'poly1');
 take(fresh,NEWQ-out.length,'new');
 const gotW=take(weak,WEAK_MAX,'weak');
 if(!first&&gotW<WEAK_MIN)take(pastWrong(wp,have),WEAK_MIN-gotW,'weak',true);
 take(rev,N-out.length,'review');
 // 복습할 때가 된 단어가 모자라면, 새 단어가 아니라 앞에서 만난 단어(아직 때가 안 된 것, 곧 올 순서)로 채움
 let ndN=0;if(out.length<N){const t0=dayNo(),nd=Object.keys(S.sr).filter(w=>wp[w]&&!S.sr[w].done&&S.sr[w].due>t0).sort((a,b)=>S.sr[a].due-S.sr[b].due);ndN=take(nd,N-out.length,'review');if(out.length<N)ndN+=take(nd,N-out.length,'review',true);}
 take(fresh,N-out.length,'new');
 // 새 단어가 모자라면 복습 대기 단어로, 그래도 모자라면 상한을 풀고 채움
 if(out.length<N)take(weak,N-out.length,'weak');
 if(out.length<N)take(rev,N-out.length,'review');
 if(out.length<N)take(fresh,N-out.length,'new',true);
 const newTotal=out.filter(o=>o[1]==='new').length+fresh.length;
 const dueN=out.filter(o=>o[1]!=='new').length-ndN;
 let review=0;
 if(out.length<N){const rest=shuffle(keys.filter(w=>!have.has(w)));for(const w of rest){if(out.length>=N)break;if(add(w,'review',true))review++;}}
 const TH={new:['오늘부터 1일','오늘 처음 만나는 단어예요.'],review:['우리 만났었지?','앞에서 본 적 있는 단어예요. 기억나는지 확인해요.'],weak:['왜 자꾸 날 잊어?','틀렸던 단어가 돌아왔어요. 이번엔 내 걸로 만들어요.']};
 out.forEach(o=>{o[0].tag=TH[o[1]][0]+' — '+TH[o[1]][1];o[0].th=o[1];});
 const TO={new:0,review:1,weak:2};
 const pool=[0,1,2].flatMap(n=>shuffle(out.filter(o=>TO[o[1]]===n))).map(o=>o[0]);
 newRound('daily');Q=pool;total=Q.length;doneN=0;
 const pend=Object.values(S.sr).some(e=>!e.done);
 const none=newTotal===0&&dueN===0&&!pend,wait=newTotal===0&&dueN===0&&pend;
 if(newTotal<N||none){
  const msg=wait?`오늘 복습할 단어는 다 했어요. 다음 복습은 ${nextDue()}일 뒤에 돌아와요. 오늘은 앞에서 공부한 단어를 가볍게 섞어서 풀어요.`:none?'더 이상 새로 만날 단어가 없어요. 앞에서 공부한 단어를 섞어서 마무리해요.':(newTotal===0?'새로 만날 단어는 모두 만났어요. ':`새로 만날 단어가 ${newTotal}개 남았어요. `)+`오늘은 복습 단어 ${dueN}개를 풀어요.`;
  $.innerHTML=`<div class="top"><button class="back" id="bk">← 처음으로</button></div>
  <div class="card"><h2>${none?'축하합니다! '+DAYTXT+'은 정말 모두 완료했어요!':wait?'오늘 복습은 다 했어요':(newTotal===0?'새 단어는 모두 만났어요':DAYTXT+' 새 단어가 거의 끝났어요')}</h2>
  <div>${msg}</div></div>
  <button class="btn pri" id="st">시작하기</button>`;
  document.getElementById('bk').onclick=home;document.getElementById('st').onclick=next;return;
 }
 next();
}
function newRound(mode){tick();actSec=0;round={mode,okN:0,wrongN:0,firstOk:0,firstN:0,cards:[]};}
function start(mode){
 let pool;
 if(mode==='weak'){const ids=new Set(weakIds());pool=allItems().filter(i=>ids.has(i.id));}
 else{
  pool=shuffle(poolOf(mode));if(mode==='judge'){const re=pool.filter(i=>i.d.rel!=='관계없음'),nr=pool.filter(i=>i.d.rel==='관계없음');pool=shuffle([...re,...nr.slice(0,Math.round(re.length*3/7))]);}
  if(mode==='w24'){pool=pool.slice(0,24);const ws=shuffle(D.w24).slice(0,3).map(x=>({t:'w24w',id:'WW-'+x.w,d:x}));
   pool=shuffle(pool);[9,15,21].forEach((pos,k)=>pool.splice(pos+k,0,ws[k]));}
  else if(mode==='poly1')pool=pool.slice(0,5);
  else pool=pool.sort((a,b)=>(S.weak[b.id]>0)-(S.weak[a.id]>0)).slice(0,10);
 }
 newRound(mode);Q=(mode==='w24')?pool:shuffle(pool);total=Q.length;doneN=0;next();
}
function next(){if(!Q.length)return summary();cur=Q.shift();answered=false;render();}
function frame(inner){
 $.innerHTML=`<div class="top"><button class="back" id="bk">← 그만하기</button><span class="sub">${doneN}/${total}</span></div>
 <div class="bar"><i style="width:${total?doneN/total*100:0}%"></i></div>${cur&&cur.tag?`<div class="pick"><b class="${({'오늘부터 1일':'c-new','왜 자꾸 날 잊어?':'c-weak','우리 만났었지?':'c-rev'})[cur.tag.split(' — ')[0]]||''}">${cur.tag.split(' — ')[0]}</b>${cur.tag.split(' — ').slice(1).join(' — ')}</div>`:''}${inner}`;
 document.getElementById('bk').onclick=()=>{tick();S.totalSec=(S.totalSec||0)+actSec;actSec=0;save();home();};
}
function render(){({judge:rJudge,broken:rBroken,deriv:rDeriv,poly1:rPoly1,poly2:rPoly2,w24:rW24,w24w:rW24w})[cur.t]();}

// ---------- 공통: 채점/기록/재출제/오답카드 ----------
function cardOf(it){
 const x=it.d;
 switch(it.t){
  case 'judge':return `<b>${x.a}</b> (${esc(x.a_ko)}) – <b>${x.b}</b> (${esc(x.b_ko)}) → ${x.rel}`;
  case 'poly1':return `<b>${x.word}</b>: ${x.senses.map(s=>esc(s.sense)).join(' / ')}`;
  case 'poly2':return `<b>${x.word}</b> = ${esc(x.senses[x.target].sense)}`;
  case 'deriv':return `<b>${x.ans}</b> (${x.pos}) ${esc(x.gloss)}`;
  case 'w24':case 'w24w':return `<b>${x.w}</b> ${esc(x.ko)}`;
  case 'broken':return x.bad?`${esc(strip(x.orig))}<br><span class="sub">${esc(strip(x.ko))}</span>`:null;
 }
 return null;
}
function record(correct,extra,silentNext){
 const first=cur.r===undefined;
 S.log.push(Object.assign({id:cur.id,t:cur.t,ok:correct?1:0,at:Date.now()},extra||{}));
 if(S.log.length>2000)S.log=S.log.slice(-2000);
 if(first){srUpdate(wordKey(cur),correct);round.firstN++;if(correct)round.firstOk++;else{const c=cardOf(cur);if(c)round.cards.push(c);}}
 if(correct){round.okN++;if(S.weak[cur.id]>0)S.weak[cur.id]-=1;doneN++;}
 else{round.wrongN++;S.weak[cur.id]=2;cur.r=(cur.r||0)+1;
  if(cur.r<=2){cur.tag='방금 틀렸어요 — 바로 한 번 더!';Q.splice(Math.min(3,Q.length),0,cur);}else doneN++;}
 save();
}
function afterAnswer(correct,html){
 answered=true;
 document.getElementById('fbbox').innerHTML=`<div class="fb ${correct?'ok':'bad'}">${correct?'정답!':'아쉬워요'} ${html}</div><button class="btn pri" id="nx">다음</button>`;
 document.getElementById('nx').onclick=next;
}

// ---------- ① 짝 판별
function rJudge(){
 const x=cur.d;
 frame(`<div class="card"><div class="sub">두 단어의 관계는?</div>
 <div class="pair"><span id="wa">${x.a}</span><em>↔</em><span id="wb">${x.b}</span></div>
 ${['유의어','반의어','관계없음'].map(r=>`<button class="btn" data-a="${r}">${r}<small>${{유의어:'비슷한 뜻',반의어:'반대 뜻',관계없음:'둘 사이에 연결이 없어요'}[r]}</small></button>`).join('')}
 <div id="fbbox"></div></div>`);
 $.querySelectorAll('[data-a]').forEach(b=>b.onclick=()=>{
  if(answered)return;const ok=b.dataset.a===x.rel;
  $.querySelectorAll('[data-a]').forEach(y=>{if(y.dataset.a===x.rel)y.classList.add('ok');});
  if(!ok)b.classList.add('bad');
  document.getElementById('wa').innerHTML=`${x.a}<br><small class="sub">${esc(x.a_ko)}</small>`;
  document.getElementById('wb').innerHTML=`${x.b}<br><small class="sub">${esc(x.b_ko)}</small>`;
  record(ok,{pick:b.dataset.a});
  afterAnswer(ok,`<b>${x.a}</b>(${esc(x.a_ko)}) – <b>${x.b}</b>(${esc(x.b_ko)}) → <b>${x.rel}</b>${exBlock(x.a,x.a_ex)}${exBlock(x.b,x.b_ex)}`,['뜻을 몰랐어요','비슷해서 헷갈렸어요','그냥 찍었어요']);
 });
}

// ---------- ② 다의어: 뜻 모두 찾기
function rPoly1(){
 const p=cur.d,chips=shuffle([...p.senses.map(s=>s.sense),...p.decoys]),sel=new Set();
 frame(`<div class="card"><div class="sub">이 단어가 가진 뜻을 <b>전부</b> 눌러요. (다른 단어의 뜻도 섞여 있어요)</div>
 <div class="pair"><span>${p.word}</span></div>
 <div id="chs">${chips.map(c=>`<button class="btn chipb" data-c="${esc(c)}">${esc(c)}</button>`).join('')}</div>
 <button class="btn pri" id="ck">확인</button><div id="fbbox"></div></div>`);
 $.querySelectorAll('[data-c]').forEach(b=>b.onclick=()=>{
  if(answered)return;const c=b.dataset.c;sel.has(c)?sel.delete(c):sel.add(c);b.classList.toggle('sel');});
 document.getElementById('ck').onclick=()=>{
  if(answered||!sel.size)return;
  const truth=new Set(p.senses.map(s=>s.sense));
  const missed=p.senses.filter(s=>!sel.has(s.sense)),wrong=[...sel].filter(c=>!truth.has(c));
  const ok=!missed.length&&!wrong.length;
  $.querySelectorAll('[data-c]').forEach(b=>{const c=b.dataset.c;
   if(truth.has(c))b.classList.add(sel.has(c)?'ok':'miss');else if(sel.has(c))b.classList.add('bad');});
  document.getElementById('ck').style.display='none';
  record(ok,{missed:missed.length,wrong:wrong.length});
  let h=ok?`<b>${p.word}</b>의 뜻 ${p.senses.length}개를 모두 찾았어요!`:`<b>${p.word}</b>의 뜻은 ${p.senses.length}개예요.`;
  if(missed.length)h+=`<div class="sub" style="margin-top:6px">놓친 뜻 </div>`+missed.map(s=>exBlock(p.word,s,s.sense)).join('');
  if(wrong.length)h+=`<div class="sub" style="margin-top:6px">잘못 누른 뜻은 다른 단어의 뜻이에요 </div>`+wrong.map(w=>{const i=senseInfo[w];return i?exBlock(i.word,i,w):'';}).join('');
  afterAnswer(ok,h,['뜻이 여러 개인 줄 몰랐어요','뜻 자체를 몰랐어요','다른 단어 뜻과 헷갈렸어요','그냥 찍었어요']);
 };
}

// ---------- ④ 다의어: 뜻 → 문장 ----------
function rPoly2(){
 const x=cur.d,t=x.senses[x.target];
 const others=shuffle(x.senses.filter((_,i)=>i!==x.target)).slice(0,2);
 const opts=shuffle([t,...others]);
 frame(`<div class="card"><div class="sub"><b>${x.word}</b>가 이 뜻으로 쓰인 문장은?</div>
 <div class="pair"><span>${esc(t.sense)}</span></div>
 ${opts.map((o,i)=>`<button class="btn" data-o="${i}" style="text-align:left;font-weight:500">${esc(strip(o.en))}</button>`).join('')}
 <div id="fbbox"></div></div>`);
 $.querySelectorAll('[data-o]').forEach(b=>b.onclick=()=>{
  if(answered)return;const o=opts[+b.dataset.o],ok=o===t;
  $.querySelectorAll('[data-o]').forEach(y=>{if(opts[+y.dataset.o]===t)y.classList.add('ok');});if(!ok)b.classList.add('bad');
  record(ok,{pick:o.sense});
  afterAnswer(ok,opts.map(q=>`<div class="sb"><b>${esc(q.sense)}</b>${sb(q.en,q.ko,q.src==='book'?'책 문장':q.src==='cam'?'Cambridge Dictionary':'예문')}</div>`).join(''),['뜻을 몰랐어요','문장 속 단서를 못 찾았어요','그냥 찍었어요']);
 });
}

// ---------- ④ 파생어 사다리
function rDeriv(){
 const x=cur.d,lv=S.lv[x.id]||0,sent=strip(x.en.replace(/<b>.*?<\/b>/,'_____'));
 const lvTxt=['① 고르기','② 첫 글자 힌트','③ 직접 쓰기'][lv];
 let body=`<div class="card"><div class="lv">${lvTxt}</div><div class="sent">${esc(sent).replace('_____','<b>_____</b>')}</div>`;
 if(lv===0){
  const rt=x.root||'compete',pick=shuffle(D.family.filter(f=>(f.root||'compete')===rt).map(f=>f.w).filter(w=>w!==x.ans&&!(x.excl||[]).includes(w))).slice(0,3);
  body+=shuffle([x.ans,...pick]).map(o=>`<button class="btn" data-o="${o}">${o}</button>`).join('');
 }else{
  body+=`<div class="sub">${lv===1?`첫 글자: <b>${x.ans[0]}</b> · ${x.ans.length}글자 · ${x.root||'compete'} 가족`:`${x.root||'compete'} 가족 중 알맞은 모양을 써요`}</div>
  <input class="t" id="inp" autocapitalize="none" autocomplete="off" spellcheck="false"><button class="btn pri" id="go">확인</button>`;
 }
 body+='<div id="fbbox"></div></div>';frame(body);
 const judge=val=>{
  if(answered)return;val=val.trim().toLowerCase();if(!val)return;
  const ok=val===x.ans;S.lv[x.id]=ok?Math.min(2,lv+1):Math.max(0,lv-1);
  $.querySelectorAll('[data-o]').forEach(b=>{if(b.dataset.o===x.ans)b.classList.add('ok');else if(b.dataset.o===val)b.classList.add('bad');});
  record(ok,{pick:val,lv});
  const f=D.family.find(f=>f.w===x.ans),pf=D.family.find(f=>f.w===val);
  let h=`<b>${x.ans}</b> (${f.pos}) ${esc(f.ko)}<br><span class="sub">${esc(x.slot)}</span>${sb(x.en,x.ko,'책 문장')}`;
  if(!ok&&pf&&famSent[val])h+=`<div class="sub" style="margin-top:6px">고른 <b>${val}</b>는 이런 뜻이에요 </div>${exBlock(val,famSent[val],'('+pf.pos+') '+pf.ko)}`;
  afterAnswer(ok,h,['뜻을 몰랐어요','자리(품사)를 몰랐어요','비슷한 모양에 낚였어요','철자 실수']);
  if(!ok&&(val.endsWith('tion')||val.endsWith('sion')||x.ans.endsWith('tion')))setTimeout(tipCard,350);
 };
 $.querySelectorAll('[data-o]').forEach(b=>b.onclick=()=>judge(b.dataset.o));
 const go=document.getElementById('go');if(go){go.onclick=()=>judge(document.getElementById('inp').value);
  document.getElementById('inp').addEventListener('keydown',e=>{if(e.key==='Enter')judge(e.target.value);});}
}
// 접사 팁 → 품사 문제 2개 (복수 선택, 뜻·예문은 누른 뒤에 공개)
function tipCard(){
 const t=D.tip,m=document.createElement('div');m.className='modal';S.tipSeen++;save();
 m.innerHTML=`<div class="sheet"><div class="sub">방금 틀린 단어, 접사로 정리해요</div>
 <div class="tipbig">${t.suffix} → ${t.pos}</div><div>${t.rule}</div>
 <div class="ex">${t.examples.map(e=>`<span>${e[0]}</span>`).join('')}</div>
 <div style="margin-top:8px"><b>예외!</b> ${t.exc_tail}</div>
 <div class="ex">${t.exceptions.map(e=>`<span>${e[0]}</span>`).join('')}</div><hr><div id="tq"></div></div>`;
 document.body.appendChild(m);
 const nouns=shuffle(D.tipq.filter(q=>q.pos.length===1))[0],excs=shuffle(D.tipq.filter(q=>q.pos.length>1))[0];
 const ask=(q,n,last)=>{
  const sel=new Set();
  document.getElementById('tq').innerHTML=`<div><b>적용 문제 ${n}/2</b> · <b>${q.w}</b> 은 무슨 품사? <span class="sub">(해당하는 걸 모두 골라요)</span></div>
  ${['명사','동사','형용사'].map(o=>`<button class="btn chipb" data-k="${o}">${o}</button>`).join('')}
  <button class="btn pri" id="ck2">확인</button><div id="tf"></div>`;
  m.querySelectorAll('[data-k]').forEach(b=>b.onclick=()=>{const k=b.dataset.k;sel.has(k)?sel.delete(k):sel.add(k);b.classList.toggle('sel');});
  document.getElementById('ck2').onclick=()=>{
   if(!sel.size)return;
   const ok=sel.size===q.pos.length&&q.pos.every(x=>sel.has(x));
   const ex=q.ex.map(e=>`<div class="sb"><b>${q.w}</b> = ${e.pos}${sb(e.en,e.ko,'예문')}</div>`).join('');
   const ans=q.pos.length>1?`<b>${q.w}</b>은 <b>${q.pos.join('·')}</b> 둘 다 돼요. (${esc(q.ko)})`:`<b>${q.w}</b>은 <b>${q.pos[0]}</b>만 돼요. (${esc(q.ko)})`;
   document.getElementById('tf').innerHTML=`<div class="fb ${ok?'ok':'bad'}">${ok?'맞아요!':'다시 골라봐요.'} ${ok?ans:'예문에서 확인해요 '}${ex}</div>`+(ok?`<button class="btn pri" id="tn">${last?'닫기':'다음 문제'}</button>`:'');
   if(ok){document.getElementById('ck2').style.display='none';document.getElementById('tn').onclick=()=>last?m.remove():ask(excs,2,true);}
  };
 };
 ask(nouns,1,false);
}

// ---------- ⑥ 오답 24 체크 / ⑦ 꺼내 쓰기 ----------
function rW24(){
 const x=cur.d,opts=shuffle([{ko:x.ko,ok:1},...x.opts.map(o=>({ko:o.ko,w:o.w}))]);
 frame(`<div class="card"><div class="sub">뜻은?</div><div class="pair"><span>${x.w}</span></div>
 ${opts.map((o,i)=>`<button class="btn" data-o="${i}">${esc(o.ko)}</button>`).join('')}<div id="fbbox"></div></div>`);
 $.querySelectorAll('[data-o]').forEach(b=>b.onclick=()=>{
  if(answered)return;const o=opts[+b.dataset.o],ok=!!o.ok;
  $.querySelectorAll('[data-o]').forEach(y=>{if(opts[+y.dataset.o].ok)y.classList.add('ok');});if(!ok)b.classList.add('bad');
  record(ok,{pick:o.ko});
  afterAnswer(ok,`<b>${x.w}</b> = ${esc(x.ko)}${ok?'':(o.w?`<div class="sub">'${esc(o.ko)}'는 <b>${o.w}</b>의 뜻이에요</div>`:'')}`,['뜻을 몰랐어요','비슷해서 헷갈렸어요','그냥 찍었어요']);
 });
}
function rW24w(){
 const x=cur.d;
 frame(`<div class="card"><div class="sub">영어로 써 보세요</div><div class="pair"><span>${esc(x.ko)}</span></div>
 <div class="sub">첫 글자: <b>${x.w[0]}</b> · ${x.w.length}글자</div>
 <input class="t" id="inp" autocapitalize="none" autocomplete="off" spellcheck="false"><button class="btn pri" id="go">확인</button><div id="fbbox"></div></div>`);
 const judge=()=>{
  if(answered)return;const v=document.getElementById('inp').value.trim().toLowerCase();if(!v)return;
  const ok=v===x.w;record(ok,{pick:v});
  afterAnswer(ok,`<b>${x.w}</b> = ${esc(x.ko)}`,['뜻은 아는데 철자를 몰랐어요','단어가 기억 안 났어요','철자 실수']);
 };
 document.getElementById('go').onclick=judge;
 document.getElementById('inp').addEventListener('keydown',e=>{if(e.key==='Enter')judge();});
}

// ---------- ⑥ 고장 난 문장
function rBroken(){
 let x=cur.d;
 if(x.bad&&x.orig){if(cur.cl===undefined)cur.cl=false;if(cur.cl)x={en:x.orig,ko:x.ko,orig:x.orig,kind:'정상',why:'원래 문장 그대로예요. 이 문장에는 틀린 곳이 없어요.',memo:{}};}
 const has=!!x.bad,toks=strip(x.en).split(/\s+/);
 frame(`<div class="card">
 <div class="sub">아래 영어 문장에 <b>틀린 곳</b>이 있을까요?</div>
 <div class="sent" id="sent">${toks.map((t,i)=>`<span class="w" data-i="${i}">${esc(t)}</span>`).join(' ')}</div>
 <div class="row" id="yn"><button class="btn" data-y="1">틀린 곳 있음</button><button class="btn" data-y="0">없음</button></div>
 <div id="fbbox"></div></div>`);
 const fin=(ok,html)=>{
  toks.forEach((t,i)=>{if(has&&norm(t)===norm(x.bad))$.querySelector(`[data-i="${i}"]`).classList.add('right');});
  record(ok,{kind:x.kind||'정상'});
  afterAnswer(ok,html+sb(x.orig||x.en,x.ko,'책 문장'),['뜻을 몰랐어요','자리·문법을 몰랐어요','비슷한 모양에 낚였어요','그냥 찍었어요']);
 };
 const memoOf=t=>{const m=(x.memo||{})[norm(t)];return `<div class="sub" style="margin-top:6px">방금 누른 <b>${esc(t)}</b>: ${m||'이 단어는 문장에서 맞게 쓰였어요.'}</div>`;};
 $.querySelectorAll('[data-y]').forEach(b=>b.onclick=()=>{
  if(answered)return;
  if(b.dataset.y==='0'){fin(!has,has?`틀린 곳이 있었어요! <b>${x.bad}</b> → ${esc(x.why)}`:esc(x.why));return;}
  document.getElementById('yn').innerHTML='<div class="sub" style="width:100%">틀린 단어를 눌러요</div>';
  $.querySelectorAll('.w').forEach(w=>{w.classList.add('tap');w.onclick=()=>{
   if(answered)return;const tk=toks[+w.dataset.i];
   if(!has){fin(false,`이 문장은 틀린 곳이 없었어요. ${esc(x.why)}${memoOf(tk)}`);return;}
   const ok=norm(tk)===norm(x.bad);
   if(!ok)w.classList.add('wrong');
   fin(ok,ok?`맞아요! ${esc(x.why)}`:`틀린 곳은 <b>${x.bad}</b> 였어요. ${esc(x.why)}${memoOf(tk)}`);};});
 });
}

// ---------- 결과 / 틀린 단어 카드 / 기록 ----------
function cardsHtml(){
 if(!round.cards.length)return '<div class="card"><b>틀린 게 없어요!</b> 종이 PART2도 자신 있게 써 봐요.</div>';
 return `<div class="card"><h2>틀린 카드 ${round.cards.length}개 — 종이 PART2에 옮겨 써요</h2>${round.cards.map(c=>`<div class="sb">${c}</div>`).join('')}</div>`;
}
function summary(){
 tick();const secs=actSec;S.totalSec=(S.totalSec||0)+secs;if(round.mode==='daily')S.doneDay=dayNo();save();
 const w24=round.mode==='w24';
 $.innerHTML=`<h1>한 판 끝!</h1><div class="card"><div style="font-size:30px;font-weight:800">처음에 맞힌 개수 ${round.firstOk} / ${round.firstN}</div>
 <div class="sub">이번 사용시간 <b>${fmtT(secs)}</b> (딴 데 다녀온 시간·멈춰 있던 시간은 빼요)</div>
 ${w24?`<div class="fb ok">종이 PART2 「오늘의 어휘력 체크」 <b>1차</b> 칸에 <b>${round.firstOk}</b> 를 적어요.</div>`:''}
 <div class="sub">틀린 문제는 내일부터 '왜 자꾸 날 잊어?'로 다시 돌아와요.</div></div>
 ${cardsHtml()}<button class="btn pri" id="h">처음으로</button>`;document.getElementById('h').onclick=home;
}
function stats(){
 const by={};S.log.forEach(l=>{const b=by[l.t]=by[l.t]||{n:0,ok:0};b.n++;b.ok+=l.ok;});
 const code=btoa(unescape(encodeURIComponent(JSON.stringify({d:1,by,sec:Math.round(S.totalSec||0)}))));
 $.innerHTML=`<div class="top"><button class="back" id="bk">← 처음으로</button></div><h1>내 기록</h1>
 <div class="card"><table><tr><th>영역</th><th>푼 수</th><th>정답률</th></tr>
 ${Object.keys(NAME).map(k=>`<tr><td>${NAME[k]}</td><td>${(by[k]||{n:0}).n}</td><td>${by[k]?Math.round(by[k].ok/by[k].n*100)+'%':'-'}</td></tr>`).join('')}</table></div>
 <div class="card"><h2>총 사용시간</h2><div><b>${fmtT(S.totalSec||0)}</b></div></div>
 <div class="card"><h2>선생님께 보내기</h2><div class="sub">아래 버튼으로 복사해서 카톡으로 보내요.</div><button class="btn pri" id="cp">기록 코드 복사</button></div>`;
 document.getElementById('bk').onclick=home;
 document.getElementById('cp').onclick=()=>{try{navigator.clipboard.writeText(code);document.getElementById('cp').textContent='복사됨!';}catch(e){prompt('복사해 주세요',code);}};
}
home();
})();
