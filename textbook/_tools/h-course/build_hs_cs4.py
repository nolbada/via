import json,re,os
SRC="/home/claude/via/vsignal-y/xray.html"
OUT_DIR="/home/claude/via/textbook/g1-cheongseok-neungryul-min/l4/y/"
R=lambda a,b:list(range(a,b))
def tk(s): return s.split(" ")
S=[]
def add(**k): S.append(k)
# 청석고1 공통영어2 (NE능률 민병천) 4과 H-S코스. 영어 조각(ch)과 해석(ko)은 jwa.html(4과 좌본문우해석) 기준.
# 마지막 조각 끝에 마침표만 덧붙였다(jwa는 조각 표시라 마침표가 없음).

# ---- 2-6
t=tk("Often, plastic waste is moved to places where it is just dumped or burned."); assert len(t)==14
add(lv="심화",id="2-6",tok=t,
 ch=["Often, plastic waste is moved to places","where it is just dumped or burned."],
 ko=["종종 플라스틱 쓰레기는 장소들로 보내진다","그저 내버려지거나 태워지는"],
 nodes=[dict(id="m",a=0,b=14,own=R(0,7),kids=[[7,14]],S=[2],V=[3,4],G=[[3,4]],form=1,fl=[0,5,6],
   sk=[dict(r="S",g=[1,2]),dict(r="V",g=[3,4])],
   note="plastic waste is moved. 주어 + 동사, 1형식입니다. is moved는 be + p.p.(수동)로 한 덩어리 동사예요. '쓰레기가 보내진다'로 문장이 완성되고, to places는 보내지는 곳을 덧붙이는 말, Often은 빈도를 덧붙이는 부사입니다."),
  dict(id="a",a=7,b=14,own=R(7,14),kids=[],S=[8],V=[9,11,13],G=[[9,11],[13]],kind="형용사절",sub="관계부사",anc=[6],np=[6],
   note="where는 장소(places)를 꾸미는 관계부사입니다. 뒤의 it is just dumped or burned가 주어와 동사를 모두 갖춘 완전한 절이라서 관계대명사가 아니에요. is dumped(be + p.p.)와 (is) burned가 or로 이어진 두 동사입니다.")],
 dec={"0":"Often은 '종종'이라는 빈도 부사입니다.","1":"plastic은 waste를 꾸미는 명사입니다.","2":"waste는 '쓰레기'라는 명사입니다.","5":"to는 전치사입니다.","6":"places는 '장소들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","7":"where는 관계부사입니다.","8":"it은 대명사입니다.","10":"just는 부사입니다.","12":"or는 접속사입니다."},
 vn="is moved는 be + p.p.(수동)라서 is와 moved를 함께 눌러요. where절에서는 is dumped(be + p.p.)와 (is) burned가 or로 이어진 두 동사예요.",why=None,
 nf=[],em=[])

# ---- 3-2
t=tk("Although polluted soil can be dug up and transported to a landfill, this process is expensive."); assert len(t)==16
add(lv="심화",id="3-2",tok=t,
 ch=["Although polluted soil can be dug up","and transported to a landfill,","this process is expensive."],
 ko=["비록 오염된 흙이 파내져서","매립지로 옮겨질 수는 있지만","이 과정은 비용이 많이 든다"],
 nodes=[dict(id="m",a=0,b=16,own=R(12,16),kids=[[0,12]],S=[13],V=[14],G=[[14]],form=2,fl=[],
   sk=[dict(r="S",g=[12,13]),dict(r="V",g=[14]),dict(r="C",g=[15])],
   note="this process is expensive. 주어 + 동사 + 보어, 2형식입니다. this process = expensive(이 과정 = 비용이 많이 드는 상태)예요. is는 '~이다'라는 동사입니다."),
  dict(id="a",a=0,b=12,own=R(0,12),kids=[],S=[2],V=[3,4,5,6,8],G=[[3,4,5,6],[8]],kind="부사절",sub="양보",
   note="Although가 이끄는 양보의 부사절('비록 ~이지만')입니다. can be dug up(조동사 + be + p.p. + up)과 (can be) transported가 and로 이어진 두 동사이고, 둘 다 수동이에요.")],
 dec={"0":"Although는 접속사입니다.","1":"polluted는 soil을 꾸미는 과거분사('오염된')라서 동사가 아닙니다.","7":"and는 접속사입니다.","9":"to는 전치사입니다.","10":"a는 관사입니다.","11":"landfill은 '매립지'라는 명사입니다.","12":"this는 '이'라는 지시형용사입니다.","13":"process는 '과정'이라는 명사입니다.","15":"expensive는 상태를 나타내는 형용사(보어)라서 문장의 동사가 아닙니다."},
 vn="is expensive에서 is가 문장의 동사예요. Although절에서는 can be dug up(조동사 + be + p.p. + up)과 (can be) transported 두 동사가 and로 이어져 있어요.",why=None,
 nf=[dict(w="polluted",t="part",who="soil",base="pollute",ing="polluting",pp="polluted",ans="pp",reason="soil은 '오염된' 수동 관계입니다. 그래서 과거분사 polluted예요.",g=[1])],em=[])

