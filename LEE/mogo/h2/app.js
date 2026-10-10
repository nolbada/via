(function(){
'use strict';
var app=document.getElementById('app');
var TITLE='26년 주성고2 (2학기 기말 대비)';
var KEY='mogo26-h2-v2';
var S={done:{},days:[2,4,6],bm:'tb',hv:'sched',open:{},seen:{},stars:{},vc:{}};
try{var raw=JSON.parse(localStorage.getItem(KEY)||'{}');for(var k in raw)S[k]=raw[k]}catch(e){}
['done','open','seen','stars','vc'].forEach(function(k){if(!S[k]||typeof S[k]!=='object')S[k]={}});
var GATE=!!(window.MOGO&&MOGO.on),gateMsg='';
if(GATE){var cr0=MOGO.cred();S.acct=cr0?{name:cr0.n,pin:cr0.p}:null}
function save(keep){if(!keep)S.ts=Date.now();try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}if(!keep)schedPush()}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
function fmt(s){return esc(s).replace(/\[\[(.+?)\]\]/g,'<span class="sig">$1</span>').replace(/\{\{(.+?)\}\}/g,'<span class="cw">$1</span>')}
function shuffle(a){var b=a.slice(),i,j,t;for(i=b.length-1;i>0;i--){j=Math.floor(Math.random()*(i+1));t=b[i];b[i]=b[j];b[j]=t}return b}
function foot(){return '<div class="foot">동남비타민영어학원</div>'}

/* ---------- 지문 목록 ---------- */
var GORDER=['tb','g2410','g23','g22','g2610'];
var GSHORT={tb:'교과서 4과 파트 ',g2410:'24년 10월 ',g23:'23년 11월 ',g22:'22년 11월 ',g2610:'26년 10월 '};
var GBM={tb:['교과서','4과'],g2410:['24년','10월'],g23:['23년','11월'],g22:['22년','11월'],g2610:['26년','10월']};
var M=window.MANIFEST.slice();
for(var q=1;q<=10;q++)M.push({id:'g2610-'+q,group:'g2610',no:q,label:'26년 10월 지문 '+q,topic:'',lesson:false,kind:'text',tb:false,ready:false});
var BYID={};
M.forEach(function(m){
  BYID[m.id]=m;m.short=GSHORT[m.group]+m.no+(m.tb?'':'번');
  var pm=/\((.+)\)\s*$/.exec(m.label||'');m.sub=m.tb?(pm?pm[1]:m.topic):(m.topic||'');
});
function ofGroup(g){return M.filter(function(m){return m.group===g}).sort(function(a,b){return (a.lesson===b.lesson?0:(a.lesson?-1:1))||a.no-b.no})}
var TABN={1:'본문+내용이해',2:'어휘 함정 피하기',3:'문법 포인트',f:'시험 직전 마무리 (파이널 주간)',4:'동사형 말하기 시험'};
var TSHORT={1:'내용이해',2:'어휘',3:'문법',f:'파이널 주간',4:'동사형'};
var WGT={tb:4,core:3,light:2,chart:1.5};
function tier(m){return m.tb?'tb':m.lesson?'core':(m.kind&&m.kind!=='text')?'chart':'light'}
function reqTabs(m){var t=tier(m);return (t==='tb'||t==='core')?[1,2,3]:[1,2]}
function hasVerb(m){var t=tier(m);return t==='tb'||t==='core'}
function menuTabs(m){var a=reqTabs(m).concat(['f']);if(hasVerb(m))a.push(4);return a}
function isDone(k){return !!S.done[k]}
function pstat(m){var r=reqTabs(m),n=0;r.forEach(function(t){if(S.done[m.id+':'+t])n++});if(n===r.length)return 'done';return (n>0||S.seen[m.id])?'prog':''}
function badge(m){var s=pstat(m);return s==='done'?'<span class="stt done">완료</span>':(s==='prog'?'<span class="stt prog">진행 중</span>':'')}
function schoolTag(m){return (m.lesson&&!m.tb)?'<span class="sch">학교</span>':''}
function togglePass(id){var m=BYID[id],all=pstat(m)==='done';reqTabs(m).forEach(function(t){var k=id+':'+t;if(all)delete S.done[k];else S.done[k]=1});if(!all)S.seen[id]=1;save()}

/* ---------- 날짜·진도표 ---------- */
var WD=['일','월','화','수','목','금','토'];
var START=new Date(2026,9,10),REVIEW=new Date(2026,10,23),EXAM=new Date(2026,11,1);
function dstr(d){return (d.getMonth()+1)+'/'+d.getDate()+'('+WD[d.getDay()]+')'}
function addDays(d,n){return new Date(d.getFullYear(),d.getMonth(),d.getDate()+n)}
function dayDiff(a,b){return Math.round((new Date(b.getFullYear(),b.getMonth(),b.getDate())-new Date(a.getFullYear(),a.getMonth(),a.getDate()))/86400000)}
var TODAY=new Date();
function todayKey(){return TODAY.getFullYear()+'-'+(TODAY.getMonth()+1)+'-'+TODAY.getDate()}
var REVIEW_PLAN=[
 [['rv1a','시험 직전 마무리: 교과서 4과 (파트 1~7)','range'],['rv1b','동사형 연습: 교과서 4과','verb'],['rv1c','별표 친 문장 다시 읽기']],
 [['rv2a','시험 직전 마무리: 학교 지문 (24년 10월)','range'],['rv2b','동사형 연습: 학교 지문','verb'],['rv2c','문법 포인트 틀린 카드 다시']],
 [['rv3a','시험 직전 마무리: 나머지 지문','range'],['rv3b','동사형 시험모드 한 번','verb'],['rv3c','어휘 틀린 문제 다시']],
 [['rv4a','약한 지문 다시','range'],['rv4b','동사형 틀린 문장만 마지막 확인','verb']]
];
function buildPlan(){
  var order=[];GORDER.forEach(function(g){ofGroup(g).forEach(function(m){order.push(m)})});
  var sess=[],d=START;
  while(d<REVIEW){if(S.days.indexOf(d.getDay())>=0)sess.push({date:d,items:[],used:0,type:'study'});d=addDays(d,1)}
  if(!sess.length)sess.push({date:START,items:[],used:0,type:'study'});
  var tot=order.reduce(function(s,m){return s+WGT[tier(m)]},0),cap=Math.max(6,Math.ceil(tot/Math.max(1,sess.length-2))),si=0;
  order.forEach(function(m){
    var w=WGT[tier(m)];
    while(si<sess.length-1&&sess[si].used+w>cap&&sess[si].used>0)si++;
    sess[si].items.push(m);sess[si].used+=w;
  });
  /* 말하기 검사: 공부한 수업의 다음 수업에 받음 (릴레이). 마지막 수업에서 공부한 것은 같은 날 공부 직후. 파이널 주간으로 안 넘어감 */
  sess.forEach(function(s){s.chk=[]});
  sess.forEach(function(s,i){s.items.forEach(function(m){if(m.ready&&hasVerb(m))sess[Math.min(i+1,sess.length-1)].chk.push(m)})});
  var rv=[],ri=0;d=REVIEW;
  while(d<EXAM){if(S.days.indexOf(d.getDay())>=0){var it=REVIEW_PLAN[Math.min(ri,REVIEW_PLAN.length-1)];rv.push({date:d,type:'review',rv:it.map(function(x){return {k:x[0],label:x[1],go:x[2]||''}})});ri++}d=addDays(d,1)}
  return {study:sess,review:rv};
}

/* ---------- 지문 데이터 ---------- */
function loadP(id,cb){
  if(window.MG&&window.MG[id]){cb(window.MG[id]);return}
  var sc=document.createElement('script');sc.src=MOGO.src('data',id);window.MOGO_DENY='';
  sc.onload=function(){
    if(window.MG&&window.MG[id]){cb(window.MG[id]);return}
    if(GATE&&window.MOGO_DENY){gateOut(window.MOGO_DENY);return}
    sc.onerror();
  };
  sc.onerror=function(){app.innerHTML='<div class="card"><h2>불러오지 못했어요</h2><p class="muted">인터넷 연결을 확인하고 다시 눌러 주세요.</p><button class="btn homebig" data-go="home">진도표로</button></div>'};
  document.head.appendChild(sc);
}

/* ---------- 신호어 · 조심할 어휘 이유 ---------- */
var SIGR=[
 [/^(but|however|yet)$/,'앞 내용과 반대로 흐름이 꺾여요. 뒤가 말하려는 핵심일 때가 많아요.'],
 [/^(whereas|while)$/,'두 내용을 대조해요. 앞뒤가 서로 반대인지 확인해요.'],
 [/^(although|though)$/,'양보예요. 앞은 인정하고 뒤가 진짜 하고 싶은 말이에요.'],
 [/^conversely$/,'앞과 반대되는 경우를 말해요.'],
 [/^alternatively$/,'다른 방법이나 선택지를 내놓아요.'],
 [/^not (simply|so much)$/,'A라기보다 B라는 구조예요. 뒤의 B가 핵심이에요.'],
 [/^not$/,'부정이에요. 어디까지 부정하는지 범위를 확인해요.'],
 [/^if\b/,'조건(가정)이에요. 뒤의 결과와 짝으로 읽어요.'],
 [/^without$/,'~이 없다면이라는 가정이에요.'],
 [/^imagine$/,'상상해 보라며 가정 상황을 시작해요.'],
 [/^the more$/,'the more A, the more B = A할수록 B해요. 짝으로 읽어요.'],
 [/^(because|due to)$/,'이유를 말해요. 뒤가 원인이에요.'],
 [/^(thus|and thus|consequently|as a result|for this reason)$/,'앞이 원인, 뒤가 결과예요.'],
 [/^(for example|for instance|such as)$/,'앞 내용을 구체적인 예로 들어요.'],
 [/^(in other words|that is)$/,'앞 내용을 쉬운 말로 다시 설명해요.'],
 [/^in fact$/,'사실은. 앞 내용을 강조하거나 바로잡아요.'],
 [/^(also|besides|furthermore|what is more|even more importantly|as well as|along with)$/,'내용을 덧붙여요.'],
 [/^to make matters worse$/,'더 나쁜 상황을 덧붙여요.'],
 [/^(first|second|third|finally|firstly|secondly)$/,'순서를 나타내요. 열거의 몇 번째인지 알려 줘요.'],
 [/^for all$/,'~에도 불구하고(양보)예요. 뒤에 반대 내용이 와요.'],
 [/^before$/,'~하기 전에(시간)예요.'],
 [/^until$/,'~할 때까지(시간)예요.'],
 [/^exception$/,'예외예요. 일반 규칙에서 벗어나는 경우를 말해요.'],
 [/^obviously$/,'명백히. 필자가 확실하다고 보는 부분이에요.']
];
function whySig(t){
  t=t.toLowerCase().replace(/\{\{|\}\}/g,'').replace(/[,.:;]/g,'').replace(/\s+/g,' ').trim();
  for(var i=0;i<SIGR.length;i++)if(SIGR[i][0].test(t))return SIGR[i][1];
  return '';
}
function chunkWhy(P,rawc){
  var out=[],m,re=/\[\[(.+?)\]\]/g;
  while((m=re.exec(rawc))){var w=whySig(m[1]);if(w)out.push('<span class="why sg2"><b>꺾이는 신호</b> '+esc(w)+'</span>')}
  re=/\{\{(.+?)\}\}/g;
  while((m=re.exec(rawc))){var r=P.cwr&&P.cwr[m[1].toLowerCase()];if(r)out.push('<span class="why cw2"><b>조심</b> '+esc(r)+'</span>')}
  return out.join('');
}

/* ---------- 공통 조각 ---------- */
function sentRow(P,n){
  var s=P.sents[n-1],key=P.id+':'+n,on=!!S.stars[key];
  var h='<div class="srow" data-n="'+n+'"><div class="srh"><span class="no">'+n+'</span><button class="star'+(on?' on':'')+'" type="button" data-a="star" data-k="'+key+'" aria-pressed="'+on+'" aria-label="막히는 문장 별표">'+(on?'★':'☆')+'</button></div><div class="stx">';
  s.c.forEach(function(c,i){
    if(i)h+='<span class="sl">/</span>';
    h+='<button class="ck" type="button" data-a="ck" aria-expanded="false"><span class="en">'+fmt(c[0])+'</span><span class="ko">'+esc(c[1])+chunkWhy(P,c[0])+'</span></button>';
  });
  h+='</div><div class="sbtn"><button type="button" data-a="tr" aria-expanded="false">해석 · 이 문장, 결국 이 얘기</button></div>';
  h+='<div class="blk ko" hidden>'+esc(s.ko)+'</div><div class="blk story" hidden>'+esc(s.story)+'</div></div>';
  return h;
}
function quizBox(o){
  var list=shuffle(o.opts);
  var h='<div class="quiz"><div class="q">'+esc(o.q)+'</div><div class="opts">';
  list.forEach(function(p){h+='<button class="opt" type="button" data-a="opt" data-ok="'+p[1]+'">'+esc(p[0])+'</button>'});
  return h+'</div><div class="verdict" hidden></div><div class="ex" hidden>'+o.ex.map(function(x){return '<p>'+esc(x)+'</p>'}).join('')+'</div></div>';
}
function nav(prev,next,lock,label){
  var h='<div class="nav'+(prev?'':' one')+'">';
  if(prev)h+='<button class="btn ghost" type="button" data-go="'+prev+'">이전</button>';
  if(next)h+='<button class="btn" type="button" data-go="'+next+'"'+(lock?' data-lock disabled':'')+'>'+(label||'다음')+'</button>';
  return h+'</div>';
}
function head(P,step){
  var m=BYID[P.id];
  var h='<header class="phd"><div class="navrow"><button class="homebtn" type="button" data-go="home">진도표로</button>'+(step!==0?'<button class="ghostbtn" type="button" data-go="p/'+P.id+'">지문 메뉴</button>':'')+'</div><h1 class="ptitle">'+esc(m.short)+'</h1>'+(m.sub?'<p class="psub">'+esc(m.sub)+'</p>':'')+'<div class="chips">';
  if(P.textbook)h+='<span class="chip">교과서</span>';
  if(P.lesson&&!P.textbook)h+='<span class="chip sch2">학교</span>';
  if(P.qtype&&P.qtype!=='교과서')h+='<span class="chip">'+esc(P.qtype)+'</span>';
  if(P.rate)h+='<span class="chip">오답률 '+P.rate+'%</span>';
  h+='</div></header>';
  if(step!==0){
    h+='<div class="tabs t'+menuTabs(m).length+'">';
    menuTabs(m).forEach(function(t){h+='<button type="button" class="'+(String(step)===String(t)?'on':'')+'" data-go="p/'+P.id+'/'+t+((t===1||t===3)?'/0':'')+'">'+TSHORT[t]+(isDone(P.id+':'+t)?'<small>완료</small>':'')+'</button>'});
    h+='</div>';
  }
  return h;
}
function markRow(P,t,text){
  var on=isDone(P.id+':'+t);
  return '<div class="mark-done"><span>'+esc(text)+'</span><button class="chk" type="button" data-a="chk" data-k="'+P.id+':'+t+'" aria-pressed="'+on+'" aria-label="완료 표시"></button></div>';
}
function exitRow(P){return '<div class="exitrow"><button class="btn homebig" type="button" data-go="home">진도표로 돌아가기</button><button class="btn ghost" type="button" data-go="p/'+P.id+'">지문 메뉴</button></div>'}
function markDone(id,t){if(!S.done[id+':'+t]){S.done[id+':'+t]=1;save()}}

/* ---------- 자동 동기화 (구글 시트, GitHub Pages 배포에서만) ---------- */
var SYNC=window.MOGO_SYNC||'',SCOPE=window.MOGO_SCOPE||'',syncMsg='',pushT=null;
function stamp(){var d=new Date();return (d.getHours()<10?'0':'')+d.getHours()+':'+(d.getMinutes()<10?'0':'')+d.getMinutes()}
function qs(o){return Object.keys(o).map(function(k){return k+'='+encodeURIComponent(o[k])}).join('&')}
function countDone(){return Object.keys(S.done).length}
function schedPush(){if(!SYNC||!S.acct)return;clearTimeout(pushT);pushT=setTimeout(push,2500)}
function setSyncMsg(m){syncMsg=m;var e=document.getElementById('syncst');if(e)e.textContent=m}
function push(){
  if(!SYNC||!S.acct)return;
  fetch(SYNC+'?'+qs({act:'put',scope:SCOPE,name:S.acct.name,pin:S.acct.pin,ts:S.ts||Date.now(),cnt:countDone(),data:exportCode()}))
   .then(function(r){return r.json()}).then(function(j){setSyncMsg(j&&j.ok?'저장됨 '+stamp():(j&&j.err==='pin'?'이 이름은 다른 번호로 이미 있어요':'저장하지 못했어요. 인터넷을 확인해요'))}).catch(function(){setSyncMsg('저장하지 못했어요. 인터넷을 확인해요')});
}
function pull(first){
  if(!SYNC||!S.acct)return;
  setSyncMsg('불러오는 중');
  fetch(SYNC+'?'+qs({act:'get',scope:SCOPE,name:S.acct.name,pin:S.acct.pin})).then(function(r){return r.json()}).then(function(j){
    if(!j||!j.ok){setSyncMsg(j&&j.err==='pin'?'번호가 달라요. 같은 이름이 이미 있어요':'연결하지 못했어요');if(j&&j.err==='pin')S.acct=null,save(1);render();return}
    if(j.data&&(!S.ts||j.ts>S.ts)){
      var r=importCode(j.data,!first&&S.synced);S.ts=j.ts;S.synced=true;save(1);
      if(first&&Object.keys(S.done).length){push()}
      setSyncMsg('불러옴 '+stamp()+(r?' · 새로 체크 '+r+'개':''));render();
    }else{S.synced=true;save(1);push()}
  }).catch(function(){setSyncMsg('연결하지 못했어요. 인터넷을 확인해요')});
}
/* ---------- 기기 옮기기 코드 (폰 <-> 태블릿) ---------- */
var SLOTS=[['tb',1,7],['g2410',20,40],['g23',20,42],['g22',28,40],['g2610',1,8]],RVK=['rv1a','rv1b','rv1c','rv2a','rv2b','rv2c','rv3a','rv3b','rv3c','rv4a','rv4b','rv4c'];
var TOR=[1,2,3,'f'],LT=[1,2,3,'f',4],B64='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
var BYG={};M.forEach(function(m){BYG[m.group+':'+m.no]=m.id});
var SL=[],SLI={};SLOTS.forEach(function(r){for(var n=r[1];n<=r[2];n++){var id=BYG[r[0]+':'+n];SL.push(id||null);if(id)SLI[id]=SL.length-1}});
function bits(n,w){var s=n.toString(2);while(s.length<w)s='0'+s;return s}
function exportCode(){
  var b='',i,id;for(i=0;i<7;i++)b+=S.days.indexOf(i)>=0?'1':'0';
  var li=1023;if(S.last&&SLI[S.last.id]!==undefined){var ti=LT.indexOf(S.last.tab);if(ti>=0)li=SLI[S.last.id]*8+ti}
  b+=bits(li,10);
  SL.forEach(function(sid){
    TOR.forEach(function(t){b+=(sid&&S.done[sid+':'+t])?'1':'0'});
    b+=(sid&&S.seen[sid])?'1':'0';
    b+=bits(Math.min(15,sid&&S.vc[sid]?S.vc[sid].n||0:0),4);
  });
  RVK.forEach(function(k){b+=S.done[k]?'1':'0'});
  var st=[];Object.keys(S.stars).forEach(function(k){if(!S.stars[k])return;var p=k.split(':'),ix=SLI[p[0]],n=+p[1];if(ix!==undefined&&n>=1&&n<=63)st.push([ix,n])});
  st=st.slice(0,255);b+=bits(st.length,8);st.forEach(function(x){b+=bits(x[0],7)+bits(x[1],6)});
  SL.forEach(function(sid){b+=(sid&&S.done[sid+':t'])?'1':'0'});
  while(b.length%6)b+='0';
  var o='';for(i=0;i<b.length;i+=6)o+=B64[parseInt(b.substr(i,6),2)];
  return 'M2.'+o;
}
function importCode(c,replace){
  c=String(c||'').replace(/\s+/g,'');
  if(c.indexOf('M2.')!==0)return null;
  var o=c.slice(3),b='',i;
  for(i=0;i<o.length;i++){var v=B64.indexOf(o[i]);if(v<0)return null;b+=bits(v,6)}
  if(b.length<7+10+SL.length*9+RVK.length+8)return null;
  var p=0,days=[];for(i=0;i<7;i++){if(b[p++]==='1')days.push(i)}
  var li=parseInt(b.substr(p,10),2);p+=10;
  var add=0;
  SL.forEach(function(sid){
    TOR.forEach(function(t){var on=b[p++]==='1';if(sid){var k=sid+':'+t;if(on&&!S.done[k]){S.done[k]=1;add++}else if(!on&&replace&&S.done[k])delete S.done[k]}});
    var sn=b[p++]==='1',vc=parseInt(b.substr(p,4),2);p+=4;
    if(sid){if(sn)S.seen[sid]=1;if(vc>((S.vc[sid]&&S.vc[sid].n)||0))S.vc[sid]={n:vc,last:(S.vc[sid]&&S.vc[sid].last)||''}}
  });
  RVK.forEach(function(k){var on=b[p++]==='1';if(on&&!S.done[k]){S.done[k]=1;add++}else if(!on&&replace&&S.done[k])delete S.done[k]});
  var cnt=parseInt(b.substr(p,8),2);p+=8;var ns={};
  for(i=0;i<cnt&&p+13<=b.length;i++){var ix=parseInt(b.substr(p,7),2),n=parseInt(b.substr(p+7,6),2);p+=13;if(SL[ix])ns[SL[ix]+':'+n]=1}
  if(replace)S.stars=ns;else for(var k2 in ns)S.stars[k2]=1;
  if(b.length-p>=SL.length){SL.forEach(function(sid){var on=b[p++]==='1';if(sid){var tk2=sid+':t';if(on&&!S.done[tk2]){S.done[tk2]=1;add++}else if(!on&&replace&&S.done[tk2])delete S.done[tk2]}})}
  if(days.length)S.days=days;
  if(li<1023){var sid2=SL[Math.floor(li/8)],t2=LT[li%8];if(sid2&&t2!==undefined)S.last={id:sid2,tab:t2}}
  save(replace?1:0);return add;
}
/* ---------- 첫 화면 ---------- */
function itemHTML(m){
  var ok=m.ready,st=pstat(m);
  return '<div class="it'+(st==='done'?' done':'')+'">'+(ok?'<button class="cb" type="button" data-a="pdone" data-id="'+m.id+'" aria-pressed="'+(st==='done')+'" aria-label="완료 표시"></button>':'<span class="cb off"></span>')
   +'<div class="im">'+(ok?'<button class="nm" type="button" data-go="p/'+m.id+'">':'<div class="nm pend">')+'<span class="nt">'+esc(m.short)+'</span>'+schoolTag(m)+badge(m)+(ok?'</button>':'<span class="pd">준비 중</span></div>')+(m.sub&&ok?'<span class="s">'+esc(m.sub)+'</span>':'')+'</div></div>';
}
function tcKey(m){return m.id+':t'}
function tcHTML(m,df){
  var on=isDone(tcKey(m)),ok=pstat(m)==='done',lock=!on&&!ok;
  return '<div class="it tc'+(on?' done':'')+(lock?' lock':'')+'"><button class="cb tcb" type="button" data-a="tchk" data-id="'+m.id+'" aria-pressed="'+on+'" aria-label="말하기 검사 완료 표시"'+(lock?' aria-disabled="true"':'')+'></button><div class="im"><span class="nm" style="cursor:default"><span class="nt">말하기 검사: '+esc(m.short)+'</span><span class="tcl">선생님 검사</span>'+(!on&&df>0?'<span class="tcl late">밀림</span>':'')+'</span>'+(lock?'<span class="s">공부(본문·어휘·문법)를 먼저 끝내면 검사를 받을 수 있어요</span>':(on?'':'<span class="s">공부 끝! 선생님께 동사형 말하기 검사를 받아요</span>'))+'</div></div>';
}
function tcStats(plan){
  var st={N:0,done:0,due:0,dueDone:0,behind:0,blocked:0,today:0};
  plan.study.forEach(function(s){(s.chk||[]).forEach(function(m){
    var d=isDone(tcKey(m))?1:0,df=dayDiff(s.date,TODAY);st.N++;st.done+=d;
    if(df>=0){st.due++;st.dueDone+=d;if(!d){if(df>0){st.behind++;if(pstat(m)!=='done')st.blocked++}else st.today++}}
  })});
  return st;
}
function tcBanner(plan){
  var st=tcStats(plan);if(!st.N)return '';
  var lastD=plan.study[plan.study.length-1].date;
  return '<div class="tcban"><div class="tch"><b>말하기 검사 (선생님께 받는 것)</b><span class="tcn">'+st.done+'/'+st.N+'</span></div>'
   +'<div class="tcrow">오늘까지 받아야 할 검사 <b>'+st.due+'개</b> 중 <b>'+st.dueDone+'개</b> 받음'+(st.behind?' · <b class="tcb2">'+st.behind+'개 밀림</b>':(st.today?' · 오늘 받을 것 '+st.today+'개':' · 밀린 것 없음'))+'</div>'
   +(st.blocked?'<div class="tcrow sm">밀린 것 중 '+st.blocked+'개는 공부가 아직 안 끝나서 못 받고 있어요. 공부를 먼저 끝내야 검사를 받을 수 있어요.</div>':'')
   +'<div class="tcrow sm">전체 '+st.N+'개를 파이널 주간 전('+dstr(lastD)+'까지)에 모두 받도록 수업마다 나눴어요. 공부한 지문은 다음 수업에서 검사를 받고, 마지막 수업에서 공부한 지문은 공부 직후에 받아요. 보라색 칸이 선생님 검사예요.</div></div>';
}
function sessHTML(s){
  var df=dayDiff(s.date,TODAY),isToday=df===0,left=0,late,tcLate=false;
  if(s.type==='review')s.rv.forEach(function(x){if(!isDone(x.k))left++});
  else s.items.forEach(function(m){if(!m.ready||pstat(m)!=='done')left++});
  late=df>0&&left>0&&(s.type==='review'||s.items.some(function(m){return m.ready}));
  if(s.chk)tcLate=df>0&&s.chk.some(function(m){return !isDone(tcKey(m))});
  var h='<div class="sess'+(isToday?' today':'')+(s.type==='review'?' rev':'')+'"><div class="dt"><b>'+(s.date.getMonth()+1)+'/'+s.date.getDate()+'</b><span>'+WD[s.date.getDay()]+'요일</span>'+(isToday?'<em>오늘</em>':late?'<em class="late">밀린 숙제</em>':tcLate?'<em class="late tcl2">밀린 검사</em>':'')+'</div><div class="items">';
  if(s.type==='review'){
    s.rv.forEach(function(x){
      var on=isDone(x.k);
      h+='<div class="it'+(on?' done':'')+'"><button class="cb" type="button" data-a="chk" data-k="'+x.k+'" aria-pressed="'+on+'" aria-label="완료 표시"></button><div class="im"><span class="nm" style="cursor:default"><span class="nt">'+esc(x.label)+'</span></span>'+(x.go?'<button class="lk" type="button" data-a="hv" data-v="'+(x.go==='verb'?'verb':'range')+'">열기</button>':'')+'</div></div>';
    });
  }else if(!s.items.length&&!(s.chk&&s.chk.length)){h+='<div class="free">예비 시간: 밀린 숙제 따라잡기, 틀린 어휘 · 동사형 다시 풀기</div>'}
  else{s.items.forEach(function(m){h+=itemHTML(m)});if(s.chk)s.chk.forEach(function(m){h+=tcHTML(m,df)})}
  return h+'</div></div>';
}
function vcN(id){return (S.vc[id]&&S.vc[id].n)||0}
function verbBanner(){
  var tot=0,vl=M.filter(function(m){return m.ready&&hasVerb(m)});vl.forEach(function(m){tot+=vcN(m.id)});
  return '<button class="vbanner" type="button" data-a="hv" data-v="verb"><span><b>동사형 말하기 시험 대비</b><small>학원에서 꼭 시험으로 봐요 · 누적 연습 '+tot+'회</small></span><i>열기</i></button>';
}
function viewSched(){
  var plan=buildPlan(),h='';
  var weeks={};
  plan.study.concat(plan.review).forEach(function(s){var w=Math.floor(dayDiff(START,s.date)/7);(weeks[w]=weeks[w]||[]).push(s)});
  var keys=Object.keys(weeks).map(Number).sort(function(a,b){return a-b});
  var curW=Math.max(0,Math.floor(dayDiff(START,TODAY)/7));
  h+='<div class="sbar"><div class="set"><span>수업 요일</span>'+WD.map(function(w,i){return '<button type="button" data-a="day" data-d="'+i+'" class="'+(S.days.indexOf(i)>=0?'on':'')+'">'+w+'</button>'}).join('')+'</div><button class="closeall" type="button" data-a="closeall">모두 닫기</button></div>';
  h+=tcBanner(plan);
  keys.forEach(function(w){
    var list=weeks[w],a=list[0].date,b=list[list.length-1].date,n=0,dn=0,cn=0,cd=0;
    list.forEach(function(s){if(s.type==='review')s.rv.forEach(function(x){n++;if(isDone(x.k))dn++});else{s.items.forEach(function(m){n++;if(m.ready&&pstat(m)==='done')dn++});(s.chk||[]).forEach(function(m){cn++;if(isDone(tcKey(m)))cd++})}});
    var hasRev=list.some(function(s){return s.type==='review'});
    var openNow=(S.open['w'+w]!==undefined)?S.open['w'+w]:(w===curW||(curW>keys[keys.length-1]&&w===keys[keys.length-1]));
    h+='<details class="wk" data-w="w'+w+'"'+(openNow?' open':'')+'><summary><span class="wt">'+(w>=7?'시험 주간':(w+1)+'주차')+(hasRev?'<span class="rv">최종점검</span>':'')+'<small>'+dstr(a)+' ~ '+dstr(b)+'</small></span><span class="cnt">'+dn+'/'+n+(cn?'<i class="tcc">검사 '+cd+'/'+cn+'</i>':'')+'</span></summary>'+list.map(sessHTML).join('')+'</details>';
  });
  h+='<div class="note">시험 전날 11/30(월)은 새 공부 없이 틀린 것만 훑어요. 체크한 항목은 줄이 그어져요. 못 끝낸 날은 밀린 숙제로 남아요. 학교 표시는 학교 수업에서 다룬 지문이에요.</div>';
  return h;
}
var RG='';
var GFULL={tb:['교과서','NE능률 영어II 4과'],g2410:['24년 10월','고2 모의고사'],g23:['23년 11월','고2 모의고사'],g22:['22년 11월','고2 모의고사'],g2610:['26년 10월','고2 모의고사']};
function viewRange(){
  var h='';
  if(!RG||!GFULL[RG]){
    h+='<div class="note" style="margin:2px 2px 8px">먼저 범위를 고르고, 그 안에서 지문을 골라요.</div><div class="shelf one">';
    GORDER.forEach(function(g){
      var L=ofGroup(g),rd=L.filter(function(m){return m.ready}),dn=rd.filter(function(m){return pstat(m)==='done'}).length;
      var sc=L.filter(function(m){return m.lesson}).length;
      h+='<button class="prow" type="button" data-a="rg" data-g="'+g+'"><span><b>'+GFULL[g][0]+'</b><span class="d">'+GFULL[g][1]+' · '+L.length+'지문'+(sc?' · 학교 '+sc:'')+(rd.length<L.length?(g==='g2610'?' · 시험 후 추가':' · 준비 중 '+(L.length-rd.length)):'')+'</span></span><span class="vcn">'+(rd.length?dn+'/'+rd.length:'예정')+' ›</span></button>';
    });
    return h+'</div>';
  }
  h+='<div class="navrow" style="margin:0 0 8px"><button class="ghostbtn" type="button" data-a="rg" data-g="">‹ 범위 선택</button></div><div class="note" style="margin:0 2px 8px"><b>'+GFULL[RG][0]+'</b> '+GFULL[RG][1]+'</div><div class="shelf one">';
  ofGroup(RG).forEach(function(m){
    if(m.ready)h+='<button class="prow" type="button" data-go="p/'+m.id+'"><span><b>'+esc(m.short)+schoolTag(m)+'</b><span class="d">'+esc(m.sub)+'</span></span><span>'+badge(m)+'</span></button>';
    else h+='<div class="prow off"><span><b>'+esc(m.short)+(m.lesson?'<span class="sch">학교</span>':'')+'</b><span class="d">'+(m.group==='g2610'?'모의고사 지문은 추후 공지 후 추가돼요':'준비 중')+'</span></span></div>';
  });
  return h+'</div><div class="note">학교 표시는 학교 수업에서 다룬 지문이에요.</div>';
}
function viewVerbTab(){
  var vl=M.filter(function(m){return m.ready&&hasVerb(m)}),tot=0;vl.forEach(function(m){tot+=vcN(m.id)});
  var h='<div class="vintro"><b>동사형은 학원에서 말하기 시험으로 봐요</b><p>한 번에 외워지지 않아요. 틈날 때마다 조금씩 반복해요. 연습을 마칠 때마다 횟수가 쌓여요. 누적 <b>'+tot+'회</b></p></div><div class="shelf one">';
  vl.forEach(function(m){
    h+='<button class="prow" type="button" data-go="p/'+m.id+'/4"><span><b>'+esc(m.short)+schoolTag(m)+'</b><span class="d">'+esc(m.sub)+'</span></span><span class="vcn">'+(isDone(tcKey(m))?'<span class="tcl">검사 완료</span> ':'')+(vcN(m.id)?vcN(m.id)+'회':'0회')+'</span></button>';
  });
  return h+'</div>';
}
function viewHome(){
  var ready=M.filter(function(m){return m.ready}),dn=ready.filter(function(m){return pstat(m)==='done'}).length;
  var dd=dayDiff(TODAY,EXAM);
  var h='<div class="top"><div class="toprow"><div><div class="brand">동남비타민영어학원</div><h1>'+TITLE+'</h1></div>'+'<div class="ddcol">'+(dd>=0?'<span class="dday">D-'+dd+'</span>':'')+'<span class="tapa" aria-label="전체 지문 중 타파한 지문"><b>'+dn+'</b>/'+M.length+' 타파</span></div></div>'
   +'<div class="meta">영어II 2학기 기말고사 12/1(화) · 주 3회 2시간 기준 진도표</div>'
   +'<div class="bar" role="img" aria-label="진행률"><i style="width:'+(M.length?Math.round(dn/M.length*100):0)+'%"></i></div>'
   +'<div class="note">지문 1개 완료 = 본문·어휘·문법 모두 체크 (시험 직전 마무리는 제외)</div></div>';
  if(S.last&&BYID[S.last.id]&&BYID[S.last.id].ready&&TABN[S.last.tab]&&S.last.tab!=='undefined'){
    var lm=BYID[S.last.id];h+='<button class="resume" type="button" data-go="p/'+lm.id+'/'+S.last.tab+((S.last.tab===1||S.last.tab===3)?'/0':'')+'"><small>마지막으로 하던 곳</small><b>'+esc(lm.short)+' · '+TABN[S.last.tab]+'</b><span>이어서 하기</span></button>';
  }
  if(S.hv!=='verb')h+=verbBanner();
  h+='<div class="hvtabs" role="tablist">'+[['sched','플래너로'],['range','범위별로'],['verb','동사형 시험 대비']].map(function(x){return '<button type="button" role="tab" class="'+(S.hv===x[0]?'on':'')+'" aria-selected="'+(S.hv===x[0])+'" data-a="hv" data-v="'+x[0]+'">'+x[1]+'</button>'}).join('')+'</div>';
  h+=S.hv==='range'?viewRange():(S.hv==='verb'?viewVerbTab():viewSched());
  var acctUI='';if(GATE){acctUI='<div class="note"><b>'+esc(S.acct?S.acct.name:'')+'</b> 님으로 자동 저장 중 · <span id="syncst">'+esc(syncMsg||'')+'</span></div><div class="cd"><button type="button" class="btn sm" data-a="acct-now">지금 동기화</button><button type="button" class="btn sm ghost" data-a="acct-out">다른 학생으로 로그인</button></div>'}
  else if(SYNC){acctUI=S.acct?'<div class="note"><b>'+esc(S.acct.name)+'</b> 님으로 자동 저장 중 · <span id="syncst">'+esc(syncMsg||'')+'</span></div><div class="cd"><button type="button" class="btn sm" data-a="acct-now">지금 동기화</button><button type="button" class="btn sm ghost" data-a="acct-out">연결 해제</button></div>':'<p class="note"><b>이름과 번호 4자리</b>를 한 번 입력하면 폰·태블릿 어디서 열어도 같은 기록이 이어져요. 같은 이름이 있으면 이름 뒤에 B나 학교를 붙여요.</p><div class="cd"><input id="acn" placeholder="이름 (예: 홍길동)" autocomplete="off"><input id="acp" placeholder="번호 4자리" inputmode="numeric" maxlength="4" style="max-width:96px"><button type="button" class="btn sm" data-a="acct-in">연결</button></div><div class="note" id="syncst" role="status">'+esc(syncMsg||'')+'</div>'}
  h+='<details class="wk syncbox" data-w="sync"'+((S.open.sync||(SYNC&&!S.acct))?' open':'')+'><summary><span class="wt">'+(SYNC?'기록 저장 · 다른 기기에서 이어하기':'다른 기기로 기록 옮기기')+'<small>폰에서 하던 것을 태블릿에서 이어서</small></span></summary><div class="sx">'+acctUI+(SYNC?'<div class="sec" style="margin:4px 0 0">코드로 옮기기 (자동 저장을 안 쓸 때)</div>':'')+'<p class="note">1) 지금 쓰던 기기에서 아래 코드를 복사해 카톡 나에게 보내요.<br>2) 다른 기기에서 이 앱을 열고 코드를 붙여넣어 불러와요.<br>체크한 것, 별표, 마지막 위치, 수업 요일이 옮겨져요. 두 기기 기록은 합쳐져요.</p><div class="cd"><input id="mycode" readonly value="'+esc(exportCode())+'" aria-label="내 기록 코드"><button type="button" class="btn sm" data-a="copy">복사</button></div><div class="cd"><input id="incode" placeholder="여기에 코드 붙여넣기" aria-label="기록 코드 붙여넣기"><button type="button" class="btn sm" data-a="imp">불러오기</button></div><div class="note" id="smsg" role="status"></div></div></details>';
  return h+foot();
}

/* ---------- 지문 메뉴 ---------- */
function viewMenu(P){
  var m=BYID[P.id];
  var D={1:'전체 '+P.sents.length+'문장 · '+P.acts.length+'막 흐름 · 직독직해 · 막히는 문장 별표',2:'유의어·반의어 연결 퀴즈 · 뜻 분류 던지기',3:'문법 카드 '+P.gram.length+'개 · 쉬운 예시와 확인',f:'흐름 핵심어 순서 · 요약문 완성 · 고장 난 문장',4:'말하기 시험 대비 · 반복 연습 · 누적 '+vcN(P.id)+'회'};
  var h=head(P,0);
  if(P.textbook)h+='<div class="legend"><span>교과서는 내용에서 많이 막혀요. 1번을 천천히 읽어요.</span></div>';
  h+='<div class="sechd">평소 학습</div>';
  reqTabs(m).forEach(function(t,i){
    h+='<button type="button" class="stepcard" data-go="p/'+P.id+'/'+t+((t===1||t===3)?'/0':'')+'"><span class="no">'+(i+1)+'</span><span><b>'+TABN[t]+'</b><span class="d">'+D[t]+'</span>'+(isDone(P.id+':'+t)?'<span class="ok">완료</span>':'')+'</span></button>';
  });
  h+='<div class="sechd">시험 직전 마무리 (파이널 주간에 해요)</div><button type="button" class="stepcard" data-go="p/'+P.id+'/f"><span class="no">&#10003;</span><span><b>'+TABN.f+'</b><span class="d">'+D.f+'</span>'+(isDone(P.id+':f')?'<span class="ok">완료</span>':'')+'</span></button>';
  if(hasVerb(m))h+='<div class="sechd">동사형 말하기 시험 (학원 시험)</div><button type="button" class="stepcard" data-go="p/'+P.id+'/4"><span class="no">&#9654;</span><span><b>'+TABN[4]+'</b><span class="d">'+D[4]+'</span></span></button>';
  return h+foot();
}

/* ---------- 탭별 화면 ---------- */
function viewV(P,t,src,txt){return head(P,t)+'<iframe class="emb" src="'+src+'" title="'+TABN[t]+'"></iframe>'+markRow(P,t,txt)+exitRow(P)+foot()}
function viewVerb(P){
  return head(P,4)+'<iframe class="emb" src="verb/index.html#'+P.id+'" title="동사형"></iframe><div class="vcrow"><span id="vcn">누적 연습 '+vcN(P.id)+'회</span><button class="btn" type="button" data-a="vcp" data-id="'+P.id+'">이번 연습 끝 (+1회)</button></div>'+exitRow(P)+foot();
}
function viewS1(P,i){
  var h=head(P,1),A=P.acts,n=A.length,N=P.sents.length;
  if(i==='s'){
    var sl=[];for(var x=1;x<=N;x++)if(S.stars[P.id+':'+x])sl.push(x);
    h+='<div class="card"><div class="kicker">별표 친 문장 '+sl.length+'개</div><div class="ctrl"><button class="btn sm" type="button" data-a="allx">모두 펼치기</button></div>';
    if(!sl.length)h+='<p class="muted">아직 별표한 문장이 없어요. 막히는 문장 번호 옆 ☆를 눌러 두면 여기에 모여요.</p>';
    sl.forEach(function(s){h+=sentRow(P,s)});
    return h+'</div>'+nav('p/'+P.id+'/1/0','',false)+foot();
  }
  if(i<n){
    var a=A[i],rg=a.sents[0]+(a.sents.length>1?'~'+a.sents[a.sents.length-1]:''),sc=0;
    for(var y=1;y<=N;y++)if(S.stars[P.id+':'+y])sc++;
    h+='<div class="card"><div class="kicker">'+esc(a.name)+' / '+n+'막 · 문장 '+rg+'번 (전체 '+N+'문장)</div><h2>'+esc(a.title)+'</h2><ul class="gist">'+a.gist.map(function(g){return '<li>'+esc(g)+'</li>'}).join('')+'</ul><div class="easy"><b>쉬운 그림</b> '+esc(a.easy)+'</div>';
    h+='<div class="ctrl"><button class="btn sm" type="button" data-a="allx">모두 펼치기</button>'+(sc?'<button class="btn sm ghost" type="button" data-go="p/'+P.id+'/1/s">별표 문장 '+sc+'개</button>':'')+'</div>';
    a.sents.forEach(function(s){h+=sentRow(P,s)});
    h+='</div><div class="card"><div class="kicker">확인</div>'+quizBox({q:a.q,opts:a.opts,ex:a.ex})+'</div>';
    h+=nav(i?'p/'+P.id+'/1/'+(i-1):'','p/'+P.id+'/1/'+(i+1),true,i===n-1?'흐름 한눈에':'다음 막');
  }else{
    markDone(P.id,1);
    h+='<div class="card"><div class="kicker">흐름 한눈에</div><h2>꺾이는 곳마다 이야기가 바뀌어요</h2>';
    if(P.flow.length){h+='<div class="flow">';P.flow.forEach(function(f,k){if(k&&f.sig)h+='<div class="fsig"><span class="sig">'+esc(f.sig)+'</span></div>';else if(k)h+='<div class="fsig"> </div>';h+='<div class="fstep"><b>'+esc(f.label)+'</b>'+esc(f.text)+'</div>'});h+='</div>'}
    if(P.bends.length){h+='<div class="kicker">흐름이 꺾이는 곳</div>';P.bends.forEach(function(b){h+='<div class="bend"><span class="num" style="font-family:var(--font-display);font-size:24px;color:var(--accent)">'+esc(b[0])+'</span><div><b>'+esc(b[1])+'</b> <span class="muted">'+esc(b[2])+'</span><div>'+esc(b[3])+'</div></div></div>'})}
    if(P.mainsent)h+='<div class="sg"><div class="en">'+esc(P.mainsent.en)+'</div><div class="ko">'+esc(P.mainsent.ko)+'</div></div>';
    h+='</div>'+nav('p/'+P.id+'/1/'+(n-1),'p/'+P.id+'/2',false,'어휘 함정 피하기로');
  }
  return h+foot();
}
function mk(s){return esc(s).replace(/&lt;mark&gt;/g,'<mark>').replace(/&lt;\/mark&gt;/g,'</mark>')}
function viewS3(P,i){
  var G=P.gram,n=G.length,h=head(P,3);
  if(!n){return h+'<div class="card"><h2>이 지문은 문법 카드가 없어요</h2><p class="muted">본문+내용이해와 어휘를 먼저 챙겨요.</p></div>'+exitRow(P)+foot()}
  if(i<n){
    var g=G[i],s=P.sents[g.n-1];
    h+='<div class="card"><div class="prog">문법 '+(i+1)+' / '+n+' · 문장 '+g.n+'번</div><h2>'+esc(g.title)+'</h2><div class="sg"><div class="en">'+mk(g.en)+'</div><div class="ko">'+esc(s?s.ko:'')+'</div></div>'
    +'<div class="eg"><div class="kicker">먼저 쉬운 예시</div><div class="en">'+esc(g.eg[0])+'</div><div class="ko">'+esc(g.eg[1])+'</div></div>'+quizBox(g)+'</div>'
    +nav(i?'p/'+P.id+'/3/'+(i-1):'','p/'+P.id+'/3/'+(i+1),true,i===n-1?'마무리':'다음');
  }else{
    markDone(P.id,3);
    h+='<div class="card"><div class="kicker">마무리</div><h2>문법 포인트를 모두 봤어요</h2><div class="sg"><div class="en">'+esc(P.mainsent?P.mainsent.en:P.label)+'</div><div class="ko">'+esc(P.mainsent?P.mainsent.ko:P.topic)+'</div></div></div>'+exitRow(P);
  }
  return h+foot();
}

/* ---------- 라우팅 ---------- */
function gateText(e){
  return e==='out'?'수강 중인 학생만 이용할 수 있어요. 선생님께 문의해요.':e==='lock'?'여러 번 틀려서 잠시 잠겼어요. 15분 뒤에 다시 해요.':e==='net'?'연결하지 못했어요. 인터넷을 확인하고 다시 해요.':'이름 또는 번호가 맞지 않아요. 다시 확인해요.';
}
function gateOut(e){MOGO.clear();S.acct=null;S.synced=false;save(1);gateMsg=gateText(e);render()}
function viewLogin(){
  return '<div class="top"><div class="toprow"><div><div class="brand">동남비타민영어학원</div><h1>'+TITLE+'</h1></div></div><div class="meta">처음 한 번만 이름과 번호를 입력해요</div></div>'
   +'<div class="card"><h2>학생 확인</h2><p class="note">선생님이 알려 준 <b>이름</b>과 <b>번호 4자리</b>를 입력해요. 입력하면 폰, 태블릿 어디서 열어도 같은 기록이 이어져요.</p>'
   +'<div class="cd"><input id="gn" placeholder="이름" autocomplete="off"><input id="gp" placeholder="번호 4자리" inputmode="numeric" maxlength="4" style="max-width:110px"><button type="button" class="btn sm" data-a="gate-in">열기</button></div>'
   +'<div class="note" id="gmsg" role="status" style="color:var(--trap)">'+esc(gateMsg||'')+'</div></div>'+foot();
}
function render(){
  if(GATE&&!MOGO.cred()){app.innerHTML=viewLogin();window.scrollTo(0,0);return}
  var hs=(location.hash||'#home').replace('#','').split('/');
  if(hs[0]!=='p'||!BYID[hs[1]]||!BYID[hs[1]].ready){app.innerHTML=viewHome();window.scrollTo(0,0);return}
  var id=hs[1],tab=hs[2],i=hs[3]==='s'?'s':(parseInt(hs[3],10)||0),m=BYID[id];
  app.innerHTML='<div class="card"><h2>불러오는 중</h2></div>';
  loadP(id,function(P){
    var html,t=tab==='f'?'f':(tab?+tab:0);
    if(t===3&&reqTabs(m).indexOf(3)<0)t=0;
    if(t===4&&!hasVerb(m))t=0;
    if([1,2,3,4,'f'].indexOf(t)<0)t=0;
    if(!S.seen[id]){S.seen[id]=1;save()}
    if(t){S.last={id:id,tab:t};save(1)}
    if(!t)html=viewMenu(P);
    else if(t===1)html=viewS1(P,i);
    else if(t===2)html=viewV(P,2,'voca/index.html#'+id,'어휘를 끝냈으면 체크해요');
    else if(t==='f')html=viewV(P,'f','voca/index.html#'+id+'/f','마무리를 끝냈으면 체크해요');
    else if(t===3)html=viewS3(P,i);
    else html=viewVerb(P);
    app.innerHTML=html;window.scrollTo(0,0);
  });
}
function go(h){if(location.hash==='#'+h)render();else location.hash=h}
function atHome(){var h=location.hash||'#home';return h==='#home'||h===''||h.indexOf('#p/')!==0}
app.addEventListener('toggle',function(e){var d=e.target;if(d.dataset&&d.dataset.w){S.open[d.dataset.w]=d.open;save(1)}},true);
app.addEventListener('click',function(e){
  var t=e.target.closest('[data-a],[data-go]');if(!t)return;
  if(t.dataset.go){if(!t.disabled)go(t.dataset.go);return}
  var a=t.dataset.a;
  if(a==='ck'){var o=t.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false')}
  else if(a==='tr'){
    var box=t.closest('.srow'),bl=box.querySelectorAll('.blk'),sh=bl[0].hidden;
    [].forEach.call(bl,function(b){b.hidden=!sh});t.setAttribute('aria-expanded',sh?'true':'false');t.classList.toggle('on',sh);
  }else if(a==='allx'){
    var card=t.closest('.card'),show=t.dataset.s!=='1';
    [].forEach.call(card.querySelectorAll('.ck'),function(c){c.classList.toggle('open',show);c.setAttribute('aria-expanded',show?'true':'false')});
    [].forEach.call(card.querySelectorAll('.blk'),function(b){b.hidden=!show});
    [].forEach.call(card.querySelectorAll('.sbtn button'),function(b){b.classList.toggle('on',show);b.setAttribute('aria-expanded',show?'true':'false')});
    t.dataset.s=show?'1':'';t.textContent=show?'모두 가리기':'모두 펼치기';
  }else if(a==='star'){
    var kk=t.dataset.k;if(S.stars[kk])delete S.stars[kk];else S.stars[kk]=1;save();
    var on=!!S.stars[kk];t.classList.toggle('on',on);t.setAttribute('aria-pressed',on?'true':'false');t.textContent=on?'★':'☆';
  }else if(a==='opt'){
    var qz=t.closest('.quiz');if(qz.dataset.done)return;qz.dataset.done='1';
    var ok=t.dataset.ok==='1';
    [].forEach.call(qz.querySelectorAll('.opt'),function(b){b.classList.add('locked');if(b.dataset.ok==='1')b.classList.add('right')});
    if(!ok)t.classList.add('wrong');
    var v=qz.querySelector('.verdict');v.hidden=false;v.className='verdict '+(ok?'r':'w');v.textContent=ok?'정답':'아쉬워요. 이유를 봐요';
    qz.querySelector('.ex').hidden=false;
    [].forEach.call(document.querySelectorAll('[data-lock]'),function(b){b.disabled=false});
  }else if(a==='chk'){
    var k=t.dataset.k;if(S.done[k])delete S.done[k];else S.done[k]=1;save();
    if(atHome())render();else t.setAttribute('aria-pressed',S.done[k]?'true':'false');
  }else if(a==='tchk'){
    var tid=t.dataset.id,tk=tid+':t';
    if(S.done[tk])delete S.done[tk];else if(pstat(BYID[tid])==='done')S.done[tk]=1;else return;
    save();render();
  }else if(a==='pdone'){togglePass(t.dataset.id);render()}
  else if(a==='hv'){if(t.dataset.v==='range')RG='';S.hv=t.dataset.v;save(1);if(atHome())render();else go('home')}
  else if(a==='vcp'){
    var vid=t.dataset.id,c=S.vc[vid]=S.vc[vid]||{n:0,last:''};c.n++;c.last=todayKey();save();
    var vn=document.getElementById('vcn');if(vn)vn.textContent='누적 연습 '+c.n+'회';
  }else if(a==='closeall'){
    [].forEach.call(app.querySelectorAll('details.wk'),function(d){d.open=false;if(d.dataset.w)S.open[d.dataset.w]=false});save(1);
  }else if(a==='acct-in'){
    var an=(document.getElementById('acn').value||'').trim(),ap=(document.getElementById('acp').value||'').trim();
    if(!an||!/^\d{4}$/.test(ap)){setSyncMsg('이름과 숫자 4자리를 입력해요');return}
    S.acct={name:an,pin:ap};S.synced=false;S.open.sync=true;save(1);pull(true);
  }else if(a==='gate-in'){
    var gn=(document.getElementById('gn').value||'').trim(),gp=(document.getElementById('gp').value||'').trim(),gm=document.getElementById('gmsg');
    if(!gn||!/^\d{4}$/.test(gp)){gm.textContent='이름과 숫자 4자리를 입력해요.';return}
    gm.textContent='확인하는 중';t.disabled=true;
    MOGO.login(gn,gp,function(r){
      if(r&&r.ok){MOGO.set(gn,gp);S.acct={name:gn,pin:gp};S.synced=false;gateMsg='';save(1);render();pull(true)}
      else{gateMsg=gateText(r&&r.err);render()}
    });
  }else if(a==='acct-out'){if(GATE){gateOut('');gateMsg='';render();return}S.acct=null;S.synced=false;save(1);setSyncMsg('');render()}
  else if(a==='acct-now'){S.synced=true;pull(false)}
  else if(a==='copy'){
    var mc=document.getElementById('mycode'),sm=document.getElementById('smsg');mc.value=exportCode();mc.select();
    var done=function(){sm.textContent='복사했어요. 카톡 나에게 보내기에 붙여넣어요.'};
    try{navigator.clipboard.writeText(mc.value).then(done,function(){try{document.execCommand('copy');done()}catch(e){sm.textContent='코드를 길게 눌러 복사해 주세요.'}})}catch(e){try{document.execCommand('copy');done()}catch(e2){sm.textContent='코드를 길게 눌러 복사해 주세요.'}}
  }else if(a==='imp'){
    var iv=document.getElementById('incode').value,r=importCode(iv);
    if(r===null){document.getElementById('smsg').textContent='코드가 올바르지 않아요. 처음부터 끝까지 복사했는지 확인해요.';return}
    S.open.sync=true;save();render();var m2=document.getElementById('smsg');if(m2)m2.textContent='불러왔어요. 새로 체크된 항목 '+r+'개';
  }else if(a==='bm'){S.bm=t.dataset.g;save(1);render()}else if(a==='rg'){RG=t.dataset.g||'';render();window.scrollTo(0,0)}
  else if(a==='day'){
    var d=+t.dataset.d,ix=S.days.indexOf(d);
    if(ix>=0){if(S.days.length>1)S.days.splice(ix,1)}else S.days.push(d);
    S.days.sort(function(x,y){return x-y});save();render();
  }
});
window.addEventListener('hashchange',render);
document.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target&&(e.target.id==='gp'||e.target.id==='gn')){var b=app.querySelector('[data-a="gate-in"]');if(b)b.click()}});
render();
if(SYNC&&S.acct)pull(!S.synced);
})();
