const OK='fbi_omr_v1';let O={};try{O=JSON.parse(localStorage.getItem(OK)||'{}')}catch(e){}
function osave(){try{localStorage.setItem(OK,JSON.stringify(O))}catch(e){}setLast({p:'omr',s:SQ,cur:cur})}
const $=document.getElementById('app'),CN=['①','②','③','④','⑤'];
const DATA=window.FBI_O[SQ],SID=DATA.set;O[SID]=O[SID]||{marks:{},sub:false};const M=O[SID];M.label=DATA.label;
let view=M.sub?'score':'sheet',cur=0,list=null,showKo={},showP=false,openAlt=true;
const RF={g1_23_31:[0,1],g1_23_39:[0,1,5],g1_25_31:[3],g1_25_36:[0,2,9]};let rd=false;
const items=DATA.items,qOf=it=>it.alt||it;
let openV={};
function v1H(it,tog){const v=it.v1;if(!v)return '';const hi=v.g<=2,c=hi?'var(--bad)':'var(--warn)',bg=hi?'var(--badbg)':'var(--warnbg)';
  let b='<div style="margin-top:8px;padding:8px 10px;border-radius:10px;background:'+bg+'"><b style="color:'+c+'">책이라면 확인하세요 · '+esc(v.t)+'</b>';
  if(tog&&!openV[it.no])return b+'</div><button class="link" onclick="openV['+it.no+']=true;sheet()">달라진 곳 보기</button>';
  b+='<div class="small" style="margin-top:4px">'+esc(v.n)+'</div>';
  v.l.forEach(x=>{b+='<div style="margin-top:10px;font-family:\'Segoe UI\',system-ui,sans-serif;font-size:15.5px"><div class="small"><b>'+x[0]+' 책</b></div><div>'+esc(x[1])+'</div><div style="text-align:center;color:var(--mu);font-size:18px;line-height:1.3">&darr;</div><div class="small"><b>'+x[0]+' 앱</b></div><div>'+esc(x[2])+'</div></div>'});
  b+='</div>';
  return tog?b+'<button class="link" onclick="openV['+it.no+']=false;sheet()">접기</button>':b}
function readScreen(){const ch=RF[SID];let h='<div class="nav"><a href="omr.html">&larr; 세트 목록</a><span class="small">'+esc(DATA.label)+'</span></div><h1>지문 먼저 읽기</h1><p class="sub">이 세트의 지문은 책(2쇄) 기준이라 시험지와 일부 문장이 달라요. 표시한 문장이 달라진 곳이에요. 충분히 읽은 뒤 답을 입력하세요.</p><div class="card" style="line-height:1.85">';DATA.passage.forEach((s,i)=>{h+=(ch.indexOf(i)>=0?'<mark>'+esc(s)+'</mark>':esc(s))+' '});h+='</div><p class="small"><mark>표시</mark> = 시험지 원문과 다른 문장</p><button class="btn" onclick="M.read=true;rd=false;osave();sheet()">다 읽었어요, 답 입력하기</button>';$.innerHTML=h;window.scrollTo(0,0)}
function sheet(){
  if(RF[SID]&&(!M.read||rd)){readScreen();return}
  const n=items.filter(x=>M.marks[x.no]&&M.marks[x.no].split(',').length>=(qOf(x).multi||1)).length;
  let h='<div class="nav"><a href="omr.html">&larr; 세트 목록</a><span class="small">'+esc(DATA.label)+'</span></div><h1>OMR 답안 입력</h1>'+(RF[SID]?'<button class="link" onclick="rd=true;sheet()">지문 다시 읽기</button>':'')+'<p class="sub">시험지에서 푼 1~10번 답을 눌러 입력하세요. 나갔다 들어와도 입력한 답이 남아 있어요. 책의 문제가 바뀐 번호에는 새 문제가 나와요. 그 문제를 읽고 답하세요. 모두 입력하면 제출할 수 있어요.</p><p class="small">책의 선지 문구가 고쳐진 번호에는 "책이라면 확인하세요" 표시가 있어요. 눌러서 달라진 곳을 확인하세요. 정답 번호는 같으니 책에서 푼 답을 그대로 입력하면 돼요.</p><div class="card"><ul class="omr">';
  items.forEach(it=>{h+='<li><div class="r"><span class="n">'+it.no+'</span>'+CN.map(c=>'<button class="bub '+(has(it.no,c)?'on':'')+'" onclick="mark('+it.no+',\''+c+'\')">'+c+'</button>').join('')+'</div>';
    if(it.alt){h+='<div style="margin-top:8px;padding:10px 12px;border:2px solid var(--bad);border-radius:10px;background:var(--badbg)"><b style="color:var(--bad)">'+it.no+'번은 책의 문제가 바뀐 번호예요</b><div class="small" style="margin-top:4px">'+esc(it.notice)+'</div></div><button class="link" onclick="openAlt=!openAlt;sheet()">'+(openAlt?'문제 접기':it.no+'번 문제 열어보기')+'</button>';
      if(openAlt){const q=it.alt;h+='<div class="stem">'+esc(q.stem)+'</div>'+(q.sentence?'<div class="sent">'+esc(q.sentence)+'</div>':'')+q.choices.map((c,i)=>'<div class="ch" style="border-color:var(--ln)"><b>'+CN[i]+'</b>'+esc(c.en)+'</div>').join('')+'<div class="small">지문은 책의 같은 세트 지문과 같아요.</div>'}}
    h+=v1H(it,true)+'</li>'});
  h+='</ul></div><p class="small" style="text-align:center">'+n+' / '+items.length+' 입력</p><button class="btn" '+(n>=items.length?'':'disabled')+' onclick="submit()">제출하고 점수 보기</button>';
  $.innerHTML=h}
