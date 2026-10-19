# -*- coding: utf-8 -*-
import json,re
from data import SECTIONS, CAT
from qa import QA
from notes import NOTES
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
for si,s in enumerate(SECTIONS):
    sents=[]
    for rows,nat,mk in s['sents']:
        sents.append(dict(n=n,rows=[r.split('|') for r in rows],nat=nat,mk=mk)); n+=1
    secs.append(dict(no=s['no'],sym=s['sym'],en=s['en'],ko=s['ko'],sents=sents,items=[dict(t=i[0],x=NOTES[si][k][0],n=NOTES[si][k][1],c=i[2],p=_ph(s['sents'],k+1),q=QA[si][k][0],a=QA[si][k][1]) for k,i in enumerate(s['items'])]))
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
.bk{margin-top:8px;border:1.5px solid;background:#fff;border-radius:999px;padding:6px 14px;font:700 13px inherit;font-family:inherit}
.flash{animation:fl 1.4s ease}@keyframes fl{0%,60%{box-shadow:0 0 0 4px #f5c84288}100%{box-shadow:none}}
.note{background:#fffbe6;border:1.5px dashed #d9c76a;border-radius:10px;padding:7px 11px;background-image:repeating-linear-gradient(transparent,transparent 25px,#efe6b3 25px,#efe6b3 26px)}.note .nl{font-size:11.5px;font-weight:800;color:#8a6d00;margin-bottom:2px}.note .ln{font-size:14px;font-weight:700;line-height:26px;color:#17202e}
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
.cta.k{background:#dcefec;border:1.5px solid #a8d3cd;color:#0f6a62}.cta.k span{color:#4f6b67}.cta.k.dn{background:#0f766e;border-color:#0f766e;color:#fff}.cta.k.dn span{color:#d7efeb}
.cta.s{background:#e6eaf9;border:1.5px solid #b7c0ec;color:#3b4bb0}.cta.s span{color:#5b6393}.cta.s.dn{background:#4338ca;border-color:#4338ca;color:#fff}.cta.s.dn span{color:#dcd9fb}
a.cta b{display:flex;align-items:center;gap:6px}
</style></head><body><div id="app"></div>
<div class="tabbar" id="tabbar"></div>
<script>
var D=__DATA__;
/* ===== 학습 일정 (날짜를 바꾸려면 여기만 고치세요) : 'YYYY-MM-DD': [Day번호] ===== */
/* 오늘 할 본문은 링크 끝에 ?today=1,2 처럼 붙여서 정해요 (본문 번호). 붙이지 않으면 4개 모두 보여요. */
var DAYS={1:'1~7번',2:'8~13번',3:'14~19번',4:'20~26번'};
var SYM={1:'❶',2:'❷',3:'❸',4:'❹'};
function isDone(kind,d){try{var s=JSON.parse(localStorage.getItem('vsig-mid-dy-l7-'+kind+'-v1')||'{}');return !!(s.best&&s.best[d])}catch(e){return false}}
var CK='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg>';
function btn(kind,d,name,sub){var dn=isDone(kind,d);return '<a class="cta '+(kind=='basic'?'k':'s')+(dn?' dn':'')+'" style="flex:1" href="../'+kind+'/?day='+d+'"><b>'+(dn?CK:'')+name+'</b><span>'+(dn?'분석 완료':sub)+'</span></a>'}
function dayRow(d){return '<div style="margin-top:8px"><div class="sub" style="font-weight:800">본문 '+SYM[d]+' · '+DAYS[d]+' 문장</div><div style="display:flex;gap:8px">'+btn('basic',d,'기본','우리말 순서부터 차근차근')+btn('adv',d,'심화','덩어리 안쪽까지 파고들기')+'</div></div>'}
var S={tab:'text',corner:'tr',sec:'1',hide:false,sel:null,ym:null,drill:null};
function el(h){return h}
function esc(t){return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function cur(){return D.secs.filter(function(s){return s.no==S.sec})[0]}
function cc(sec,i){return D.cat[sec.items[i-1].c]}
function plainMark(t,sec,only,sn){
  var out='',pos=0,re=/\[(\d+)\|([^\]]*)\]/g,m;
  while((m=re.exec(t))){out+=esc(t.slice(pos,m.index));var c=cc(sec,m[1]),k=sec.items[m[1]-1].c;
    if(only){ if(k==only){out+='<span style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 2px">'+esc(m[2])+'</span>'}else{out+=esc(m[2])} }
    else out+='<span class="hlk" data-i="'+m[1]+'" data-n="'+sn+'" style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 2px;cursor:pointer">'+esc(m[2])+'</span>';
    pos=re.lastIndex}
  return out+esc(t.slice(pos))}
function noteBox(n){return '<div class="note"><div class="nl">노트에 이렇게 적어요</div>'+n.map(function(l){return '<div class="ln">'+esc(l)+'</div>'}).join('')+'</div>'}
function legend(){return '<div class="card" style="display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;font-size:12.5px;padding:10px 14px">'+['g','b','k','o'].map(function(k){var c=D.cat[k];return '<div style="display:flex;align-items:center;gap:6px"><span style="width:14px;height:14px;border-radius:4px;flex:none;background:'+c.l+';border:1.5px solid '+c.d+'"></span>'+esc(c.n)+'</div>'}).join('')+'</div>'}
function drillBar(cur){return '<div style="display:flex;gap:6px;margin:0 0 10px">'+['g','b','k','o'].map(function(k){var c=D.cat[k];return '<button data-dr="'+k+'" style="flex:1;padding:8px 0;border-radius:10px;border:1.5px solid '+c.d+';background:'+(cur==k?c.d:c.l)+';color:'+(cur==k?'#fff':'#17202e')+';font:800 13px inherit;font-family:inherit">'+c.s+'</button>'}).join('')+'</div>'}
function vDrill(){
  var k=S.drill,c=D.cat[k],h='<button class="btn" data-dr="'+k+'" style="margin-bottom:8px">← 전체 문법 설명으로</button><h2>'+c.s+' 모아보기</h2><div class="sub" style="margin-bottom:8px">본문은 그대로 보고, 표시된 말이 무엇이었는지 떠올린 뒤 눌러서 확인해요.</div>'+drillBar(k)+'<div class="row" style="justify-content:flex-end"><button class="btn" id="dclose">설명 다시 가리기</button></div><div id="list">';
  D.secs.forEach(function(s){
    var cards=s.sents.filter(function(x){var re=/\[(\d+)\|/g,m,f=false;while((m=re.exec(x.mk)))if(s.items[m[1]-1].c==k)f=true;return f});
    if(!cards.length)return;
    h+='<div class="sub" style="font-weight:800;margin:10px 2px 6px">본문 '+s.sym+'</div>';
    cards.forEach(function(x){
      var seen={},rows='',re=/\[(\d+)\|/g,m;
      while((m=re.exec(x.mk))){var ix=+m[1];if(s.items[ix-1].c==k&&!seen[ix]){seen[ix]=1;var it=s.items[ix-1];
        rows+='<div class="rv"><div class="q" style="border-color:'+c.d+'"><span style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 3px;font-weight:700">'+esc(it.p)+'</span><div style="margin-top:3px">'+esc(it.q)+'</div><div class="sub" style="margin-top:2px">눌러서 확인</div></div><div class="a" style="background:'+c.l+'88;border-color:'+c.d+'"><div style="font-weight:800;color:'+c.d+';margin-bottom:3px">'+esc(it.a)+'</div>'+noteBox(it.n)+'<div style="font-size:13px;color:#44545b;margin-top:6px">'+esc(it.x)+'</div></div></div>'}}
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
    return h+'<h2>7과 핵심 문장 분석</h2><div class="sub" style="margin-bottom:10px">본문 ❶~❹를 한 문장씩 뜯어 봐요.</div>'+
    '<div class="card">'+[1,2,3,4].map(dayRow).join('')+'</div>'}
  h+=psel();
  var a=s.sents[0].n,b=s.sents[s.sents.length-1].n;
  if(S.corner=='tr'){
    h+='<div class="row"><div><h2 style="margin:0">7과 · 본문 '+s.sym+' 문장 해석</h2><div class="sub">'+esc(s.ko)+' · '+a+'~'+b+'번</div></div></div>';
    h+='<div class="tog"><button id="b1" class="'+(S.hide?'':'on')+'">해석 보이기</button><button id="b2" class="'+(S.hide?'on':'')+'">해석 가리기</button></div><div class="sub" style="margin:0 2px 6px">해석을 가렸을 때는 한 줄씩 눌러서 열어 보세요.</div>';
    h+='<div id="list" class="'+(S.hide?'hide':'')+'">'+s.sents.map(function(x){return '<div class="card"><div class="no">'+x.n+'</div>'+x.rows.map(function(r){return '<div class="pair"><div class="en">'+esc(r[0])+'</div><div class="ko">'+esc(r[1])+'</div></div>'}).join('')+'<div class="nat">'+esc(x.nat)+'</div></div>'}).join('')+'</div>';
  }else{
    h+='<h2>7과 · 본문 '+s.sym+' 문법 설명</h2><div class="sub" style="margin-bottom:8px">'+a+'~'+b+'번</div>'+'';
    h+='<div class="sub" style="font-weight:800;margin:2px 2px 6px">형광펜 이름별로 모아보기 (복습)</div>'+drillBar('');
    h+='<div class="card"><div class="sub" style="font-weight:800;margin-bottom:4px">본문에서 찾아요 · 색칠한 부분과 같은 말이 아래 설명 카드에 있어요</div>'+s.sents.map(function(x){return '<div class="ps" id="ps-'+x.n+'"><i>'+x.n+'</i><span>'+plainMark(x.mk,s,null,x.n)+'</span></div>'}).join('')+'</div>';
    h+=s.items.map(function(it,i){var c=D.cat[it.c];return '<div class="it" id="it-'+(i+1)+'" style="background:'+c.l+'88;border:1.5px solid '+c.d+'"><h4><span style="background:'+c.l+';border-bottom:2px solid '+c.d+';border-radius:3px;padding:0 4px;flex:1">'+esc(it.p)+'</span><span style="font-size:11.5px;color:#fff;background:'+c.d+';border-radius:99px;padding:2px 9px;flex:none">'+esc(c.s)+'</span></h4><div style="font-size:15px;font-weight:800;color:'+c.d+';margin-bottom:6px">'+esc(it.a)+'</div>'+noteBox(it.n)+'<p style="margin-top:7px;font-size:13px;color:#44545b">'+esc(it.x)+'</p><button class="bk" data-back="'+(i+1)+'" style="border-color:'+c.d+';color:'+c.d+'">↑ 본문으로 돌아가기</button></div>'}).join('');
  }
  return h}
function todayList(){
  var p='';try{p=new URLSearchParams(location.search).get('today')||''}catch(e){}
  var l=p.split(',').map(function(x){return +x}).filter(function(x){return x>=1&&x<=4});
  return l.length?l:null}
function vToday(){
  var t=todayList(),all=[1,2,3,4],h='<h2>오늘의 학습</h2>';
  if(t){h+='<div class="sub" style="margin:2px 2px 10px">선생님이 정해 준 오늘 학습이에요.</div><div class="card" style="border:1.5px solid #8fb3ac;padding:14px"><b style="font-size:18px">문장 분석</b><div class="sub">7과 · 본문 '+t.map(function(d){return SYM[d]}).join(' ')+'</div>'+t.map(dayRow).join('')+'</div>'}
  else{h+='<div class="sub" style="margin:2px 2px 10px">선생님이 정해 준 본문을 골라서 해요.</div><div class="card" style="padding:14px"><b style="font-size:18px">문장 분석</b><div class="sub">7과</div>'+all.map(dayRow).join('')+'</div>'}
  return h}
function vKey(){return '<h2>답안지</h2><div class="card sub" style="margin-top:10px">7과·8과 답안지는 곧 열려요.</div>'}
var ICON={text:'<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5"/><path d="M9 13h7M9 17h7"/>',key:'<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 12l3 3 5-6"/>',today:'<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>'};
function render(){
  var v=S.tab=='text'?vText():S.tab=='key'?vKey():vToday();
  document.getElementById('app').innerHTML=v;
  document.getElementById('tabbar').innerHTML=[['text','원문'],['key','답안지'],['today','오늘의 학습']].map(function(x){return '<button data-t="'+x[0]+'" class="'+(S.tab==x[0]?'on':'')+'"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+ICON[x[0]]+'</svg><span>'+x[1]+'</span></button>'}).join('');
  window.scrollTo(0,0)}
function firstSent(i){var s=cur();for(var k=0;k<s.sents.length;k++){if(new RegExp('\\['+i+'\\|').test(s.sents[k].mk))return s.sents[k].n}return s.sents[0].n}
function goTo(el){if(!el)return;el.scrollIntoView({behavior:'smooth',block:'center'});el.classList.remove('flash');void el.offsetWidth;el.classList.add('flash')}
document.addEventListener('click',function(e){
  var hk=e.target.closest('.hlk');if(hk){S.back=hk.dataset.n;S.backI=hk.dataset.i;goTo(document.getElementById('it-'+hk.dataset.i));return}
  var bk=e.target.closest('.bk');if(bk){var i=bk.dataset.back,n=(S.backI==i&&S.back)?S.back:firstSent(i);goTo(document.getElementById('ps-'+n));return}
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
window.addEventListener('pageshow',function(ev){if(ev.persisted&&!document.getElementById('list'))render()});
render();
</script></body></html>'''
HTML=HTML.replace('__DATA__',DATA)
open('../../../dongah-yun/l7/app/index.html','w').write(HTML)
print(len(HTML))
