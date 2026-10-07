/* 본문 구워삶기 (final 시리즈) - 공통 앱 코드
   규칙: 영어 단어는 화면에 뜻을 괄호로 붙인다. 빨간 '틀림' 표시는 쓰지 않는다(부드러운 안내색). */
(function(){
'use strict';
var D=window.FLOWDATA[VID], KEY='final:'+VID, app=document.getElementById('app');
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function shuffle(a){return a.map(function(v){return [Math.random(),v]}).sort(function(x,y){return x[0]-y[0]}).map(function(x){return x[1]})}
function load(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){return {}}}
function save(o){try{localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}}
var SAVED=load();
var STEPS=[{k:'story',t:'① 한글로 먼저 읽기'},{k:'topic',t:'② 주제 판정 (맞는 말 vs 낚시)'},{k:'fact',t:'③ 내용 일치 판정 (선지 낚시)'},{k:'ref',t:'④ 지칭 잡기'},{k:'pair',t:'⑤ 단어 잡기 (반의어)'},{k:'order',t:'⑥ 순서 잡기'},{k:'trap',t:'⑦ 함정 잡기'}];
var S={view:'home',pi:0,step:0,sub:0,res:{},locked:false,tmp:{}};

function P(){return D.parts[S.pi]}
function count(k){var p=P();return {story:1,topic:p.judge.length,fact:p.facts.length,ref:p.refs.length,pair:p.pairs.length,order:1,trap:p.traps.length}[k]}
function rec(k,ok){(S.res[k]=S.res[k]||[]).push(!!ok)}
function go(v){S.view=v;draw()}
function start(i){S={view:'part',pi:i,step:0,sub:0,res:{},locked:false,tmp:{}};draw()}
function next(){
  var k=STEPS[S.step].k; S.sub++; S.locked=false; S.tmp={};
  if(S.sub>=count(k)){S.step++;S.sub=0}
  if(S.step>=STEPS.length){finish();return}
  draw()
}
function finish(){
  var tot=0,ok=0;Object.keys(S.res).forEach(function(k){S.res[k].forEach(function(b){tot++;if(b)ok++})});
  SAVED[P().id]={ok:ok,tot:tot,at:Date.now()};save(SAVED);S.view='card';draw()
}
function dots(){var h='<div class="dots">';STEPS.forEach(function(s,i){h+='<i class="'+(i<S.step?'on':i===S.step?'cur':'')+'"></i>'});return h+'</div>'}
function head(){
  var p=P();
  return '<div class="top"><a data-a="home">← 처음으로</a><span>'+esc(p.lesson+'과 '+p.name+' '+p.title)+'</span></div>'+dots()+'<div class="step">'+STEPS[S.step].t+(count(STEPS[S.step].k)>1?' <span class="pill">'+(S.sub+1)+' / '+count(STEPS[S.step].k)+'</span>':'')+'</div>'
}

/* ---------- 화면 ---------- */
function draw(){
  var h='';
  if(S.view==='home')h=home();
  else if(S.view==='card')h=card();
  else h=head()+body();
  app.innerHTML=h+'<div class="foot">동남비타민영어학원</div>';
  bind();window.scrollTo(0,0)
}
function home(){
  var h='<h1>'+esc(D.title)+'</h1><p class="sub">'+esc(D.school)+' · '+esc(D.book)+'</p>';
  D.parts.forEach(function(p,i){
    var s=SAVED[p.id];
    h+='<div class="card"><b>'+p.lesson+'과 '+p.name+'</b> '+esc(p.title)+(s?'<div class="sub">최근 결과: '+s.ok+' / '+s.tot+'</div>':'')+'<button class="btn main" data-a="start" data-i="'+i+'">시작하기</button></div>'
  });
  return h
}
function body(){
  var k=STEPS[S.step].k,p=P();
  if(k==='story'){
    var h='<div class="card">'+esc(p.hook).replace(/\n/g,'<br>')+'</div><details><summary>영어 본문 + 해석 보기</summary><div class="card">';
    p.sents.forEach(function(s){h+='<span class="en">'+esc(s.en)+'</span><span class="kk">'+esc(s.ko)+'</span>'});
    return h+'</div></details><button class="btn main" data-a="next">읽었어요 →</button>'
  }
  if(k==='topic')return judge();
  if(k==='fact')return fact();
  if(k==='ref')return mcq(p.refs[S.sub]);
  if(k==='pair')return mcq(pairQ(p.pairs[S.sub]));
  if(k==='order')return order();
  if(k==='trap')return trap();
}
function mcq(q){
  var key='o'+S.step+'_'+S.sub;
  if(!S.tmp.opts)S.tmp.opts=shuffle(q.opts.map(function(o,i){return i}));
  var h='<div class="card">'+q.stem+'</div>';
  S.tmp.opts.forEach(function(i){
    var o=q.opts[i],c='';
    if(S.locked){c=o.ok?' ok':(S.tmp.pick===i?' no':'')}
    h+='<button class="btn'+c+'" data-a="pick" data-i="'+i+'"'+(S.locked?' disabled':'')+'>'+esc(o.t)+'</button>'
  });
  if(S.locked){h+='<div class="fb '+(S.tmp.ok?'ok':'no')+'">'+(S.tmp.ok?'맞았어요!':'다시 볼까요?')+'</div><div class="why">'+q.why+'</div><button class="btn main" data-a="next">다음 →</button>'}
  return h
}
function pairQ(w){
  var pool=[{t:w.ans+'('+w.am+')',ok:true},{t:w.trap+'('+w.tm+')',ok:false}];
  w.others.forEach(function(o){pool.push({t:o[0]+'('+o[1]+')',ok:false})});
  return {stem:'<b>'+w.w+'('+w.m+')</b>의 <b>반의어</b>는?<div class="sub">그 단어는 본문 어디에서 나왔을까요? 답을 고르면 알려 줄게요.</div>',opts:pool,
   why:'<b>'+w.w+'('+w.m+')</b>는 <b>'+w.ans+'('+w.am+')</b>의 반의어입니다.<br><b>'+w.trap+'('+w.tm+')</b>는 반의어가 아니라 비슷한 말이라서 낚시 선지예요.<br>'+esc(w.story)}
}
var JL={A:'전체를 포괄하는 맞는 말',B:'맞는 내용이지만 일부만',C:'본문 소재만 가져온 낚시',D:'반대이거나 과장'};
function judge(){
  var p=P(),q=p.judge[S.sub];
  var h='<div class="card"><div class="sub">네 가지 중 하나로 판정해 보세요.<br><b>A</b> 전체를 포괄하는 맞는 말 · <b>B</b> 맞지만 일부만(부분이라 정답 아님) · <b>C</b> 본문 소재만 가져온 낚시 · <b>D</b> 반대이거나 과장</div>'+(q.src?'<span class="pill">'+esc(q.src)+'</span>':'')+'<div class="en">'+esc(q.t)+'</div>'+(S.locked?'<span class="kk">'+esc(q.ko)+'</span>':'')+'</div>';
  ['A','B','C','D'].forEach(function(k){
    var c='';
    if(S.locked){c=k===q.a?' ok':(S.tmp.pick===k?' no':'')}
    h+='<button class="btn'+c+'" data-a="jd" data-k="'+k+'"'+(S.locked?' disabled':'')+'><b>'+k+'</b> '+JL[k]+'</button>'
  });
  if(S.locked){
    h+='<div class="fb '+(S.tmp.ok?'ok':'no')+'">'+(S.tmp.ok?'맞았어요!':'다시 볼까요? 정답은 '+q.a+' ('+JL[q.a]+')')+'</div><div class="why">'+q.why+(q.map?'<br>'+q.map:'')+'</div><button class="btn main" data-a="next">다음 →</button>'
  }
  return h
}
function fact(){
  var p=P(),q=p.facts[S.sub];
  var h='<div class="card"><div class="sub">이 선지는 본문과 <b>일치</b>할까요? 한 군데라도 다르면 일치하지 않아요.</div><span class="pill">'+esc(q.src||'선지')+'</span><div class="en">'+esc(q.t)+'</div></div>';
  [['1','본문과 일치'],['0','일치하지 않음']].forEach(function(b){
    var c='';
    if(S.locked){var isAns=(b[0]==='1')===q.ok;c=isAns?' ok':(S.tmp.pick===b[0]?' no':'')}
    h+='<button class="btn'+c+'" data-a="fk" data-v="'+b[0]+'"'+(S.locked?' disabled':'')+'>'+b[1]+'</button>'
  });
  if(S.locked){
    h+='<div class="fb '+(S.tmp.ok?'ok':'no')+'">'+(S.tmp.ok?'맞았어요!':'다시 볼까요?')+'</div><div class="why"><b>'+(q.ok?'일치하는 선지':'낚시 유형: '+esc(q.type))+'</b><br>'+q.why+'<br><br><b>근거 문장</b>';
    q.sid.forEach(function(i){h+='<br>'+esc(p.sents[i].en)+'<br>'+esc(p.sents[i].ko)});
    h+='</div><button class="btn main" data-a="next">다음 →</button>'
  }
  return h
}
function order(){
  var p=P();
  if(!S.tmp.ord){S.tmp.ord=shuffle(p.chunks.map(function(c,i){return i}));if(S.tmp.ord.join()===p.chunks.map(function(c,i){return i}).join())S.tmp.ord.reverse();S.tmp.sel=[]}
  var h='<div class="card">덩어리를 <b>흐름 순서대로</b> 눌러 보세요. 다시 누르면 취소돼요.</div>';
  S.tmp.ord.forEach(function(ci){
    var c=p.chunks[ci],n=S.tmp.sel.indexOf(ci),txt=p.sents.slice(c.a,c.b+1).map(function(s){return s.en}).join(' ');
    var cls='chunk'+(n>=0?' sel':'');
    if(S.locked)cls='chunk'+(S.tmp.sel.indexOf(ci)===ci?' ok':' no');
    h+='<div class="'+cls+'" data-a="ch" data-i="'+ci+'"><span class="num">'+(n>=0?n+1:'')+'</span>'+esc(txt)+(S.locked?'<span class="ko"><b>'+(ci+1)+'번째 · '+esc(c.t)+'</b></span>':'')+'</div>'
  });
  if(!S.locked)return h+'<button class="btn main" data-a="chk"'+(S.tmp.sel.length===p.chunks.length?'':' disabled')+'>확인</button>';
  h+='<div class="fb '+(S.tmp.ok?'ok':'no')+'">'+(S.tmp.ok?'맞았어요!':'다시 볼까요? 정답 순서는 아래예요.')+'</div>';
  p.chunks.forEach(function(c,i){h+='<div class="why"><b>'+(i+1)+'. '+esc(c.t)+'</b><br>'+c.why+'</div>'});
  return h+'<button class="btn main" data-a="next">다음 →</button>'
}
function trap(){
  var p=P(),t=p.traps[S.sub];
  if(S.tmp.shuf===undefined){S.tmp.shuf=1;S.tmp.phase=0}
  var toks=t.text.split(' ');
  var h='<div class="card"><div class="sub">이 문장, 교과서와 같을까요? 한 군데 망가졌을 수도 있고, 정상일 수도 있어요.</div><div>';
  toks.forEach(function(w,i){
    var c='tk';
    var clean=w.replace(/[,.]$/,'');
    var isBad=t.bad&&clean===t.bad;
    if(S.tmp.phase===1)c+=' hit';
    if(S.locked){c='tk';if(isBad)c+=' ok';if(S.tmp.tap===i&&!isBad)c+=' no'}
    h+='<span class="'+c+'" data-a="tk" data-i="'+i+'" data-b="'+(isBad?1:0)+'">'+esc(w)+'</span> '
  });
  h+='</div></div>';
  if(!S.locked&&S.tmp.phase===0)h+='<div class="two"><button class="btn" data-a="norm">정상이에요</button><button class="btn" data-a="odd">이상한 데가 있어요</button></div>';
  if(!S.locked&&S.tmp.phase===1)h+='<div class="card">이상한 단어를 눌러 보세요.</div>';
  if(S.locked){
    h+='<div class="fb '+(S.tmp.ok?'ok':'no')+'">'+(S.tmp.ok?'맞았어요!':'다시 볼까요?')+'</div>';
    var sent=p.sents[t.sid];
    if(t.bad)h+='<div class="why">'+t.why+'<br><br><b>원래 문장</b><br>'+esc(sent.en)+'<br>'+esc(sent.ko)+'</div>';
    else h+='<div class="why">이 문장은 <b>교과서 그대로</b>예요. 정상 문장도 섞여 있으니 무조건 의심하지 말고 근거를 찾아요.<br><br>'+esc(sent.en)+'<br>'+esc(sent.ko)+'</div>';
    h+='<button class="btn main" data-a="next">다음 →</button>'
  }
  return h
}
function card(){
  var p=P(),h='<div class="top"><a data-a="home">← 처음으로</a></div><h1>내 정리 카드</h1><p class="sub">'+p.lesson+'과 '+p.name+' '+esc(p.title)+' · 캡처해서 시험 전날 보세요</p>';
  h+='<div class="card"><b>흐름</b><ol class="sum">';p.chunks.forEach(function(c){h+='<li>'+esc(c.t)+'</li>'});h+='</ol></div>';
  var ts=p.topic;
  h+='<div class="card"><b>주제문</b><br><span class="en">'+esc(ts.en)+'</span><span class="kk">'+esc(ts.ko)+'</span></div>';
  h+='<div class="card"><b>맞는 선지는 이렇게 바뀌어요</b><ul class="sum">';
  p.judge.forEach(function(j){if(j.a==='A')h+='<li>'+esc(j.t)+'<span class="kk">'+esc(j.ko)+'</span>'+(j.map?'<br>'+j.map:'')+'</li>'});
  h+='</ul><div class="sub">B 일부만 · C 소재만 낚시 · D 반대/과장은 정답이 될 수 없어요.</div></div>';
  var tys={};p.facts.forEach(function(f){if(!f.ok)tys[f.type]=1});
  h+='<div class="card"><b>기출에서 선지를 낚는 방법</b><ul class="sum">';
  Object.keys(tys).forEach(function(t){h+='<li>'+esc(t)+'</li>'});
  h+='</ul><div class="sub">정답 선지는 본문을 해석한 그대로예요. 한 군데라도 다르면 틀린 선지!</div></div>';
  h+='<div class="card"><b>지칭</b><ul class="sum">';
  p.refs.forEach(function(r){var a=r.opts.filter(function(o){return o.ok})[0];h+='<li>'+esc(p.sents[r.sid].en.split(' ').slice(0,6).join(' '))+'… → '+esc(a.t)+'</li>'});
  h+='</ul></div><div class="card"><b>반의어</b><ul class="sum">';
  p.pairs.forEach(function(w){h+='<li>'+esc(w.w)+'('+esc(w.m)+') ↔ '+esc(w.ans)+'('+esc(w.am)+')</li>'});
  h+='</ul></div><div class="card"><b>학교 쌤이 낚는 자리</b><ul class="sum">';
  p.traps.forEach(function(t){if(t.bad)h+='<li>'+esc(t.bad)+' ✕ → '+esc(t.orig)+(t.om?'('+esc(t.om)+')':'')+'</li>'});
  h+='</ul></div>';
  var s=SAVED[p.id];if(s)h+='<p class="sub">이번 결과: '+s.ok+' / '+s.tot+'</p>';
  return h+'<button class="btn main" data-a="start" data-i="'+S.pi+'">한 번 더 돌리기</button>'
}

/* ---------- 이벤트 ---------- */
function bind(){
  app.querySelectorAll('[data-a]').forEach(function(el){el.addEventListener('click',function(){act(el)})})
}
function act(el){
  var a=el.getAttribute('data-a'),i=+el.getAttribute('data-i'),p=P?P():null;
  if(a==='home'){go('home');return}
  if(a==='start'){start(i);return}
  if(a==='next'){next();return}
  if(S.locked&&a!=='next')return;
  var k=S.view==='part'?STEPS[S.step].k:'';
  if(a==='pick'){
    var q=k==='ref'?P().refs[S.sub]:pairQ(P().pairs[S.sub]);
    S.tmp.pick=i;S.tmp.ok=!!q.opts[i].ok;S.locked=true;rec(k,S.tmp.ok);draw();return}
  if(a==='fk'){var vv=el.getAttribute('data-v')==='1';S.tmp.pick=el.getAttribute('data-v');S.tmp.ok=(vv===P().facts[S.sub].ok);S.locked=true;rec('fact',S.tmp.ok);draw();return}
  if(a==='jd'){var kk=el.getAttribute('data-k');S.tmp.pick=kk;S.tmp.ok=(kk===P().judge[S.sub].a);S.locked=true;rec('topic',S.tmp.ok);draw();return}
  if(a==='ch'){var s=S.tmp.sel,n=s.indexOf(i);if(n>=0)s.splice(n);else s.push(i);draw();return}
  if(a==='chk'){var ok=S.tmp.sel.every(function(v,j){return v===j});S.tmp.ok=ok;S.locked=true;rec('order',ok);draw();return}
  if(a==='norm'){var t=P().traps[S.sub];S.tmp.ok=!t.bad;S.locked=true;rec('trap',S.tmp.ok);draw();return}
  if(a==='odd'){S.tmp.phase=1;draw();return}
  if(a==='tk'){
    if(S.tmp.phase!==1)return;
    var isBad=el.getAttribute('data-b')==='1';
    S.tmp.tap=i;S.tmp.ok=isBad;S.locked=true;rec('trap',isBad);draw();return}
}
draw();
})();
