import json,re,os
SRC="/home/claude/via/vsignal-y/xray.html"
OUT_DIR="/home/claude/via/textbook/g1-cheongseok-neungryul-min/l3/y/"
R=lambda a,b:list(range(a,b))
def tk(s): return s.split(" ")
S=[]
def add(**k): S.append(k)

# ---- 1-2
t=tk("Its story starts with a girl who meets a tiger"); assert len(t)==10
add(lv="심화",id="1-2",tok=t,
 ch=["Its story starts with a girl","who meets a tiger"],
 ko=["그것의(=책의) 이야기는 한 소녀로부터 시작된다","호랑이를 만나는"],
 nodes=[dict(id="m",a=0,b=10,own=R(0,6),kids=[[6,10]],S=[1],V=[2],G=[[2]],form=1,fl=[3,4,5],
   sk=[dict(r="S",g=[0,1]),dict(r="V",g=[2])],
   note="Its story starts. 주어 + 동사, 1형식입니다. starts with는 자동사 + 전치사 표현이라 with a girl은 목적어가 아니라 전치사구(필수 수식어)예요. who절은 a girl을 꾸밉니다."),
  dict(id="a",a=6,b=10,own=R(6,10),kids=[],S=[6],V=[7],G=[[7]],kind="형용사절",sub="주격 관계대명사",anc=[5],np=[4,5],
   note="___ meets a tiger 에서 주어 자리(= a girl)가 비어 있어서 who는 주격 관계대명사입니다. who절은 a girl을 뒤에서 꾸며서 '호랑이를 만나는 한 소녀'가 돼요.")],
 dec={"0":"Its는 '그것의'라는 소유격 대명사입니다.","1":"story는 '이야기'라는 명사입니다.","3":"with는 전치사입니다.","4":"a는 관사입니다.","5":"girl은 '소녀'라는 명사입니다.","6":"who는 관계대명사입니다.","8":"a는 관사입니다.","9":"tiger는 '호랑이'라는 명사로, meets의 목적어예요."},
 vn="starts는 주절의 동사, who절 안의 meets도 동사예요.",
 why="기준 ①: 자동사 + 전치사 = 1형식, 전치사구 = 필수 수식어\nstart with(~로 시작하다)는 자동사 + 전치사 표현, 동사 표시는 starts까지이고 with a girl은 전치사구 수식어",
 nf=[],em=[])

# ---- 1-5
t=tk("Keller’s inspiration for her award-winning book was an old folktale that her halmoni (grandmother) used to tell her"); assert len(t)==18
add(lv="심화",id="1-5",tok=t,
 ch=["Keller’s inspiration for her award-winning book","was an old folktale","that her halmoni (grandmother) used to tell her"],
 ko=["Keller의 수상 도서에 대한 영감은","옛 설화였다","그녀의 할머니가 그녀에게 이야기해 주던"],
 nodes=[dict(id="m",a=0,b=18,own=R(0,10),kids=[[10,18]],S=[1],V=[6],G=[[6]],form=2,fl=R(2,6),
   sk=[dict(r="S",g=[0,1]),dict(r="V",g=[6]),dict(r="C",g=[7,8,9])],
   note="Keller’s inspiration was an old folktale. 주어 + 동사 + 보어, 2형식입니다. inspiration = folktale(영감 = 옛 설화)이에요. for her award-winning book은 inspiration을 꾸미는 전치사구이고, that절은 folktale을 꾸밉니다."),
  dict(id="a",a=10,b=18,own=R(10,18),kids=[],S=[12],V=[14,15,16],G=[[14,15,16]],kind="형용사절",sub="목적격 관계대명사",anc=[9],np=[7,8,9],
   note="her halmoni used to tell her ___ 에서 tell의 목적어(이야기해 주던 '것' = folktale)가 비어 있어서 that은 목적격 관계대명사입니다. that 뒤에 주어(her halmoni)가 바로 나오는 것도 단서예요. used to tell은 '~하곤 했다'는 뜻의 한 덩어리 동사입니다.")],
 dec={"0":"Keller’s는 '켈러의'라는 소유격 명사입니다.","1":"inspiration은 '영감'이라는 명사입니다.","2":"for는 전치사입니다.","3":"her는 '그녀의'라는 소유격 대명사입니다.","4":"award-winning은 book을 꾸미는 형용사('상을 받은')입니다.","5":"book은 '책'이라는 명사입니다.","7":"an은 관사입니다.","8":"old는 형용사입니다.","9":"folktale은 '옛 설화'라는 명사입니다.","10":"that은 관계대명사입니다.","11":"her는 '그녀의'라는 소유격 대명사입니다.","12":"halmoni는 '할머니'라는 명사이고, 관계절의 주어예요.","13":"(grandmother)는 halmoni를 풀어 쓴 말(명사)입니다.","17":"her는 '그녀에게'라는 대명사(간접목적어)입니다."},
 vn="was는 주절의 동사, used to tell은 that절 안의 한 덩어리 동사예요. 그래서 used, to, tell을 모두 눌러요.",why=None,
 nf=[],em=[])