# ---- 4-2
t=tk("The coffee-making process, however, generates used coffee grounds, which are normally sent to landfills."); assert len(t)==14
add(lv="심화",id="4-2",tok=t,
 ch=["The coffee-making process, however, generates used coffee grounds,","which are normally sent to landfills."],
 ko=["그러나 커피 만드는 과정은 사용된 커피 찌꺼기를 발생시킨다","보통 매립지로 보내지는"],
 nodes=[dict(id="m",a=0,b=14,own=R(0,8),kids=[[8,14]],S=[2],V=[4],G=[[4]],form=3,fl=[3],
   sk=[dict(r="S",g=[0,1,2]),dict(r="V",g=[4]),dict(r="O",g=[5,6,7])],
   note="The coffee-making process generates used coffee grounds. 주어 + 동사 + 목적어, 3형식입니다. however는 문장 중간에 끼어든 '그러나'로, 빼도 문장이 말이 돼서 덧붙이는 말이에요."),
  dict(id="a",a=8,b=14,own=R(8,14),kids=[],S=[8],V=[9,11],G=[[9,11]],kind="형용사절",sub="주격 관계대명사",anc=[7],np=[5,6,7],
   note="콤마 뒤 which는 앞의 used coffee grounds를 받는 계속적 용법입니다. ___ are normally sent 에서 주어 자리가 비어 있어서 which는 주격 관계대명사예요. '그리고 그것은 ~' 순서로 이어서 해석합니다. are normally sent는 be + p.p.(수동)로 한 덩어리 동사입니다.")],
 dec={"0":"The는 관사입니다.","1":"coffee-making은 '커피 만드는'이라는 뜻으로 process를 꾸미는 말이라 동사가 아닙니다.","2":"process는 '과정'이라는 명사입니다.","3":"however는 '그러나'라는 부사입니다.","5":"used는 grounds를 꾸미는 과거분사('사용된')라서 문장의 동사가 아닙니다.","6":"coffee는 grounds를 꾸미는 명사입니다.","7":"grounds는 '찌꺼기'라는 명사예요. -s가 붙었지만 동사가 아닙니다.","10":"normally는 부사입니다.","12":"to는 전치사입니다.","13":"landfills는 '매립지들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다."},
 vn="주절의 동사는 generates예요. which절의 are normally sent는 be + p.p.(수동)라서 are와 sent를 함께 눌러요.",why=None,
 nf=[dict(w="used",t="part",who="grounds",base="use",ing="using",pp="used",ans="pp",reason="coffee grounds는 '사용된' 수동 관계입니다. 그래서 과거분사 used예요.",g=[5])],em=[])

# ---- 4-6
t=tk("Biofuel is a natural fuel that is made from plant or animal sources."); assert len(t)==13
add(lv="심화",id="4-6",tok=t,
 ch=["Biofuel is a natural fuel","that is made from plant or animal sources."],
 ko=["바이오 연료는 천연 연료이다","식물이나 동물성 원료로 만들어진"],
 nodes=[dict(id="m",a=0,b=13,own=R(0,5),kids=[[5,13]],S=[0],V=[1],G=[[1]],form=2,fl=[],
   sk=[dict(r="S",g=[0]),dict(r="V",g=[1]),dict(r="C",g=[2,3,4])],
   note="Biofuel is a natural fuel. 주어 + 동사 + 보어, 2형식입니다. Biofuel = a natural fuel(바이오 연료 = 천연 연료)이고, is는 '~이다'라는 동사예요."),
  dict(id="a",a=5,b=13,own=R(5,13),kids=[],S=[5],V=[6,7],G=[[6,7]],kind="형용사절",sub="주격 관계대명사",anc=[4],np=[2,3,4],
   note="___ is made from plant or animal sources 에서 주어 자리(= fuel)가 비어 있어서 that은 주격 관계대명사입니다. is made는 be + p.p.(수동)로 한 덩어리 동사예요.")],
 dec={"0":"Biofuel은 '바이오 연료'라는 명사입니다.","2":"a는 관사입니다.","3":"natural은 fuel을 꾸미는 형용사입니다.","4":"fuel은 '연료'라는 명사입니다.","8":"from은 전치사입니다.","9":"plant는 sources를 꾸미는 명사입니다.","10":"or는 접속사입니다.","11":"animal은 sources를 꾸미는 명사입니다.","12":"sources는 '원료들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다."},
 vn="주절의 동사는 is예요. that절의 is made는 be + p.p.(수동)라서 is와 made를 함께 눌러요.",why=None,
 nf=[],em=[])

