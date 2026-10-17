import json,re,os
SRC="/home/claude/via/vsignal-e/index.html"
OUT="/home/claude/via/textbook/g1-geumcheon-mirae/l4/e/index.html"
def C(t,r,k,c=None,a=None,g=False,alt=None):
    o={"t":t,"r":r,"k":k}
    if c:o["c"]=c
    if a:o["a"]=a
    if g:o["g"]=True
    if alt:o["alt"]=alt
    return o
ALT=["목적어","동사"]
D=[
("Traditionally, researchers have studied various functions of neural implants, which are medical devices like computer chips that can be implanted in the nervous system.",
 "전통적으로 연구자들은 신경 임플란트의 다양한 기능을 연구해 왔고, 신경 임플란트는 신경계에 이식될 수 있는 컴퓨터 칩과 같은 의료 기기이다.",
 [C("Traditionally,","수식어","전통적으로","방법의 부사","동사(have studied) 수식"),C("researchers","주어","연구자들은"),C("have studied","동사","연구해 왔다",g=False),
  C("various functions of neural implants,","목적어","신경 임플란트의 다양한 기능을"),
  C("which are medical devices like computer chips that can be implanted in the nervous system.","수식어","그것은 신경계에 이식될 수 있는 컴퓨터 칩과 같은 의료 기기이다","형용사절","명사(neural implants) 수식")],
 "have studied = have + p.p.(현재완료), 동사 한 덩어리\n쉼표 뒤 which = 앞의 neural implants를 받아 '그리고 그것은 ~' 순서로 이어서 해석\nwhich절 안의 that can be implanted ~ 는 computer chips를 꾸미는 관계절이에요"),
("Similarly, those who have lost their arms can use artificial arms operated by the same mechanism.",
 "마찬가지로 팔을 잃은 사람들은 동일한 메커니즘으로 작동하는 의수를 사용할 수 있다.",
 [C("Similarly,","수식어","마찬가지로","방법의 부사","동사(can use) 수식"),C("those","주어","사람들은"),
  C("who have lost their arms","수식어","팔을 잃은","형용사절","명사(those) 수식"),
  C("can use","동사","사용할 수 있다"),C("artificial arms","목적어","의수를"),
  C("operated by the same mechanism.","수식어","동일한 메커니즘으로 작동하는","분사구","명사(artificial arms) 수식")],
 "those who ~ = ~하는 사람들 (who절이 those를 꾸며서 주어가 길어져요)\ncan use = 조동사 + 동사, 한 덩어리 동사\noperated by ~ 는 artificial arms를 뒤에서 꾸미는 과거분사구 (의수는 '작동되는' 수동 관계)"),
("Some futurists predict that these implants will become commercially available in the next 20 to 30 years and significantly change our daily lives.",
 "일부 미래학자들은 이러한 임플란트가 향후 20~30년 이내에 상용화되고 우리의 일상을 크게 변화시킬 것이라고 예측한다.",
 [C("Some futurists","주어","일부 미래학자들은"),C("predict","동사","예측한다"),
  C("that these implants will become commercially available in the next 20 to 30 years and significantly change our daily lives.","목적어","이러한 임플란트가 향후 20~30년 이내에 상용화되고 우리의 일상을 크게 변화시킬 것이라고")],
 "that절 전체가 predict의 목적어 (예측하는 내용)\nthat절 안에는 동사가 두 개 (will become / (will) significantly change)로, and가 이어줘요"),
("Before we can fully embrace the era of AI-powered neural implants, many tricky ethical issues should be addressed.",
 "우리가 AI 기반 신경 임플란트 시대를 완전히 받아들이기 전에 여러 가지 까다로운 윤리적 문제들이 해결되어야 한다.",
 [C("Before we can fully embrace the era of AI-powered neural implants,","수식어","우리가 AI 기반 신경 임플란트 시대를 완전히 받아들이기 전에","시간의 부사절","동사(should be addressed) 수식"),
  C("many tricky ethical issues","주어","여러 가지 까다로운 윤리적 문제들이"),C("should be addressed.","동사","해결되어야 한다")],
 "should be addressed = 조동사 + be + p.p.(수동), 동사 한 덩어리\n목적어 없이 '문제들이 해결된다'로 끝나서 S + V 모양(1형식 닮은꼴)으로 봐요\nBefore가 이끄는 절은 시간을 덧붙이는 부사절"),
("There’s a risk that organizations or hackers could access personal data without permission through AI-connected implants.",
 "조직이나 해커가 AI와 연결된 임플란트를 통해 허가 없이 개인 정보에 접근할 수 있는 위험이 있다.",
 [C("There’s","동사","있다"),C("a risk","주어","위험이"),
  C("that organizations or hackers could access personal data without permission through AI-connected implants.","수식어","조직이나 해커가 AI와 연결된 임플란트를 통해 허가 없이 개인 정보에 접근할 수 있다는","형용사절","명사(risk) 수식")],
 "There is ~ 구문: There는 해석하지 않고, is 뒤의 a risk가 주어 (있다 + 위험이)\nthat절 = a risk의 내용을 설명하는 동격 (that 뒤가 완전한 문장)"),
("This means that our thoughts, emotions, and behaviors could be controlled by hackers.",
 "이것은 우리의 생각, 감정, 행동이 해커에 의해 통제될 수 있다는 것을 뜻한다.",
 [C("This","주어","이것은"),C("means","동사","뜻한다"),
  C("that our thoughts, emotions, and behaviors could be controlled by hackers.","목적어","우리의 생각, 감정, 행동이 해커에 의해 통제될 수 있다는 것을")],
 "that절 전체가 means의 목적어 (뜻하는 내용)\nthoughts, emotions, and behaviors = 주어가 세 개 나열된 것"),
("I’m really worried about the privacy issues it might cause.",
 "나는 그것이 초래할 수 있는 프라이버시 문제가 정말 걱정된다.",
 [C("I","주어","나는"),C("’m","동사","~이다",g=True),C("really worried","보어","정말 걱정된다"),
  C("about the privacy issues","수식어","프라이버시 문제에 대해","전치사구","형용사(worried) 수식"),
  C("it might cause.","수식어","그것이 초래할 수 있는","형용사절","명사(issues) 수식")],
 "the privacy issues (that) it might cause = 목적격 관계대명사 that이 생략된 형태\ncause의 목적어가 앞의 issues라서, 명사 + 주어 + 동사가 바로 붙어 있으면 생략을 의심해요"),
]
GQ=[
 {"cl":[{"ci":4,"kind":"형용사절","sub":"계속적 용법(which)"}],"fm":3},
 {"cl":[{"ci":2,"kind":"형용사절","sub":"주격 관계대명사"}],"fm":3},
 {"cl":[{"ci":2,"kind":"명사절","sub":"목적어"}],"fm":3},
 {"cl":[{"ci":0,"kind":"부사절","sub":"시간"}],"fm":1},
 {"cl":[{"ci":2,"kind":"명사절","sub":"동격"}],"fm":1},
 {"cl":[{"ci":2,"kind":"명사절","sub":"목적어"}],"fm":3},
 {"cl":[{"ci":4,"kind":"형용사절","sub":"목적격 관계대명사"}],"fm":2},
]
DATA=[]
for i,(en,ko,ch,memo) in enumerate(D):
    assert "".join((" " if (j and not c.get("g")) else "")+c["t"] for j,c in enumerate(ch)).replace("’","'")==en.replace("’","'"),(i,)
    DATA.append({"id":"G4-%d"%(i+1),"d":1,"n":i+1,"en":en,"ko":ko,"ch":ch,"memo":memo,"gq":GQ[i]})