const has=(no,c)=>(M.marks[no]||'').split(',').indexOf(c)>=0;
const isAns=(q,l)=>String(q.answer).split(',').indexOf(l)>=0;
function mark(no,c){const it=items.find(x=>x.no==no),mx=qOf(it).multi||it.multi||1;
  if(mx>1){let a=(M.marks[no]||'').split(',').filter(Boolean);const i=a.indexOf(c);if(i>=0)a.splice(i,1);else{if(a.length>=mx)a.shift();a.push(c)}a.sort();M.marks[no]=a.join(',')}else M.marks[no]=c;osave();sheet()}
function submit(){if(!confirm('제출할까요? 제출하면 답을 바꿀 수 없어요.'))return;M.sub=true;osave();view='score';render()}
function ok(it){const q=qOf(it),m=M.marks[it.no];return (q.multi>1?String(m||'').split(',').sort().join(',')==String(q.answer).split(',').sort().join(','):m==q.answer)||(q.also&&q.also.indexOf(m)>=0&&!it.alt)}
function score(){
  const s=items.filter(ok).length,w=items.filter(it=>!ok(it));
  M.wrong=w.map(x=>x.no);M.score=s;M.total=items.length;M.label=DATA.label;try{localStorage.setItem(OK,JSON.stringify(O))}catch(e){}
  let h='<div class="nav"><a href="omr.html">&larr; 세트 목록</a><span class="small">'+esc(DATA.label)+'</span></div><h1>점수</h1><div class="card"><div style="font-size:34px;font-weight:700">'+s+' <span style="font-size:18px;color:var(--mu)">/ '+items.length+'</span></div><div class="small">'+(w.length?'틀린 문제 '+w.length+'개. 해설을 보고 오늘 오답노트를 써 보세요.':'전부 맞았어요.')+'</div></div>'
   +'<div class="card"><ul class="res">'+items.map((it,i)=>'<li onclick="openExp('+i+',null)"><span>'+it.no+'번 · '+esc(qOf(it).type)+'</span><span class="tg '+(ok(it)?'t-cum':'t-wr')+'">'+(ok(it)?'맞음':'틀림')+'</span></li>').join('')+'</ul></div>';
  if(w.length)h+='<button class="btn" onclick="openExp('+items.indexOf(w[0])+',\'wr\')">틀린 문제 해설 보기</button>';
  h+='<button class="btn sec" onclick="openExp(0,null)">전체 해설 보기</button><button class="btn sec" onclick="if(confirm(\'답과 제출 기록을 지우고 처음부터 다시 할까요?\')){O[SID]={marks:{},sub:false};osave();location.reload()}">처음부터 다시 하기</button>';
  $.innerHTML=h}
