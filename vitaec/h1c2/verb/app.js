document.head.insertAdjacentHTML('beforeend','<style>'+"\n:root{--bg:#f6f7fb;--c:#fff;--ink:#222;--sub:#667;--pri:#3b5bdb;--ok:#e8590c;--line:#e3e6ef;--fs:1}\n*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,\"Malgun Gothic\",sans-serif;line-height:1.6}\n.w{max-width:760px;margin:0 auto;padding:12px 12px 90px}\nh1{font-size:19px;margin:6px 0 2px}.sub{color:var(--sub);font-size:13px;margin-bottom:10px}\n.bar{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}\n.bar button,.chip{border:1px solid var(--line);background:var(--c);border-radius:20px;padding:7px 13px;font-size:14px;color:var(--ink)}\n.bar button.on{background:var(--pri);color:#fff;border-color:var(--pri)}\n.sel{width:100%;padding:10px;border-radius:10px;border:1px solid var(--line);font-size:15px;background:#fff;margin-bottom:6px}\n.top{display:flex;gap:6px;align-items:center}.top .sel{flex:1;margin:0}.fsb{flex:none;border:1px solid var(--line);background:#fff;border-radius:10px;padding:9px 11px;font-size:14px}\n.it{background:var(--c);border:1px solid var(--line);border-radius:12px;margin:8px 0;overflow:hidden}\n.hd{display:flex;gap:10px;padding:12px;align-items:flex-start;cursor:pointer}\n.no{flex:none;min-width:30px;height:30px;border-radius:15px;background:#edf0ff;color:var(--pri);font-weight:700;text-align:center;line-height:30px;font-size:14px;padding:0 6px}\n.seen .no{background:var(--pri);color:#fff}\n.tx{flex:1;font-size:calc(17px*var(--fs));line-height:1.75}.tx .ko{color:var(--sub);font-size:calc(14px*var(--fs));line-height:1.55;margin-top:4px}\n.bl{display:inline-block;border-bottom:2px solid #999;min-width:42px;text-align:center;color:#888;font-size:calc(14px*var(--fs));margin:0 2px}\n.st,.bk{flex:none;font-size:22px;background:none;border:0;color:#bbb;padding:0 3px}.st.on{color:#f59f00}.bk{opacity:.3;filter:grayscale(1)}.bk.on{opacity:1;filter:none}\n.btns{display:flex;flex-direction:column;align-items:center}\n.dt{display:none;border-top:1px dashed var(--line);padding:12px;background:#fbfcff;font-size:calc(15px*var(--fs))}\n.open .dt{display:block}\n.ans b{color:var(--ok)}.ans{font-size:calc(18px*var(--fs));margin-bottom:8px;line-height:1.7}\n.why{font-size:calc(14px*var(--fs));margin:6px 0;color:#444}.why li{margin:2px 0}.why b{color:var(--ok)}\n.sec{font-size:12px;color:var(--sub);margin:10px 0 3px;font-weight:700}\ntable{border-collapse:collapse;width:100%;font-size:calc(14px*var(--fs))}td{border:1px solid var(--line);padding:5px 7px;vertical-align:top}td:first-child{width:52%;background:#fff}td:last-child{background:#fffaf0;color:#444}\n.stat{background:var(--c);border:1px solid var(--line);border-radius:12px;padding:12px;margin:8px 0;font-size:14px}\n.stat h3{margin:0 0 6px;font-size:15px}\n.hint{font-size:13px;color:var(--sub)}\n.chips{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}.chips button{border:1px solid var(--line);background:#fff;border-radius:18px;padding:6px 12px;font-size:14px}.chips button.on{background:#364fc7;color:#fff;border-color:#364fc7}\n.ph{background:#edf0ff;border:1px solid #cdd5ff;border-radius:12px;padding:10px 12px;margin:10px 0}.ph b{font-size:16px}.ph .ps{color:var(--sub);font-size:13px}\n.ph details{margin-top:6px;font-size:14px}.ph summary{color:var(--pri);cursor:pointer}\n.bn{background:#fff5f5;border:2px solid #ffa8a8;border-radius:12px;padding:10px 12px;margin:8px 0;font-size:15px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}.bn b{color:#c92a2a}.bn button{border:0;border-radius:10px;padding:8px 12px;font-size:14px;background:#e03131;color:#fff}.bn button.g{background:#fff;color:#555;border:1px solid #ccc}\n.pn{display:flex;gap:8px;margin:14px 0}.pn button{flex:1;padding:12px;border-radius:12px;border:1px solid var(--line);background:#fff;font-size:15px}.pn button.p{background:var(--pri);color:#fff;border-color:var(--pri)}\n@keyframes fl{0%{background:#ffe066}100%{background:var(--c)}}.flash{animation:fl 2s}\nbody.exam{background:#2b2d42}body.exam h1,body.exam .sub{color:#fff}body.exam .sub{display:none}\n.exam .it{background:#fffbe6;border:2px solid #ffd43b}.exam .no{background:#ffd43b;color:#222}.exam .hd{cursor:default}.exam .tx .ko{color:#444}\n.mode{display:flex;gap:8px;margin:8px 0}.mode button{flex:1;padding:11px;border-radius:12px;border:2px solid var(--line);background:#fff;font-size:15px;font-weight:700}.mode button.on{background:var(--pri);color:#fff;border-color:var(--pri)}.exam .mode button{border-color:#555}.exam .mode button.on{background:#ffd43b;color:#222;border-color:#ffd43b}\n.exbar{background:#ffd43b;color:#222;border-radius:10px;padding:10px 12px;font-size:14px;font-weight:700;margin:8px 0}\n.exfoot{position:sticky;bottom:0;background:#2b2d42;padding:10px 0;display:flex;gap:8px;align-items:center;justify-content:space-between;color:#fff;font-size:14px}\n.b2{border:0;border-radius:10px;background:#ffd43b;color:#222;font-weight:700;padding:11px 16px;font-size:15px}\n.it.mk{background:#ffc078;border:3px solid #e8590c;color:#222}.wr{border:0;background:#ffe3e3;color:#e03131;border-radius:12px;padding:2px 8px;font-size:12px;font-weight:700;margin-top:4px}\nbutton.lnk{background:none;border:0;color:var(--pri);font-size:13px;text-decoration:underline;padding:4px}\n"+'</style>');
document.body.innerHTML='<div class="w"><h1></h1><div class="sub"></div><div class="mode" id="mode"></div><div class="top"><select id="ls" class="sel"></select></div><div id="bn"></div><div class="chips" id="chips"></div><div class="bar" id="bar"></div><div id="list"></div><div id="stat"></div></div>';
(function(){var d=VERBDATA[VID];document.querySelector('h1').textContent=d.grade+' '+d.pub+' 동사형 연습';
document.querySelector('.sub').textContent=d.school+' · '+d.term+' · 파트를 골라 번호를 눌러 연습하세요. 먼저 괄호를 머릿속으로(또는 소리 내어) 채운 뒤, 눌러서 정답을 확인! 책갈피를 꽂으면 나중에 이어서 할 수 있어요.';document.title=d.grade+' '+d.pub+' 동사형 연습'})();
var SCH=VERBDATA[VID],LS=SCH.lessons;
var KEY='verb_study_'+VID+'_v1',S;
function load(){try{S=JSON.parse(localStorage.getItem(KEY))}catch(e){}S=S||{};S.views=S.views||{};S.stars=S.stars||{};S.wrong=S.wrong||{};S.secs=S.secs||{};S.first=S.first||Date.now();S.fs=1}
function save(){try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}}
load();
var cur=0,pt=0,onlyStar=false,showStat=false,hideKo=false,exam=false,done=false,EX={},onlyWrong=false,rpi=0,showAll=false;
var FS=[0.9,1,1.15,1.3];
function applyFs(){document.documentElement.style.setProperty('--fs',FS[S.fs])}applyFs();
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function escb(s){return esc(s).replace(/\n/g,'<br>')}
function today(){var d=new Date();return d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate()}
var lastAct=Date.now();
['touchstart','click','scroll','keydown'].forEach(function(e){addEventListener(e,function(){lastAct=Date.now()},{passive:true})});
setInterval(function(){if(document.hidden)return;if(Date.now()-lastAct>60000)return;var t=today();S.secs[t]=(S.secs[t]||0)+5;if(exam){S.esecs=S.esecs||{};S.esecs[t]=(S.esecs[t]||0)+5}save()},5000);
function fmt(s){var m=Math.round(s/60);return m<60?m+'분':Math.floor(m/60)+'시간 '+(m%60)+'분'}
var sel=document.getElementById('ls');
LS.forEach(function(L,i){var o=document.createElement('option');o.value=i;o.textContent=SCH.grade+' '+SCH.pub+' · '+L.name+' ('+L.items.length+'문장)';sel.appendChild(o)});
sel.onchange=function(){cur=+sel.value;pt=0;EX={};done=false;render()};


