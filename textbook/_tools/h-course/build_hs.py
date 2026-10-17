import json,re,os
SRC="/home/claude/via/vsignal-y/xray.html"
OUT_DIR="/home/claude/via/textbook/g1-geumcheon-mirae/l3/y/"
R=lambda a,b:list(range(a,b))
def tk(s): return s.split(" ")
S=[]
def add(**k): S.append(k)

# ---- 1-3
t=tk("Today, you're going to meet three amazing artists who never gave up on their art, despite challenges in their lives."); assert len(t)==20
add(lv="심화",id="1-3",tok=t,
 ch=["Today, you're going to meet three amazing artists","who never gave up on their art,","despite challenges in their lives."],
 ko=["오늘 여러분은 세 명의 놀라운 예술가들을 만나게 될 것이다","그들은 자신의 예술을 결코 포기하지 않았다","인생의 역경에도 불구하고"],
 nodes=[dict(id="m",a=0,b=20,own=R(0,8),kids=[[8,20]],S=[1],V=[1,2,3,4],G=[[1,2,3,4]],form=3,fl=[0],
   sk=[dict(r="S",g=[1]),dict(r="V",g=[2,3,4]),dict(r="O",g=[5,6,7])],
   note="you're going to meet three amazing artists. 주어 + 동사 + 목적어, 3형식입니다. you're는 you + are이고, are going to meet(~하게 될 것이다)이 한 덩어리 동사예요. Today는 시간을 덧붙이는 말입니다."),
  dict(id="a",a=8,b=20,own=R(8,20),kids=[],S=[8],V=[10,11],G=[[10,11]],kind="형용사절",sub="주격 관계대명사",anc=[7],np=[5,6,7],
   note="___ never gave up on their art 에서 주어 자리(= artists)가 비어 있어서 who는 주격 관계대명사입니다. gave up은 구동사(포기하다)이고 on은 전치사예요. despite challenges in their lives는 '인생의 역경에도 불구하고'라는 양보의 꾸밈말입니다.")],
 dec={"0":"Today는 시간을 나타내는 부사입니다.","5":"three는 숫자(형용사)입니다.","6":"amazing은 artists를 꾸미는 말(분사형 형용사)이라 문장의 동사가 아닙니다.","9":"never는 부정 부사입니다.","12":"on은 전치사입니다. give up on = ~을 포기하다에서 on은 동사 뒤에 붙는 전치사예요.","15":"despite는 '~에도 불구하고'라는 전치사입니다.","16":"challenges는 명사(역경)입니다."},
 vn="you're going to meet는 are going to meet이라는 한 덩어리 동사예요. 그래서 going과 meet도 함께 눌러요. gave up은 구동사라 두 단어가 한 동사입니다.",
 why="기준 ⑥: 구동사 = 불변화사까지 한 덩어리 동사\ngive up(포기하다)의 up은 동사와 한 덩어리이고, on their art는 전치사 + 명사 덩어리(수식어)",
 nf=[dict(w="amazing",t="part",who="artists",base="amaze",ing="amazing",pp="amazed",ans="ing",reason="artists는 사람들을 놀라게 하는 능동 관계입니다. 그래서 현재분사 amazing이에요.",g=[6])],em=[])