function openExp(i,l){cur=i;list=l=='wr'?items.filter(x=>!ok(x)).map(x=>items.indexOf(x)):null;view='exp';showP=false;showKo={};osave();render();window.scrollTo(0,0)}
function passH(q){let h='';DATA.passage.forEach(s=>{const k=q.quote?s.indexOf(q.quote):-1;if(k>=0)h+=esc(s.slice(0,k))+'<mark>'+esc(q.quote)+'</mark>'+esc(s.slice(k+q.quote.length))+' ';else h+=esc(s)+' '});return h}
function exp(){
  const it=items[cur],q=qOf(it),m=M.marks[it.no],good=ok(it);
  let h='<div class="nav"><button onclick="view=\'score\';render()">&lt; 점수</button><span class="small">'+esc(DATA.label)+'</span></div><div class="chips">'+items.map((x,i)=>'<button class="chip '+(i==cur?'on ':'')+(ok(x)?'ok':'no')+'" onclick="openExp('+i+','+(list?'\'wr\'':'null')+')">'+x.no+'</button>').join('')+'</div>';
  h+='<div class="card"><span class="tg t-new">'+it.no+'번 · '+esc(q.type)+'</span>'+(it.alt?'<span class="tg t-wr" style="margin-left:6px">새 문제 · 출처 '+esc(q.src)+'</span>':'')
   +(it.notice&&!it.alt?'<div class="note">'+esc(it.notice)+'</div>':'')+v1H(it,false)+'<p class="stem" style="margin-top:10px">'+esc(q.stem)+'</p>'+(q.sentence?'<div class="sent">'+esc(q.sentence)+'<div class="small" style="margin-top:4px">'+esc(q.sentence_ko)+'</div></div>':'')
   +'<div class="verd" style="color:'+(good?'var(--ok)':'var(--bad)')+'">'+(good?'맞았어요. 내 답 '+m.replace(/,/g,', '):'내 답 '+(m||'').replace(/,/g,', ')+' · 정답 '+String(q.answer).replace(/,/g,', '))+'</div>';
  q.choices.forEach((c,i)=>{const lab=CN[i];let cl='ch',tg='';
    if(isAns(q,lab)){cl+=' ans';tg='<span class="tg2" style="color:var(--ok)">정답</span>'}else if(q.also&&!it.alt&&q.also.indexOf(lab)>=0){cl+=' ans';tg='<span class="tg2" style="color:var(--ok)">인정 답안</span>'}
    if(has(it.no,lab)&&!isAns(q,lab)){cl+=' wr';tg='<span class="tg2" style="color:var(--bad)">내 선택</span>'}else if(has(it.no,lab)&&isAns(q,lab))tg='<span class="tg2" style="color:var(--ok)">내 선택 · 정답</span>';
    h+='<div class="'+cl+'">'+tg+'<b>'+lab+'</b>'+esc(c.en)+'<span class="ko">'+esc(c.ko)+'</span><span class="why">'+(isAns(q,lab)?'정답입니다.':(c.trap?'<span class="trap">'+esc(c.trap)+'</span>':'')+esc(c.why||''))+'</span>'+(!isAns(q,lab)&&c.int?'<span class="int">출제 의도: '+esc(c.int)+'</span>':'')+'</div>'});
  h+='</div><div class="card"><div class="secT" style="margin-top:0">쉽게 말해</div><div>'+esc(q.basis)+'</div><div class="secT">근거 문장</div><div class="ev"><div class="en">'+esc(q.quote)+'</div><div class="kk">'+esc(q.quote_ko)+'</div></div><button class="link" onclick="showP=!showP;exp()">'+(showP?'지문 접기':'지문에서 근거 위치 보기')+'</button>'+(showP?'<div class="psg">'+passH(q)+'</div>':'')+'</div>';
  const mm=q.memo||it.memo;
  if(mm&&mm.length)h+='<div class="memo"><h3>즉! 책 해설서 memo에 꼭 적어 두세요</h3><ul style="margin:0;padding-left:18px">'+mm.map(x=>'<li><span class="w">'+esc(x[0])+'</span> '+esc(x[1])+'</li>').join('')+'</ul><div class="small" style="margin-top:8px">오답노트는 이 순서로 써 보세요. 1) 정답과 근거 문장 2) 내가 고른 답이 틀린 이유 3) 위 memo 단어.</div></div>';
  const L=list||items.map((x,i)=>i),pos=L.indexOf(cur);
  h+='<div style="display:flex;gap:8px;margin-top:12px">'+(pos>0?'<button class="btn sec" style="margin-top:0;flex:1" onclick="openExp('+L[pos-1]+','+(list?'\'wr\'':'null')+')">이전</button>':'')+(pos<L.length-1?'<button class="btn" style="margin-top:0;flex:1" onclick="openExp('+L[pos+1]+','+(list?'\'wr\'':'null')+')">다음 문제</button>':'<button class="btn" style="margin-top:0;flex:1" onclick="view=\'score\';render();window.scrollTo(0,0)">점수로 돌아가기</button>')+'</div>';
  $.innerHTML=h+'</div>'}
function render(){if(view=='sheet')sheet();else if(view=='score')score();else exp()}
const mh=location.hash.match(/^#exp=(\d+)/),mi=mh&&M.sub?items.findIndex(x=>x.no==+mh[1]):-1;
if(mi>=0)openExp(mi,null);else render();