# ---- 1-7
t=tk("Keller wanted to revive the public’s interest in tigers by writing her own book"); assert len(t)==14
add(lv="심화",id="1-7",tok=t,
 ch=["Keller wanted to revive","the public’s interest in tigers","by writing her own book"],
 ko=["Keller는 되살리고 싶어 했다","호랑이에 대한 대중의 흥미를","그녀 자신의 책을 씀으로써"],
 nodes=[dict(id="m",a=0,b=14,own=R(0,14),kids=[],S=[0],V=[1],G=[[1]],form=3,fl=R(9,14),
   sk=[dict(r="S",g=[0]),dict(r="V",g=[1]),dict(r="O",g=R(2,9))],
   note="Keller wanted to revive the public’s interest. 주어 + 동사 + 목적어, 3형식입니다. wanted의 목적어는 to부정사구(to revive ~)예요. by writing her own book은 수단을 덧붙이는 전치사구(수식어)입니다.")],
 dec={"2":"to revive의 to예요. to부정사의 일부라서 동사가 아닙니다.","3":"revive는 to revive(되살리는 것)라는 to부정사라서 동사가 아닙니다.","4":"the는 관사입니다.","5":"public’s는 '대중의'라는 소유격 명사입니다.","6":"interest는 '흥미'라는 명사입니다.","7":"in은 전치사입니다.","8":"tigers는 '호랑이들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","9":"by는 전치사입니다.","10":"writing은 전치사 by 뒤의 동명사라서 동사가 아닙니다.","11":"her는 '그녀의'라는 소유격 대명사입니다.","12":"own은 '자신의'라는 형용사입니다.","13":"book은 '책'이라는 명사입니다."},
 vn="wanted가 문장의 동사예요. to revive(to부정사)와 writing(동명사)은 동사처럼 보여도 준동사라서 동사로 누르지 않아요.",why=None,
 nf=[dict(w="to revive",t="to",use="명사적 용법",reason="wanted의 목적어 자리에 들어가 '되살리는 것을'이라는 명사 역할을 하므로 명사적 용법입니다.",g=[2,3]),
     dict(w="writing",t="ger",reason="전치사 by 뒤의 -ing는 동명사입니다. by writing은 '쓰는 것에 의해', 즉 '씀으로써'예요.",g=[10])],em=[])