# ---- 1-4
t=tk("Each artist has a unique painting style and story that has made their work highly valued."); assert len(t)==16
add(lv="심화",id="1-4",tok=t,
 ch=["Each artist has","a unique painting style and story","that has made their work highly valued."],
 ko=["각 예술가에게는 있다","독특한 화풍과 이야기가","그 이야기가 그들의 작품을 높이 평가받게 만들어 왔다"],
 nodes=[dict(id="m",a=0,b=16,own=R(0,9),kids=[[9,16]],S=[1],V=[2],G=[[2]],form=3,fl=[],
   sk=[dict(r="S",g=[0,1]),dict(r="V",g=[2]),dict(r="O",g=R(3,9))],
   note="Each artist has a unique painting style and story. 주어 + 동사 + 목적어, 3형식입니다. style and story가 has의 목적어이고, that 이하는 이 목적어를 꾸밉니다."),
  dict(id="a",a=9,b=16,own=R(9,16),kids=[],S=[9],V=[10,11],G=[[10,11]],kind="형용사절",sub="주격 관계대명사",anc=[8],np=[6,7,8],
   note="___ has made their work highly valued 에서 주어 자리(= style and story)가 비어 있어서 that은 주격 관계대명사입니다. has made + their work + highly valued는 make + 목적어 + 목적격보어의 5형식이에요.")],
 dec={"4":"unique는 형용사입니다.","5":"painting은 style을 꾸미는 동명사(그림 그리는 방식)라 동사가 아닙니다.","9":"that은 관계대명사입니다.","14":"highly는 부사입니다.","15":"valued는 their work의 상태를 설명하는 과거분사(목적격보어)라서 문장의 동사가 아닙니다."},
 vn="has는 본동사(가지고 있다), has made는 현재완료(has + p.p.)로 둘 다 동사예요.",why=None,
 nf=[dict(w="painting",t="ger",reason="painting style은 '그림 그리는 방식', 즉 화풍입니다. 명사 style의 용도를 나타내는 동명사예요.",g=[5]),
     dict(w="valued",t="part",who="work",base="value",ing="valuing",pp="valued",ans="pp",reason="their work는 높이 평가를 받는 대상이라 수동 관계입니다. 그래서 과거분사 valued예요.",g=[15])],em=[])

# ---- 2-5
t=tk("It wasn't until he was 85 years old and became too ill to work that he turned to drawing to express his life experiences."); assert len(t)==24
add(lv="심화",id="2-5",tok=t,
 ch=["It wasn't until he was 85 years old","and became too ill to work","that he turned to drawing","to express his life experiences."],
 ko=["그가 85세가 되고","몸이 너무 아파 일할 수 없게 된 후에야","그는 그림으로 눈을 돌렸다","자신의 인생 경험을 표현하기 위해"],
 nodes=[dict(id="m",a=0,b=24,own=[0,1]+R(14,24),kids=[[2,14]],S=[0,15],V=[1,16],G=[[1],[16]],form=1,fl=[0,1,14]+R(17,24),
   sk=[dict(r="S",g=[15]),dict(r="V",g=[16])],
   note="he turned. 주어 + 동사, 1형식입니다. It wasn't until A that B는 'A하고 나서야 비로소 B했다'는 강조구문이라 that 뒤(he turned …)가 문장의 뼈대예요. to drawing은 목적어가 아니라 turned를 꾸미는 전치사구입니다."),
  dict(id="a",a=2,b=14,own=R(2,14),kids=[],S=[3],V=[4,9],G=[[4],[9]],kind="부사절",sub="시간",
   note="until이 이끄는 시간의 부사절입니다. not until은 '~하고서야'라는 뜻이고, he was 85 years old와 became too ill to work 두 동사가 and로 이어져 있어요.")],
 dec={"0":"It은 강조구문의 It이에요. 동사가 아닙니다.","2":"until은 접속사입니다.","7":"old는 형용사(보어)입니다.","10":"too는 부사입니다.","11":"ill은 형용사(보어)입니다.","12":"to work의 to예요. to부정사의 일부라서 동사가 아닙니다.","13":"work는 too ill to work(너무 아파서 일할 수 없다)의 to부정사라서 동사가 아닙니다.","14":"that은 강조구문의 that이에요. 동사가 아닙니다.","17":"to는 turn to의 전치사예요. 동사는 turned 하나입니다.","18":"drawing은 전치사 to 뒤의 동명사라서 동사가 아닙니다.","19":"to express의 to예요. to부정사의 일부라서 동사가 아닙니다.","20":"express는 to express(표현하기 위해)라는 to부정사라서 동사가 아닙니다."},
 vn="wasn't(강조구문의 틀), turned(that 뒤 문장), until절 안의 was와 became, 모두 4개예요.",
 why="기준 ①: 자동사 + 전치사 = 1형식, 전치사구 = 필수 수식어\nturn to(~로 눈을 돌리다)는 자동사 + 전치사 표현, 동사 표시는 turned까지이고 to drawing은 전치사구 수식어",
 nf=[dict(w="to work",t="to",use="부사적 용법",reason="too ill to work(너무 아파서 일할 수 없다)에서 정도를 나타내므로 부사적 용법입니다.",rel=dict(h="이 문장에서는 too ill을 뒤에서 꾸밉니다",p=[["too ill","꾸밈받는 말"],["to work","정도 · ~하기에"]],ko="일하기에는 너무 아픈"),g=[12,13]),
     dict(w="drawing",t="ger",reason="전치사 to 뒤의 -ing는 동명사입니다. 명사 역할을 해요.",g=[18]),
     dict(w="to express",t="to",use="부사적 용법",reason="그림으로 눈을 돌린 목적(~하기 위해)을 덧붙이므로 부사적 용법입니다.",g=[19,20])],em=[])

