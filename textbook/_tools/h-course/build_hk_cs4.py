import json,re,os
SRC="/home/claude/via/vsignal-e/index.html"
OUT="/home/claude/via/textbook/g1-cheongseok-neungryul-min/l4/e/index.html"
def C(t,r,k,c=None,a=None,g=False,alt=None):
    o={"t":t,"r":r,"k":k}
    if c:o["c"]=c
    if a:o["a"]=a
    if g:o["g"]=True
    if alt:o["alt"]=alt
    return o
# 청석고1 공통영어2 (NE능률 민병천) 4과 H-K코스. 영어 원문/해석은 jwa.html(4과 좌본문우해석) 기준.
# 영어 문장의 마지막 마침표만 덧붙였고(jwa는 조각 표시라 마침표가 없음) 나머지는 한 글자도 바꾸지 않았다.
# ko 는 jwa 한글 조각을 우리말 어순(관형형이 명사 앞)으로 재배열한 것이며, 각 청크의 k 는 ko 안에 그대로 들어 있다.
D=[
("Often, plastic waste is moved to places where it is just dumped or burned.",
 "종종 플라스틱 쓰레기는 그저 내버려지거나 태워지는 장소들로 보내진다.",
 [C("Often,","수식어","종종","부사","동사(is moved) 수식"),C("plastic waste","주어","플라스틱 쓰레기는"),C("is moved","동사","보내진다"),
  C("to places","수식어","장소들로","장소의 부사구","동사(is moved) 수식"),
  C("where it is just dumped or burned.","수식어","그저 내버려지거나 태워지는","형용사절","명사(places) 수식")],
 "is moved = be + p.p.(수동), 동사 한 덩어리\n'to places'는 어디로 보내지는지 덧붙이는 말이고, '쓰레기가 보내진다'로 문장이 완성되는 S + V 모양(1형식 닮은꼴)이에요\nwhere절 = places를 꾸미는 관계부사절 (뒤가 완전한 문장: it is just dumped or burned)"),
("Although polluted soil can be dug up and transported to a landfill, this process is expensive.",
 "비록 오염된 흙이 파내져서 매립지로 옮겨질 수는 있지만 이 과정은 비용이 많이 든다.",
 [C("Although polluted soil can be dug up and transported to a landfill,","수식어","비록 오염된 흙이 파내져서 매립지로 옮겨질 수는 있지만","양보의 부사절","동사(is) 수식"),
  C("this process","주어","이 과정은"),C("is","동사","~이다"),C("expensive.","보어","비용이 많이 드는")],
 "Although가 이끄는 절 = 양보의 부사절 ('비록 ~이지만'), 절 안에 can be dug up과 (can be) transported가 and로 이어져 있어요\n뼈대는 this process is expensive: 주어 + 동사 + 보어(this process = expensive), 2형식\nis는 '~이다', expensive는 상태를 설명하는 보어예요"),
("The coffee-making process, however, generates used coffee grounds, which are normally sent to landfills.",
 "그러나 커피 만드는 과정은 보통 매립지로 보내지는 사용된 커피 찌꺼기를 발생시킨다.",
 [C("The coffee-making process,","주어","커피 만드는 과정은"),C("however,","수식어","그러나","부사","동사(generates) 수식"),C("generates","동사","발생시킨다"),
  C("used coffee grounds,","목적어","사용된 커피 찌꺼기를"),
  C("which are normally sent to landfills.","수식어","보통 매립지로 보내지는","형용사절","명사(grounds) 수식")],
 "however는 문장 중간에 끼어든 '그러나', 빼도 문장이 말이 돼서 꾸밈말이에요\n쉼표 뒤 which = 앞의 used coffee grounds를 받는 계속적 용법 (직독직해로는 '그리고 그것은 ~' 순서로 이어 읽어요)\nwhich절 안의 are normally sent = be + p.p.(수동), 동사 한 덩어리"),
("Biofuel is a natural fuel that is made from plant or animal sources.",
 "바이오 연료는 식물이나 동물성 원료로 만들어진 천연 연료이다.",
 [C("Biofuel","주어","바이오 연료는"),C("is","동사","~이다"),C("a natural fuel","보어","천연 연료"),
  C("that is made from plant or animal sources.","수식어","식물이나 동물성 원료로 만들어진","형용사절","명사(fuel) 수식")],
 "Biofuel = a natural fuel 이라서 주어 + 동사 + 보어, 2형식이에요\nthat is made ~ 에서 that 뒤에 주어가 없고 바로 동사(is made)가 나오니까 주격 관계대명사예요\nis made = be + p.p.(수동), 동사 한 덩어리"),
("Researchers have found that they can grow algae on old coffee grounds without adding any other nutrients.",
 "연구자들은 그들이 어떤 다른 영양분도 더하지 않고 오래된 커피 찌꺼기에서 조류를 자라게 할 수 있다는 것을 알아냈다.",
 [C("Researchers","주어","연구자들은"),C("have found","동사","알아냈다"),
  C("that they can grow algae on old coffee grounds without adding any other nutrients.","목적어","그들이 어떤 다른 영양분도 더하지 않고 오래된 커피 찌꺼기에서 조류를 자라게 할 수 있다는 것을")],
 "have found = have + p.p.(현재완료), 동사 한 덩어리\nthat절 전체가 found의 목적어 (알아낸 내용)\nthat절 안의 without adding ~ 은 'can grow'를 꾸미는 말이고, without 뒤의 adding은 동명사예요"),
("There could be many more possible solutions to the problems we currently face.",
 "우리가 현재 직면한 문제들에 대한 훨씬 더 많은 가능성 있는 해결책들이 있을 수 있다.",
 [C("There could be","동사","있을 수 있다"),C("many more possible solutions","주어","훨씬 더 많은 가능성 있는 해결책들이"),
  C("to the problems","수식어","문제들에 대한","형용사구","명사(solutions) 수식"),
  C("we currently face.","수식어","우리가 현재 직면한","형용사절","명사(problems) 수식")],
 "There could be ~ 구문: There는 해석하지 않고, be 뒤의 many more possible solutions가 주어 (있을 수 있다 + 해결책들이)\ncould be = 조동사 + be, 동사 한 덩어리\nthe problems (that) we currently face = 목적격 관계대명사 that이 생략된 형태, face의 목적어가 앞의 problems예요"),
("Therefore, this promising area should be further explored to find out which trees are the most effective.",
 "그러므로 이 촉망받는 분야는 어떤 나무들이 가장 효과적인지 찾아내기 위해 더 깊게 탐구되어야 한다.",
 [C("Therefore,","수식어","그러므로","부사","동사(should be explored) 수식"),C("this promising area","주어","이 촉망받는 분야는"),
  C("should be further explored","동사","더 깊게 탐구되어야 한다"),
  C("to find out which trees are the most effective.","수식어","어떤 나무들이 가장 효과적인지 찾아내기 위해","목적의 부사구","동사(should be explored) 수식")],
 "should be further explored = 조동사 + be + p.p.(수동), 사이에 부사 further가 끼어 있어도 동사 한 덩어리\n'분야가 탐구되어야 한다'로 끝나서 S + V 모양(1형식 닮은꼴)이에요\nto find out ~ = '~을 찾아내기 위해' 목적을 덧붙이는 to부정사구 (안에 which trees are ~ 의문사절이 들어 있어요)"),
]
GQ=[
 {"cl":[{"ci":4,"kind":"형용사절","sub":"관계부사"}],"fm":1},
 {"cl":[{"ci":0,"kind":"부사절","sub":"양보"}],"fm":2},
 {"cl":[{"ci":4,"kind":"형용사절","sub":"계속적 용법(which)"}],"fm":3},
 {"cl":[{"ci":3,"kind":"형용사절","sub":"주격 관계대명사"}],"fm":2},
 {"cl":[{"ci":2,"kind":"명사절","sub":"목적어"}],"fm":3},
 {"cl":[{"ci":3,"kind":"형용사절","sub":"목적격 관계대명사"}],"fm":1},
 {"cl":[],"fm":1},
]
DATA=[]
for i,(en,ko,ch,memo) in enumerate(D):
    assert "".join((" " if (j and not c.get("g")) else "")+c["t"] for j,c in enumerate(ch)).replace("’","'")==en.replace("’","'"),(i,)
    DATA.append({"id":"CS4-%d"%(i+1),"d":1,"n":i+1,"en":en,"ko":ko,"ch":ch,"memo":memo,"gq":GQ[i]})
