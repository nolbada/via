import json,re,os
SRC="/home/claude/via/vsignal-y/xray.html"
OUT_DIR="/home/claude/via/textbook/g1-geumcheon-mirae/l4/y/"
R=lambda a,b:list(range(a,b))
def tk(s): return s.split(" ")
S=[]
def add(**k): S.append(k)

# ---- 1-2
t=tk("Traditionally, researchers have studied various functions of neural implants, which are medical devices like computer chips that can be implanted in the nervous system."); assert len(t)==24
add(lv="심화",id="1-2",tok=t,
 ch=["Traditionally, researchers have studied various functions of neural implants,","which are medical devices like computer chips","that can be implanted in the nervous system."],
 ko=["전통적으로 연구자들은 신경 임플란트의 다양한 기능을 연구해 왔다","그것(=신경 임플란트)은 컴퓨터 칩과 같은 의료 기기이다","신경계에 이식될 수 있는"],
 nodes=[dict(id="m",a=0,b=24,own=R(0,9),kids=[[9,24]],S=[1],V=[2,3],G=[[2,3]],form=3,fl=[0],
   sk=[dict(r="S",g=[1]),dict(r="V",g=[2,3]),dict(r="O",g=R(4,9))],
   note="researchers have studied various functions. 주어 + 동사 + 목적어, 3형식입니다. have studied는 현재완료(have + p.p.)로 한 덩어리 동사예요. Traditionally는 방식을 덧붙이는 말입니다."),
  dict(id="a",a=9,b=24,own=R(9,16),kids=[[16,24]],S=[9],V=[10],G=[[10]],kind="형용사절",sub="주격 관계대명사",anc=[8],np=[7,8],
   note="콤마 뒤 which는 앞의 neural implants를 받는 계속적 용법입니다. ___ are medical devices 에서 주어 자리가 비어 있어서 which는 주격 관계대명사예요. '그리고 그것은 ~' 순서로 이어서 해석합니다."),
  dict(id="b",a=16,b=24,own=R(16,24),kids=[],S=[16],V=[17,18,19],G=[[17,18,19]],kind="형용사절",sub="주격 관계대명사",anc=[15],np=[14,15],
   note="___ can be implanted 에서 주어 자리(= computer chips)가 비어 있어서 that은 주격 관계대명사입니다. can be implanted는 조동사 + be + 과거분사(수동)로 한 덩어리 동사예요.")],
 dec={"0":"Traditionally는 방식을 나타내는 부사입니다.","4":"various는 형용사입니다.","5":"functions는 '기능들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","6":"of는 전치사입니다.","7":"neural은 implants를 꾸미는 형용사입니다.","11":"medical은 형용사입니다.","13":"like는 '~와 같은'이라는 전치사라서 동사가 아닙니다.","14":"computer는 chips를 꾸미는 명사입니다.","20":"in은 전치사입니다.","22":"nervous는 형용사입니다."},
 vn="have studied는 현재완료(have + p.p.)라서 have와 studied를 함께 눌러요. which절의 are, that절의 can be implanted(조동사 + be + p.p.)도 모두 동사입니다.",why=None,
 nf=[],em=[])

# ---- 2-7
t=tk("Similarly, those who have lost their arms can use artificial arms operated by the same mechanism."); assert len(t)==16
add(lv="심화",id="2-7",tok=t,
 ch=["Similarly, those who have lost their arms","can use artificial arms","operated by the same mechanism."],
 ko=["마찬가지로 팔을 잃은 사람들은","의수를 사용할 수 있다","동일한 메커니즘으로 작동하는"],
 nodes=[dict(id="m",a=0,b=16,own=[0,1]+R(7,16),kids=[[2,7]],S=[1],V=[7,8],G=[[7,8]],form=3,fl=[0]+R(11,16),
   sk=[dict(r="S",g=[1]),dict(r="V",g=[7,8]),dict(r="O",g=[9,10])],
   note="those can use artificial arms. 주어 + 동사 + 목적어, 3형식입니다. can use는 조동사 + 동사로 한 덩어리 동사예요. who절은 those를 꾸미고, operated by the same mechanism은 artificial arms를 꾸밉니다."),
  dict(id="a",a=2,b=7,own=R(2,7),kids=[],S=[2],V=[3,4],G=[[3,4]],kind="형용사절",sub="주격 관계대명사",anc=[1],np=[1],
   note="___ have lost their arms 에서 주어 자리(= those)가 비어 있어서 who는 주격 관계대명사입니다. those who ~ 는 '~하는 사람들'이라는 뜻이고, have lost는 현재완료(have + p.p.)예요.")],
 dec={"0":"Similarly는 '마찬가지로'라는 부사입니다.","5":"their는 '그들의'라는 대명사입니다.","6":"arms는 '팔'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","9":"artificial은 형용사입니다.","10":"arms는 '의수(팔)'라는 명사로, can use의 목적어예요.","11":"operated는 artificial arms를 뒤에서 꾸미는 과거분사라서 문장의 동사가 아닙니다.","12":"by는 전치사입니다.","14":"same은 형용사입니다."},
 vn="can use는 조동사 + 동사로 한 덩어리 동사예요. who절 안의 have lost는 현재완료(have + p.p.)라서 둘 다 눌러요.",why=None,
 nf=[dict(w="operated",t="part",who="arms",base="operate",ing="operating",pp="operated",ans="pp",reason="artificial arms는 '작동되는' 수동 관계입니다. 그래서 과거분사 operated예요.",g=[11])],em=[])