# ---- 2-7
t=tk("Traylor had a strong fear of dogs because they had often been used on farms to watch and hunt slaves."); assert len(t)==20
add(lv="심화",id="2-7",tok=t,
 ch=["Traylor had a strong fear of dogs","because they had often been used on farms","to watch and hunt slaves."],
 ko=["Traylor는 개에 대한 강한 두려움이 있었다","개가 농장에서 자주 이용되었기 때문이다","노예를 감시하고 사냥하기 위해"],
 nodes=[dict(id="m",a=0,b=20,own=R(0,7),kids=[[7,20]],S=[0],V=[1],G=[[1]],form=3,fl=[],
   sk=[dict(r="S",g=[0]),dict(r="V",g=[1]),dict(r="O",g=R(2,7))],
   note="Traylor had a strong fear of dogs. 주어 + 동사 + 목적어, 3형식입니다. of dogs는 fear를 꾸미는 말이에요."),
  dict(id="a",a=7,b=20,own=R(7,20),kids=[],S=[8],V=[9,11,12],G=[[9,11,12]],bd=[10],kind="부사절",sub="이유",
   note="because가 이끄는 이유의 부사절입니다. had often been used는 had been + 과거분사(과거완료 수동태)로, '이용되었다'는 뜻의 한 덩어리 동사예요.")],
 dec={"3":"strong은 형용사입니다.","7":"because는 접속사입니다.","10":"often은 빈도를 나타내는 부사입니다.","13":"on은 전치사입니다.","15":"to watch and hunt의 to예요. to부정사의 일부라서 동사가 아닙니다.","16":"watch는 to watch(감시하기 위해)라는 to부정사라서 동사가 아닙니다.","18":"hunt도 to에 걸린 to부정사(watch and hunt)라서 동사가 아닙니다."},
 vn="had often been used는 had been used(이용되었다)라는 수동태 한 덩어리예요. 그래서 had, been, used를 모두 눌러요.",why=None,
 nf=[dict(w="to watch and hunt",t="to",use="부사적 용법",reason="개가 농장에서 이용된 목적(~하기 위해)을 나타내므로 부사적 용법입니다. watch와 hunt가 and로 이어져 둘 다 to에 걸려요.",g=[15,16,17,18])],em=[])

