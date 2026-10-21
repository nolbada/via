(function(){
"use strict";
// 보카링크 1차 테스트(A형) — 시험지에 표시한 답을 앱에 입력 → 제출 → 채점 → 해설/오답 정리.
// 풀다가 나가면 0점을 기록하지 않고 '중간에 나간 횟수'만 센다. 다시 들어오면 처음부터 새로 풀기. 기록은 이 폰에만 저장.
const C='①②③④',N=20,PASS=16,DAYS=30,KEY='vl_test_v1',LIM=2,CODE='8800';
const AV=Array.from({length:DAYS},(_,i)=>i+1);
let $=null,back=null,D=null,pick={};
// 예전에 '나가서 0점'으로 남은 기록(20문항 모두 미응답)은 점수 기록에서 빼고 '중간에 나간 횟수'로 옮긴다.
// 제출은 20문항을 모두 골라야만 되므로 전부 0인 기록은 반드시 이탈 기록이다.
function mig(st){let ch=false;Object.keys(st.d).forEach(k=>{const r=st.d[k],all=[r.first].concat(r.re||[]),ok=all.filter(a=>!/^0+$/.test(a.p)),z=all.length-ok.length;
 if(z){ch=true;st.ab=st.ab||{};st.ab[k]=(st.ab[k]||0)+z;if(ok.length)st.d[k]={first:ok[0],re:ok.slice(1)};else delete st.d[k];}});return ch;}
const load=()=>{try{const v=JSON.parse(localStorage.getItem(KEY)||'null')||{d:{}};if(mig(v))save(v);return v;}catch(e){return{d:{}};}};
const save=v=>{try{localStorage.setItem(KEY,JSON.stringify(v));}catch(e){}};
const stamp=()=>{const d=new Date(),p=x=>String(x).padStart(2,'0');return d.getFullYear()+'.'+p(d.getMonth()+1)+'.'+p(d.getDate())+' '+p(d.getHours())+':'+p(d.getMinutes());};
function add(st,n,rec){const r=st.d[n];if(r)r.re=(r.re||[]).concat([rec]);else st.d[n]={first:rec,re:[]};}
// 풀던 중 화면을 닫았거나 나갔다면 점수는 남기지 않고 '중간에 나간 횟수'만 올린다
function settle(){const st=load();if(!st.pend)return;const n=st.pend.n;st.ab=st.ab||{};st.ab[n]=(st.ab[n]||0)+1;delete st.pend;save(st);}
const best=r=>Math.max.apply(null,[r.first].concat(r.re||[]).map(a=>a.s));
function ensure(n,cb){
 window.VL_TEST=window.VL_TEST||{};
 if(window.VL_TEST[n])return cb(true);
 const s=document.createElement('script');s.src='data/t'+n+'.js?v=2';
 s.onload=()=>cb(!!window.VL_TEST[n]);s.onerror=()=>cb(false);document.head.appendChild(s);
}
function list(){
 settle();
 const st=load();
 let done=0,pass=0;
 for(let n=1;n<=DAYS;n++){const r=st.d[n];if(r){done++;if(best(r)>=PASS)pass++;}}
 $.innerHTML=`<div class="top"><button class="back" id="vb">← 처음으로</button></div><h1>1차 테스트</h1>
 <div class="sub">DAY별 20문제 · ${PASS}개 이상이면 통과 · 칸의 점수는 최고 점수</div>
 <div class="stats"><div><b>${done}</b><span>푼 DAY</span></div><div><b>${pass}</b><span>통과한 DAY</span></div><div><b>${DAYS-done}</b><span>남은 DAY</span></div></div>
 <div class="vt-grid">${Array.from({length:DAYS},(_,i)=>{const n=i+1,r=st.d[n];
  const on=AV.indexOf(n)>=0;
  return `<button class="vt-d${r?(best(r)>=PASS?' p':' f'):''}" data-n="${n}"${on?'':' disabled style="opacity:.4"'}>${n}<small>${r?best(r)+'/'+N:(on?'DAY':'준비 중')}</small></button>`;}).join('')}</div>`;
 document.getElementById('vb').onclick=()=>back();
 $.querySelectorAll('[data-n]').forEach(b=>b.onclick=()=>openDay(+b.dataset.n));
 window.scrollTo(0,0);
}
function openDay(n){
 $.innerHTML=`<div class="top"><button class="back" id="vb">← 목록</button></div><div class="card">DAY ${n} 문제를 불러오는 중…</div>`;
 document.getElementById('vb').onclick=list;
 ensure(n,ok=>{
  if(!ok){$.innerHTML=`<div class="top"><button class="back" id="vb">← 목록</button></div><div class="card">DAY ${n} 문제를 불러오지 못했어요. 인터넷 연결을 확인하고 다시 눌러 주세요.</div>`;document.getElementById('vb').onclick=list;return;}
  D=window.VL_TEST[n];const r=load().d[n];
  if(r){const all=[r.first].concat(r.re||[]);result(n,all.length-1);}else entry(n);
 });
}
// 중간에 나간 횟수가 LIM에 이르면 그 DAY는 잠김 — 선생님 코드를 넣으면 한 번 더 풀 수 있음
function lock(n){
 const ab=(load().ab||{})[n]||0;
 $.innerHTML=`<div class="top"><button class="back" id="vb">← 목록</button></div><h1>DAY ${n} · 1차 테스트</h1>
 <div class="card"><b>중간에 ${ab}번 나가서 잠겼어요.</b><div class="sub" style="margin-top:6px">선생님께 이 화면을 보여 주세요.</div>
 <input id="vk" type="password" inputmode="numeric" maxlength="8" placeholder="선생님 코드" style="margin-top:10px;width:100%;box-sizing:border-box;font:inherit;padding:10px;border:1.5px solid currentColor;border-radius:8px;background:transparent;color:inherit">
 <div class="sub" id="vm" style="margin-top:6px"></div></div>
 <button class="btn pri" id="vo">확인</button>`;
 document.getElementById('vb').onclick=list;
 document.getElementById('vo').onclick=()=>{
  if(document.getElementById('vk').value.trim()===CODE){const st=load();st.ab=st.ab||{};st.ab[n]=LIM-1;save(st);entry(n);}
  else{document.getElementById('vm').textContent='코드가 달라요.';document.getElementById('vk').value='';}
 };
 window.scrollTo(0,0);
}
function entry(n){
 if((((load().ab)||{})[n]||0)>=LIM)return lock(n);
 pick={};
 const st=load();st.pend={n,t:stamp()};save(st); // 제출 전에 나가면 점수 기록 없이 '나간 횟수'만 +1
 let h='';D.forEach((it,i)=>{
  if(i===0||D[i-1].sec!==it.sec)h+=`<div class="vt-sec">${it.sec}</div>`;
  h+=`<div class="vt-row" data-r="${it.n}"><span class="vt-no">${it.n}.</span><div class="vt-pk">${[1,2,3,4].map(k=>`<button data-n="${it.n}" data-k="${k}">${C[k-1]}</button>`).join('')}</div></div>`;
 });
 $.innerHTML=`<div class="top"><button class="back" id="vb">← 나가기</button><span class="sub" id="vc"></span></div><h1>DAY ${n} · 1차 테스트</h1>${h}
 <button class="btn pri" id="vg" disabled>제출</button>`;
 const upd=()=>{const c=Object.keys(pick).length;document.getElementById('vc').textContent=c+'/'+N;const g=document.getElementById('vg');g.disabled=c<N;g.textContent=c<N?'남은 문항 '+(N-c)+'개':'제출';};
 upd();
 document.getElementById('vb').onclick=()=>{if(confirm('지금 나가면 이번 시험은 점수가 기록되지 않아요. 다시 들어오면 처음부터 새로 풀어요. 나갈까요?')){settle();list();}};
 $.querySelectorAll('.vt-pk button').forEach(b=>b.onclick=()=>{
  pick[+b.dataset.n]=+b.dataset.k;
  b.parentNode.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));upd();});
 document.getElementById('vg').onclick=()=>submit(n);
 window.scrollTo(0,0);
}
// 틀린 문항 -> 오늘의 오답노트 카드 (앱 본체와 같은 목록에 합침)
function wcard(it){
 const m=/<u>(.*?)<\/u>/.exec(it.q),tw=m?m[1].replace(/<[^>]+>/g,''):'',key=s=>String(s).toLowerCase().replace(/[^a-z']/g,'');
 if(it.kind==='poly'){const se=it.senses&&it.senses[it.slot-1];return tw&&se?[key(tw),'<b>'+tw+'</b> = '+se]:null;}
 const ans=it.opts[it.slot-1],g=it.gloss&&it.gloss[it.slot-1]?it.gloss[it.slot-1][1]:'';
 if(!ans)return null;
 return [key(ans),(tw&&/class="tg"/.test(it.q)?'<b>'+tw+'</b> – ':'')+'<b>'+ans+'</b>'+(g?' '+g:'')];
}
function submit(n){
 let s=0;D.forEach(it=>{if(pick[it.n]===it.slot)s++;});
 const st=load();delete st.pend;
 add(st,n,{p:D.map(it=>pick[it.n]||0).join(''),s,t:stamp()});save(st);
 if(window.VLWN)D.forEach(it=>{if(pick[it.n]!==it.slot){const c=wcard(it);if(c)VLWN.add(c[0],c[1]);}});
 const r=st.d[n],all=[r.first].concat(r.re||[]);result(n,all.length-1);
}
function explain(it){
 let h=`<div class="q">${it.n}. ${it.q}</div><div class="vt-ko">${it.ko}</div><div class="vt-key"><b>정답 ${C[it.slot-1]}</b> ${it.key}</div>`;
 if(it.kind==='blank'){
  if(it.wrong&&it.wrong.length)h+=`<div class="vt-wr">${it.wrong.map(w=>`<div>✕ ${(w[1].startsWith(w[0])?w[1].replace(w[0],'<b>'+w[0]+'</b>'):'<b>'+w[0]+'</b> — '+w[1])}</div>`).join('')}</div>`;
  h+=`<div class="vt-opl">${it.opts.map((o,i)=>`<div class="${i+1===it.slot?'a':''}">${C[i]} ${o}${it.gloss&&it.gloss[i]?` <span class="gl">${it.gloss[i][1]}</span>`:''}</div>`).join('')}</div>`;
 }else{
  h+=`<div class="vt-opl">${it.opts.map((o,i)=>`<div class="${i+1===it.slot?'a':''}">${C[i]} ${o}${it.senses&&it.senses[i]?` <span class="gl">(${it.senses[i]})</span>`:''}${it.trans&&it.trans[i]?`<div class="tr">${it.trans[i]}</div>`:''}</div>`).join('')}</div>`;
  if(it.wrong&&it.wrong.length)h+=`<div class="vt-wr">${it.wrong.map(w=>`<div>✕ ${w[0]} — ${w[1]}</div>`).join('')}</div>`;
 }
 return h;
}
function result(n,idx){
 const stt=load(),r=stt.d[n],ab=(stt.ab&&stt.ab[n])||0,all=[r.first].concat(r.re||[]),rec=all[idx],p=rec.p;
 const bad=D.filter((it,i)=>+p[i]!==it.slot).length;
 let rows='';D.forEach((it,i)=>{
  if(i===0||D[i-1].sec!==it.sec)rows+=`<div class="vt-sec">${it.sec}</div>`;
  const mine=+p[i],ok=mine===it.slot;
  rows+=`<div class="vt-row ${ok?'ok':'no'}"><span class="vt-no">${it.n}.</span><span class="vt-ans">내 답 ${mine?C[mine-1]:'-'} · 정답 <b>${C[it.slot-1]}</b></span><span class="vt-mk">${ok?'○':'✕'}</span><button class="vt-tg" data-e="${i}">해설</button></div><div class="vt-ex${ok?'':' open'}" id="ve${i}">${explain(it)}</div>`;
 });
 $.innerHTML=`<div class="top"><button class="back" id="vb">← 목록</button></div><h1>DAY ${n} · 1차 테스트</h1>
 <div class="card vt-sc"><div class="vt-big">${rec.s} / ${N}</div>
 <div class="${rec.s>=PASS?'vt-pass':'vt-fail'}">${rec.s>=PASS?'통과 — 다음 DAY로 넘어가도 돼요.':'통과 기준은 '+PASS+'개예요. 틀린 문항의 해설을 읽고 다시 풀어 봐요.'}</div>
 <div class="sub" style="margin-top:6px">${idx?'재도전 '+idx+' · ':'첫 기록 · '}${rec.t}</div>
 ${all.length>1||ab?`<div class="sub" style="margin-top:4px">첫 기록 ${r.first.s}/${N} · 최고 ${best(r)}/${N}${ab?' · 중간에 나간 횟수 '+ab+'회':''}</div>`:''}</div>
 ${all.length>1?`<div class="vt-his">${all.map((a,i)=>`<button data-h="${i}" class="${i===idx?'on':''}">${i?'재도전 '+i:'첫 기록'} ${a.s}/${N}</button>`).join('')}</div>`:''}
 <div class="sub" style="margin:10px 2px 0">${bad?'틀린 문항 '+bad+'개의 해설이 열려 있어요.':'모두 맞았어요!'}</div>${rows}
 <button class="btn" id="vr">다시 풀기 (첫 기록은 그대로 남아요)</button><button class="btn pri" id="vl">다른 DAY 고르기</button>`;
 document.getElementById('vb').onclick=list;document.getElementById('vl').onclick=list;
 document.getElementById('vr').onclick=()=>entry(n);
 $.querySelectorAll('[data-h]').forEach(b=>b.onclick=()=>result(n,+b.dataset.h));
 $.querySelectorAll('[data-e]').forEach(b=>b.onclick=()=>document.getElementById('ve'+b.dataset.e).classList.toggle('open'));
 window.scrollTo(0,0);
}
window.VLTEST={open:(el,onBack)=>{$=el;back=onBack;list();}};
})();
