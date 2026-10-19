# -*- coding: utf-8 -*-
import json,re
from data import SECTIONS, CAT
def _ph(sents,i):
    out=[]
    for r,n_,m in sents:
        for mm in re.finditer(r'\[(\d+)\|([^\]]*)\]',m):
            if int(mm.group(1))==i: out.append(mm.group(2).strip())
    seen=[]
    for o in out:
        if o not in seen: seen.append(o)
    return ' … '.join(seen)
n=1; secs=[]
for s in SECTIONS:
    sents=[]
    for rows,nat,mk in s['sents']:
        sents.append(dict(n=n,rows=[r.split('|') for r in rows],nat=nat,mk=mk)); n+=1
    secs.append(dict(no=s['no'],sym=s['sym'],en=s['en'],ko=s['ko'],sents=sents,items=[dict(t=i[0],x=i[1],c=i[2],p=_ph(s['sents'],k+1)) for k,i in enumerate(s['items'])]))
DATA=json.dumps(dict(secs=secs,cat={k:dict(d=v[0],l=v[1],n=v[3],s=v[2]) for k,v in CAT.items()}),ensure_ascii=False)
HTML=r'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>중2 동아(윤) 7과</title>
<style>
:root{--teal:#0f766e;--bd:#d3e0dd;--mut:#53626a}
*{box-sizing:border-box}
body{margin:0;background:#f3f7f6;color:#17202e;font-family:"Noto Sans KR",-apple-system,"Malgun Gothic",sans-serif}
#app{max-width:440px;margin:0 auto;min-height:100vh;padding:16px 16px 84px}
.chips{display:flex;gap:6px;background:#e4ecea;border-radius:12px;padding:4px;margin-bottom:10px}
.chips button{flex:1;border:0;background:none;padding:9px 2px;font:700 13.5px inherit;font-family:inherit;color:var(--mut);border-radius:9px}
.chips button.on{background:#fff;color:var(--teal);font-weight:800;box-shadow:0 1px 2px rgba(15,60,50,.15)}
.psel{display:flex;gap:6px;margin-bottom:10px}
.psel button{flex:1;padding:7px 0;border-radius:10px;font:700 14px inherit;font-family:inherit;background:#fff;color:#44545b;border:1.5px solid #c3cfcc}
.psel button.on{background:var(--teal);color:#fff;border-color:var(--teal);font-weight:800}
h2{font-size:20px;margin:6px 2px 4px}.sub{font-size:13px;color:var(--mut)}
.row{display:flex;justify-content:space-between;align-items:center;margin:6px 0 10px;gap:8px}
.btn{padding:8px 16px;border:1.5px solid #c3cfcc;background:#fff;border-radius:10px;font:700 13.5px inherit;font-family:inherit;color:#44545b}
.card{background:#fff;border:1px solid var(--bd);border-radius:14px;padding:12px 14px 13px;margin-bottom:10px}
.no{font-size:12px;font-weight:800;color:var(--teal);margin-bottom:6px}
.pair{margin:6px 0;padding:3px 2px;border-radius:8px;cursor:pointer;-webkit-tap-highlight-color:transparent}
.pair .en{font-size:16px;font-weight:700;line-height:1.5;color:#1e2a44}
.pair .ko{font-size:15.5px;line-height:1.5;margin-top:3px;border-left:4px solid var(--teal);background:#e3f3f0;border-radius:0 8px 8px 0;padding:2px 0 2px 10px}
.hide .pair .ko,.hide .nat{visibility:hidden;background:#fff}
.hide .pair .ko.show,.hide .nat.show{visibility:visible;background:#e3f3f0}
.hide .pair:active{background:#e3f3f0}
.nat{font-size:14px;line-height:1.6;border-top:1px dashed #c3cfcc;padding-top:8px;margin-top:8px}
.hide .nat{cursor:pointer}
.tog{position:sticky;top:0;z-index:5;background:#f3f7f6;padding:8px 0;display:flex;gap:8px;margin-bottom:4px}
.tog button{border:1px solid var(--bd);background:#fff;color:#17202e;border-radius:999px;padding:7px 14px;font:14px inherit;font-family:inherit}
.tog button.on{background:var(--teal);color:#fff;border-color:var(--teal)}
.ps{font-size:15px;line-height:2;display:flex;gap:8px;border-top:1px solid #edf2f1;padding-top:4px;margin-top:4px}
.ps i{font-style:normal;font-size:12px;font-weight:800;color:var(--teal);flex:none;width:18px}
.pl{display:inline-flex;align-items:center;height:17px;padding:0 6px;border-radius:99px;color:#fff;font-size:10.5px;font-weight:800;margin:0 2px;vertical-align:1px;white-space:nowrap}
.b{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;border-radius:99px;color:#fff;font-size:10px;font-weight:800;margin:0 2px;vertical-align:1px}
.b.l{width:22px;height:22px;font-size:12px;margin:0}
.it{border-radius:14px;padding:12px 14px 13px;margin-bottom:10px}
.it h4{margin:0 0 6px;font-size:15px;display:flex;align-items:center;gap:8px}
.rv{margin-top:6px;cursor:pointer}.rv .q{border-left:4px solid;padding:4px 8px;font-size:14px}.rv .a{display:none;margin-top:4px;border:1.5px solid;border-radius:10px;padding:8px 10px;font-size:13.5px;line-height:1.6}.rv.open .a{display:block}
.bl{display:inline-block;min-width:54px;border-bottom:2.5px solid;margin:0 2px;vertical-align:bottom;cursor:pointer;line-height:1.5}
.bl .tx{visibility:hidden;padding:0 2px;border-radius:3px}.bl.open .tx{visibility:visible}.it p{margin:0;font-size:13.5px;line-height:1.65}
.tabbar{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid var(--bd);display:flex;height:64px;max-width:440px;margin:0 auto}
.tabbar button{flex:1;border:0;background:none;display:flex;flex-direction:column;align-items:center;gap:3px;padding-top:6px;font:700 12.5px inherit;font-family:inherit;color:var(--mut)}
.tabbar button.on{color:var(--teal);font-weight:800;box-shadow:inset 0 3px 0 -0px var(--teal)}
.cal{background:#fff;border:1px solid var(--bd);border-radius:14px;padding:10px 8px 8px}
.cal .hd,.cal .gr{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));text-align:center}
.cal .hd{font-size:12px;font-weight:700;color:#7a8a86;padding-bottom:2px}
.cal .gr button{height:38px;border:0;background:none;font:700 14px inherit;font-family:inherit;color:#17202e;margin:1.5px 0}
.cal .gr button.sun{color:#b4534a}.cal .gr button.l7{background:#cfe8e4}
.cal .gr button.today{outline:2px solid var(--teal);outline-offset:-3px;border-radius:99px}
.cal .gr button.sel{background:var(--teal);color:#fff;border-radius:99px}
.mon{display:flex;justify-content:space-between;align-items:baseline;padding:0 2px 8px}.mon button{border:0;background:none;font-size:20px;color:var(--mut);padding:0 8px}
a.cta{display:block;text-decoration:none;border-radius:12px;padding:13px 14px;margin-top:8px}
a.cta b{display:block;font-size:17px}a.cta span{font-size:12px}
.k{background:var(--teal);color:#fff}.k span{color:#d7efeb}.s{background:#fff;border:1.5px solid var(--teal);color:var(--teal)}.s span{color:#44545b}
</style></head><body><div id="app"></div>
<div class="tabbar" id="tabbar"></div>
<script>
var D=__DATA__;
/* ===== 학습 일정 (날짜를 바꾸려면 여기만 고치세요) : 'YYYY-MM-DD': [Day번호] ===== */
var SCHEDULE={'2026-10-19':[1,2],'2026-10-20':[3,4]};
var DAYS={1:'1~7번',2:'8~13번',3:'14~19번',4:'20~26번'};
var SYM={1:'❶',2:'❷',3:'❸',4:'❹'};
function dayRow(d){return '<div style="margin-top:8px"><div class="sub" style="font-weight:800">본문 '+SYM[d]+' · '+DAYS[d]+' 문장</div><div style="display:flex;gap:8px"><a class="cta k" style="flex:1" href="../basic/?day='+d+'"><b>기본</b><span>우리말 순서부터 차근차근</span></a><a class="cta s" style="flex:1" href="../adv/?day='+d+'"><b>심화</b><span>덩어리 안쪽까지 파고들기</span></a></div></div>'}
var S={tab:'text',corner:'tr',sec:'1',hide:false,sel:null,ym:null,drill:null};
function el(h){return h}
function esc(t){return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function cur(){return D.secs.filter(function(s){return s.no==S.sec})[0]}
function cc(sec,i){return D.cat[sec.items[i-1].c]}
function plainMark(t,sec,only){
  var out='',pos=0,re=/\[(\d+)\|([^\]]*)\]/g,m;
  while((m=re.exec(t))){out+=esc(t.slice(pos,m.index));var c=cc(sec,m[1]),k=sec.items[m[1]-1].c;
    if(only){ if(k==only){out+='<span style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 2px">'+esc(m[2])+'</span>'}else{out+=esc(m[2])} }
    else out+='<span style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 2px">'+esc(m[2])+'</span>';
    pos=re.lastIndex}
  return out+esc(t.slice(pos))}
function legend(){return '<div class="card" style="display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;font-size:12.5px;padding:10px 14px">'+['g','b','k','o'].map(function(k){var c=D.cat[k];return '<div style="display:flex;align-items:center;gap:6px"><span style="width:14px;height:14px;border-radius:4px;flex:none;background:'+c.l+';border:1.5px solid '+c.d+'"></span>'+esc(c.n)+'</div>'}).join('')+'</div>'}
function drillBar(cur){return '<div style="display:flex;gap:6px;margin:0 0 10px">'+['g','b','k','o'].map(function(k){var c=D.cat[k];return '<button data-dr="'+k+'" style="flex:1;padding:8px 0;border-radius:10px;border:1.5px solid '+c.d+';background:'+(cur==k?c.d:c.l)+';color:'+(cur==k?'#fff':'#17202e')+';font:800 13px inherit;font-family:inherit">'+c.s+'</button>'}).join('')+'</div>'}
function vDrill(){
  var k=S.drill,c=D.cat[k],h='<h2>'+c.s+' 모아보기</h2><div class="sub" style="margin-bottom:8px">본문은 그대로 보고, 표시된 말이 무엇이었는지 떠올린 뒤 눌러서 확인해요.</div>'+drillBar(k)+'<div class="row" style="justify-content:flex-end"><button class="btn" id="dclose">설명 다시 가리기</button></div><div id="list">';
  D.secs.forEach(function(s){
    var cards=s.sents.filter(function(x){var re=/\[(\d+)\|/g,m,f=false;while((m=re.exec(x.mk)))if(s.items[m[1]-1].c==k)f=true;return f});
    if(!cards.length)return;
    h+='<div class="sub" style="font-weight:800;margin:10px 2px 6px">본문 '+s.sym+'</div>';
    cards.forEach(function(x){
      var seen={},rows='',re=/\[(\d+)\|/g,m;
      while((m=re.exec(x.mk))){var ix=+m[1];if(s.items[ix-1].c==k&&!seen[ix]){seen[ix]=1;var it=s.items[ix-1];
        rows+='<div class="rv"><div class="q" style="border-color:'+c.d+'"><span style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 3px;font-weight:700">'+esc(it.p)+'</span><span class="sub"> · 눌러서 확인</span></div><div class="a" style="background:'+c.l+'88;border-color:'+c.d+'"><div style="font-weight:800;color:'+c.d+';margin-bottom:3px">'+esc(it.t)+'</div>'+esc(it.x)+'</div></div>'}}
      h+='<div class="card"><div class="no">'+x.n+'</div><div class="ps" style="border:0;padding:0"><span>'+plainMark(x.mk,s,k)+'</span></div><div class="sub" style="margin:4px 0 6px">'+esc(x.nat)+'</div>'+rows+'</div>'});
  });
  return h+'</div>'}
function chips(){var n=[['tr','문장 해석'],['gr','문법 설명'],['an','문장 분석']];
  return '<div class="chips">'+n.map(function(x){return '<button data-c="'+x[0]+'" class="'+(S.corner==x[0]?'on':'')+'">'+x[1]+'</button>'}).join('')+'</div>'}
function psel(){return '<div class="psel">'+D.secs.map(function(s){return '<button data-s="'+s.no+'" class="'+(S.sec==s.no?'on':'')+'">본문 '+s.sym+'</button>'}).join('')+'</div>'}
function vText(){
  var s=cur(),h=chips();
  if(S.corner=='gr'&&S.drill)return h+vDrill();
  if(S.corner=='an'){
    return h+'<h2>7과 핵심 문장 분석</h2><div class="sub" style="margin-bottom:10px">본문 2개씩, 2회차로 나눠서 한 문장씩 뜯어 봐요.</div>'+
    [[1,2],[3,4]].map(function(g,k){return '<div class="card"><b style="font-size:16px">'+(k+1)+'회차</b>'+dayRow(g[0])+dayRow(g[1])+'</div>'}).join('')}
  h+=psel();
  var a=s.sents[0].n,b=s.sents[s.sents.length-1].n;
  if(S.corner=='tr'){
    h+='<div class="row"><div><h2 style="margin:0">7과 · 본문 '+s.sym+' 문장 해석</h2><div class="sub">'+esc(s.ko)+' · '+a+'~'+b+'번</div></div></div>';
    h+='<div class="tog"><button id="b1" class="'+(S.hide?'':'on')+'">해석 보이기</button><button id="b2" class="'+(S.hide?'on':'')+'">해석 가리기</button></div><div class="sub" style="margin:0 2px 6px">해석을 가렸을 때는 한 줄씩 눌러서 열어 보세요.</div>';
    h+='<div id="list" class="'+(S.hide?'hide':'')+'">'+s.sents.map(function(x){return '<div class="card"><div class="no">'+x.n+'</div>'+x.rows.map(function(r){return '<div class="pair"><div class="en">'+esc(r[0])+'</div><div class="ko">'+esc(r[1])+'</div></div>'}).join('')+'<div class="nat">'+esc(x.nat)+'</div></div>'}).join('')+'</div>';
  }else{
    h+='<h2>7과 · 본문 '+s.sym+' 문법 설명</h2><div class="sub" style="margin-bottom:8px">'+a+'~'+b+'번</div>'+'';
    h+='<div class="sub" style="font-weight:800;margin:2px 2px 6px">형광펜 이름별로 모아보기 (복습)</div>'+drillBar('');
    h+='<div class="card"><div class="sub" style="font-weight:800;margin-bottom:4px">본문에서 찾아요 · 색칠한 부분과 같은 말이 아래 설명 카드에 있어요</div>'+s.sents.map(function(x){return '<div class="ps"><i>'+x.n+'</i><span>'+plainMark(x.mk,s)+'</span></div>'}).join('')+'</div>';
    h+=s.items.map(function(it,i){var c=D.cat[it.c];return '<div class="it" style="background:'+c.l+'88;border:1.5px solid '+c.d+'"><h4><span style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 4px;flex:1">'+esc(it.p)+'</span><span style="font-size:11.5px;color:#fff;background:'+c.d+';border-radius:99px;padding:2px 9px;flex:none">'+esc(c.s)+'</span></h4><div style="font-size:14px;font-weight:800;color:'+c.d+';margin-bottom:5px">'+esc(it.t)+'</div><p>'+esc(it.x)+'</p></div>'}).join('');
  }
  return h}
function ymd(d){return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function vToday(){
  var now=new Date(),t=ymd(now);
  if(!S.ym)S.ym=[now.getFullYear(),now.getMonth()];
  if(!S.sel)S.sel=t;
  var y=S.ym[0],m=S.ym[1],first=new Date(y,m,1),lead=(first.getDay()+6)%7,days=new Date(y,m+1,0).getDate();
  var g='';for(var i=0;i<lead;i++)g+='<button disabled></button>';
  for(var d=1;d<=days;d++){var key=y+'-'+('0'+(m+1)).slice(-2)+'-'+('0'+d).slice(-2),col=(lead+d-1)%7,c=[];
    if(col==6)c.push('sun');if(SCHEDULE[key])c.push('l7');if(key==t)c.push('today');if(key==S.sel)c.push('sel');
    g+='<button data-d="'+key+'" class="'+c.join(' ')+'">'+d+'</button>'}
  var h='<div class="mon"><h2 style="margin:0">오늘의 학습</h2><div><button id="pm">‹</button><b>'+y+'년 '+(m+1)+'월</b><button id="nm">›</button></div></div>';
  h+='<div class="cal"><div class="hd"><div>월</div><div>화</div><div>수</div><div>목</div><div>금</div><div>토</div><div>일</div></div><div class="gr">'+g+'</div></div>';
  var sd=S.sel.split('-'),dt=new Date(+sd[0],+sd[1]-1,+sd[2]),wk='일월화수목금토'[dt.getDay()];
  h+='<div class="row" style="margin-top:14px"><b style="font-size:16px">'+(+sd[1])+'월 '+(+sd[2])+'일 '+wk+'요일</b>'+(SCHEDULE[S.sel]?'<span class="sub">7과 · 축제</span>':'')+'</div>';
  var dn=SCHEDULE[S.sel];
  if(dn){h+='<div class="card" style="border:1.5px solid #8fb3ac;padding:14px"><b style="font-size:18px">문장 분석</b><div class="sub">7과 · 본문 '+SYM[dn[0]]+' '+SYM[dn[1]]+'</div>'+dayRow(dn[0])+dayRow(dn[1])+'</div>'}
  else h+='<div class="card sub">이 날은 정해진 학습이 없어요.</div>';
  return h}
function vKey(){return '<h2>답안지</h2><div class="card sub" style="margin-top:10px">7과·8과 답안지는 곧 열려요.</div>'}
var ICON={text:'<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5"/><path d="M9 13h7M9 17h7"/>',key:'<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 12l3 3 5-6"/>',today:'<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>'};
function render(){
  var v=S.tab=='text'?vText():S.tab=='key'?vKey():vToday();
  document.getElementById('app').innerHTML=v;
  document.getElementById('tabbar').innerHTML=[['text','원문'],['key','답안지'],['today','오늘의 학습']].map(function(x){return '<button data-t="'+x[0]+'" class="'+(S.tab==x[0]?'on':'')+'"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+ICON[x[0]]+'</svg><span>'+x[1]+'</span></button>'}).join('');
  window.scrollTo(0,0)}
document.addEventListener('click',function(e){
  var L=document.getElementById('list');
  if(L){
    var bb=e.target.closest('#b1,#b2');
    if(bb){S.hide=bb.id=='b2';L.classList.toggle('hide',S.hide);document.getElementById('b1').className=S.hide?'':'on';document.getElementById('b2').className=S.hide?'on':'';
      var o=L.querySelectorAll('.show');for(var i=0;i<o.length;i++)o[i].classList.remove('show');return}
    var rv=e.target.closest('.rv');if(rv){rv.classList.toggle('open');return}
    if(S.hide){var p=e.target.closest('.pair');if(p){p.querySelector('.ko').classList.toggle('show');return}
      var n=e.target.closest('.nat');if(n){n.classList.toggle('show');return}}
  }
  var t=e.target.closest('button');if(!t)return;
  if(t.dataset.t){S.tab=t.dataset.t}
  else if(t.dataset.c){S.corner=t.dataset.c;S.drill=null}
  else if(t.dataset.dr){S.drill=S.drill==t.dataset.dr?null:t.dataset.dr}
  else if(t.id=='dclose'){var o2=document.querySelectorAll('.rv.open');for(var q=0;q<o2.length;q++)o2[q].classList.remove('open');return}
  else if(t.dataset.s){S.sec=t.dataset.s}
  else if(t.dataset.d){S.sel=t.dataset.d}
  else if(t.id=='pm'||t.id=='nm'){var d=new Date(S.ym[0],S.ym[1]+(t.id=='pm'?-1:1),1);S.ym=[d.getFullYear(),d.getMonth()]}
  else return;
  render()});
try{var p=new URLSearchParams(location.search).get('tab');if(p)S.tab=p}catch(e){}
render();
</script></body></html>'''
HTML=HTML.replace('__DATA__',DATA)
open('../../../dongah-yun/l7/app/index.html','w').write(HTML)
print(len(HTML))