# ---- 3-9
t=tk("Although her physical limitations confined her to a small cottage, her talent and imagination were both limitless."); assert len(t)==17
add(lv="심화",id="3-9",tok=t,
 ch=["Although her physical limitations confined her to a small cottage,","her talent and imagination were both limitless."],
 ko=["비록 신체적 제약이 그녀를 작은 오두막집에 가두었지만","그녀의 재능과 상상력은 둘 다 무한했다"],
 nodes=[dict(id="m",a=0,b=17,own=R(10,17),kids=[[0,10]],S=[11,13],V=[14],G=[[14]],form=2,fl=[15],
   sk=[dict(r="S",g=R(10,14)),dict(r="V",g=[14]),dict(r="C",g=[16])],
   note="her talent and imagination were limitless. 주어 + 동사 + 보어, 2형식입니다. 재능과 상상력 = 무한한(주어 = 보어)이에요. both는 '둘 다'라는 뜻의 꾸미는 말입니다."),
  dict(id="a",a=0,b=10,own=R(0,10),kids=[],S=[3],V=[4],G=[[4]],kind="부사절",sub="양보",
   note="Although가 이끄는 양보절('비록 ~이지만')입니다. 절 안은 limitations(주어) + confined(동사) + her(목적어) + to a small cottage(전치사구)로, confine A to B는 'A를 B에 가두다'예요.")],
 dec={"0":"Although는 접속사입니다.","2":"physical은 형용사입니다.","6":"to는 confine A to B의 전치사예요.","8":"small은 형용사입니다.","15":"both는 '둘 다'를 뜻하는 말로, 동사가 아닙니다.","16":"limitless는 상태를 설명하는 형용사(보어)입니다."},
 vn="",why="confine A to B = A를 B에 가두다 (3형식 + 전치사구)\nher가 confined의 목적어이고, to a small cottage는 전치사구 수식어",
 nf=[],em=[])

# ---- 4-4
t=tk("After that, she even studied abroad in Paris, which was unusual for women at the time."); assert len(t)==16
add(lv="심화",id="4-4",tok=t,
 ch=["After that, she even studied abroad in Paris,","which was unusual for women at the time."],
 ko=["그 후 그녀는 파리에서 유학까지 했다","그것은(=파리 유학) 당시 여성들에게 드문 일이었다"],
 nodes=[dict(id="m",a=0,b=16,own=R(0,8),kids=[[8,16]],S=[2],V=[4],G=[[4]],form=1,fl=[0,1,3,5,6,7],
   sk=[dict(r="S",g=[2]),dict(r="V",g=[4])],
   note="she studied. 주어 + 동사, 1형식입니다. After that, even, abroad in Paris는 studied를 꾸미는 말이에요."),
  dict(id="a",a=8,b=16,own=R(8,16),kids=[],S=[8],V=[9],G=[[9]],kind="형용사절",sub="주격 관계대명사",anc=[7],np=[4,5,6,7],
   note="콤마 뒤 which는 앞 내용 전체(파리에서 유학까지 한 것)를 받는 계속적 용법입니다. ___ was unusual 에서 주어 자리가 비어 있어서 which는 주격 관계대명사예요. '그리고 그것은 ~' 순서로 이어서 해석합니다.")],
 dec={"1":"that은 After that에서 '그 후'라는 뜻을 만드는 말이에요. 동사가 아닙니다.","3":"even은 '~까지도'라는 부사입니다.","5":"abroad는 '해외에서'라는 부사입니다.","10":"unusual은 형용사(보어)입니다."},
 vn="",why=None,nf=[],em=[])

