const M=D.meta;
const $=id=>document.getElementById(id);
const esc=t=>String(t).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
let tab=1,si=0,st=0,cj=0;const stg=[];for(let i=0;i<20;i++)stg.push(0);
const NS=D.sent.length;
$('ptxt').innerHTML=D.sent.map(s=>{
  let h=(s.seg?'<div class="segl'+(s.seg==='주어진 문장'?' given':'')+'">'+esc(s.seg)+'</div>':'')+'<p class="xs" id="s'+s.no+'"><span class="xno">'+s.no+'</span><span class="xrb" id="rb'+s.no+'"></span>';
  s.tok.forEach((t,i)=>{
    if(t[2]==='blank') h+='<span class="blank" id="bl">&nbsp;</span> ';
    else h+='<span class="xw" id="t'+s.no+'_'+i+'"><span class="xe">'+esc(t[0])+'</span><span class="xg">'+esc(t[1])+'</span></span> ';
  });
  return h+(s.slot?'<span class="slot">'+esc(s.slot)+'</span>':'')+'</p>';
}).join('');
function clearMarks(){document.querySelectorAll('.xw').forEach(e=>{e.className='xw'});const b=$('bl');if(!b)return;b.className='blank';b.textContent=' '}
function mark(list,kindMap){list.forEach(m=>{for(let i=m.a;i<=m.b;i++){const e=$('t'+m.s+'_'+i);if(e)e.classList.add('m-'+(kindMap?kindMap(m):m.kind))}})}
function maxSt(s){if(M.nl)return D.clue[s.no].some(c=>c.kind!=='k'&&c.ko)?3:2;return 2}
function scrollTo(el){const cl=$('cl');if(!el)return;const r=el.getBoundingClientRect(),b=cl.getBoundingClientRect();cl.scrollTo({top:cl.scrollTop+r.top-b.top-b.height/5,behavior:'smooth'})}
function applyLec(){
  const s=D.sent[si];clearMarks();
  D.sent.forEach((x,k)=>{const p=$('s'+x.no);p.className='xs '+(k<si?'past':k===si?'cur':'next');
    const rb=$('rb'+x.no);const on=(k===si?st:stg[k])>=2;rb.textContent=x.role;rb.classList.toggle('on',on)});
  D.sent.forEach((x,k)=>{const g=k===si?st:stg[k];if(M.nl){if(g>=1)mark(D.clue[x.no].filter(c=>c.kind==='k'));if(g>=3)mark(D.clue[x.no].filter(c=>c.kind!=='k'),c=>c.kind==='g'?'og':'or')}else if(g>=1)mark(D.clue[x.no]);});
  let h='';
  $('nbar').innerHTML='<button type="button" class="nv" data-d="-1" aria-label="이전">\u25c0</button><div class="schips">'+D.sent.map((x,k)=>'<button type="button" class="sc'+(k===si?' cur':'')+'" data-i="'+k+'">'+x.no+'</button>').join('')+'</div><button type="button" class="nv go" data-d="1" aria-label="다음">\u25b6</button>';
    if(M.nl){if(st>=2)h+='<div class="sub">한 줄 정리</div><div class="bubble">'+esc(s.gist)+'</div>';
      if(st>=3){const cl=D.clue[s.no].filter(c=>c.kind!=='k'&&c.ko);if(cl.length)h+='<div class="sub">순서 단서</div>'+cl.map(c=>'<div class="bubble oc '+(c.kind==='g'?'og':'or')+'"><b>'+esc(c.en)+'</b> : '+esc(c.ko)+'</div>').join('')}}
    else if(st===2)h+='<div class="sub">한 줄 정리</div><div class="bubble">'+esc(s.gist)+'</div>';
  if(st===3&&!M.nl){const f=D.flag[s.no],mu=f.filter(x=>x.kind==='mu'),sk=f.filter(x=>x.kind==='sk');
    h+='<div class="sub">단어</div>';
    if(mu.length)h+='<div class="fl mu"><span class="t">★ 꼭 알았어야</span>'+mu.map(x=>'<span class="c"><b>'+esc(x.en)+'</b> '+esc(x.ko)+'</span>').join('')+'</div>';
    if(sk.length)h+='<div class="fl sk"><span class="t">○ 몰라도 됐다</span>'+sk.map(x=>'<span class="c"><b>'+esc(x.en)+'</b> '+esc(x.ko)+'</span>').join('')+'</div>';
    if(sk.length)h+='<div class="sub" style="font-weight:500">같은 말이 다른 곳에 또 나오기 때문</div>'}
  if(hae)h+='<div class="hae"><b>해석</b> '+esc(s.hae)+'</div>';
  document.querySelectorAll('.sarr,.ibub').forEach(e=>e.remove());
  const cp=$('s'+s.no);
  cp.insertAdjacentHTML('beforeend','<button type="button" class="sarr" aria-label="다음">\u25b6</button>');
  if(h)cp.insertAdjacentHTML('beforeend','<div class="ibub">'+h+'</div>');
  $('cr').innerHTML='';
  $('st').textContent='문장 '+(LP.indexOf(si)+1)+' / '+NS;
  requestAnimationFrame(()=>scrollTo($('s'+s.no)));
}
function sentHtml(s,marks,fill){
  let h='';
  s.tok.forEach((t,i)=>{
    if(t[2]==='blank'){h+='<span class="blank'+(fill?' fill':'')+'">'+(fill?M.ans:'\u00a0')+'</span> ';return}
    const m=marks.find(m=>i>=m.a&&i<=m.b);
    h+='<span class="xw'+(m?' m-'+m.kind:'')+'"><span class="xe">'+esc(t[0])+'</span><span class="xg">'+esc(t[1])+'</span></span> ';
  });
  return h;
}
const seen=new Set();
function applyCho(){
  const cur=cj>=1?D.order[cj-1]:-1;
  if(cur>=0)seen.add(cur);
  const last=D.sent.find(s=>s.tok.some(t=>t[2]==='blank')),cc=cur>=0?D.chs[cur]:null;
  const bare=s=>s.replace(/^[\u2460-\u2464]\s*/,'');
  let blank='<span class="xno">'+last.no+'</span>'+last.tok.map(t=>t[2]==='blank'?'<span class="blank'+(cc?(cc.ok?' fill':' fillbad'):'')+'">'+(cc?esc(bare(cc.en)):'\u00a0')+'</span> ':'<span class="xw"><span class="xe">'+esc(t[0])+'</span><span class="xg">'+esc(t[1])+'</span></span> ').join('');
  let h='<div class="rp"><div class="navrow"><div class="sub" style="margin:0;flex:1">다음 빈칸에 들어갈 말로 가장 적절한 것은?</div><button type="button" class="rst" id="rst">선지 초기화</button></div>'+
   '<div class="qs pin">'+blank+'<div class="qk">'+esc(last.hae.replace('(빈칸)','(      )'))+'</div></div><div class="clist2">'+
   D.chs.map((c,i)=>{
    const open=i===cur,sn=seen.has(i)&&!open;
    let r='<div class="crow'+(open?' open '+(c.ok?'ok':'no'):'')+'"><button type="button" class="cb wide'+(open?' cur '+(c.ok?'ok':'no'):'')+(sn?' seen '+(c.ok?'ok':'no'):'')+'" data-i="'+i+'"><b>'+esc(c.en)+'</b><span class="ck">('+esc(c.ko)+')</span>'+((open||sn)?'<span class="mk">'+(c.ok?'\u25cb 정답':'\u00d7 탈락')+'</span>':'')+'</button>';
    if(open){
      const nos=new Set(c.ev.map(m=>m.s));
      r+='<div class="det"><div class="vt">'+esc(c.verdict)+'</div><div class="evb">'+D.sent.filter(s=>nos.has(s.no)).map(s=>
        '<div class="evs"><span class="xno">'+s.no+'</span>'+sentHtml(s,c.ev.filter(m=>m.s===s.no),false)+'<div class="evk">'+esc(s.hae)+'</div></div>').join('')+'</div><div class="tr">'+esc(c.trap)+'</div></div>';
    }
    return r+'</div>'}).join('')+'</div></div>';
  $('cr').innerHTML=h;
  $('st').textContent=cc?'선지 '+(cur+1)+'번':'선지 선택';
  requestAnimationFrame(()=>{const o=document.querySelector('.crow.open');if(o)o.scrollIntoView({block:'nearest',behavior:'smooth'})});
}
function apply(){$('stage').classList.toggle('wide',tab===2);$('stage').classList.toggle('solo',tab===1);if(tab===1){if(st<0)st=stg[si]||0;stg[si]=st;applyLec()}else if(tab===2)applyCho();try{localStorage.setItem(window.__ID+'pos',JSON.stringify([si,st,cj]))}catch(e){}}
const LP=(M.path||D.sent.map(x=>x.no)).map(n=>D.sent.findIndex(x=>x.no===n));
function next(){
  if(tab===1){if(st<maxSt(D.sent[si]))st++;else{const p=LP.indexOf(si);if(p<LP.length-1){si=LP[p+1];st=-1}else{show(5);return}}}
  else if(tab===2){if(cj<D.order.length)cj++;else{show(3);return}}
  apply()}
