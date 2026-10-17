import json,re,os
SRC="/home/claude/via/vsignal-e/index.html"
OUT="/home/claude/via/textbook/g1-geumcheon-mirae/l3/e/index.html"
def C(t,r,k,c=None,a=None,g=False,alt=None):
    o={"t":t,"r":r,"k":k}
    if c:o["c"]=c
    if a:o["a"]=a
    if g:o["g"]=True
    if alt:o["alt"]=alt
    return o
ALT=["목적어","동사"]
D=[
("Today, you're going to meet three amazing artists who never gave up on their art, despite challenges in their lives.",
 "오늘 여러분은 인생의 역경에도 불구하고 자신의 예술을 결코 포기하지 않은 세 명의 놀라운 예술가를 만나게 될 것이다.",
 [C("Today,","수식어","오늘","시간의 부사구","동사(’re going to meet) 수식"),C("you","수식어" if False else "주어","여러분은"),C("’re going to meet","동사","만나게 될 것이다",g=True),
  C("three amazing artists","목적어","세 명의 놀라운 예술가들을"),
  C("who never gave up on their art,","수식어","자신의 예술을 결코 포기하지 않은","형용사절","명사(artists) 수식"),
  C("despite challenges in their lives.","수식어","인생의 역경에도 불구하고","양보의 부사구","동사(gave up) 수식")],
 "be going to = 조동사처럼 한 덩어리 동사 (’re going to meet)\nyou’re = you + ’re(are)라서 주어와 동사를 나눠 표시"),
("Each artist has a unique painting style and story that has made their work highly valued.",
 "예술가마다 독특한 화풍과 이야기가 있고, 그 덕분에 작품이 높이 평가받아 왔다.",
 [C("Each artist","주어","각 예술가는"),C("has","동사","가지고 있다"),C("a unique painting style and story","목적어","독특한 화풍과 이야기를"),
  C("that has made their work highly valued.","수식어","그것이 그들의 작품을 높이 평가받게 만들어 온","형용사절","명사(style and story) 수식")],
 "that절 안 = has made(동사) + their work(목적어) + highly valued(목적격보어) → 5형식"),
("It wasn't until he was 85 years old and became too ill to work that he turned to drawing to express his life experiences.",
 "그는 85세가 되어 몸이 너무 아파 일할 수 없게 되고 나서야, 자신의 인생 경험을 표현하려고 그림에 눈을 돌렸다.",
 [C("It wasn't until he was 85 years old and became too ill to work","수식어","그가 85세가 되고 몸이 너무 아파 일할 수 없게 된 후에야","시간의 부사절","동사(turned) 수식"),
  C("that","접속사","(that 뒤가 진짜 문장)"),C("he","주어","그는"),C("turned","동사","눈을 돌렸다"),
  C("to drawing","수식어","그림으로","부가의 부사구","동사(turned) 수식",alt=ALT),
  C("to express his life experiences.","수식어","자신의 인생 경험을 표현하기 위해","목적의 부사구","동사(turned) 수식")],
 "It wasn't until A that B = A하고 나서야 비로소 B (강조구문): A는 시간 수식어, that 뒤가 뼈대\n기준 ①: 자동사+전치사 = 1형식, 전치사구 = 필수 수식어\nturn(눈을 돌리다)는 목적어 없이 쓰는 자동사, to(~로) + 명사 덩어리 = 짝으로 따라오는 필수 수식어"),
("Traylor had a strong fear of dogs because they had often been used on farms to watch and hunt slaves.",
 "Traylor는 개를 몹시 무서워했는데, 개가 농장에서 노예를 감시하고 사냥하는 데 자주 이용되었기 때문이다.",
 [C("Traylor","주어","Traylor는"),C("had","동사","가지고 있었다"),C("a strong fear of dogs","목적어","개에 대한 강한 두려움을"),
  C("because they had often been used on farms","수식어","개가 농장에서 자주 이용되었기 때문에","이유의 부사절","동사(had) 수식"),
  C("to watch and hunt slaves.","수식어","노예를 감시하고 사냥하기 위해","목적의 부사구","동사(had been used) 수식")],
 "had often been used = had been + 과거분사 (과거완료 수동태), 동사 한 덩어리"),
("Although her physical limitations confined her to a small cottage, her talent and imagination were both limitless.",
 "신체적 제약 때문에 그녀는 작은 오두막집에 갇혀 지냈지만, 그녀의 재능과 상상력은 둘 다 끝이 없었다.",
 [C("Although her physical limitations confined her to a small cottage,","수식어","비록 신체적 제약이 그녀를 작은 오두막집에 가두었지만","양보의 부사절","동사(were) 수식"),
  C("her talent and imagination","주어","그녀의 재능과 상상력은"),C("were","동사","~였다"),C("both limitless.","보어","둘 다 무한한")],
 "Although절 안 = confined(동사) + her(목적어) + to a small cottage (confine A to B)"),
("After that, she even studied abroad in Paris, which was unusual for women at the time.",
 "그 후 그녀는 파리로 유학까지 갔는데, 이는 당시 여성에게는 드문 일이었다.",
 [C("After that,","수식어","그 후","시간의 부사구","동사(even studied) 수식"),C("she","주어","그녀는"),C("even studied","동사","유학까지 했다"),
  C("abroad in Paris,","수식어","파리에서","장소의 부사구","동사(even studied) 수식"),
  C("which was unusual for women at the time.","수식어","그것은 당시 여성에게 드문 일이었다","형용사절","문장 전체 수식")],
 "쉼표 뒤 which = 앞 내용 전체를 받음 (파리에서 유학까지 한 것) → 앞에서부터 이어서 해석"),
("Even after getting married, Ancher persisted in painting, objecting to the social pressure that married women were to solely focus on household duties.",
 "결혼한 뒤에도 Ancher는 계속 그림을 그렸고, 기혼 여성은 가사에만 집중해야 한다는 사회적 압력에 맞섰다.",
 [C("Even after getting married,","수식어","결혼 후에도","시간의 부사구","동사(persisted) 수식"),C("Ancher","주어","Ancher는"),C("persisted","동사","계속했다"),
  C("in painting,","수식어","그림 그리기를","부가의 부사구","동사(persisted) 수식",alt=ALT),
  C("objecting to the social pressure","수식어","사회적 압력에 저항하며","방법의 부사구","동사(persisted) 수식"),
  C("that married women were to solely focus on household duties.","수식어","기혼 여성은 가사에만 집중해야 한다는","형용사절","명사(pressure) 수식")],
 "기준 ①: 자동사+전치사 = 1형식, 전치사구 = 필수 수식어\npersist(계속하다)는 목적어 없이 쓰는 자동사, in(~에서) + 명사 덩어리 = 짝으로 따라오는 필수 수식어\nthat절 = the social pressure의 내용(동격). were to focus = be to(~해야 한다)"),
]
GQ=[
 {"cl":[{"ci":4,"kind":"형용사절","sub":"주격 관계대명사"}],"fm":3},
 {"cl":[{"ci":3,"kind":"형용사절","sub":"주격 관계대명사"}],"fm":3},
 {"cl":[{"ci":0,"kind":"부사절","sub":"시간"}],"fm":1},
 {"cl":[{"ci":3,"kind":"부사절","sub":"이유"}],"fm":3},
 {"cl":[{"ci":0,"kind":"부사절","sub":"양보"}],"fm":2},
 {"cl":[{"ci":4,"kind":"형용사절","sub":"계속적 용법(which)"}],"fm":1},
 {"cl":[{"ci":5,"kind":"명사절","sub":"동격"}],"fm":1},
]
DATA=[]
for i,(en,ko,ch,memo) in enumerate(D):
    assert "".join((" " if (j and not c.get("g")) else "")+c["t"] for j,c in enumerate(ch)).replace("’","'")==en.replace("’","'"),(i,)
    DATA.append({"id":"G3-%d"%(i+1),"d":1,"n":i+1,"en":en,"ko":ko,"ch":ch,"memo":memo,"gq":GQ[i]})