t=open(SRC,encoding="utf8").read().split("\n")
assert t[739].startswith("var DATA=")
t[739]="var DATA="+json.dumps(DATA,ensure_ascii=False)+";"
s="\n".join(t)
s=s.replace("var KEY='vsig-e-v1';","var KEY='vsig-tb-g1cs-l4-e-real-v1';")
CSS='<style>.r-word,.r-rv,.r-xray{display:none!important}button.primary[disabled]{opacity:.35;pointer-events:none}.gqs{line-height:2.3;font-size:17px;margin:6px 0 12px}.gqh{background:#fde047;color:#14202b;padding:2px 5px;border-radius:6px;font-weight:700}.gqc{color:#566474;padding:2px 3px}.gqk{background:#fef9c3;color:#14202b;padding:2px 5px;border-radius:6px}.gqk.act{outline:2px solid #eab308;font-weight:700}.gqm{display:inline-block;min-width:54px;text-align:center;padding:0 9px;margin:0 2px;border-radius:8px;border:1.5px solid #64748b;font-size:14px;font-weight:700;color:#334155;background:repeating-linear-gradient(135deg,#cbd5e1 0 7px,#f1f5f9 7px 14px);vertical-align:middle}.gqm.act{border-color:#eab308;box-shadow:0 0 0 2px #fde047}.gqf{display:flex;flex-direction:column;gap:8px}.gqo{text-align:left;display:block;width:100%}.gqo b{font-size:16px;margin-right:6px}.gqko,.gqfo{display:block;font-size:13px;color:#566474;font-weight:400}</style>'
s=re.sub(r"<title>.*?</title>",lambda _m:"<title>청석고1 4과 핵심 7문장 · H-K코스</title>"+CSS,s,count=1)