# ---- 4-6
t=tk("Even after getting married, Ancher persisted in painting, objecting to the social pressure that married women were to solely focus on household duties."); assert len(t)==23
add(lv="심화",id="4-6",tok=t,
 ch=["Even after getting married,","Ancher persisted in painting,","objecting to the social pressure","that married women were to solely focus on household duties."],
 ko=["결혼 후에도","Ancher는 그림을 계속 그렸다","사회적 압력에 저항하며","그 압력은 기혼 여성이 가사에만 집중해야 한다는 것이었다"],
 nodes=[dict(id="m",a=0,b=23,own=R(0,13),kids=[[13,23]],S=[4],V=[5],G=[[5]],form=1,fl=[0,1,2,3]+R(6,13),
   sk=[dict(r="S",g=[4]),dict(r="V",g=[5])],
   note="Ancher persisted. 주어 + 동사, 1형식입니다. persist in은 자동사 + 전치사라서 in painting은 목적어가 아니라 persisted를 꾸미는 전치사구예요. Even after getting married와 objecting to the social pressure도 꾸미는 말입니다."),
  dict(id="a",a=13,b=23,own=R(13,23),kids=[],S=[15],V=[16,17,19],G=[[16,17,19]],bd=[18],kind="명사절",sub="동격",gv=[["pressure","명사"]],
   note="pressure 뒤의 that은 the social pressure의 내용을 설명하는 동격의 that입니다. that 뒤가 완전한 문장(주어 women, 동사 were to focus, 전치사구 on household duties)이라서 관계대명사가 아니에요. were to focus는 be to(~해야 한다)라는 한 덩어리 동사입니다.")],
 dec={"0":"Even은 부사입니다.","2":"getting은 전치사 after 뒤의 동명사(get married)라서 동사가 아닙니다.","3":"married는 get married(결혼하다)의 일부(형용사)입니다.","6":"in은 persist in의 전치사입니다.","7":"painting은 전치사 in 뒤의 동명사라서 동사가 아닙니다.","8":"objecting은 '~에 저항하며'라는 분사구문의 분사라서 문장의 동사가 아닙니다.","9":"to는 object to의 전치사입니다.","14":"married는 women을 꾸미는 과거분사(결혼한)입니다.","18":"solely는 부사입니다.","20":"on은 focus on의 전치사입니다."},
 vn="were to focus는 be to(~해야 한다)라는 한 덩어리 동사예요. 그래서 were, to, focus를 모두 눌러요.",
 why="기준 ①: 자동사 + 전치사 = 1형식, 전치사구 = 필수 수식어\npersist in(~을 고집하다)은 자동사 + 전치사 표현, 동사 표시는 persisted까지이고 in painting은 전치사구 수식어",
 nf=[dict(w="getting",t="ger",reason="전치사 after 뒤의 -ing는 동명사입니다. get married는 '결혼하다'예요.",g=[2]),
     dict(w="painting",t="ger",reason="전치사 in 뒤의 -ing는 동명사입니다.",g=[7]),
     dict(w="objecting",t="part",who="Ancher",base="object",ing="objecting",pp="objected",ans="ing",reason="주어 Ancher가 직접 저항하는 능동 관계(분사구문)입니다. 그래서 현재분사 objecting이에요.",g=[8]),
     dict(w="married",t="part",who="women",base="marry",ing="marrying",pp="married",ans="pp",reason="women은 결혼을 한(된) 상태로 수동 관계입니다. 그래서 과거분사 married예요.",g=[14])],em=[])

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
t=t.replace('const KEY="vsignalY_clause_v3";','const KEY="vsig-tb-g1gc-l3-y-xray-v1";').replace("vsig-y-wl-v1","vsig-tb-g1gc-l3-wl-v1")
t=t.replace("const STARS=new Set([","const STARS=new Set([].concat([")
t=re.sub(r"const STARS=new Set\(\[\]\.concat\(\[.*?\]\);","const STARS=new Set([]);",t,count=1,flags=re.S)
t=t.replace("let TAB=location.hash=='#adv'?'심화':'기본';","let TAB='심화';")
t=t.replace("'<h1>'+TAB+' 문장 분석</h1>","'<h1>3과 핵심 7문장 · H-S코스</h1>")
t=re.sub(r"<title>.*?</title>","<title>금천고1 3과 핵심 7문장 · H-S코스</title>",t,count=1)
os.makedirs(OUT_DIR,exist_ok=True)
# remove old day clone
for f in ("index.html","note.html"):
    p=OUT_DIR+f
open(OUT_DIR+"index.html","w",encoding="utf8").write(t)
n=open("/home/claude/via/vsignal-y/note.html",encoding="utf8").read().replace("vsig-y-wl-v1","vsig-tb-g1gc-l3-wl-v1")
open(OUT_DIR+"note.html","w",encoding="utf8").write(n)
print("ok",len(t))