# ---- 3-2
t=tk("Some futurists predict that these implants will become commercially available in the next 20 to 30 years and significantly change our daily lives."); assert len(t)==23
add(lv="심화",id="3-2",tok=t,
 ch=["Some futurists predict","that these implants will become commercially available in the next 20 to 30 years","and significantly change our daily lives."],
 ko=["일부 미래학자들은 예측한다","이러한 임플란트가 향후 20~30년 이내에 상용화될 것이라고","그리고 우리의 일상을 크게 변화시킬 것이라고"],
 nodes=[dict(id="m",a=0,b=23,own=R(0,3),kids=[[3,23]],S=[1],V=[2],G=[[2]],form=3,fl=[],
   sk=[dict(r="S",g=[0,1]),dict(r="V",g=[2])],
   note="Some futurists predict that 절. 주어 + 동사 + 목적어, 3형식입니다. that 이하 전체가 predict의 목적어 자리를 채웁니다."),
  dict(id="a",a=3,b=23,own=R(3,23),kids=[],S=[5],V=[6,7,19],G=[[6,7],[19]],kind="명사절",sub="목적어",gv=[["predict","동사"]],
   note="이 that은 관계사가 아니라 predict의 목적어 절을 이끄는 접속사입니다. 뒤에 주어(implants)와 동사(will become)가 완전하게 있어요. and 뒤의 (will) significantly change도 같은 주어의 동사이고, will은 change에도 걸립니다.")],
 dec={"0":"Some은 '일부의'라는 뜻의 한정사입니다.","3":"that은 접속사입니다.","4":"these는 '이러한'이라는 지시형용사입니다.","8":"commercially는 부사입니다.","9":"available은 형용사(보어)입니다.","10":"in은 전치사입니다.","13":"20은 숫자입니다.","14":"to는 '20에서 30'을 뜻하는 말(전치사)이라 to부정사가 아닙니다.","16":"years는 '년'이라는 명사예요.","18":"significantly는 부사입니다.","21":"daily는 '일상의'라는 형용사입니다.","22":"lives는 '삶, 일상'이라는 명사예요. -s가 붙었지만 동사가 아닙니다."},
 vn="predict는 주절의 동사예요. that절 안에는 will become과 change 두 동사가 and로 이어져 있어요.",why=None,
 nf=[],em=[])