# ---- 2-10
t=tk("For example, in one story, a tiger helps a human become rich after the human saves the tiger’s life"); assert len(t)==19
add(lv="심화",id="2-10",tok=t,
 ch=["For example, in one story,","a tiger helps a human become rich","after the human saves the tiger’s life"],
 ko=["예를 들어 한 이야기에서","호랑이는 한 인간이 부유해지도록 돕는다","그 인간이 그 호랑이의 생명을 구해 준 이후"],
 nodes=[dict(id="m",a=0,b=19,own=R(0,12),kids=[[12,19]],S=[6],V=[7],G=[[7]],form=5,fl=R(0,5),
   sk=[dict(r="S",g=[5,6]),dict(r="V",g=[7]),dict(r="O",g=[8,9]),dict(r="C",g=[10,11])],
   note="a tiger helps a human become rich. 주어 + 동사 + 목적어 + 목적격보어, 5형식입니다. help + 목적어 + 동사원형은 '~가 …하도록 돕다'이고, a human = become rich(한 인간이 부유해지다) 관계예요. For example, in one story는 문장 앞에 덧붙는 말입니다."),
  dict(id="a",a=12,b=19,own=R(12,19),kids=[],S=[14],V=[15],G=[[15]],kind="부사절",sub="시간",
   note="after가 이끄는 시간의 부사절('~한 이후')입니다. 이 절 안에서 the human이 주어, saves가 동사, the tiger’s life가 목적어예요.")],
 dec={"0":"For는 전치사입니다.","1":"example은 '예'라는 명사입니다.","2":"in은 전치사입니다.","3":"one은 '한'이라는 형용사입니다.","4":"story는 '이야기'라는 명사입니다.","5":"a는 관사입니다.","6":"tiger는 주어인 명사예요.","8":"a는 관사입니다.","9":"human은 '인간'이라는 명사로, helps의 목적어예요.","10":"become은 help의 목적격보어 자리에 쓰인 동사원형이에요. 문장의 동사가 아닙니다.","11":"rich는 형용사입니다.","12":"after는 접속사입니다.","13":"the는 관사입니다.","14":"human은 after절의 주어(명사)입니다.","16":"the는 관사입니다.","17":"tiger’s는 '호랑이의'라는 소유격 명사입니다.","18":"life는 '생명'이라는 명사입니다."},
 vn="helps가 주절의 동사, saves가 after절의 동사예요. become은 help 뒤 목적격보어 자리의 원형부정사라서 동사로 누르지 않아요.",
 why="help + 목적어 + 동사원형 = 5형식\nhelps a human become rich는 '한 인간이 부유해지도록 돕다'. become rich가 목적격보어이고, 문장의 동사는 helps 하나",
 nf=[],em=[])

# ---- 3-5
t=tk("However, they were also scared of tigers because being injured or even killed by tigers was common in the past"); assert len(t)==20
add(lv="심화",id="3-5",tok=t,
 ch=["However, they were also scared of tigers","because being injured or even killed by tigers","was common in the past"],
 ko=["그러나 그들은 호랑이를 무서워하기도 했다","호랑이에게 상처를 입거나 심지어 죽임을 당하는 일이","과거에는 흔했기 때문에"],
 nodes=[dict(id="m",a=0,b=20,own=R(0,7),kids=[[7,20]],S=[1],V=[2],G=[[2]],form=2,fl=[0,5,6],
   sk=[dict(r="S",g=[1]),dict(r="V",g=[2]),dict(r="C",g=[3,4])],
   note="they were also scared. 주어 + 동사 + 보어, 2형식입니다. scared는 '무서워하는 상태'를 나타내는 형용사(보어)예요. However와 of tigers는 덧붙는 말이고, because절은 이유를 더해 줍니다."),
  dict(id="a",a=7,b=20,own=R(7,20),kids=[],S=[8,9,12],V=[15],G=[[15]],kind="부사절",sub="이유",
   note="because가 이끄는 이유의 부사절('~하기 때문에')입니다. being injured or even killed by tigers 전체가 이 절의 주어(동명사구)이고, 동사는 was예요.")],
 dec={"0":"However는 '그러나'라는 부사입니다.","3":"also는 '~도'라는 부사입니다.","4":"scared는 '무서워하는'이라는 형용사(보어)라서 문장의 동사가 아닙니다.","5":"of는 전치사입니다.","6":"tigers는 '호랑이들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","7":"because는 접속사입니다.","8":"being은 injured or killed와 함께 절의 주어가 되는 동명사라서 동사가 아닙니다.","9":"injured는 being 뒤의 과거분사(수동)라서 동사가 아닙니다.","10":"or는 접속사입니다.","11":"even은 부사입니다.","12":"killed는 being 뒤의 과거분사(수동)라서 동사가 아닙니다.","13":"by는 전치사입니다.","14":"tigers는 '호랑이들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","16":"common은 형용사(보어)입니다.","17":"in은 전치사입니다.","19":"past는 '과거'라는 명사입니다."},
 vn="주절의 were와 because절의 was, 모두 2개예요. being, injured, killed는 동사처럼 보여도 동사가 아니에요.",why=None,
 nf=[dict(w="being",t="ger",reason="being injured or even killed by tigers 전체가 because절의 주어 역할을 하는 동명사구예요. '호랑이에게 상처를 입거나 죽임을 당하는 일'이라는 뜻입니다.",g=[8])],em=[])

