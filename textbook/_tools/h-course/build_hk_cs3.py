import json,re,os
SRC="/home/claude/via/vsignal-e/index.html"
OUT="/home/claude/via/textbook/g1-cheongseok-neungryul-min/l3/e/index.html"
def C(t,r,k,c=None,a=None,g=False,alt=None):
    o={"t":t,"r":r,"k":k}
    if c:o["c"]=c
    if a:o["a"]=a
    if g:o["g"]=True
    if alt:o["alt"]=alt
    return o
ALT=["목적어","동사"]
D=[
("Its story starts with a girl who meets a tiger",
 "그것의(=책의) 이야기는 호랑이를 만나는 한 소녀로부터 시작된다",
 [C("Its story","주어","그것의(=책의) 이야기는"),C("starts","동사","시작된다"),
  C("with a girl","수식어","한 소녀로부터","전치사구","동사(starts) 수식"),
  C("who meets a tiger","수식어","호랑이를 만나는","형용사절","명사(girl) 수식")],
 "starts with = 자동사 + 전치사 표현. with a girl은 목적어가 아니라 전치사구(필수 수식어)라서 1형식이에요\nwho meets a tiger = a girl을 뒤에서 꾸미는 관계절. who 앞이 사람(a girl)이고 who 바로 뒤에 동사가 와서 주격 관계대명사예요"),
("Keller’s inspiration for her award-winning book was an old folktale that her halmoni (grandmother) used to tell her",
 "Keller의 수상 도서에 대한 영감은 그녀의 할머니가 그녀에게 이야기해 주던 옛 설화였다",
 [C("Keller’s inspiration","주어","Keller의 영감은"),
  C("for her award-winning book","수식어","수상 도서에 대한","전치사구","명사(inspiration) 수식"),
  C("was","동사","였다"),C("an old folktale","보어","옛 설화"),
  C("that her halmoni (grandmother) used to tell her","수식어","그녀의 할머니가 그녀에게 이야기해 주던","형용사절","명사(folktale) 수식")],
 "was = 주어와 보어를 이어 주는 동사. Keller’s inspiration = an old folktale 이라서 2형식이에요\nthat절 안에서 tell her 뒤에 '이야기'(tell의 직접목적어)가 빠져 있고, 그 자리를 an old folktale이 채워요 (목적격 관계대명사)\nused to tell = 예전에 ~하곤 했다, 한 덩어리 동사"),
("Keller wanted to revive the public’s interest in tigers by writing her own book",
 "Keller는 그녀 자신의 책을 씀으로써 호랑이에 대한 대중의 흥미를 되살리고 싶어 했다",
 [C("Keller","주어","Keller는"),C("wanted","동사","원했다"),
  C("to revive the public’s interest in tigers","목적어","호랑이에 대한 대중의 흥미를 되살리기를"),
  C("by writing her own book","수식어","그녀 자신의 책을 씀으로써","전치사구","동사(wanted to revive) 수식")],
 "wanted의 목적어는 to revive ~ (to부정사구). want는 to부정사를 목적어로 취하는 동사예요\nby writing = ~함으로써. by 뒤의 -ing는 동명사이고, 수단을 덧붙이는 말(수식어)이에요"),
("For example, in one story, a tiger helps a human become rich after the human saves the tiger’s life",
 "예를 들어 한 이야기에서 호랑이는 한 인간이 부유해지도록 돕는다, 그 인간이 그 호랑이의 생명을 구해 준 이후",
 [C("For example, in one story,","수식어","예를 들어 한 이야기에서","부가의 부사구","동사(helps) 수식"),
  C("a tiger","주어","호랑이는"),C("helps","동사","돕는다"),
  C("a human","목적어","한 인간이"),C("become rich","목적격보어","부유해지도록"),
  C("after the human saves the tiger’s life","수식어","그 인간이 그 호랑이의 생명을 구해 준 이후","시간의 부사절","동사(helps) 수식")],
 "help + 목적어 + 동사원형 = 5형식. a human = become rich (한 인간이 부유해지다) 관계라서 목적격보어예요\nhelps가 문장의 동사이고, become은 목적격보어 자리의 원형부정사라 동사 덩어리가 따로 생기는 게 아니에요\nafter가 이끄는 절은 시간을 덧붙이는 부사절"),
("However, they were also scared of tigers because being injured or even killed by tigers was common in the past",
 "그러나 그들은 호랑이에게 상처를 입거나 심지어 죽임을 당하는 일이 과거에는 흔했기 때문에 호랑이를 무서워하기도 했다",
 [C("However,","수식어","그러나","부가의 부사","문장 전체 수식"),
  C("they","주어","그들은"),C("were","동사","~였다"),C("also scared","보어","무서워하기도 했다"),
  C("of tigers","수식어","호랑이를","전치사구","형용사(scared) 수식"),
  C("because being injured or even killed by tigers was common in the past","수식어","호랑이에게 상처를 입거나 심지어 죽임을 당하는 일이 과거에는 흔했기 때문에","이유의 부사절","동사(were) 수식")],
 "they were scared = 2형식. scared는 '무서워하는 상태'를 나타내는 형용사(보어)로 봐요. of tigers는 무서워하는 대상을 덧붙이는 말이에요\nbecause절 안의 being injured or even killed by tigers 전체가 절의 주어(동명사구)이고, 동사는 was예요"),
("One verse of the song is a reinterpreted version of “Sugungga,” which is a traditional Korean song",
 "이 노래의 한 구절은 한국의 전통 가곡인 ‘수궁가’의 재해석판이다",
 [C("One verse of the song","주어","이 노래의 한 구절(가사)은"),C("is","동사","~이다"),
  C("a reinterpreted version of “Sugungga,”","보어","‘수궁가’의 재해석판"),
  C("which is a traditional Korean song","수식어","한국의 전통 가곡인","형용사절","명사(Sugungga) 수식")],
 "One verse = a reinterpreted version (한 구절 = 재해석판), 2형식이에요\n쉼표 뒤 which = 앞의 “Sugungga”를 받아 '그리고 그것은 ~' 순서로 이어 해석하는 계속적 용법"),
("Who can deny that the tiger is a symbol of Korea",
 "누가 호랑이가 한국의 상징이라는 점을 부정할 수 있을까",
 [C("Who","주어","누가"),C("can deny","동사","부정할 수 있을까"),
  C("that the tiger is a symbol of Korea","목적어","호랑이가 한국의 상징이라는 점을")],
 "Who가 주어, can deny가 한 덩어리 동사. 의문문이라도 who가 주어 자리에 있어서 3형식 S + V + O예요\nthat절 전체가 deny의 목적어 (that 뒤는 완전한 문장이라 접속사)"),
]
GQ=[
 {"cl":[{"ci":3,"kind":"형용사절","sub":"주격 관계대명사"}],"fm":1},
 {"cl":[{"ci":4,"kind":"형용사절","sub":"목적격 관계대명사"}],"fm":2},
 {"cl":[],"fm":3},
 {"cl":[{"ci":5,"kind":"부사절","sub":"시간"}],"fm":5},
 {"cl":[{"ci":5,"kind":"부사절","sub":"이유"}],"fm":2},
 {"cl":[{"ci":3,"kind":"형용사절","sub":"계속적 용법(which)"}],"fm":2},
 {"cl":[{"ci":2,"kind":"명사절","sub":"목적어"}],"fm":3},
]
DATA=[]
for i,(en,ko,ch,memo) in enumerate(D):
    assert "".join((" " if (j and not c.get("g")) else "")+c["t"] for j,c in enumerate(ch)).replace("’","'")==en.replace("’","'"),(i,)
    DATA.append({"id":"CS3-%d"%(i+1),"d":1,"n":i+1,"en":en,"ko":ko,"ch":ch,"memo":memo,"gq":GQ[i]})