# ---- 4-1
t=tk("Before we can fully embrace the era of AI-powered neural implants, many tricky ethical issues should be addressed."); assert len(t)==18
add(lv="심화",id="4-1",tok=t,
 ch=["Before we can fully embrace the era of AI-powered neural implants,","many tricky ethical issues should be addressed."],
 ko=["우리가 AI 기반 신경 임플란트 시대를 완전히 받아들이기 전에","여러 가지 까다로운 윤리적 문제들이 해결되어야 한다"],
 nodes=[dict(id="m",a=0,b=18,own=R(11,18),kids=[[0,11]],S=[14],V=[15,16,17],G=[[15,16,17]],form=1,fl=[],
   sk=[dict(r="S",g=[11,12,13,14]),dict(r="V",g=[15,16,17])],
   note="many tricky ethical issues should be addressed. 주어 + 동사, 1형식입니다. should be addressed는 조동사 + be + 과거분사(수동)로 한 덩어리 동사예요. '문제들이 해결되어야 한다'처럼 목적어 없이 끝납니다."),
  dict(id="a",a=0,b=11,own=R(0,11),kids=[],S=[1],V=[2,4],G=[[2,4]],bd=[3],kind="부사절",sub="시간",
   note="Before가 이끄는 시간의 부사절('~하기 전에')입니다. can fully embrace에서 fully는 동사 사이에 끼어든 부사예요.")],
 dec={"0":"Before는 접속사입니다.","3":"fully는 부사입니다.","6":"era는 '시대'라는 명사입니다.","7":"of는 전치사입니다.","8":"AI-powered는 implants를 꾸미는 형용사입니다.","10":"implants는 '임플란트들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","12":"tricky는 형용사입니다.","13":"ethical은 형용사입니다.","14":"issues는 '문제들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다."},
 vn="can fully embrace(조동사 + 동사)와 should be addressed(조동사 + be + p.p.)는 각각 한 덩어리 동사예요.",why=None,
 nf=[dict(w="AI-powered",t="part",who="implants",base="power",ing="powering",pp="powered",ans="pp",reason="implants는 AI에 의해 '작동되는' 수동 관계입니다. 그래서 과거분사 powered예요.",g=[8])],em=[])

# ---- 4-6
t=tk("There's a risk that organizations or hackers could access personal data without permission through AI-connected implants."); assert len(t)==16
add(lv="심화",id="4-6",tok=t,
 ch=["There's a risk","that organizations or hackers could access personal data","without permission through AI-connected implants."],
 ko=["위험이 있다","조직이나 해커가 개인 정보에 접근할 수 있다는","허가 없이 AI와 연결된 임플란트를 통해"],
 nodes=[dict(id="m",a=0,b=16,own=R(0,3),kids=[[3,16]],S=[2],V=[0],G=[[0]],form=1,fl=[],
   sk=[dict(r="S",g=[1,2]),dict(r="V",g=[0])],
   note="There's a risk. There is ~ 구문이라 '위험이 있다', 주어 + 동사의 1형식입니다. There는 해석하지 않고 자리만 채우며, 주어는 is 뒤의 a risk예요. that 이하는 risk의 내용을 설명합니다."),
  dict(id="a",a=3,b=16,own=R(3,16),kids=[],S=[4,6],V=[7,8],G=[[7,8]],kind="명사절",sub="동격",gv=[["risk","명사"]],
   note="risk 뒤의 that은 a risk의 내용을 설명하는 동격의 that입니다. that 뒤가 완전한 문장(주어 organizations or hackers, 동사 could access, 목적어 personal data)이라서 관계대명사가 아니에요.")],
 dec={"1":"a는 관사입니다.","3":"that은 접속사입니다.","5":"or는 접속사입니다.","9":"personal은 형용사입니다.","10":"data는 '자료, 정보'라는 명사입니다.","11":"without은 전치사입니다.","12":"permission은 명사입니다.","13":"through는 전치사입니다.","14":"AI-connected는 implants를 꾸미는 형용사입니다."},
 vn="There's는 There is예요. 동사는 is이고, There는 자리를 채우는 말입니다. 그래서 There's를 동사로 눌러요. could access(조동사 + 동사)도 한 덩어리 동사예요.",why=None,
 nf=[dict(w="AI-connected",t="part",who="implants",base="connect",ing="connecting",pp="connected",ans="pp",reason="implants는 AI와 '연결되는' 수동 관계입니다. 그래서 과거분사 connected예요.",g=[14])],em=[])