# ---- 4-2
t=tk("One verse of the song is a reinterpreted version of “Sugungga,” which is a traditional Korean song"); assert len(t)==17
add(lv="심화",id="4-2",tok=t,
 ch=["One verse of the song","is a reinterpreted version of “Sugungga,”","which is a traditional Korean song"],
 ko=["이 노래의 한 구절(가사)은","‘수궁가’의 재해석판이다","한국의 전통 가곡인"],
 nodes=[dict(id="m",a=0,b=17,own=R(0,11),kids=[[11,17]],S=[1],V=[5],G=[[5]],form=2,fl=[2,3,4,9,10],
   sk=[dict(r="S",g=[0,1]),dict(r="V",g=[5]),dict(r="C",g=[6,7,8])],
   note="One verse is a reinterpreted version. 주어 + 동사 + 보어, 2형식입니다. verse = version(한 구절 = 재해석판)이에요. of the song과 of “Sugungga,”는 앞 명사를 꾸미는 전치사구입니다."),
  dict(id="a",a=11,b=17,own=R(11,17),kids=[],S=[11],V=[12],G=[[12]],kind="형용사절",sub="주격 관계대명사",anc=[10],np=[10],
   note="쉼표 뒤 which는 앞의 “Sugungga”를 받는 계속적 용법입니다. ___ is a traditional Korean song 에서 주어 자리가 비어 있어서 which는 주격 관계대명사예요. '그리고 그것은 ~' 순서로 이어서 해석합니다.")],
 dec={"0":"One은 '하나의'라는 뜻의 한정사입니다.","1":"verse는 '구절'이라는 명사입니다.","2":"of는 전치사입니다.","3":"the는 관사입니다.","4":"song은 '노래'라는 명사입니다.","6":"a는 관사입니다.","7":"reinterpreted는 version을 꾸미는 과거분사라서 문장의 동사가 아닙니다.","8":"version은 '판, 버전'이라는 명사입니다.","9":"of는 전치사입니다.","10":"“Sugungga,”는 노래 이름(고유명사)입니다.","11":"which는 관계대명사입니다.","13":"a는 관사입니다.","14":"traditional은 형용사입니다.","15":"Korean은 형용사입니다.","16":"song은 '노래'라는 명사입니다."},
 vn="주절의 is와 which절의 is, 모두 2개예요.",why=None,
 nf=[dict(w="reinterpreted",t="part",who="version",base="reinterpret",ing="reinterpreting",pp="reinterpreted",ans="pp",reason="version은 '다시 해석된' 수동 관계입니다. 그래서 과거분사 reinterpreted예요.",g=[7])],em=[])