# ---- 4-7
t=tk("Researchers have found that they can grow algae on old coffee grounds without adding any other nutrients."); assert len(t)==17
add(lv="심화",id="4-7",tok=t,
 ch=["Researchers have found","that they can grow algae on old coffee grounds","without adding any other nutrients."],
 ko=["연구자들은 알아냈다","그들이 오래된 커피 찌꺼기에서 조류를 자라게 할 수 있다는 것을","어떤 다른 영양분도 더하지 않고"],
 nodes=[dict(id="m",a=0,b=17,own=R(0,3),kids=[[3,17]],S=[0],V=[1,2],G=[[1,2]],form=3,fl=[],
   sk=[dict(r="S",g=[0]),dict(r="V",g=[1,2])],
   note="Researchers have found that 절. 주어 + 동사 + 목적어, 3형식입니다. have found는 현재완료(have + p.p.)로 한 덩어리 동사예요. that 이하 전체가 found의 목적어 자리를 채웁니다."),
  dict(id="a",a=3,b=17,own=R(3,17),kids=[],S=[4],V=[5,6],G=[[5,6]],kind="명사절",sub="목적어",gv=[["found","동사"]],
   note="이 that은 관계사가 아니라 found의 목적어 절을 이끄는 접속사입니다. 뒤에 주어(they)와 동사(can grow), 목적어(algae)가 완전하게 있어요. without adding any other nutrients는 can grow를 꾸미는 말이고, without 뒤의 adding은 동명사입니다.")],
 dec={"0":"Researchers는 '연구자들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","3":"that은 접속사입니다.","4":"they는 대명사입니다.","7":"algae는 '조류'라는 명사입니다.","8":"on은 전치사입니다.","9":"old는 형용사입니다.","10":"coffee는 grounds를 꾸미는 명사입니다.","11":"grounds는 '찌꺼기'라는 명사예요. -s가 붙었지만 동사가 아닙니다.","12":"without은 전치사입니다.","13":"adding은 전치사 without 뒤의 동명사('더하는 것')라서 문장의 동사가 아닙니다.","14":"any는 형용사입니다.","15":"other는 형용사입니다.","16":"nutrients는 '영양분들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다."},
 vn="have found는 현재완료(have + p.p.)라서 have와 found를 함께 눌러요. that절 안에는 can grow가 동사예요. adding은 동명사라서 동사가 아닙니다.",why=None,
 nf=[dict(w="adding",t="ger",reason="전치사 without 뒤에는 -ing가 옵니다. adding은 동명사('더하는 것')예요.",g=[13])],em=[])

# ---- 4-11
t=tk("There could be many more possible solutions to the problems we currently face."); assert len(t)==13
add(lv="심화",id="4-11",tok=t,
 ch=["There could be many more possible solutions","to the problems we currently face."],
 ko=["훨씬 더 많은 가능성 있는 해결책들이 있을 수 있다","우리가 현재 직면한 문제들에 대한"],
 nodes=[dict(id="m",a=0,b=13,own=R(0,10),kids=[[10,13]],S=[6],V=[1,2],G=[[1,2]],form=1,fl=[7,8,9],
   sk=[dict(r="S",g=[3,4,5,6]),dict(r="V",g=[1,2])],
   note="There could be many more possible solutions. There is ~ 구문이라 '있을 수 있다', 주어 + 동사의 1형식입니다. There는 해석하지 않고 자리만 채우며, 주어는 be 뒤의 many more possible solutions예요. could be는 조동사 + be로 한 덩어리 동사입니다."),
  dict(id="a",a=10,b=13,own=R(10,13),kids=[],S=[10],V=[12],G=[[12]],kind="형용사절",sub="목적격 관계대명사",anc=[9],np=[8,9],
   note="the problems (that) we currently face ___ 에서 face의 목적어(= problems)가 비어 있어서, 생략된 that은 목적격 관계대명사입니다. 명사 뒤에 '주어 + 동사'가 바로 붙어 있으면 관계대명사 생략을 의심하세요.")],
 dec={"0":"There는 '거기에'가 아니라 자리를 채우는 말이라 동사가 아닙니다. 동사는 뒤의 could be예요.","3":"many는 '많은'이라는 형용사입니다.","4":"more는 '더'를 뜻하는 말로 many를 꾸밉니다.","5":"possible은 형용사입니다.","6":"solutions는 '해결책들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","7":"to는 전치사입니다.","8":"the는 관사입니다.","9":"problems는 '문제들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","11":"currently는 부사입니다."},
 vn="There는 자리를 채우는 말이에요. 동사는 could be(조동사 + be)이고 한 덩어리라서 함께 눌러요. 관계절 안의 동사는 face입니다.",why=None,
 nf=[],em=[])