function key(li,i){return LS[li].name+':'+(i+1)}
function blankHTML(it){return escb(it.en).replace(/___\[([^\]]*)\]/g,function(m,b){return '<span class="bl">'+esc(b)+'</span>'})}
function ansHTML(it){var k=0;return escb(it.en).replace(/___\[[^\]]*\]/g,function(){return '<b>'+esc(it.ans[k++])+'</b>'})}
function jjHTML(it){if(!it.jj||!it.jj.length)return '';var h='<div class="sec">직독직해 (끊어 읽기)</div><table>';it.jj.forEach(function(s){s.e.forEach(function(c,i){h+='<tr><td>'+esc(c)+'</td><td>'+esc(s.k[i]||'')+'</td></tr>'})});return h+'</table>'}
function whyH(it){return it.why?'<ul class="why">'+it.ans.map(function(a,j){return '<li><b>'+esc(a)+'</b> — '+esc(it.why[j]||'')+'</li>'}).join('')+'</ul>':''}
function partRange(li,p){var s=0,P=LS[li].parts;for(var i=0;i<P.length;i++){if(i==p)break;s+=P[i].n}return [s,s+P[p].n]}
function inPart(li,i){return pt<0||LS[li].items[i].part==pt}
function partHead(li,p){var P=LS[li].parts[p];return '<div class="ph"><b>'+esc(P.name)+(P.sub?' <span class="ps">· '+esc(P.sub)+'</span>':'')+'</b><div>'+esc(P.title)+'</div>'+(P.hook?'<details><summary>이 파트 무슨 얘기야?</summary><div style="margin-top:4px">'+esc(P.hook)+'</div></details>':'')+'</div>'}
function bmBanner(){var b=S.bm,el=document.getElementById('bn');el.innerHTML='';if(!b||exam)return;
  el.innerHTML='<div class="bn"><span><b>책갈피</b> '+esc(LS[b.li].name)+' '+(b.i+1)+'번 문장</span><button id="bgo">이어서 하기</button><button class="g" id="bdel">지우기</button></div>';
  document.getElementById('bgo').onclick=function(){var b2=S.bm;delete S.bm;save();cur=b2.li;sel.value=cur;pt=LS[cur].items[b2.i].part;onlyStar=false;onlyWrong=false;render();var e=document.querySelector('[data-i="'+b2.i+'"]');if(e){e.scrollIntoView({block:'center'});e.classList.add('flash')}};
  document.getElementById('bdel').onclick=function(){delete S.bm;save();render()}}