# ---- 4-6
t=tk("Who can deny that the tiger is a symbol of Korea"); assert len(t)==11
add(lv="심화",id="4-6",tok=t,
 ch=["Who can deny","that the tiger is a symbol of Korea"],
 ko=["누가 부정할 수 있을까","호랑이가 한국의 상징이라는 점을"],
 nodes=[dict(id="m",a=0,b=11,own=R(0,3),kids=[[3,11]],S=[0],V=[1,2],G=[[1,2]],form=3,fl=[],
   sk=[dict(r="S",g=[0]),dict(r="V",g=[1,2])],
   note="Who can deny that 절. 주어 + 동사 + 목적어, 3형식입니다. 의문사 Who가 주어 자리에 있고, can deny는 조동사 + 동사로 한 덩어리 동사예요. that 이하 전체가 deny의 목적어 자리를 채웁니다."),
  dict(id="a",a=3,b=11,own=R(3,11),kids=[],S=[5],V=[6],G=[[6]],kind="명사절",sub="목적어",gv=[["deny","동사"]],
   note="이 that은 관계사가 아니라 deny의 목적어 절을 이끄는 접속사입니다. 뒤에 주어(the tiger)와 동사(is), 보어(a symbol of Korea)가 완전하게 있어요.")],
 dec={"0":"Who는 '누가'라는 의문사(주어)입니다.","3":"that은 접속사입니다.","4":"the는 관사입니다.","5":"tiger는 that절의 주어(명사)입니다.","7":"a는 관사입니다.","8":"symbol은 '상징'이라는 명사입니다.","9":"of는 전치사입니다.","10":"Korea는 '한국'이라는 고유명사입니다."},
 vn="can deny는 조동사 + 동사로 한 덩어리 동사예요. 그래서 can과 deny를 모두 눌러요. that절 안의 동사는 is입니다.",why=None,
 nf=[],em=[])

# sanity: node own/kids consistency
for s in S:
    n=len(s["tok"])
    for nd in s["nodes"]:
        assert all(0<=i<n for i in nd["own"]+nd["S"]+nd["V"]),(s["id"],nd["id"])
        for g in nd["G"]: assert all(i in nd["V"] for i in g),(s["id"],g)
    cov=set()
    for nd in s["nodes"]: cov|=set(nd["own"])
    assert cov>=set(range(n)) or True
    miss=set(range(n))-cov
    assert not miss,(s["id"],sorted(miss))
    ids=[tuple(g) for nd in s["nodes"] for g in nd["G"]]

t=open(SRC,encoding="utf8").read()
t=re.sub(r"const S=\[.*?\];\n","const S="+json.dumps(S,ensure_ascii=False).replace("\\","\\\\")+";\n",t,count=1,flags=re.S)
t=t.replace('const KEY="vsignalY_clause_v3";','const KEY="vsig-tb-g1cs-l3-y-xray-v1";').replace("vsig-y-wl-v1","vsig-tb-g1cs-l3-wl-v1")
t=t.replace("const STARS=new Set([","const STARS=new Set([].concat([")
t=re.sub(r"const STARS=new Set\(\[\]\.concat\(\[.*?\]\);","const STARS=new Set([]);",t,count=1,flags=re.S)
t=t.replace("let TAB=location.hash=='#adv'?'심화':'기본';","let TAB='심화';")
t=t.replace("'<h1>'+TAB+' 문장 분석</h1>","'<h1>3과 핵심 7문장 · H-S코스</h1>")
t=re.sub(r"<title>.*?</title>","<title>청석고1 3과 핵심 7문장 · H-S코스</title>",t,count=1)
os.makedirs(OUT_DIR,exist_ok=True)
# remove old day clone
for f in ("index.html","note.html"):
    p=OUT_DIR+f
def deb(x):
    x=x.replace('<a href="./" style="color:var(--ac);text-decoration:none;padding:6px 0">&larr; Y단계 홈','<a href="../" style="color:var(--ac);text-decoration:none;padding:6px 0">&larr; 3과 코스 선택')
    x=x.replace('<a class="hm" href="./">&larr; Y단계 홈','<a class="hm" href="../">&larr; 3과 코스 선택')
    return x.replace("V시그널 Y단계 - 오답노트","오답노트")
t=deb(t)
open(OUT_DIR+"index.html","w",encoding="utf8").write(t)
n=open("/home/claude/via/vsignal-y/note.html",encoding="utf8").read().replace("vsig-y-wl-v1","vsig-tb-g1cs-l3-wl-v1")
open(OUT_DIR+"note.html","w",encoding="utf8").write(deb(n))
open(OUT_DIR+"words.html","w",encoding="utf8").write(deb(open("/home/claude/via/vsignal-y/words.html",encoding="utf8").read()))
print("ok",len(t))