s=s.replace("Day '+S.day+'","4과 핵심 7문장")
s=s.replace('<div class="rec-h">V SIGNAL E</div>','<div class="rec-h">청석고1 4과 · H-K코스</div>')
s=s.replace('<div class="cv-t">V SIGNAL</div>','<div class="cv-t">H-K</div>')
OV = """<script>
function home(){
  S=null;C=null;Q=null;
  var b=store.best[1];var cu=store.cur&&store.cur.day===1&&store.cur.res&&(store.cur.i>0||store.cur.quiz||store.cur.c)?store.cur:null;
  var h='<a href="../" style="display:inline-block;color:#0f766e;text-decoration:none;padding:8px 0;font-size:14px">&larr; 4과 핵심 7문장 선택</a>'
   +'<div class="card" style="margin-bottom:10px"><h2 style="margin-top:0">4과 핵심 7문장 · H-K코스</h2>'
   +'<p class="hint" style="margin:0 0 12px">영어 덩어리의 뜻을 고르고 역할을 정한 뒤, 어순을 쌓고 마무리 퀴즈를 풉니다. 정답률 90% 이상이면 통과예요.</p>'
   +(cu?'<button class="primary" data-act="resume" data-day="1">이어서 하기</button><p class="hint" style="margin:8px 0 12px">'+(cu.quiz?'문장 연습은 끝났어요. 마무리 퀴즈부터':'7문장 중 '+(cu.i+1)+'번째 문장부터')+'</p><button class="ghost" data-act="startnext" data-day="1" style="width:100%">처음부터 다시 하기</button>':'<button class="primary" data-act="startnext" data-day="1">'+(b?'다시 풀기':'시작')+'</button>')
   +(b?'<p class="hint" style="margin:12px 0 0">4과 핵심 7문장 분석 완료 · 실수 '+b.mis+'개</p>':'')
   +'</div>';
  app.innerHTML=h;window.scrollTo(0,0);
}
function renderFin(){
  var f=S.fin;
  app.innerHTML='<div class="top"><button class="back" data-act="home">목록</button><div class="ttl">4과 핵심 7문장</div></div>'
   +'<div class="card"><h2 style="margin-top:0">4과 핵심 7문장 분석 완료</h2>'
   +'<p class="hint" style="margin:0">정답률 '+Math.round(f.acc*100)+'% · '+(f.pass?'통과':'한번 더')+' · 실수 '+f.total+'개</p></div>'
   +noteBlock(S.day)
   +'<div class="two" style="margin-top:12px"><button class="ghost" data-act="again">다시 하기</button><button class="primary" data-act="home">목록으로</button></div>';
  window.scrollTo(0,0);
}
TAB='day';home();
</script>"""
OVJ=OV.replace("<script>","").replace("</script>","")
assert s.count("BRK.init(app,")==1
s=s.replace("BRK.init(app,",OVJ+"\nBRK.init(app,",1)