function render(){
  document.body.className=(exam&&!done)?'exam':'';
  var md=document.getElementById('mode');
  md.innerHTML='<button id="m1" class="'+(exam?'':'on')+'">연습모드</button><button id="m2" class="'+(exam?'on':'')+'">시험모드</button>';
  document.getElementById('m1').onclick=function(){exam=false;done=false;render()};
  document.getElementById('m2').onclick=function(){exam=true;done=false;EX={};showStat=false;render();scrollTo(0,0)};
  bmBanner();
  var ch=document.getElementById('chips');ch.innerHTML='';
  if(!(exam&&done)){var P=LS[cur].parts;var hasF=onlyStar||onlyWrong;
    var mk=function(lab,v){var b=document.createElement('button');b.textContent=lab;b.className=(pt===v&&!hasF)?'on':'';b.onclick=function(){pt=v;onlyStar=false;onlyWrong=false;EX={};render();scrollTo(0,0)};ch.appendChild(b)};
    P.forEach(function(p,i){mk(p.name,i)});mk('전체',-1)}
  if(exam){if(done)renderResult();else renderExam();return}
  var bar=document.getElementById('bar');
  bar.innerHTML='<button id="bs" class="'+(onlyStar?'on':'')+'">별표만 보기</button><button id="bw" class="'+(onlyWrong?'on':'')+'">틀린 문장만</button><button id="bk" class="'+(hideKo?'on':'')+'">한글 숨기기</button><button id="bt" class="'+(showStat?'on':'')+'">내 기록</button>';
  document.getElementById('bs').onclick=function(){onlyStar=!onlyStar;render()};
  document.getElementById('bw').onclick=function(){onlyWrong=!onlyWrong;render()};
  document.getElementById('bk').onclick=function(){hideKo=!hideKo;render()};
  document.getElementById('bt').onclick=function(){showStat=!showStat;render();if(showStat)scrollTo(0,document.body.scrollHeight)};
  var box=document.getElementById('list');box.innerHTML='';
  var filt=onlyStar||onlyWrong,li=+cur,n=0,lastP=-9;
  if(!filt&&pt>=0)box.insertAdjacentHTML('beforeend',partHead(li,pt));
  LS[li].items.forEach(function(it,i){
    var k=key(li,i);
    if(filt){if(onlyStar&&!S.stars[k])return;if(onlyWrong&&!S.wrong[k])return}else if(!inPart(li,i))return;
    n++;
    if(!filt&&pt<0&&it.part!==lastP){lastP=it.part;box.insertAdjacentHTML('beforeend',partHead(li,it.part))}
    var isbm=S.bm&&S.bm.li==li&&S.bm.i==i;
    var d=document.createElement('div');d.className='it'+(S.views[k]?' seen':'');d.setAttribute('data-i',i);
    d.innerHTML='<div class="hd"><div class="no">'+(i+1)+'</div><div class="tx">'+blankHTML(it)+(hideKo?'':'<div class="ko">'+escb(it.ko)+'</div>')+(S.wrong[k]?'<button class="wr">틀렸던 문장 (눌러서 해제)</button>':'')+'</div><div class="btns"><button class="st'+(S.stars[k]?' on':'')+'">'+(S.stars[k]?'★':'☆')+'</button><button class="bk'+(isbm?' on':'')+'" title="책갈피">'+'책갈피'+'</button></div></div>'
     +'<div class="dt"><div class="sec">정답</div><div class="ans">'+ansHTML(it)+'</div><div class="sec">해석</div><div>'+escb(it.ko)+'</div>'
     +(it.why?'<div class="sec">왜 이 형태?</div>'+whyH(it):'')+jjHTML(it)+'</div>';
    d.querySelector('.hd').onclick=function(e){
      var c=e.target.classList;if(c.contains('st')||c.contains('bk'))return;
      if(c.contains('wr')){delete S.wrong[k];save();if(onlyWrong)d.style.display='none';else e.target.remove();return}
      var o=d.classList.toggle('open');
      if(o){S.views[k]=(S.views[k]||0)+1;d.classList.add('seen');save()}};
    d.querySelector('.st').onclick=function(e){e.stopPropagation();if(S.stars[k])delete S.stars[k];else S.stars[k]=1;save();e.target.className='st'+(S.stars[k]?' on':'');e.target.textContent=S.stars[k]?'★':'☆';if(onlyStar&&!S.stars[k])d.style.display='none'};
    d.querySelector('.bk').onclick=function(e){e.stopPropagation();if(S.bm&&S.bm.li==li&&S.bm.i==i)delete S.bm;else S.bm={li:li,i:i};save();var sc=pageYOffset;render();scrollTo(0,sc)};
    box.appendChild(d)});
  [['wrong',onlyWrong,'이 단원 틀린 문장 모두 해제'],['stars',onlyStar,'이 단원 별표 모두 해제']].forEach(function(c){if(!n||!c[1])return;var cb=document.createElement('button');cb.textContent=c[2];cb.style.cssText='margin:8px 8px 8px 0;padding:8px 12px;border:1px solid #bbb;background:#fff;border-radius:10px;font-size:14px';cb.onclick=function(){if(!confirm('이 단원의 '+(c[0]=='wrong'?'틀린 문장 표시':'별표')+'를 모두 해제할까요?'))return;var pre=LS[cur].name+':';Object.keys(S[c[0]]).forEach(function(k){if(k.indexOf(pre)===0)delete S[c[0]][k]});save();render()};box.insertBefore(cb,box.firstChild)});
  if(!n)box.innerHTML='<div class="stat hint">'+(onlyWrong?'기록된 틀린 문장이 없어요. ':onlyStar?'아직 ★ 별표한 문장이 없어요. 어려운 문장 오른쪽 ☆를 눌러 보세요.':'문장이 없습니다.')+'</div>';
  if(!filt&&pt>=0){var P2=LS[cur].parts,pn=document.createElement('div');pn.className='pn';
    pn.innerHTML=(pt>0?'<button id="pp">◀ 이전 파트</button>':'')+(pt<P2.length-1?'<button class="p" id="pnx">다음 파트 ▶</button>':'');box.appendChild(pn);
    if(pt>0)document.getElementById('pp').onclick=function(){pt--;render();scrollTo(0,0)};
    if(pt<P2.length-1)document.getElementById('pnx').onclick=function(){pt++;render();scrollTo(0,0)}}
  var st=document.getElementById('stat');st.innerHTML='';
  if(showStat){
    var tot=0,td=S.secs[today()]||0;for(var d2 in S.secs)tot+=S.secs[d2];
    var vc=Object.keys(S.views),stars=Object.keys(S.stars);
    var top=vc.sort(function(a,b){return S.views[b]-S.views[a]}).slice(0,5).map(function(k){return k+'번('+S.views[k]+'회)'}).join(', ');
    st.innerHTML='<div class="stat"><h3>내 학습 기록 (이 폰에만 저장)</h3>오늘 사용: '+fmt(td)+' · 전체: '+fmt(tot)+'<br>시험모드 사용: '+fmt(Object.keys(S.esecs||{}).reduce(function(a,k){return a+S.esecs[k]},0))+'<br>살펴본 문장: '+vc.length+'개 · 별표: '+stars.length+'개 · 틀림: '+Object.keys(S.wrong||{}).length+'개'
     +'<br>자주 연 문장: '+(top||'-')+'<br>★ 문장: '+(stars.length?stars.join(', '):'-')
     +'<div class="hint" style="margin-top:6px">사용시간은 화면을 켜고 만지고 있는 시간만 셉니다. 카톡 앱 안에서 연 것과 크롬에서 연 것은 기록이 따로 저장돼요.</div>'
     +'<button class="lnk" id="rs">기록 지우기</button></div>';
    document.getElementById('rs').onclick=function(){if(confirm('기록을 모두 지울까요?')){var f=S.fs;S={};try{localStorage.removeItem(KEY)}catch(e){}load();S.fs=f;render()}};
  }
}
function examIdx(){var r=[];LS[cur].items.forEach(function(it,i){if(pt<0||it.part==pt)r.push(i)});return r}
function renderExam(){
  document.getElementById('bar').innerHTML='';document.getElementById('stat').innerHTML='';
  var box=document.getElementById('list');box.innerHTML='<div class="exbar">시험모드 — '+LS[cur].name+' '+(pt<0?'전체':LS[cur].parts[pt].name)+' · 틀린 문장은 문장을 눌러 표시하세요. 시험을 끝내면 "틀린 문장만"에 모여요.</div>';
  examIdx().forEach(function(i){var it=LS[cur].items[i];
    var d=document.createElement('div');d.className=EX[i]?'it mk':'it';
    d.innerHTML='<div class="hd"><div class="no">'+(i+1)+'</div><div class="tx">'+blankHTML(it)+'</div></div>';
    d.onclick=function(){if(EX[i])delete EX[i];else EX[i]=1;d.className=EX[i]?'it mk':'it';cnt()};
    box.appendChild(d)});
  var f=document.createElement('div');f.className='exfoot';f.innerHTML='<span id="xc"></span><button class="b2" id="xe">시험 종료</button>';box.appendChild(f);
  function cnt(){document.getElementById('xc').textContent='표시한 문장 '+Object.keys(EX).length+'개'}cnt();
  document.getElementById('xe').onclick=function(){if(!confirm('시험을 끝낼까요? 표시한 문장은 "틀린 문장만"에 저장돼요.'))return;
    Object.keys(EX).forEach(function(i){S.wrong[key(+cur,+i)]=1});save();var n=Object.keys(EX).length;EX={};exam=false;done=false;onlyWrong=false;onlyStar=false;render();scrollTo(0,0);document.getElementById('list').insertAdjacentHTML('afterbegin','<div class="stat hint">'+(n?'시험 종료! 표시한 '+n+'문장은 위쪽 "틀린 문장만"에 모였어요.':'시험 종료! 모두 맞았어요 ')+'</div>')};
}
function renderResult(){exam=false;done=false;render()}
render();
