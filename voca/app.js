/* 주성고 어휘 함정 피하기 (voca 시리즈) - 공통 앱 코드
   규칙: 영어 단어를 화면에 보일 때는 반드시 뜻을 괄호로 붙인다. 뜻이 없는 단어는 문제에서 뺀다. */
(function(){
'use strict';
var QUOTA=20, ROUND=10;
var TYPE_NAME={S:'유의어',A:'반의어'};
var LV_NAME=['새것','보는 중','익힘','정복'];
var LV_COL=['var(--line)','var(--warn)','var(--accent)','var(--done)'];

function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function rnd(a){return a[Math.floor(Math.random()*a.length)]}
function shuffle(a){return a.map(function(v){return [Math.random(),v]}).sort(function(x,y){return x[0]-y[0]}).map(function(x){return x[1]})}
function today(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function dateLabel(){var d=new Date(),n=['일','월','화','수','목','금','토'];return (d.getMonth()+1)+'/'+d.getDate()+'('+n[d.getDay()]+')'}

/* ---------- 번들 -> 그래프 ---------- */
function build(B){
  var cw={};Object.keys(B.words).forEach(function(k){cw[k]=String(B.words[k]).replace(/\[([^\]]*)\]/g,'/$1').replace(/[()]/g,'').replace(/\s+/g,' ').trim()});
  var G={B:B,words:cw,L:{}};
  B.lessons.forEach(function(ls){
    var l=String(ls.no), edges=[], seen={}, adj={}, hubs={};
    B.hubs.filter(function(h){return String(h.l)===l}).forEach(function(h){
      hubs[h.w]=h;
      ['S','A'].forEach(function(t){
        (h[t]||[]).forEach(function(w){
          if(!B.words[h.w]||!B.words[w])return;            /* 뜻 누락 필터 */
          var id=l+':'+[h.w,w].sort().join('~')+':'+t;
          if(seen[id])return; seen[id]=1;
          edges.push({id:id,l:l,a:h.w,b:w,t:t,hub:h});
        });
      });
    });
    edges.forEach(function(e){
      (adj[e.a]=adj[e.a]||[]).push({o:e.b,t:e.t,e:e});
      (adj[e.b]=adj[e.b]||[]).push({o:e.a,t:e.t,e:e});
    });
    /* 같은 묶음(연결된 단어들) 계산 */
    var comp={},cid=0;
    Object.keys(adj).forEach(function(w){
      if(comp[w]!==undefined)return;
      var st=[w];comp[w]=cid;
      while(st.length){var x=st.pop();(adj[x]||[]).forEach(function(n){if(comp[n.o]===undefined){comp[n.o]=cid;st.push(n.o)}})}
      cid++;
    });
    var clash={};((B.clash||{})[l]||[]).forEach(function(p){(clash[p[0]]=clash[p[0]]||{})[p[1]]=1;(clash[p[1]]=clash[p[1]]||{})[p[0]]=1});
    var pool=Object.keys(adj);
    G.L[l]={no:l,title:ls.title,edges:edges,adj:adj,comp:comp,pool:pool,hubs:hubs,clash:clash,
      broken:B.broken.filter(function(b){return String(b.l)===l&&B.words[b.gl]&&B.words[b.bl]})};
  });
  return G;
}
function JB(G,w,a,b){var k=G.words[w],c=k.charCodeAt(k.length-1);return (c>=0xAC00&&c<=0xD7A3&&((c-0xAC00)%28)!==0)?a:b}
function W(G,w,jo){   /* 단어(뜻) + 조사. jo: '은는' '이가' '과와' '을를' 중 하나 */
  var k=G.words[w],s='<b class="v">'+esc(w)+'</b>('+esc(k)+')';
  if(!jo)return s;
  var c=k.charCodeAt(k.length-1),has=c>=0xAC00&&c<=0xD7A3&&((c-0xAC00)%28)!==0;
  return s+(has?jo.charAt(0):jo.charAt(1));
}

/* ---------- 기록 ---------- */
function newState(){return {v:1,name:'',lesson:null,rec:{},broken:{},days:{},recent:[]}}
function Store(id){
  this.key='voca:'+id; this.s=newState();
  try{var r=localStorage.getItem(this.key); if(r){var o=JSON.parse(r); if(o&&o.v===1)this.s=o}}catch(e){}
}
Store.prototype.save=function(){try{localStorage.setItem(this.key,JSON.stringify(this.s))}catch(e){}};
Store.prototype.code=function(id){return 'V1.'+btoa(unescape(encodeURIComponent(JSON.stringify({id:id,s:this.s}))))};
function decode(code){
  code=String(code).trim(); if(code.indexOf('V1.')!==0)throw new Error('형식이 달라요');
  var o=JSON.parse(decodeURIComponent(escape(atob(code.slice(3))))); if(!o||!o.s||o.s.v!==1)throw new Error('읽을 수 없어요'); return o;
}
function dirRec(s,id,dir){var r=s.rec[id]=s.rec[id]||{}; return r[dir]=r[dir]||{ok:0,tr:0,last:''}}
function mark(s,id,dir,ok){
  var d=dirRec(s,id,dir); d.tr++;
  if(ok){ if(d.last!==today()){d.ok++;d.last=today()} } else {d.ok=0;d.last=''}
}
function level(s,e){
  var r=s.rec[e.id]||{}, f=r.f,v=r.r;
  if(!((f&&f.tr)||(v&&v.tr)))return 0;
  var m=Math.min(f?f.ok:0,v?v.ok:0);
  return m>=2?3:m===1?2:1;
}
function counts(s,L){var c=[0,0,0,0];L.edges.forEach(function(e){c[level(s,e)]++});return c}
function todayN(s,l){var d=s.days[today()];return d&&d[l]?d[l]:0}
function addToday(s,l){var t=today();s.days[t]=s.days[t]||{};s.days[t][l]=(s.days[t][l]||0)+1}
function immunity(s,L){
  var n=0,ok=0;L.broken.forEach(function(b){var r=s.broken[b.l+':'+b.n+':'+b.g];if(r&&r.tr){n++;if(r.last)ok++}});
  return n?Math.round(ok/n*100):null;
}

/* ---------- 문제 만들기 ---------- */
function pickEdge(s,L,avoid){
  var ws=[];
  L.edges.forEach(function(e){
    if(avoid&&avoid[e.id])return;
    var lv=level(s,e); ws.push([e,[3.2,4,2,0.4][lv]]);
  });
  var tot=ws.reduce(function(a,x){return a+x[1]},0),r=Math.random()*tot;
  for(var i=0;i<ws.length;i++){r-=ws[i][1];if(r<=0)return ws[i][0]}
  return ws[0]?ws[0][0]:null;
}
function weakerDir(s,e){
  var r=s.rec[e.id]||{},f=r.f?r.f.ok:-1,v=r.r?r.r.ok:-1;
  if(f===v)return Math.random()<.5?'f':'r';
  return f<v?'f':'r';
}
function decoys(G,L,X,correct,n){
  var bad={};var cx=L.comp[X];
  var kos={};kos[G.words[X]]=1;
  (L.adj[X]||[]).forEach(function(a){kos[G.words[a.o]]=1});
  var out=[],pool=shuffle(L.pool);
  for(var i=0;i<pool.length&&out.length<n;i++){
    var w=pool[i];
    if(w===X||w===correct||L.comp[w]===cx)continue;
    if(L.clash&&L.clash[X]&&L.clash[X][w])continue;
    var k=G.words[w]; if(!k||kos[k])continue;
    if(out.some(function(o){return G.words[o]===k}))continue;
    out.push(w);
  }
  return out;
}
function makeQuiz(G,s,L,avoid){
  var e=pickEdge(s,L,avoid); if(!e)return null;
  var dir=weakerDir(s,e), X=dir==='f'?e.a:e.b, Y=dir==='f'?e.b:e.a;
  var ds=decoys(G,L,X,Y,3); if(ds.length<3)return null;
  return {kind:'quiz',e:e,dir:dir,X:X,Y:Y,choices:shuffle(ds.concat([Y]))};
}
function makeSort(G,s,L){
  var real=Math.random()<.6;
  if(real){
    var e=pickEdge(s,L); if(!e)return null;
    return {kind:'sort',e:e,X:e.a,Y:e.b,ans:e.t};
  }
  var h=rnd(Object.keys(L.hubs).filter(function(w){return L.adj[w]}));
  var ds=decoys(G,L,h,null,1); if(!ds.length)return null;
  var from=(L.adj[ds[0]]||[])[0];
  return {kind:'sort',X:h,Y:ds[0],ans:'N',from:from?from.o:null,fromT:from?from.t:null,fromHub:from?from.e.hub:null};
}
function pickBroken(s,L,used){
  var arr=L.broken.filter(function(b){return !used[b.l+':'+b.n+':'+b.g]});
  if(!arr.length)return null;
  var ws=arr.map(function(b){var r=s.broken[b.l+':'+b.n+':'+b.g];return [b,!r?4:(r.last?1:5)]});
  var tot=ws.reduce(function(a,x){return a+x[1]},0),r=Math.random()*tot;
  for(var i=0;i<ws.length;i++){r-=ws[i][1];if(r<=0)return ws[i][0]}
  return ws[0][0];
}

/* ---------- 설명 문장 ---------- */
function relLine(G,X,Y,t,asked){
  /* asked: 'hub' = 허브를 물어본 방향 / 'other' = 반대 방향 */
  if(t==='A') return asked==='hub' ? W(G,Y,'은는')+' '+W(G,X)+'의 반의어입니다.' : W(G,X)+'의 반대말은 '+W(G,Y)+'입니다.';
  return asked==='hub' ? W(G,Y,'은는')+' '+W(G,X,'과와')+' 뜻이 비슷한 유의어입니다.' : W(G,X,'과와')+' 뜻이 비슷한 말은 '+W(G,Y)+'입니다.';
}
function relF(G,X,Y,t){
  var sym=t==='A'?'\u2194':(t==='S'?'=':'\u2715');
  return '<span class="fm"><span class="fw"><b class="v">'+esc(X)+'</b> '+esc(G.words[X])+'</span><span class="sym s'+t+'">'+sym+'</span><span class="fw"><b class="v">'+esc(Y)+'</b> '+esc(G.words[Y])+'</span></span>';
}
function srcBlock(G,l,hub){
  if(!hub||!hub.n||!hub.story)return '';
  var sn=G.B.sents[l][String(hub.n)];
  return '<div class="src"><div class="num">교과서 '+l+'과 '+hub.n+'번 문장</div><div class="story">'+esc(hub.story).replace(/\(([A-Za-z~\- ]+)\)/,'(<b class="v">$1</b>)')+'</div>'+
    '<details><summary>이 문장 보기</summary><div class="en">'+esc(sn.e)+'</div><div class="ko">'+esc(sn.k)+'</div></details></div>';
}

/* ---------- 화면 ---------- */
function App(G,id,root){
  this.G=G;this.id=id;this.root=root;this.st=new Store(id);
  var first=G.B.lessons[0].no; this.l=String(this.st.s.lesson||first);
  this.home();
}
App.prototype.totalQ=function(no){var G=this.G,l=String(no),L=G.L[l];return this.listFor('all',no).length+L.broken.length+L.edges.length};
App.prototype.L=function(){return this.G.L[this.l]};
App.prototype.set=function(h){this.root.innerHTML=h};
App.prototype.home=function(){
  var self=this,G=this.G,s=this.st.s,L=this.L();
  var c=counts(s,L),tot=L.edges.length,n=Math.min(QUOTA,todayN(s,this.l));
  var im=immunity(s,L),bs=0,es=0;L.broken.forEach(function(x){var r=s.broken[x.l+':'+x.n+':'+x.g];if(r&&r.tr)bs++});L.edges.forEach(function(e){if(level(s,e)>0)es++});
  var tabs=G.B.lessons.map(function(ls){
    return '<button role="tab" data-l="'+ls.no+'" aria-selected="'+(String(ls.no)===self.l)+'">'+ls.no+'과<small>'+esc(ls.title)+'</small><small class="tot">전체 '+self.totalQ(ls.no)+'문항</small></button>';
  }).join('');
  var q='';for(var i=0;i<QUOTA;i++)q+='<i'+(i<n?' class="on"':'')+'></i>';
  var stack='',leg='';
  for(i=0;i<4;i++){
    stack+='<i style="width:'+(tot?c[i]/tot*100:0)+'%;background:'+LV_COL[i]+'"></i>';
    leg+='<div><b>'+c[i]+'</b><span class="dot" style="background:'+LV_COL[i]+'"></span>'+LV_NAME[i]+'</div>';
  }
  var recA=s.recent.filter(function(r){return String(r.l)===self.l}).map(function(r){return self.recentLine(r)}).filter(Boolean),rec=recA.join(''),recN=recA.length;
  var html='<main class="wrap">'+
  '<header><div class="brand">동남비타민영어학원</div><h1>'+esc(G.B.school||'')+' <em>어휘 함정</em> 피하기</h1>'+
  '<p class="sub">'+esc(G.B.book)+'</p></header>'+
  '<div class="who"><button class="chip" id="nm">'+(s.name?esc(s.name):'이름 적기')+'</button><span class="chip">'+dateLabel()+'</span></div>'+
  '<div class="tabs" role="tablist" aria-label="단원 선택">'+tabs+'</div>'+
  '<h3 class="grp">본문 내용 · 총 '+(self.prog('all',this.l).tot+L.broken.length)+'문항 <span>파트(❶❷❸…) 단위로 묻습니다</span></h3>'+
  '<section class="modes">'+
  (G.B.flow&&G.B.flow.length?'<button class="mode" data-m="flow"><strong>흐름 핵심어 순서 ('+self.prog('flow',this.l).seen+'/'+self.prog('flow',this.l).tot+')</strong><span>'+self.progLine('flow')+'</span><b class="go">'+self.goLabel('flow')+'</b></button>':'')+
  (G.B.summ&&G.B.summ.length?'<button class="mode" data-m="summ"><strong>요약문 완성 ('+self.prog('summ',this.l).seen+'/'+self.prog('summ',this.l).tot+')</strong><span>'+self.progLine('summ')+'</span><b class="go">'+self.goLabel('summ')+'</b></button>':'')+
  '<button class="mode trap" data-m="broken"><strong>고장 난 문장 ('+bs+'/'+L.broken.length+')</strong><span>교과서 문장 속 바뀐 단어를 찾는다</span><b class="go">시작</b></button>'+
  '</section>'+
  '<h3 class="grp">어휘 연결 · '+es+'/'+L.edges.length+' <span>같은 어휘 '+L.edges.length+'개를 연결로 한 번, 분류로 또 한 번 잡아줍니다</span></h3>'+
  '<section class="modes">'+
  '<button class="mode" data-m="quiz"><strong>연결 퀴즈 ('+es+'/'+L.edges.length+')</strong><span>유의어·반의어를 거꾸로도 묻는다</span><b class="go">시작</b></button>'+
  '<button class="mode" data-m="sort"><strong>뜻 분류 던지기 ('+es+'/'+L.edges.length+')</strong><span>답을 고른 뒤에야 뜻이 나온다</span><b class="go">시작</b></button>'+
  '</section>'+
  '<h3 class="grp">내 기록 <span>이 단원 전체 문항 기준</span></h3>'+
  (function(){var p=self.prog('all',self.l),T=self.totalQ(self.l),sn=p.seen+bs+es,pc=T?Math.round(sn/T*100):0;return '<section class="panel score"><h2>내 진도 <span>'+self.l+'과 전체 '+T+'문항 중</span></h2><div class="immune"><b>'+sn+'</b><div class="bar"><i style="width:'+pc+'%"></i></div></div>'+(p.wrong?'<p class="note">틀린 문제 '+p.wrong+'개</p><div class="btnrow"><button class="btn pri" id="wr">틀린 문제만 다시 풀기 ('+p.wrong+')</button></div>':'')+'</section>'})()+
  (rec?'<section class="panel score"><details class="recd"><summary><b>함정에 빠진 포인트 ('+recN+')</b> <span>최근에 틀린 문제 · 눌러서 펼치기</span></summary><ul class="miss">'+rec+'</ul></details></section>':'')+
  '<section class="panel save"><details><summary>기록 옮기기 (다른 기기·선생님께 보내기)</summary>'+
  '<p class="note">아래 코드를 복사해 두면 다른 기기에서 붙여넣어 이어 할 수 있어요.</p>'+
  '<textarea id="code" readonly></textarea><div class="btnrow"><button class="btn pri" id="cp">코드 복사</button></div>'+
  '<p class="note">다른 기기에서 받은 코드를 붙여넣고 복원하면 이 기기 기록이 바뀝니다.</p>'+
  '<textarea id="in" placeholder="여기에 코드를 붙여넣기"></textarea><div class="btnrow"><button class="btn" id="rs">붙여넣은 코드로 복원</button></div><p class="note" id="msg"></p></details></section>'+
  '<p class="foot">기록은 이 기기의 브라우저에 저장됩니다.</p></main>';
  this.set(html);
  var r=this.root;
  r.querySelector('.tabs').onclick=function(ev){var b=ev.target.closest('button');if(!b)return;self.l=b.getAttribute('data-l');self.st.s.lesson=self.l;self.st.save();self.home()};
  var wr=r.querySelector('#wr');if(wr)wr.onclick=function(){self.run('wrong')};
  r.querySelectorAll('.mode').forEach(function(b){b.onclick=function(){self.run(b.getAttribute('data-m'))}});
  r.querySelector('#nm').onclick=function(){
    var box=document.createElement('div');box.className='panel';
    box.innerHTML='<h2>이름</h2><input id="nmi" maxlength="12" style="width:100%;font:inherit;padding:9px;border-radius:10px;border:1px solid var(--line);background:var(--soft);color:var(--ink)" value="'+esc(s.name)+'"><div class="btnrow"><button class="btn pri" id="nmok">저장</button></div>';
    r.querySelector('.who').after(box);r.querySelector('#nmi').focus();
    r.querySelector('#nmok').onclick=function(){s.name=r.querySelector('#nmi').value.trim();self.st.save();self.sync();self.home()};
  };
  var ta=r.querySelector('#code');ta.value=this.st.code(this.id);
  r.querySelector('#cp').onclick=function(){
    var m=r.querySelector('#msg');
    try{navigator.clipboard.writeText(ta.value).then(function(){m.textContent='복사했어요.'},function(){ta.select();m.textContent='선택해 두었어요. 직접 복사해 주세요.'})}
    catch(e){ta.select();m.textContent='선택해 두었어요. 직접 복사해 주세요.'}
  };
  r.querySelector('#rs').onclick=function(){
    var m=r.querySelector('#msg');
    try{var o=decode(r.querySelector('#in').value); if(o.id!==self.id)throw new Error('다른 묶음의 코드예요'); self.st.s=o.s;self.st.save();self.l=String(o.s.lesson||self.l);self.home()}
    catch(e){m.textContent='복원하지 못했어요: '+e.message}
  };
};
App.prototype.recentLine=function(r){
  var G=this.G,L=this.G.L[r.l];
  if(r.k==='b'){
    var b=L.broken.filter(function(x){return x.n===r.n&&x.g===r.g})[0]; if(!b)return '';
    return '<li><div class="tag">'+r.l+'과 · '+r.n+'번 문장</div>'+esc(b.why)+'</li>';
  }
  if(r.k==='f'){var g=G.B.flow.filter(function(x){return x.id===r.id})[0]; if(!g)return '';
    return '<li><div class="tag">'+r.l+'과 · 흐름 순서</div>'+esc(g.scope)+'</li>';}
  if(r.k==='s'){var m=G.B.summ.filter(function(x){return x.id===r.id})[0]; if(!m)return '';
    return '<li><div class="tag">'+r.l+'과 · 요약문</div>'+esc(m.k)+'</li>';}
  var e=L.edges.filter(function(x){return x.id===r.id})[0]; if(!e)return '';
  return '<li><div class="tag">연결 오답</div>'+relF(G,e.b,e.a,e.t)+'</li>';
};
App.prototype.pushRecent=function(o){
  var s=this.st.s;o.at=Date.now();
  s.recent=s.recent.filter(function(r){return !(r.k===o.k&&r.l===o.l&&r.n===o.n&&r.g===o.g&&r.id===o.id)});
  s.recent.unshift(o);s.recent=s.recent.slice(0,12);
};
App.prototype.run=function(m){
  this.mode=m;this.cnt=0;this.right=0;this.used={};this.again=[];this.next();
};
App.prototype.shell=function(label,body){
  var self=this;
  this.set('<main class="wrap"><div class="top"><button class="back" id="bk">← 처음으로</button><span class="tagline">'+label+'</span></div>'+body+'</main>');
  this.root.querySelector('#bk').onclick=function(){self.home()};
};
App.prototype.end=function(){
  var self=this;
  this.shell('한 판 끝','<div class="card done"><div class="tagline">ROUND END</div><div class="score">'+this.right+' / '+this.cnt+'</div>'+
   '<div>틀린 건 다음 판에 먼저 다시 나옵니다. </div><button class="next" id="ag">한 판 더</button></div>');
  this.root.querySelector('#ag').onclick=function(){self.run(self.mode)};
  if(this.mode==='wrong'||this.mode==='all'){
    var ag=this.root.querySelector('#ag'),done=this.listFor('all',this.l).every(function(x){var d=self.st.s.done||{};return d[x.id]&&d[x.id].ok});
    if(this.mode==='wrong'||done){ag.textContent='처음으로';ag.onclick=function(){self.home()};
      var dv=this.root.querySelector('.card.done div:nth-child(3)');if(dv)dv.textContent=this.mode==='wrong'?'다시 풀 틀린 문제를 모두 풀었어요. 아직 틀린 건 홈에서 다시 볼 수 있어요.':'이 단원 본문 내용 문제를 모두 맞혔어요.'}
  }
};
App.prototype.next=function(){
  if(this.cnt>=this.rounds()){this.end();return}
  if(this.mode==='all'||this.mode==='wrong'){
    var L=this.listFor('all',this.l),d=this.st.s.done||{};
    var left=L.filter(function(x){return !d[x.id]||!d[x.id].ok});
    if(this.mode==='wrong')left=L.filter(function(x){return d[x.id]&&!d[x.id].ok});
    if(!left.length&&(this.cnt>0||this.mode==='wrong')){this.end();return}
    var it=this.pickItem(left.length?left:L);this.forced=it;
    if(it.steps)this.flowQ();else this.summ();return;
  }
  if(this.mode==='quiz')this.quiz();else if(this.mode==='sort')this.sort();else if(this.mode==='flow')this.flowQ();else if(this.mode==='summ')this.summ();else this.broken();
};
App.prototype.finish=function(ok,nm){ /* 한 문제 끝 */
  this.cnt++;if(ok)this.right++;
  if(nm!=='broken')addToday(this.st.s,this.l);
  this.st.save();this.sync();
};
/* --- 선생님 시트로 자동 기록 (voca/sync.js 에 주소가 있을 때만) --- */
App.prototype.sync=function(){
  var self=this,url=window.VOCA_SYNC; if(!url)return;
  clearTimeout(this._t);
  this._t=setTimeout(function(){
    try{
      var s=self.st.s; if(!s.dev){s.dev=Math.random().toString(36).slice(2,10)+Date.now().toString(36);self.st.save()}
      var G=self.G,ls=Object.keys(G.L).map(function(l){var L=G.L[l],c=counts(s,L),im=immunity(s,L);
        return {l:l,n:L.edges.length,c:c,im:im,t:todayN(s,l)}});
      var body=JSON.stringify({dev:s.dev,name:s.name||'',id:self.id,date:today(),ls:ls,code:self.st.code(self.id)});
      fetch(url,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain;charset=utf-8'},body:body,keepalive:true}).catch(function(){});
    }catch(e){}
  },1500);
};
/* --- 연결 퀴즈 --- */
App.prototype.quiz=function(){
  var self=this,G=this.G,s=this.st.s,L=this.L(),q;
  if(this.again.length&&this.cnt>=2&&Math.random()<.7)q=this.again.shift();
  else{for(var t=0;t<8&&!q;t++)q=makeQuiz(G,s,L,this.used)}
  if(!q){this.end();return}
  this.used[q.e.id]=1;
  var asked=q.dir==='f'?'hub':'other';
  var ch=q.choices.map(function(w,i){return '<button data-w="'+esc(w)+'">'+esc(w)+'<small class="ks"></small></button>'}).join('');
  this.shell('연결 퀴즈 '+(this.cnt+1)+' / '+ROUND,'<div class="card"><div class="hub"><div class="q">'+(q.e.t==='A'?'반의어(반대말)':'유의어(비슷한 말)')+'를 고르세요</div>'+
   '<div class="w">'+esc(q.X)+'</div><div class="k hide">&nbsp;</div></div><div class="choices" id="ch">'+ch+'</div><div id="fb"></div></div>');
  this.root.querySelectorAll('#ch button').forEach(function(b){b.onclick=function(){
    var w=b.getAttribute('data-w'),ok=w===q.Y;
    mark(s,q.e.id,q.dir,ok);
    self.finish(ok);
    if(!ok){self.again.push(q);self.pushRecent({k:'e',l:self.l,id:q.e.id})}
    self.root.querySelectorAll('#ch button').forEach(function(x){
      x.disabled=true;var ww=x.getAttribute('data-w');x.querySelector('.ks').textContent=G.words[ww];
      if(ww===q.Y)x.classList.add('ok');else if(ww===w)x.classList.add('no');
    });
    self.root.querySelector('.hub .k').innerHTML=esc(G.words[q.X]);self.root.querySelector('.hub .k').classList.remove('hide');
    var msg=(ok?'정답! ':'아쉬워요. ')+'<div class="fml">'+relF(G,q.X,q.Y,q.e.t)+'</div>';
    if(!ok)msg+='<div class="fml">'+relF(G,q.X,w,'N')+'</div>';
    self.root.querySelector('#fb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+msg+'</div>'+srcBlock(G,self.l,q.e.hub)+'<button class="next" id="nx">다음</button>';
    var nx=self.root.querySelector('#nx');nx.onclick=function(){self.next()};nx.focus();
  }});
};
/* --- 뜻 분류 던지기 --- */
App.prototype.sort=function(){
  var self=this,G=this.G,s=this.st.s,L=this.L(),q;
  for(var t=0;t<8&&!q;t++)q=makeSort(G,s,L);
  if(!q){this.end();return}
  this.shell('뜻 분류 던지기 '+(this.cnt+1)+' / '+ROUND,'<div class="card"><div class="hub"><div class="w">'+esc(q.X)+'</div><div class="k hide">&nbsp;</div></div>'+
   '<div class="chipbox"><div class="q">이 단어는 '+esc(q.X)+'와(과)</div><div class="c">'+esc(q.Y)+'</div><div class="k hide">&nbsp;</div></div>'+
   '<div class="choices three" id="ch"><button class="S" data-a="S"><span class="mark">=</span>비슷한 뜻<small>유의어</small></button><button class="A" data-a="A"><span class="mark">↔</span>반대 뜻<small>반의어</small></button><button class="N" data-a="N"><span class="mark">✕</span>상관없음<small>관계 없음</small></button></div><div id="fb"></div></div>');
  this.root.querySelectorAll('#ch button').forEach(function(b){b.onclick=function(){
    var a=b.getAttribute('data-a'),ok=a===q.ans;
    if(q.e)mark(s,q.e.id,'f',ok);
    self.finish(ok);
    if(!ok&&q.e)self.pushRecent({k:'e',l:self.l,id:q.e.id});
    self.root.querySelectorAll('#ch button').forEach(function(x){x.disabled=true;x.style.opacity=x.getAttribute('data-a')===q.ans||x===b?1:.45});
    var ks=self.root.querySelectorAll('.k');ks[0].innerHTML=esc(G.words[q.X]);ks[1].innerHTML=esc(G.words[q.Y]);
    ks[0].classList.remove('hide');ks[1].classList.remove('hide');
    var msg=ok?'정답! ':'아쉬워요. ';
    msg+='<div class="fml">'+relF(G,q.X,q.Y,q.ans)+'</div>';
    if(q.ans==='N'&&q.from)msg+='<div class="fml sub">'+relF(G,q.Y,q.from,q.fromT)+'</div>';
    self.root.querySelector('#fb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+msg+'</div>'+(q.e?srcBlock(G,self.l,q.e.hub):srcBlock(G,self.l,L.hubs[q.X])+(q.fromHub?srcBlock(G,self.l,q.fromHub):''))+'<button class="next" id="nx">다음</button>';
    var nx=self.root.querySelector('#nx');nx.onclick=function(){self.next()};nx.focus();
  }});
};
/* --- 고장 난 문장 --- */
function swap(tok,g,b){
  var m=/^([^A-Za-z]*)(.*?)([^A-Za-z]*)$/.exec(tok);
  var core=m[2]===g?m[2]:null; if(core===null)return null;
  var nb=(/^[A-Z]/.test(m[2]))?b.charAt(0).toUpperCase()+b.slice(1):b;
  return m[1]+nb+m[3];
}
App.prototype.broken=function(){
  var self=this,G=this.G,s=this.st.s,L=this.L();
  var b=pickBroken(s,L,this.used); if(!b){this.end();return}
  this.used[b.l+':'+b.n+':'+b.g]=1;
  var sn=G.B.sents[this.l][String(b.n)], toks=sn.e.split(' '), hit=-1, bad=null;
  for(var i=0;i<toks.length;i++){var sw=swap(toks[i],b.g,b.b);if(sw){hit=i;bad=sw;break}}
  if(hit<0){this.next();return}
  var altI={};(b.alt||[]).forEach(function(a){toks.forEach(function(t,i){var m=/^([^A-Za-z]*)(.*?)([^A-Za-z]*)$/.exec(t);if(i!==hit&&m[2]===a)altI[i]=1})});
  var html=toks.map(function(t,i){return i===hit?bad.split(' ').map(function(p){return '<button data-i="'+i+'">'+esc(p)+'</button>'}).join(' '):'<button data-i="'+i+'">'+esc(t)+'</button>'}).join(' ');
  this.shell('고장 난 문장 '+(this.cnt+1)+' / '+ROUND,'<div class="card"><div>교과서 문장인데 <b>한 단어가 다른 뜻으로 바뀌어</b> 있어요. 어디일까요?</div>'+
   '<div class="sent" id="sent">'+html+'</div><div id="fb"></div></div>');
  var key=b.l+':'+b.n+':'+b.g;
  this.root.querySelectorAll('#sent button').forEach(function(x){x.onclick=function(){
    var ci=+x.getAttribute('data-i'),ok=ci===hit||!!altI[ci];
    var r=s.broken[key]=s.broken[key]||{tr:0,last:false};r.tr++;r.last=ok;
    self.finish(ok,'broken');
    if(!ok)self.pushRecent({k:'b',l:self.l,n:b.n,g:b.g});
    var btns=[].slice.call(self.root.querySelectorAll('#sent button'));
    btns.forEach(function(y){y.disabled=true});
    btns.forEach(function(y){if(+y.getAttribute('data-i')===hit)y.classList.add('hit')}); if(!ok)x.classList.add('miss'); else if(ci!==hit)x.classList.add('hit');
    var truth=toks.map(function(t,i){return i===hit?'<mark>'+esc(t)+'</mark>':esc(t)}).join(' ');
    self.root.querySelector('#fb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+(ok?(ci!==hit?'이 단어를 고쳐도 말이 되는 문장이라 정답으로 인정해요. ':'정답! '):'아쉬워요. ')+'바뀐 단어는 '+W(G,b.bl)+JB(G,b.bl,'이고','고')+', 원래는 '+W(G,b.gl)+JB(G,b.gl,'이었어요','였어요')+'.</div>'+
     '<div class="truebox"><div class="tagline">진짜 문장 · 교과서 '+self.l+'과 '+b.n+'번</div><div>'+truth+'</div><div class="ko">'+esc(sn.k)+'</div></div>'+
     '<div class="trapbox"><div class="tagline">학교 선생님이 이렇게 뒤통수 칠 수 있어요</div>'+esc(b.why)+'</div>'+
     '<button class="next" id="nx">다음 문장</button>';
    var nx=self.root.querySelector('#nx');nx.onclick=function(){self.next()};nx.focus();
  }});
};

/* ---------- 제목·주제 낚시 / 요약문 완성 ---------- */
function evBlock(G,l,ev){
  return '<details class="evd"><summary>근거 문장 보기 ('+ev.map(function(n){return n+'번'}).join(', ')+')</summary>'+ev.map(function(n){
    var sn=G.B.sents[l][String(n)];return sn?'<div class="en">'+n+'. '+esc(sn.e)+'</div><div class="ko">'+esc(sn.k)+'</div>':''}).join('')+'</details>';
}
App.prototype.listFor=function(m,l){var B=this.G.B;var L=m==='flow'?B.flow:(m==='summ'?B.summ:(B.flow||[]).concat(B.summ||[]));return (L||[]).filter(function(x){return x.l===+l})};
App.prototype.prog=function(m,l){
  var d=(this.st.s.done=this.st.s.done||{}),L=this.listFor(m,l),seen=0,wrong=0;
  L.forEach(function(x){var r=d[x.id];if(r){seen++;if(!r.ok)wrong++}});
  return {tot:L.length,seen:seen,wrong:wrong};
};
App.prototype.pickItem=function(L){
  /* 안 푼 문제 먼저 -> 틀린 문제 -> 맞힌 문제(복습). 같은 문제가 연달아 나오지 않게 */
  var d=(this.st.s.done=this.st.s.done||{}),last=this.lastId;
  var c=L.filter(function(x){return x.id!==last||L.length===1});
  var a=c.filter(function(x){return !d[x.id]}); if(a.length)return rnd(a);
  a=c.filter(function(x){return !d[x.id].ok}); if(a.length)return rnd(a);
  return rnd(c);
};
App.prototype.markDone=function(id,ok){
  var d=(this.st.s.done=this.st.s.done||{});var r=d[id]=d[id]||{n:0};
  r.n++;r.ok=!!ok;r.at=Date.now();this.lastId=id;this.st.save();
};
App.prototype.progLine=function(m){
  var p=this.prog(m,this.l);
  if(!p.seen)return '아직 안 풀었어요';
  if(p.seen>=p.tot)return '모두 풀었어요'+(p.wrong?' · 틀린 '+p.wrong+'개 다시':' · 전부 맞힘, 복습 중');
  return p.seen+'/'+p.tot+' 풀어 봄'+(p.wrong?' · 틀린 '+p.wrong+'개':'')+' · 이어서 풀기';
};
App.prototype.goLabel=function(m){var p=this.prog(m,this.l);return p.seen&&p.seen<p.tot?'이어서':(p.seen?'복습':'시작')};
App.prototype.rounds=function(){
  var l=+this.l,B=this.G.B;
  if(this.mode==='flow'||this.mode==='summ'||this.mode==='all'||this.mode==='wrong')return Infinity;
  return ROUND;
};
App.prototype.flowQ=function(){
  var self=this,G=this.G,l=+this.l;
  var it=this.forced||this.pickItem(this.listFor('flow',l));this.forced=null;
  var st=it.steps,pg=this.prog((this.mode==='all'||this.mode==='wrong')?'all':'flow',l);
  var order=shuffle(st.map(function(x,i){return i}));
  var chips=order.map(function(i){return '<button class="chip2" data-i="'+i+'"><b>'+esc(st[i].en)+'</b><span>'+esc(st[i].ko)+'</span></button>'}).join('');
  this.shell((this.mode==='all'?l+'과 본문 내용 문제 · ':(this.mode==='wrong'?l+'과 틀린 문제 다시 풀기 · ':''))+'흐름 핵심어 순서 · '+pg.seen+'/'+pg.tot+' 풀어 봄',
    '<div class="card"><div class="tagline">'+l+'과 · '+esc(it.scope)+'</div><div class="qline"><b>글의 흐름 순서대로 핵심어를 눌러 보세요.</b></div>'+
    '<ol class="slots" id="slots"></ol><div class="pool" id="pool">'+chips+'</div>'+
    '<div class="btnrow"><button class="btn" id="undo">되돌리기</button><button class="btn pri" id="ck" disabled>확인</button></div><div id="fb"></div></div>');
  var placed=[],card=this.root.querySelector('.card');
  var qline=card.querySelector('.qline'),kof=document.createElement('button');
  kof.className='btn';kof.id='kof';qline.insertAdjacentElement('afterend',kof);
  function setKo(on){card.classList.toggle('koon',!!on);kof.textContent=on?'한글 가리기':'한글 함께보기';self.st.s.koOpen=!!on;self.st.save()}
  setKo(!!this.st.s.koOpen);
  kof.onclick=function(){setKo(!card.classList.contains('koon'))};
  function draw(){
    self.root.querySelector('#slots').innerHTML=placed.map(function(i,k){return '<li><b>'+(k+1)+'</b> '+esc(st[i].en)+' <small>'+esc(st[i].ko)+'</small></li>'}).join('');
    self.root.querySelectorAll('#pool .chip2').forEach(function(b){var k=placed.indexOf(+b.getAttribute('data-i'));b.disabled=k>=0;b.classList.toggle('used',k>=0);if(k>=0)b.setAttribute('data-no',k+1);else b.removeAttribute('data-no')});
    self.root.querySelector('#ck').disabled=placed.length<st.length;
  }
  this.root.querySelectorAll('#pool .chip2').forEach(function(b){b.onclick=function(){placed.push(+b.getAttribute('data-i'));draw()}});
  this.root.querySelector('#undo').onclick=function(){placed.pop();draw()};
  this.root.querySelector('#ck').onclick=function(){
    var res=placed.map(function(i,k){return i===k}),ok=res.every(Boolean);
    self.finish(ok,'broken');self.markDone(it.id,ok);
    if(!ok)self.pushRecent({k:'f',l:String(l),id:it.id});
    self.root.querySelectorAll('#pool .chip2,#undo,#ck').forEach(function(b){b.disabled=true});
    self.root.querySelector('#pool').className='pool off';self.root.querySelector('#undo').style.display='none';self.root.querySelector('#ck').style.display='none';
    self.root.querySelector('#slots').innerHTML=placed.map(function(i,k){return '<li class="'+(res[k]?'hit':'miss')+'"><b>'+(k+1)+'</b> '+esc(st[i].en)+' <small>'+esc(st[i].ko)+'</small></li>'}).join('');
    var chain=st.map(function(x){return '<span class="cl"><b>'+esc(x.en)+'</b> ('+esc(x.ko)+')</span>'}).join('<span class="ar"> → </span>');
    card.classList.add('koon');kof.style.display='none';
    var cards=st.map(function(x,k){
      var sn=G.B.sents[String(l)][String(x.n)];
      return '<details class="step"><summary><b>'+(k+1)+'</b> '+esc(x.en)+' <small>'+esc(x.ko)+'</small></summary><div class="line">'+esc(x.line)+' <span class="rg">('+esc(x.r)+'번 문장)</span></div>'+
        '<div class="en">'+x.n+'. '+esc(sn.e)+'</div><div class="ko">'+esc(sn.k)+'</div></details>'}).join('');
    self.root.querySelector('#fb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+(ok?'정답! 흐름을 순서대로 떠올렸어요.':'아쉬워요. 빨간 칸이 순서가 틀린 곳이에요.')+'</div>'+
      '<div class="truebox"><div class="tagline">흐름 한 줄</div><div class="chain">'+chain+'</div></div>'+
      '<div class="tagline" style="margin-top:10px">눌러서 뒤집어 보기 · 핵심어 뒤에 숨은 내용</div>'+cards+'<button class="next" id="nx">다음</button>';
    var nx=self.root.querySelector('#nx');nx.onclick=function(){self.next()};nx.focus();
  };
};
App.prototype.partOf=function(l,n){var P=(this.G.B.parts||{})[String(l)]||[];for(var i=0;i<P.length;i++)if(n>=P[i][0]&&n<=P[i][1])return P[i][2];return ''};
App.prototype.summ=function(){
  var self=this,G=this.G,l=+this.l,R=this.rounds();
  var m=this.forced||this.pickItem(this.listFor('summ',l));this.forced=null;
  var lab=['A','B'],cir=['①','②','③','④','⑤'];
  var opts=shuffle(m.opts);
  var text=esc(m.e).replace(/\(([AB])\)/g,'<b class="blank">($1)</b>');
  var two=opts[0].p.length===2;
  var html=opts.map(function(o,i){
    return '<button class="opt" data-i="'+i+'"><span class="no">'+cir[i]+'</span><span class="tx">'+o.p.map(function(w){return esc(w[0])}).join(two?'  –  ':'')+'</span><span class="kor pre">'+o.p.map(function(w,k){return (two?'('+lab[k]+') ':'')+'<b class="v">'+esc(w[0])+'</b> '+esc(w[2])}).join(' / ')+'</span></button>'}).join('');
  var T=(G.B.tales||{})[String(l)]||{},ps=[];
  m.ev.forEach(function(n){var p=self.partOf(l,n);if(p&&ps.indexOf(p)<0)ps.push(p)});
  var tl=ps.map(function(p){return '본문 '+p+(T[p]?' \u300c'+esc(T[p].t)+'\u300d':'')}).join(' + ');
  var tale=ps.map(function(p){return T[p]?'<div class="tale"><div class="tagline">이야기꾼 · 본문 '+p+' '+esc(T[p].t)+'</div><p>'+esc(T[p].s).replace(/([A-Za-z][A-Za-z\'\-, ]*[A-Za-z!])( \([^)]*\))/g,'<b>$1</b>$2')+'</p></div>':''}).join('');
  var pg=this.prog((this.mode==='all'||this.mode==='wrong')?'all':'summ',l);
  this.shell((this.mode==='all'?l+'과 본문 내용 문제 · ':(this.mode==='wrong'?l+'과 틀린 문제 다시 풀기 · ':''))+'요약문 완성 · '+pg.seen+'/'+pg.tot+' 풀어 봄','<div class="card"><div class="tagline">'+l+'과 '+tl+' · 빈칸에 들어갈 말로 가장 알맞은 것은?</div>'+
    (two?'<div class="tagline">(A) – (B) 순서</div>':'')+'<div class="btnrow"><button class="btn" id="kot">한글 펼치기</button></div><div class="sumtx">'+text+'</div><div class="kobox" id="kobox">'+esc(m.kb||m.k)+'</div><div class="optlist" id="ol">'+html+'</div><div id="fb"></div></div>');
  var done=false,card=this.root.querySelector('.card'),kot=this.root.querySelector('#kot');
  function setKo(on){card.classList.toggle('koon',!!on);kot.textContent=on?'한글 가리기':'한글 펼치기';self.st.s.koOpen=!!on;self.st.save()}
  setKo(!!this.st.s.koOpen);
  kot.onclick=function(){setKo(!card.classList.contains('koon'))};
  this.root.querySelectorAll('#ol .opt').forEach(function(b){b.onclick=function(){
    if(done)return;done=true;
    var pick=opts[+b.getAttribute('data-i')],ok=!!pick.c;
    self.finish(ok,'broken');self.markDone(m.id,ok);
    if(!ok)self.pushRecent({k:'s',l:String(l),id:m.id});
    self.root.querySelectorAll('#ol .opt').forEach(function(y,i){
      var o=opts[i];y.disabled=true;
      if(o.c)y.classList.add('hit');else if(y===b)y.classList.add('miss');
    });
    card.classList.add('koon');kot.style.display='none';self.root.querySelector('#kobox').style.display='none';
    var full=esc(m.e),ci=opts.filter(function(o){return o.c})[0];
    ci.p.forEach(function(w,k){full=full.replace('('+lab[k]+')','<mark>'+esc(w[0])+'</mark>')});
    self.root.querySelector('#fb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+(ok?'정답!':'아쉬워요. 정답은 '+cir[opts.indexOf(ci)]+'번이에요.')+'</div>'+
     '<div class="truebox"><div class="tagline">완성된 요약문</div><div>'+full+'</div><div class="ko">'+esc(m.k)+'</div></div>'+tale+
     evBlock(G,String(l),m.ev)+'<button class="next" id="nx">다음</button>';
    var nx=self.root.querySelector('#nx');nx.onclick=function(){self.next()};nx.focus();
  }});
};

/* ---------- 시작 ---------- */
window.VocaCore={build:build,decode:decode,counts:counts,level:level,immunity:immunity,todayN:todayN,W:W,relLine:relLine,LV_NAME:LV_NAME,QUOTA:QUOTA,esc:esc};
if(window.VID&&window.VOCADATA&&window.VOCADATA[window.VID]){
  var G=build(window.VOCADATA[window.VID]);
  var root=document.getElementById('app');
  window.VOCA_APP=new App(G,window.VID,root);
}
})();