# engine patches
PATCH = open(''+__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'gq_patch.js')+'',encoding='utf8').read()
s=s.replace("function finishDay(){", PATCH+"function finishDay(){",1)

old2="""h+='<p class="msg ok">이번 문장 '+(ms?'실수 '+ms+'개':'실수 없음')+'</p><button class="primary" data-act="next">'+(S.i+1<S.list.length?'다음 문장':'Day 결과 보기')+'</button>';}"""
assert old2 in s
s=s.replace(old2,"""h+=gqHtml();h+='<p class="msg ok">이번 문장 '+(ms?'실수 '+ms+'개':'실수 없음')+'</p><button class="primary" data-act="next"'+(gqDone()?'':' disabled')+'>'+(S.i+1<S.list.length?'다음 문장':'마무리 퀴즈로')+'</button>';}""",1)
old="""h+='<button class="primary" data-act="next">'+(S.i+1<S.list.length?'다음 문장':'Day 결과 보기')+'</button>';"""
assert old in s
s=s.replace(old,"""h+=gqHtml();h+='<button class="primary" data-act="next"'+(gqDone()?'':' disabled')+'>'+(S.i+1<S.list.length?'다음 문장':'마무리 퀴즈로')+'</button>';""",1)
oldn="  else if(a==='next'){\n    if(C.step<2){C.step++;}"
assert oldn in s
s=s.replace(oldn,"""  else if(a==='xq'){
    var tt=t.getAttribute('data-t'),v=t.getAttribute('data-v'),ci=t.getAttribute('data-ci');C.bk=C.bk||{};gqInit();
    if(tt==='kind'){var x=s.gq.cl.filter(function(z){return String(z.ci)===ci;})[0];
      if(x.kind===v)C.cq[ci].k=true;else{C.bk[ci+v]=1;C.mist[3]++;logW({day:S.day,n:s.n,kind:'clause',t:s.ch[ci].t,right:x.kind,picked:v});}}
    else if(tt==='sub'){var x2=s.gq.cl.filter(function(z){return String(z.ci)===ci;})[0];
      if(x2.sub===v)C.cq[ci].s=true;else{C.bk[ci+'s'+v]=1;C.mist[3]++;logW({day:S.day,n:s.n,kind:'clause',t:s.ch[ci].t,right:x2.sub,picked:v});}}
    else if(tt==='fm'){if(Number(v)===s.gq.fm)C.fmOk=true;else{C.bk['f'+v]=1;C.mist[3]++;logW({day:S.day,n:s.n,kind:'form',t:s.en,right:s.gq.fm+'형식',picked:v+'형식'});}}
  }
"""+oldn,1)
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf8").write(s)
print("ok",len(s))