# ---- 3-10
t=tk("Therefore, this promising area should be further explored to find out which trees are the most effective."); assert len(t)==17
add(lv="심화",id="3-10",tok=t,
 ch=["Therefore, this promising area should be further explored","to find out which trees are the most effective."],
 ko=["그러므로 이 촉망받는 분야는 더 깊게 탐구되어야 한다","어떤 나무들이 가장 효과적인지 찾아내기 위해"],
 nodes=[dict(id="m",a=0,b=17,own=R(0,11),kids=[[11,17]],S=[3],V=[4,5,7],G=[[4,5,7]],form=1,fl=[0,8,9,10],
   sk=[dict(r="S",g=[1,2,3]),dict(r="V",g=[4,5,7])],
   note="this promising area should be further explored. 주어 + 동사, 1형식입니다. should be explored는 조동사 + be + p.p.(수동)로 한 덩어리 동사이고, 사이의 further는 부사예요. '분야가 탐구되어야 한다'로 끝나고, to find out ~ 은 목적을 덧붙이는 말입니다."),
  dict(id="a",a=11,b=17,own=R(11,17),kids=[],S=[12],V=[13],G=[[13]],kind="명사절",sub="목적어",gv=[["find out","동사"]],
   note="which trees are the most effective는 find out의 목적어 절입니다('어떤 나무들이 가장 효과적인지'). which는 trees를 꾸미는 의문형용사이고, 뒤에 주어(trees)와 동사(are), 보어(the most effective)가 갖춰져 있어요.")],
 dec={"0":"Therefore는 '그러므로'라는 접속부사입니다.","1":"this는 '이'라는 지시형용사입니다.","2":"promising은 area를 꾸미는 형용사('촉망받는')라서 동사가 아닙니다.","3":"area는 '분야'라는 명사입니다.","6":"further는 '더 깊게'라는 부사입니다.","8":"to는 to부정사를 만드는 말이라 문장의 동사가 아닙니다.","9":"find out은 to부정사 안의 동사라서 문장의 동사가 아닙니다.","10":"out은 find와 함께 쓰이는 말입니다.","11":"which는 trees를 꾸미는 의문형용사('어떤')입니다.","12":"trees는 '나무들'이라는 명사예요. -s가 붙었지만 동사가 아닙니다.","14":"the는 관사입니다.","15":"most는 '가장'을 뜻하는 부사입니다.","16":"effective는 상태를 나타내는 형용사(보어)라서 문장의 동사가 아닙니다."},
 vn="should be further explored는 조동사 + be + p.p.(수동)이고 사이에 부사 further가 끼어 있어도 한 덩어리 동사예요. to find out은 to부정사라서 동사가 아닙니다. 명사절 안의 동사는 are예요.",why=None,
 nf=[dict(w="to find out",t="to",use="부사적 용법",reason="to find out ~ 은 '~을 찾아내기 위해'라는 목적을 나타내서 동사 should be explored를 꾸미는 부사적 용법입니다.",g=[8,9,10])],em=[])

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
t=t.replace('const KEY="vsignalY_clause_v3";','const KEY="vsig-tb-g1cs-l4-y-xray-v1";').replace("vsig-y-wl-v1","vsig-tb-g1cs-l4-wl-v1")
t=t.replace("const STARS=new Set([","const STARS=new Set([].concat([")
t=re.sub(r"const STARS=new Set\(\[\]\.concat\(\[.*?\]\);","const STARS=new Set([]);",t,count=1,flags=re.S)
t=t.replace("let TAB=location.hash=='#adv'?'심화':'기본';","let TAB='심화';")
t=t.replace("'<h1>'+TAB+' 문장 분석</h1>","'<h1>4과 핵심 7문장 · H-S코스</h1>")
t=re.sub(r"<title>.*?</title>","<title>청석고1 4과 핵심 7문장 · H-S코스</title>",t,count=1)
os.makedirs(OUT_DIR,exist_ok=True)
# remove old day clone
for f in ("index.html","note.html"):
    p=OUT_DIR+f
open(OUT_DIR+"index.html","w",encoding="utf8").write(t)
n=open("/home/claude/via/vsignal-y/note.html",encoding="utf8").read().replace("vsig-y-wl-v1","vsig-tb-g1cs-l4-wl-v1")
open(OUT_DIR+"note.html","w",encoding="utf8").write(n)
print("ok",len(t))

import shutil
shutil.copyfile("/home/claude/via/vsignal-y/words.html",OUT_DIR+"words.html")
