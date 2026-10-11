/* 어색한 곳 찾기 엔진 (내용 / 문법 공용)
   APP = {kind:'find'|'tier', step:'content'|'grammar', bid, lno, title, rule:[...], modes:[{key,name,desc}]} */
(function(){
var APP=window.APP,HUB=window.HUB,esc=HUB.esc;
var app=document.getElementById('app');
var RAW=(window.TFDATA||{})[APP.bid+'|'+APP.lno];
if(!RAW){app.innerHTML='<h1>자료를 불러오지 못했어요</h1><p class="sub">잠시 뒤 다시 열어 주세요.</p>';return}
HUB.bar(APP.step);
var META=RAW.meta,SECS=RAW.secs;
document.title=APP.title+' · '+META.pub+' '+META.lesson;
var KEY='hub_'+APP.bid+'_'+APP.step;
var SAVED=HUB.get(KEY)||{};
var MODE=null,SI=null,SUB={},RES={};
var V={view:'home'};
function mst(m){if(!SAVED[m])SAVED[m]={sel:{},bm:null,best:null};return SAVED[m]}
function persist(){HUB.put(KEY,SAVED)}
function itemsOf(m){return APP.kind==='find'?RAW.find:RAW.tiers[m]}
function modeName(m){var r='';APP.modes.forEach(function(x){if(x.key===m)r=x.name});return r}
function tokenize(t){var re=/\S+/g,m,o=[];while((m=re.exec(t)))o.push({w:m[0],s:m.index,e:m.index+m[0].length});return o}
function swapsOf(m,si,n){return itemsOf(m).filter(function(w){return w.s===si&&w.n===n})}
function posOf(en,w){var p=-1,k;for(k=0;k<=(w.occ||0);k++)p=en.indexOf(w.orig,p+1);return p}
function build(m,si,i){
  var en=SECS[si].sents[i].en,sws=swapsOf(m,si,i+1),reps=[],text='',cur=0,spans=[];
  sws.forEach(function(w){reps.push({p:posOf(en,w),w:w})});
  reps.sort(function(a,b){return a.p-b.p});
  reps.forEach(function(r){text+=en.slice(cur,r.p);var f=text.length;text+=r.w.neu;spans.push({w:r.w,from:f,to:text.length});cur=r.p+r.w.orig.length});
  text+=en.slice(cur);
  var toks=tokenize(text);
  spans.forEach(function(sp){sp.bad=[];toks.forEach(function(t,ti){if(t.s<sp.to&&t.e>sp.from)sp.bad.push(ti)})});
  return {toks:toks,spans:spans};
}
function totalOf(m){return itemsOf(m).length}
function secTotal(m,si){return itemsOf(m).filter(function(w){return w.s===si}).length}
/* 같은 문장의 다른 문법 포인트 (맞는 문장의 이유로 사용) */
function pointsOf(si,n){
  var out=[],seen={};
  if(APP.kind!=='tier')return out;
  ['basic','core','high'].forEach(function(t){
    (RAW.tiers[t]||[]).forEach(function(w){
      if(w.s===si&&w.n===n&&!seen[w.orig+'|'+w.kind]){seen[w.orig+'|'+w.kind]=1;out.push(w)}
    });
  });
  return out;
}
function selCount(m){return Object.keys(mst(m).sel).length}
function secSel(m,si){var c=0,k;for(k in mst(m).sel)if(k.split(':')[0]==si)c++;return c}
function grade(m){
  var sel=mst(m).sel,found={},spanKeys={},foundN=0,wrong=0,perSec={};
  SECS.forEach(function(sec,si){
    perSec[si]={found:0,wrong:0,n:0};
    sec.sents.forEach(function(s,i){
      var b=build(m,si,i);
      b.spans.forEach(function(sp){
        sp.bad.forEach(function(ti){spanKeys[si+':'+i+':'+ti]=1});
        var hit=sp.bad.some(function(ti){return sel[si+':'+i+':'+ti]});
        found[si+':'+i+':'+sp.w.orig+'|'+sp.w.neu]=hit;perSec[si].n++;if(hit){foundN++;perSec[si].found++}
      });
    });
  });
  Object.keys(sel).forEach(function(k){if(!spanKeys[k]){wrong++;perSec[+k.split(':')[0]].wrong++}});
  var N=totalOf(m);
  return {found:found,foundN:foundN,wrong:wrong,score:Math.max(0,foundN-wrong),N:N,perSec:perSec};
}
/* ---------- 화면 ---------- */
function setFoot(html){
  var f=document.getElementById('foot');
  if(!html){if(f)f.remove();return}
  if(!f){f=document.createElement('div');f.id='foot';document.body.appendChild(f)}
  f.innerHTML=html;
}
function home(){
  V={view:'home'};MODE=null;setFoot('');
  var h='<h1>'+esc(APP.title)+'</h1><p class="sub">'+esc(META.grade)+' '+esc(META.pub)+' '+esc(META.lesson)+' · '+esc(META.school)+' '+esc(META.term)+'</p>';
  h+='<div class="rule">'+APP.rule.map(function(r){return '<p>'+esc(r)+'</p>'}).join('')+'</div><div class="menu">';
  APP.modes.forEach(function(md){
    var b=mst(md.key).best;
    h+='<button data-m="'+md.key+'"><b>'+esc(md.name)+' <span class="stat">'+(b?'지난 점수 '+b.score+' / '+totalOf(md.key):'')+'</span></b><span>'+esc(md.desc)+' · 틀린 곳 '+totalOf(md.key)+'군데</span></button>';
  });
  h+='</div><div class="foot">단어잡고 구문잡고 · 동남비타민영어학원</div>';
  app.innerHTML=h;
  app.querySelectorAll('[data-m]').forEach(function(b){b.onclick=function(){openMode(b.getAttribute('data-m'))}});
  window.scrollTo(0,0);
}
function openMode(m){
  MODE=m;SUB[m]=false;RES[m]=null;regions();
}
function bmText(m){
  var b=mst(m).bm;if(!b)return '';
  return SECS[b.si].key+' '+(b.i+1)+'번 문장';
}
function regions(){
  V={view:'regions'};HUB.last.stop();
  var m=MODE,st=mst(m),res=RES[m],submitted=SUB[m],N=totalOf(m);
  var h='<h1>'+esc(modeName(m))+'</h1>';
  if(APP.modes.length>1)h+='<div class="ask"><a href="#" id="back">다른 코너 고르기</a></div>';
  if(!submitted)h+='<p class="ask">영역을 골라 본문을 읽으면서 '+(APP.kind==='find'?'내용이 이상한':'문법이 틀린')+' 곳을 눌러 표시하세요. 표시는 영역을 옮겨도 남아요.</p>';
  if(submitted)h+=routeBox(m,res);
  if(st.bm&&!submitted)h+='<div class="bmbar"><span>책갈피 · '+esc(bmText(m))+'</span><span><button id="gobm">이어서 읽기</button><button id="clrbm">지우기</button></span></div>';
  h+='<div class="menu">';
  SECS.forEach(function(sec,si){
    var n=secTotal(m,si),sc=secSel(m,si),st2='';
    if(submitted){var p=res.perSec[si];st2='찾음 '+p.found+'/'+n+(p.wrong?' · 잘못 '+p.wrong:'')}
    else st2=sc?('표시 '+sc+'개'):'';
    var hasbm=st.bm&&st.bm.si===si&&!submitted;
    h+='<button data-s="'+si+'"><b>본문 '+esc(sec.key)+' <span class="stat">'+esc(st2)+(hasbm?' · 책갈피':'')+'</span></b><span>'+esc(sec.title.split(' · ')[0])+' · '+sec.sents.length+'문장 · 틀린 곳 '+n+'군데</span></button>';
  });
  h+='</div>';
  app.innerHTML=h;
  var k=selCount(m);
  if(!submitted)setFoot('<div class="info"><b>표시 '+k+' / '+N+'개</b><small>'+(k<N?'앞으로 '+(N-k)+'개 더 찾을 수 있어요':(k===N?'다 골랐어요. 확인 후 제출하세요':(k-N)+'개 더 골랐어요'))+'</small></div><button id="sub">제출하기</button>');
  else setFoot('<div class="info"><b>점수 '+res.score+' / '+N+'</b><small>찾은 곳 '+res.foundN+'개 · 잘못 누른 곳 '+res.wrong+'개</small></div><button class="ghost" id="redo">다시 풀기</button>');
  wireCommon();
  app.querySelectorAll('[data-s]').forEach(function(b){b.onclick=function(){openRegion(+b.getAttribute('data-s'))}});
  var bk=document.getElementById('back');if(bk)bk.onclick=function(e){e.preventDefault();home()};
  var g=document.getElementById('gobm');if(g)g.onclick=function(){openRegion(st.bm.si,st.bm.i)};
  var c=document.getElementById('clrbm');if(c)c.onclick=function(){st.bm=null;persist();regions()};
  window.scrollTo(0,0);
}
function routeBox(m,res){
  var N=res.N,need=Math.ceil(N*0.8),steps=HUB.cfg.steps,nx=null,k;
  if(APP.kind==='find'){
    for(k=0;k<steps.length;k++)if(steps[k].k===APP.step){var j;for(j=k+1;j<steps.length;j++)if(steps[j].href&&!steps[j].test){nx=steps[j];break}}
    return '<div class="route"><p class="big">내용 확인 끝</p><p>영역별로 열어서 해설을 읽고, 놓친 곳을 다시 확인하세요.</p>'+(nx?'<a class="go" href="'+HUB.base+nx.href+'">다음 단계: '+esc(nx.name)+'</a>':'')+'</div>';
  }
  if(m==='core'){
    var up=res.score>=need;
    return '<div class="route"><p class="big">'+(up?'고득점문제에 도전해 보세요':'기본문제로 먼저 다져 볼까요')+'</p><p>'+(up?'중심 내용을 잘 잡았어요. 한 단계 더 깊은 함정에 도전해 보세요.':'놓친 부분을 기본 문법부터 차근차근 짚어 봐요. 다지고 나면 중심문제에 다시 도전해요.')+'</p>'+
     '<button data-go="'+(up?'high':'basic')+'">'+(up?'고득점문제 시작':'기본문제 시작')+'</button><button class="ghost" data-go="'+(up?'basic':'high')+'">'+(up?'기본문제로 가기':'고득점문제로 가기')+'</button></div>';
  }
  return '<div class="route"><p class="big">'+esc(modeName(m))+' 끝</p><p>영역별로 열어서 해설을 읽고 놓친 곳을 다시 확인한 뒤 중심문제에 다시 도전해 보세요.</p><button data-go="core">중심문제 다시 도전</button></div>';
}
function wireCommon(){
  var m=MODE,s=document.getElementById('sub'),r=document.getElementById('redo');
  if(s)s.onclick=function(){
    var res=grade(m);RES[m]=res;SUB[m]=true;
    var st=mst(m);if(!st.best||res.score>st.best.score)st.best={score:res.score};
    st.bm=null;persist();
    HUB.setStep(APP.step,{done:true,mode:m,score:res.score,N:res.N,best:(HUB.stepState(APP.step).best||{})});
    var sv=HUB.stepState(APP.step),bb=sv.best||{};if(!bb[m]||res.score>bb[m])bb[m]=res.score;HUB.setStep(APP.step,{best:bb});
    if(V.view==='region')openRegion(SI);else regions();
  };
  if(r)r.onclick=function(){mst(m).sel={};persist();SUB[m]=false;RES[m]=null;regions()};
  app.querySelectorAll('[data-go]').forEach(function(b){b.onclick=function(){openMode(b.getAttribute('data-go'))}});
}
function openRegion(si,focusI){
  V={view:'region'};SI=si;
  var m=MODE,sec=SECS[si],st=mst(m),submitted=SUB[m],res=RES[m],N=totalOf(m);
  var h='<div class="rnav"><button id="tolist">영역 목록</button><div class="t"><b>본문 '+esc(sec.key)+'</b>'+esc(sec.title.split(' · ')[0])+'</div><button id="pv"'+(si===0?' disabled':'')+'>이전</button><button id="nx"'+(si===SECS.length-1?' disabled':'')+'>다음</button></div>';
  h+='<div class="ask">'+(submitted?'해설을 읽고 놓친 곳을 확인하세요.':'문장 번호를 누르면 책갈피가 꽂혀요. 다시 누르면 지워져요.')+'</div>';
  h+='<div id="pas"'+(submitted?' class="done"':'')+'>';
  sec.sents.forEach(function(s,i){
    var b=build(m,si,i),words='',spanOf={};
    b.spans.forEach(function(sp){sp.bad.forEach(function(ti){spanOf[ti]=sp})});
    b.toks.forEach(function(t,ti){
      var key=si+':'+i+':'+ti,cls='wd',sp=spanOf[ti];
      if(!submitted){if(st.sel[key])cls+=' sel'}
      else{
        if(sp)cls+=(res.found[si+':'+i+':'+sp.w.orig+'|'+sp.w.neu]?' ok':' miss');
        else if(st.sel[key])cls+=' wrong';
      }
      words+='<span class="'+cls+'" data-k="'+key+'">'+esc(t.w)+'</span> ';
    });
    var isbm=st.bm&&st.bm.si===si&&st.bm.i===i;
    h+='<div class="sent" id="s'+i+'"><button class="n'+(isbm?' bm':'')+'" data-bm="'+i+'" aria-label="책갈피">'+(i+1)+'</button><span class="t">'+words;
    if(submitted){
      if(b.spans.length){
        b.spans.forEach(function(sp){
          var f=res.found[si+':'+i+':'+sp.w.orig+'|'+sp.w.neu];
          h+='<div class="note '+(f?'found':'lost')+'"><div class="tag">'+(f?'찾았어요':'놓쳤어요')+' · '+esc(sp.w.kind)+'</div><div class="swap">'+esc(sp.w.neu)+' → '+esc(sp.w.orig)+'</div>';
          sp.w.lines.forEach(function(l){h+='<div class="ln">'+esc(l)+'</div>'});
          h+='</div>';
        });
      }else{
        var pts=pointsOf(si,i+1);
        if(pts.length){
          h+='<div class="note good"><div class="tag">이 문장은 맞는 문장이에요</div>';
          pts.forEach(function(p){h+='<div class="pt"><b>'+esc(p.kind)+' · '+esc(p.orig)+'</b>'+p.lines.map(function(l){return '<div class="ln">'+esc(l)+'</div>'}).join('')+'</div>'});
          h+='</div>';
        }
      }
      h+='<div class="note"><div class="orig" style="margin:0;padding:0;border:0"><div class="en">'+esc(s.en)+'</div><div class="ko">'+esc(s.ko)+'</div></div></div>';
    }
    h+='</span></div>';
  });
  h+='</div>';
  app.innerHTML=h;
  var k=selCount(m);
  if(!submitted)setFoot('<div class="info"><b>표시 '+k+' / '+N+'개</b><small>이 영역 '+secSel(m,si)+'개</small></div><button id="sub">제출하기</button>');
  else setFoot('<div class="info"><b>점수 '+res.score+' / '+N+'</b><small>이 영역 찾음 '+res.perSec[si].found+' / '+secTotal(m,si)+'</small></div><button class="ghost" id="redo">다시 풀기</button>');
  document.getElementById('tolist').onclick=function(){HUB.last.clear(APP.step);regions()};
  document.getElementById('pv').onclick=function(){if(si>0)openRegion(si-1)};
  document.getElementById('nx').onclick=function(){if(si<SECS.length-1)openRegion(si+1)};
  app.querySelectorAll('[data-bm]').forEach(function(b){b.onclick=function(){
    var i=+b.getAttribute('data-bm'),cur=st.bm;
    if(cur&&cur.si===si&&cur.i===i)st.bm=null;else st.bm={si:si,i:i};
    persist();
    app.querySelectorAll('[data-bm]').forEach(function(x){x.classList.remove('bm')});
    if(st.bm)b.classList.add('bm');
  }});
  if(!submitted){
    app.querySelectorAll('.wd').forEach(function(w){w.onclick=function(){
      var kk=w.getAttribute('data-k');
      if(st.sel[kk]){delete st.sel[kk];w.classList.remove('sel')}else{st.sel[kk]=1;w.classList.add('sel')}
      persist();
      var c=selCount(m),ft=document.querySelector('#foot .info');
      if(ft)ft.innerHTML='<b>표시 '+c+' / '+N+'개</b><small>이 영역 '+secSel(m,si)+'개</small>';
    }});
  }
  wireCommon();
  if(!submitted){HUB.last.set(APP.step,{m:m,si:si,a:focusI!=null?focusI:0});HUB.last.track(APP.step,'.sent',function(){return {m:MODE,si:SI}})}
  var fi=(focusI!=null)?focusI:(st.bm&&st.bm.si===si?st.bm.i:null);
  if(fi!=null){var el=document.getElementById('s'+fi);if(el)setTimeout(function(){el.scrollIntoView({block:'center'})},30)}else window.scrollTo(0,0);
}
home();
if(APP.modes.length===1)openMode(APP.modes[0].key);
(function(){
  var L=HUB.last.get(APP.step);
  if(L&&L.m&&SECS[L.si]&&APP.modes.some(function(x){return x.key===L.m})){
    MODE=L.m;SUB[L.m]=false;RES[L.m]=null;
    openRegion(L.si,L.a||0);
    HUB.last.toast('마지막으로 보던 곳(본문 '+SECS[L.si].key+' · '+((L.a||0)+1)+'번 문장)에서 이어서 열었어요','처음부터',function(){HUB.last.clear(APP.step);regions()});
  }
})();
})();