t=open(SRC,encoding="utf8").read().split("\n")
assert t[739].startswith("var DATA=")
t[739]="var DATA="+json.dumps(DATA,ensure_ascii=False)+";"
s="\n".join(t)
s=s.replace("var KEY='vsig-e-v1';","var KEY='vsig-tb-g1cs-l3-e-real-v1';")
CSS='<style>.r-word,.r-rv,.r-xray{display:none!important}button.primary[disabled]{opacity:.35;pointer-events:none}.gqs{line-height:2.3;font-size:17px;margin:6px 0 12px}.gqh{background:#fde047;color:#14202b;padding:2px 5px;border-radius:6px;font-weight:700}.gqc{color:#566474;padding:2px 3px}.gqk{background:#fef9c3;color:#14202b;padding:2px 5px;border-radius:6px}.gqk.act{outline:2px solid #eab308;font-weight:700}.gqm{display:inline-block;min-width:54px;text-align:center;padding:0 9px;margin:0 2px;border-radius:8px;border:1.5px solid #64748b;font-size:14px;font-weight:700;color:#334155;background:repeating-linear-gradient(135deg,#cbd5e1 0 7px,#f1f5f9 7px 14px);vertical-align:middle}.gqm.act{border-color:#eab308;box-shadow:0 0 0 2px #fde047}.gqf{display:flex;flex-direction:column;gap:8px}.gqo{text-align:left;display:block;width:100%}.gqo b{font-size:16px;margin-right:6px}.gqko,.gqfo{display:block;font-size:13px;color:#566474;font-weight:400}</style>'
s=re.sub(r"<title>.*?</title>",lambda _m:"<title>청석고1 3과 핵심 7문장 · H-K코스</title>"+CSS,s,count=1)

s=s.replace("Day '+S.day+'","3과 핵심 7문장")
s=s.replace('<div class="rec-h">V SIGNAL E</div>','<div class="rec-h">청석고1 3과 · H-K코스</div>')
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
s=s.replace("V SIGNAL E 단어 퀴즈","단어 퀴즈").replace("V SIGNAL E단계","3과 핵심 7문장").replace("V시그널 E단계 문장 분석(벽돌깨기) 모듈","3과 핵심 7문장 분석 모듈")
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,"w",encoding="utf8").write(s)
print("ok",len(s))