function prev(){
  if(tab===1){if(st>0)st--;else{const p=LP.indexOf(si);if(p>0){si=LP[p-1];st=maxSt(D.sent[si])}}}
  else if(tab===2){if(cj>0)cj--;else{show(5);return}}
  apply()}
let touchNav=false;
$('stage').addEventListener('click',e=>{if(e.target.closest('.sarr')){e.stopPropagation();next();return}const xn=e.target.closest('#pass .xno');if(xn&&tab===1){const k=D.sent.findIndex(x=>x.no===xn.textContent.trim());if(k>=0){if(k===si)st=Math.min(st+1,maxSt(D.sent[si]));else{si=k;st=-1}apply();return}}const sc=e.target.closest('.sc');if(sc){const k=+sc.dataset.i;if(k===si)st=Math.min(st+1,maxSt(D.sent[si]));else{si=k;st=-1}apply();return}if(e.target.closest('.rst')){cj=0;seen.clear();apply();return}const cb=e.target.closest('.cb');if(cb){const i=+cb.dataset.i,k=D.order.indexOf(i)+1;cj=(cj===k)?0:k;apply();return}if(tab===2&&!e.target.closest('.nv'))return;const b=e.target.closest('.nv');if(b){e.stopPropagation();(+b.dataset.d>0?next:prev)();return}if(touchNav)next()});
$('bt').onclick=()=>{touchNav=!touchNav;setTog('bt',touchNav);try{localStorage.setItem(window.__ID+'t',touchNav?'1':'0')}catch(e){}};
$('nbar').addEventListener('click',e=>{const sc=e.target.closest('.sc');if(sc){const k=+sc.dataset.i;if(k===si)st=Math.min(st+1,maxSt(D.sent[si]));else{si=k;st=-1}apply();return}const b=e.target.closest('.nv');if(b)(+b.dataset.d>0?next:prev)()});
$('next').onclick=next;$('prev').onclick=prev;
$('bhome').onclick=()=>{stg.fill(0);si=0;st=0;cj=0;seen.clear();show(1)};
function setTog(id,on){$(id).setAttribute('aria-pressed',String(on))}
$('bg').onclick=()=>{const on=document.body.classList.toggle('nog');setTog('bg',!on);try{localStorage.setItem(window.__ID+'g',on?'0':'1')}catch(e){}};
let hae=false;
$('bh').onclick=()=>{hae=!hae;setTog('bh',hae);apply()};
function fs(d){let v=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--fs'))||1;v=Math.min(1.6,Math.max(.7,v+d));document.documentElement.style.setProperty('--fs',v);try{localStorage.setItem(window.__ID+'fs',v)}catch(e){}}
$('beq').onclick=()=>{const on=document.body.classList.toggle('eq');setTog('beq',on);try{localStorage.setItem(window.__ID+'eq',on?'1':'0')}catch(e){}};
try{if(localStorage.getItem(window.__ID+'eq')==='1'){document.body.classList.add('eq');setTog('beq',true)}}catch(e){}
$('bm').onclick=()=>fs(-.1);$('bp').onclick=()=>fs(.1);
document.querySelectorAll('.tools button,#foot button').forEach(b=>b.addEventListener('click',e=>e.stopPropagation()));
$('foot').addEventListener('click',e=>e.stopPropagation());
document.addEventListener('keydown',e=>{
  if(tab===3&&['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();cj=D.order.length;show(M.nocho?5:2);return}
  if(tab===5){if(['ArrowRight','PageDown',' ','Enter'].includes(e.key)){e.preventDefault();cj=0;show(M.nocho?3:2)}if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();si=LP[LP.length-1];st=maxSt(D.sent[si]);show(1)}return}
  if(tab>2)return;
  if(['ArrowRight','PageDown',' ','Enter'].includes(e.key)){e.preventDefault();next()}
  if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();prev()}
});
try{const q=JSON.parse(localStorage.getItem(window.__ID+'pos')||'null');if(q&&q[0]>=0&&q[0]<NS&&q[1]>=0&&q[1]<=maxSt(D.sent[q[0]])&&q[2]>=0&&q[2]<=D.order.length){si=q[0];st=q[1];cj=q[2]}if(localStorage.getItem(window.__ID+'t')==='1'){touchNav=true;setTog('bt',true)}}catch(e){}
try{const v=localStorage.getItem(window.__ID+'fs');if(v)document.documentElement.style.setProperty('--fs',v);if(localStorage.getItem(window.__ID+'g')==='0'){document.body.classList.add('nog');setTog('bg',false)}}catch(e){}
// ---- 마무리 ----
function photoHtml(){
  const F=D.fin;
  const N=(n,role,h,c)=>'<div class="nd'+(c?' '+c:'')+'"><span class="no2">'+n+'</span><span class="role">'+role+'</span><span class="bd">'+h+'</span></div>';
  const wl=a=>a.map(([x,y,z])=>'<li><b>'+esc(x)+'</b><span>'+esc(y)+'</span>'+(z?'<em>'+esc(z)+'</em>':'')+'</li>').join('');
  return '<div class="fin"><div class="fflow">'+
   D.flow+'</div>'+
   '<div class="topic"><div class="tl">'+esc(M.topic_label||'주제문')+'</div><div class="te">'+esc(M.topic_en)+'</div><div class="tk">'+esc(M.topic_ko)+'</div></div>'+
   '<div class="fv"><div class="vb must"><h3>꼭 알았어야 하는 단어</h3><div class="vcols"><div><h4>본문 핵심</h4><ul>'+wl(F.must)+'</ul></div><div><h4>'+esc(F.choTitle||'오지선다 · 답과 함정')+'</h4><ul>'+wl(F.cho)+'</ul></div></div></div>'+
   '<div class="vb skip"><h3>몰라도 됐던 단어 <small>'+esc(F.skipNote||'같은 말이 다른 곳에 또 나옴')+'</small></h3><ul>'+wl(F.skip)+'</ul></div></div></div>';
}
$('p3').innerHTML=photoHtml();
// ---- 지문 ----
$('p4').innerHTML='<div class="pw"><section class="ps"><div class="ph"><span class="n">'+M.qno+'</span><span class="t">문제</span></div><div class="nat"><b>'+esc(M.qtext)+'</b></div>'+(M.qline?'<div class="nat">'+esc(M.qline)+'</div>':'')+'</section>'+(P.intro?'<div class="world"><h2>이 글의 세계관: '+esc(P.title)+'</h2>'+esc(P.intro)+'</div>':'')+
 P.items.map(s=>'<section class="ps" data-n="'+s.no+'"><div class="ph"><span class="n">'+s.no+'</span><span class="t">'+esc(s.title)+'</span></div>'+
  (s.chunks?'<div>'+s.chunks.map(c=>'<div class="cr"><div class="e"><i>/</i>'+esc(c.en)+'</div><div class="k">'+esc(c.ko)+'</div></div>').join('')+'</div>':'<div class="cr"><div class="e">'+esc(s.en)+'</div></div>')+
  '<div class="nat"><b>해석</b> '+esc(s.hae)+(s.pre?' <small style="opacity:.6">(검수 전)</small>':'')+'</div>'+
  (s.gist?'<div class="gist"><span class="lab">이 문장, 결국 이 얘기</span>'+esc(s.gist)+'</div>':'')+
  (s.ex?'<div class="life"><span class="lab">생활 예시 · '+esc(P.title)+'</span>'+esc(s.ex)+'</div>':'')+
  (s.cheat&&s.cheat.length?'<div class="nat"><b>단어</b><ul class="wordl">'+s.cheat.map(([w,m])=>'<li><b>'+esc(w)+'</b> '+esc(m)+'</li>').join('')+'</ul></div>':'')+'</section>').join('')+'</div>';
function prepHtml(){
  const R=D.prep;
  return '<div class="prp"><div class="navrow"><div class="pt">'+esc(M.prepTitle||'오지선다에 가기 전에 \u2014 지문 정리')+'</div></div>'+
   '<div class="pflow">'+R.parts.map(p=>'<div class="pc '+p[3]+'"><span class="pn">'+p[0]+'</span><span class="pr">'+p[1]+'</span><span class="pb">'+p[2].replace(/<br>/g,'<br> ')+'</span></div>').join('')+'</div>'+
   '<div class="pfind"><div class="pl">'+esc(M.findLabel||'그래서 오지선다에서 찾을 말')+'</div><div class="pw2">'+R.find+'</div><div class="ps2">'+R.sub1+'</div><div class="ps2">'+R.sub2+'</div></div></div>';
}
$('p5').addEventListener('click',e=>{const b=e.target.closest('.nv');if(!b)return;if(+b.dataset.d>0){cj=0;show(2)}else{si=LP[LP.length-1];st=maxSt(D.sent[si]);show(1)}});
function show(t){
  tab=t;const sg=t===1||t===2;$('stage').hidden=!sg;$('p5').hidden=t!==5;$('p3').hidden=t!==3;$('p4').hidden=t!==4;$('nbar').hidden=t!==1;$('foot').hidden=t!==2;$('lt').hidden=!sg;
  if(t===5)$('p5').innerHTML=prepHtml();
  [1,2,3,4,5].forEach(i=>$('tab'+i).setAttribute('aria-selected',String(i===t)));
  if(sg)apply();
  try{localStorage.setItem(window.__ID+'tab7',String(t))}catch(e){}
}
[1,2,3,4,5].forEach(i=>$('tab'+i).onclick=()=>{if(i===2&&tab!==2)cj=0;show(i)});
let t0=1;try{const v=+localStorage.getItem(window.__ID+'tab7');if([1,2,3,4,5].includes(v))t0=v}catch(e){}
if(M.nl)document.body.classList.add('nl');if(M.nocho){$('tab2').hidden=true;if(t0===2)t0=1}
show(t0);
$('ttl').innerHTML=esc(M.ttl)+'<small>'+esc(M.type)+'</small>';