t=open(SRC,encoding="utf8").read().split("\n")
assert t[739].startswith("var DATA=")
t[739]="var DATA="+json.dumps(DATA,ensure_ascii=False)+";"
s="\n".join(t)
s=s.replace("var KEY='vsig-e-v1';","var KEY='vsig-tb-g1gc-l3-e-real-v1';")
CSS='<style>.r-word,.r-rv,.r-xray{display:none!important}button.primary[disabled]{opacity:.35;pointer-events:none}.gqs{line-height:2.3;font-size:17px;margin:6px 0 12px}.gqh{background:#fde047;color:#14202b;padding:2px 5px;border-radius:6px;font-weight:700}.gqc{color:#566474;padding:2px 3px}.gqk{background:#fef9c3;color:#14202b;padding:2px 5px;border-radius:6px}.gqk.act{outline:2px solid #eab308;font-weight:700}.gqm{display:inline-block;min-width:54px;text-align:center;padding:0 9px;margin:0 2px;border-radius:8px;border:1.5px solid #64748b;font-size:14px;font-weight:700;color:#334155;background:repeating-linear-gradient(135deg,#cbd5e1 0 7px,#f1f5f9 7px 14px);vertical-align:middle}.gqm.act{border-color:#eab308;box-shadow:0 0 0 2px #fde047}.gqf{display:flex;flex-direction:column;gap:8px}.gqo{text-align:left;display:block;width:100%}.gqo b{font-size:16px;margin-right:6px}.gqko,.gqfo{display:block;font-size:13px;color:#566474;font-weight:400}</style>'
s=re.sub(r"<title>.*?</title>",lambda _m:"<title>금천고1 3과 핵심 7문장 · H-K코스</title>"+CSS,s,count=1)