t=open(SRC,encoding="utf8").read().split("\n")
assert t[739].startswith("var DATA=")
t[739]="var DATA="+json.dumps(DATA,ensure_ascii=False)+";"
s="\n".join(t)
s=s.replace("var KEY='vsig-e-v1';","var KEY='vsig-tb-g1gc-l4-e-real-v1';")
CSS='<style>.r-word,.r-rv,.r-xray{display:none!important}button.primary[disabled]{opacity:.35;pointer-events:none}.gqs{line-height:2.3;font-size:17px;margin:6px 0 12px}.gqh{background:#fde047;color:#14202b;padding:2px 5px;border-radius:6px;font-weight:700}.gqc{color:#566474;padding:2px 3px}.gqk{background:#fef9c3;color:#14202b;padding:2px 5px;border-radius:6px}.gqk.act{outline:2px solid #eab308;font-weight:700}.gqm{display:inline-block;min-width:54px;text-align:center;padding:0 9px;margin:0 2px;border-radius:8px;border:1.5px solid #64748b;font-size:14px;font-weight:700;color:#334155;background:repeating-linear-gradient(135deg,#cbd5e1 0 7px,#f1f5f9 7px 14px);vertical-align:middle}.gqm.act{border-color:#eab308;box-shadow:0 0 0 2px #fde047}.gqf{display:flex;flex-direction:column;gap:8px}.gqo{text-align:left;display:block;width:100%}.gqo b{font-size:16px;margin-right:6px}.gqko,.gqfo{display:block;font-size:13px;color:#566474;font-weight:400}</style>'
s=re.sub(r"<title>.*?</title>",lambda _m:"<title>금천고1 4과 핵심 7문장 · H-K코스</title>"+CSS,s,count=1)

s=s.replace("Day '+S.day+'","4과 핵심 7문장")
s=s.replace('<div class="rec-h">V SIGNAL E</div>','<div class="rec-h">금천고1 4과 · H-K코스</div>')
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
