import json,re,os,sys
SRC="/home/claude/nolbada/via/vsignal-e/index.html"
HERE=os.path.dirname(os.path.abspath(__file__))
def build(lesson,data,out,title,key,deepmap=None):
    units={u['id']:u for u in json.load(open(HERE+'/units.json'))}
    DATA=[];days={}
    for d in data:
        u=units[d['id']];days.setdefault(u['day'],[]).append(d)
    n=0
    for dd in sorted(days):
        for k,d in enumerate(days[dd],1):
            DATA.append({"id":d['id'],"d":dd,"n":k,"en":d['en'],"ko":d['ko'],"ch":d['ch'],"memo":d.get('memo',''),"x":d['x'],"lab":units[d['id']]['label']})
            if deepmap is not None:DATA[-1]["deep"]=deepmap.get(d['id'],[])
    t=open(SRC,encoding="utf8").read().split("\n")
    assert t[739].startswith("var DATA=")
    t[739]="var DATA="+json.dumps(DATA,ensure_ascii=False)+";"
    s="\n".join(t)
    s=s.replace("var KEY='vsig-e-v1';","var KEY='%s';"%key)
    CSS=re.search(r"CSS='(.*?)'\n",open(HERE+'/css.txt',encoding='utf8').read(),re.S).group(1)
    s=re.sub(r"<title>.*?</title>",lambda _m:"<title>%s</title>"%title+CSS,s,count=1)
    s=s.replace("Day '+S.day+'","%d과 · Day '+S.day+'"%lesson)
    L=lesson
    DESC='동사·접착제·뼈대 닮은꼴 찾기와 덩어리 안쪽 분석 → 성분 맞추기' if deepmap is not None else '한글 어순 맞추기 → 동사·접착제·뼈대 닮은꼴 찾기 → 성분 맞추기'
    OV="""
function home(){
  S=null;C=null;Q=null;
  var cu=store.cur&&store.cur.res&&(store.cur.i>0||store.cur.quiz||store.cur.c)?store.cur:null;
  var h='<a href="../" style="display:inline-block;color:#0f766e;text-decoration:none;padding:8px 0;font-size:14px">&larr; 과 선택</a>'
   +'<div class="card" style="margin-bottom:10px"><h2 style="margin-top:0">LL과 핵심 문장 분석 · TT</h2>'
   +'<p class="hint" style="margin:0 0 12px">'+DESC+' → 영어 어순 쌓기 → 마무리 퀴즈 순서로 풀어요. 정답률 90% 이상이면 통과예요.</p>';
  if(cu)h+='<button class="primary" data-act="resume" data-day="'+cu.day+'">Day '+cu.day+' 이어서 하기</button><p class="hint" style="margin:8px 0 4px">'+(cu.quiz?'문장 연습은 끝났어요. 마무리 퀴즈부터':days[cu.day].length+'문장 중 '+(cu.i+1)+'번째 문장부터')+'</p>';
  h+='</div><div class="card"><h2 style="margin-top:0">Day 고르기</h2><div class="dgrid">';
  dayList.forEach(function(d){var b=store.best[d];h+='<button class="dg'+(b?' ok':'')+'" data-act="start" data-day="'+d+'">'+d+(b?'<small class="dd">\\u2713</small>':'')+'</button>';});
  h+='</div><p class="hint" style="margin:10px 0 0">'+dayList.map(function(d){var a=days[d];return 'Day '+d+' : '+a[0].lab.replace(/^\\d+과 /,'').replace(/ [①②③]/,'')+(a.length>1?' ~ '+a[a.length-1].lab.replace(/^\\d+과 /,'').replace(/ [①②③]/,''):'');}).join('<br>')+'</p></div>';
  app.innerHTML=h;window.scrollTo(0,0);
}
function renderFin(){
  var f=S.fin,nextDay=dayList[dayList.indexOf(S.day)+1];
  app.innerHTML='<div class="top"><button class="back" data-act="home">목록</button><div class="ttl">LL과 Day '+S.day+'</div></div>'
   +'<div class="card"><h2 style="margin-top:0">LL과 Day '+S.day+' 분석 완료</h2>'
   +'<p class="hint" style="margin:0">정답률 '+Math.round(f.acc*100)+'% · '+(f.pass?'통과':'한번 더')+' · 실수 '+f.total+'개</p></div>'
   +noteBlock(S.day)
   +'<div class="two" style="margin-top:12px"><button class="ghost" data-act="again">다시 하기</button>'+(nextDay?'<button class="primary" data-act="startnext" data-day="'+nextDay+'">Day '+nextDay+' 시작</button>':'<button class="primary" data-act="home">목록으로</button>')+'</div>';
  window.scrollTo(0,0);
}
TAB='day';home();
""".replace("'+DESC+'",DESC).replace("LL",str(L)).replace("TT",title.split('(')[-1].rstrip(')') if '(' in title else '')
    if deepmap is not None:
        k0="kdone:{},k2:{},ph:(s.ch.some(function(c){return !!c.k;})?'K':'R')};";assert k0 in s
        s=s.replace(k0,"kdone:{},k2:{},ph:'X',xi:0};core.forEach(function(k){C.kdone[k]=true;});xNew();",1)
    if deepmap is not None:s=s.replace("['1 뜻·성분','2 어순']","['1 분석·성분','2 어순']")
    s=s.replace("BRK.init(app,",OV+"\nBRK.init(app,",1)
    XJS=open(HERE+"/xray_patch.js",encoding="utf8").read();XH=open(HERE+"/xray_handlers.js",encoding="utf8").read()
    s=s.replace("function finishDay(){",XJS+"function finishDay(){",1)
    a1="  fixH();\n  flyIn();\n}";assert a1 in s
    s=s.replace(a1,"  fixH();\n  flyIn();\n  try{if(C&&C.ph==='X')xDraw();}catch(e){}\n}",1)
    a2="function vA(){\n  var s=C.s,ph=C.ph,cur=ph==='K'?curK():curA();";assert a2 in s
    s=s.replace(a2,a2+"\n  if(ph==='X')return vX();",1)
    a3="{C.ph='R';C.lastDrop=null;}";assert s.count(a3)==1
    s=s.replace(a3,"{C.ph=(s.x?'X':'R');C.xi=0;xNew();C.lastDrop=null;}",1)
    a4="  else if(a==='next'){\n    if(C.step<2){C.step++;}";assert a4 in s
    s=s.replace(a4,XH+a4,1)
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,"w",encoding="utf8").write(s);return len(DATA)