s=s.replace("Day '+S.day+'","3과 핵심 7문장")
s=s.replace('<div class="rec-h">V SIGNAL E</div>','<div class="rec-h">금천고1 3과 · H-K코스</div>')
s=s.replace('<div class="cv-t">V SIGNAL</div>','<div class="cv-t">H-K</div>')
OV = """<script>
function home(){
  S=null;C=null;Q=null;
  var b=store.best[1];var cu=store.cur&&store.cur.day===1&&store.cur.res&&(store.cur.i>0||store.cur.quiz||store.cur.c)?store.cur:null;
  var h='<a href="../" style="display:inline-block;color:#0f766e;text-decoration:none;padding:8px 0;font-size:14px">&larr; 3과 핵심 7문장 선택</a>'
   +'<div class="card" style="margin-bottom:10px"><h2 style="margin-top:0">3과 핵심 7문장 · H-K코스</h2>'
   +'<p class="hint" style="margin:0 0 12px">영어 덩어리의 뜻을 고르고 역할을 정한 뒤, 어순을 쌓고 마무리 퀴즈를 풉니다. 정답률 90% 이상이면 통과예요.</p>'
   +(cu?'<button class="primary" data-act="resume" data-day="1">이어서 하기</button><p class="hint" style="margin:8px 0 12px">'+(cu.quiz?'문장 연습은 끝났어요. 마무리 퀴즈부터':'7문장 중 '+(cu.i+1)+'번째 문장부터')+'</p><button class="ghost" data-act="startnext" data-day="1" style="width:100%">처음부터 다시 하기</button>':'<button class="primary" data-act="startnext" data-day="1">'+(b?'다시 풀기':'시작')+'</button>')
   +(b?'<p class="hint" style="margin:12px 0 0">3과 핵심 7문장 분석 완료 · 실수 '+b.mis+'개</p>':'')
   +'</div>';
  app.innerHTML=h;window.scrollTo(0,0);
}
function renderFin(){
  var f=S.fin;
  app.innerHTML='<div class="top"><button class="back" data-act="home">목록</button><div class="ttl">3과 핵심 7문장</div></div>'
   +'<div class="card"><h2 style="margin-top:0">3과 핵심 7문장 분석 완료</h2>'
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