# ---- 4-7
t=tk("This means that our thoughts, emotions, and behaviors could be controlled by hackers."); assert len(t)==13
add(lv="심화",id="4-7",tok=t,
 ch=["This means","that our thoughts, emotions, and behaviors","could be controlled by hackers."],
 ko=["이것은 뜻한다","우리의 생각, 감정, 행동이","해커에 의해 통제될 수 있다는 것을"],
 nodes=[dict(id="m",a=0,b=13,own=R(0,2),kids=[[2,13]],S=[0],V=[1],G=[[1]],form=3,fl=[],
   sk=[dict(r="S",g=[0]),dict(r="V",g=[1])],
   note="This means that 절. 주어 + 동사 + 목적어, 3형식입니다. that 이하 전체가 means의 목적어 자리를 채웁니다."),
  dict(id="a",a=2,b=13,own=R(2,13),kids=[],S=[4,5,7],V=[8,9,10],G=[[8,9,10]],kind="명사절",sub="목적어",gv=[["means","동사"]],
   note="이 that은 관계사가 아니라 means의 목적어 절을 이끄는 접속사입니다. 뒤에 주어(thoughts, emotions, behaviors)와 동사(could be controlled)가 완전하게 있어요. could be controlled는 조동사 + be + 과거분사(수동)로 한 덩어리 동사입니다.")],
 dec={"2":"that은 접속사입니다.","3":"our는 '우리의'라는 대명사입니다.","4":"thoughts는 '생각들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","5":"emotions는 '감정들'이라는 명사입니다.","6":"and는 접속사입니다.","7":"behaviors는 '행동들'이라는 명사입니다.","11":"by는 전치사입니다.","12":"hackers는 '해커들'이라는 명사입니다."},
 vn="means는 주절의 동사, could be controlled는 that절 안의 한 덩어리 동사예요.",why=None,
 nf=[],em=[])

# ---- 5-9
t=tk("I'm really worried about the privacy issues it might cause."); assert len(t)==10
add(lv="심화",id="5-9",tok=t,
 ch=["I'm really worried","about the privacy issues","it might cause."],
 ko=["나는 정말 걱정된다","프라이버시 문제에 대해","그것이 초래할 수 있는"],
 nodes=[dict(id="m",a=0,b=10,own=R(0,7),kids=[[7,10]],S=[0],V=[0],G=[[0]],form=2,fl=R(3,7),
   sk=[dict(r="S",g=[0]),dict(r="V",g=[0]),dict(r="C",g=[1,2])],
   note="I'm really worried. 주어 + 동사 + 보어, 2형식입니다. I'm은 I am이고, I = worried(나 = 걱정되는 상태)예요. about the privacy issues는 걱정되는 대상을 덧붙이는 말입니다."),
  dict(id="a",a=7,b=10,own=R(7,10),kids=[],S=[7],V=[8,9],G=[[8,9]],kind="형용사절",sub="목적격 관계대명사",anc=[6],np=[4,5,6],
   note="the privacy issues (that) it might cause ___ 에서 cause의 목적어(= issues)가 비어 있어서, 생략된 that은 목적격 관계대명사입니다. 명사 뒤에 '주어 + 동사'가 바로 붙어 있으면 관계대명사 생략을 의심하세요.")],
 dec={"1":"really는 부사입니다.","2":"worried는 상태를 나타내는 형용사(보어)라서 문장의 동사가 아닙니다.","3":"about은 전치사입니다.","5":"privacy는 issues를 꾸미는 명사입니다.","6":"issues는 '문제들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다."},
 vn="I'm은 I am이에요. 주어(I)와 동사(am)가 한 단어에 붙어 있어서 같은 단어를 주어이자 동사로 눌러요. might cause(조동사 + 동사)는 한 덩어리 동사입니다.",why=None,
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
t=t.replace('const KEY="vsignalY_clause_v3";','const KEY="vsig-tb-g1gc-l4-y-xray-v1";').replace("vsig-y-wl-v1","vsig-tb-g1gc-l4-wl-v1")
t=t.replace("const STARS=new Set([","const STARS=new Set([].concat([")
t=re.sub(r"const STARS=new Set\(\[\]\.concat\(\[.*?\]\);","const STARS=new Set([]);",t,count=1,flags=re.S)
t=t.replace("let TAB=location.hash=='#adv'?'심화':'기본';","let TAB='심화';")
t=t.replace("'<h1>'+TAB+' 문장 분석</h1>","'<h1>4과 핵심 7문장 · H-S코스</h1>")
t=re.sub(r"<title>.*?</title>","<title>금천고1 4과 핵심 7문장 · H-S코스</title>",t,count=1)
os.makedirs(OUT_DIR,exist_ok=True)
# remove old day clone
for f in ("index.html","note.html"):
    p=OUT_DIR+f
open(OUT_DIR+"index.html","w",encoding="utf8").write(t)
n=open("/home/claude/via/vsignal-y/note.html",encoding="utf8").read().replace("vsig-y-wl-v1","vsig-tb-g1gc-l4-wl-v1")
open(OUT_DIR+"note.html","w",encoding="utf8").write(n)
print("ok",len(t))
