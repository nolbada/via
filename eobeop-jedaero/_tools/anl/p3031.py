from gen import *
I=[]
def D(en,key,f,me,merel,easy,notes): I.append(mk(en,key,f,me,merel,easy,notes))
D("Just then, [[a dolphin]] [[appeared]].","돌고래 한 마리가 나타났다.","1형식",
[["Just then,","x"],["a dolphin","s"],["appeared.","v"]],"",
[["먼저 뼈대부터:","A dolphin appeared","돌고래 한 마리가 나타났다(appear 나타나다)."],["언제?","Just then","바로 그때."],["요약: 바로 그때 돌고래가 나타났다."]],
["<b>appear(나타나다)</b>처럼 목적어 없는 동사는 <b>수동태 불가</b>: was appeared(X) → <b>appeared</b>","수동태는 '~을 …하다'(목적어 있는 동사)에서만 만든다. 예: happen, arrive, die도 수동 X"])
D("Without hesitation, [[the dolphin]] [[positioned]] [[itself]] beneath him, and supported his weight.","돌고래는 자리를 잡았다.","3형식",
[["Without hesitation,","x"],["the dolphin","s"],["positioned","v"],["itself","o"],["beneath him,","x"],["and supported","v"],["his weight.","o"]],"dolphin ≠ weight",
[["먼저 뼈대부터:","The dolphin positioned itself","돌고래는 스스로 자리를 잡았다(position 자리 잡다)."],["어떻게?","Without hesitation","망설임 없이."],["어디에?","beneath him","그의 아래에."],["그리고?","and supported his weight","그리고 그의 몸무게를 지탱해 주었다(support 지탱하다)."],["요약: 돌고래는 망설임 없이 아래로 가 그를 받쳐 주었다."]],
["<b>and로 이어지는 동사는 모양을 맞춘다</b>: positioned(과거형) and <b>supported</b>(과거형). supporting(X)","<b>itself</b> = the dolphin 자신 (주어와 같은 대상일 때 -self)"])
base="David has found new respect for animals since he was saved by the dolphin, an experience that has changed his life forever, and he now volunteers at a marine wildlife center that protects dolphins."
me=[["David","s"],["has found","v"],["new respect","o"],["for animals since he was saved by the dolphin,","x"],["an experience that has changed his life forever,","x"],["and he now volunteers at a marine wildlife center that protects dolphins.","x"]]
mk3=lambda: "[[David]] [[has found]] [[new respect]] for animals since he was saved by the dolphin, an experience that has changed his life forever, and he now volunteers at a marine wildlife center that protects dolphins."
D(mk3(),"David는 새로운 존경심을 갖게 되었다.","3형식",me,"David ≠ respect",
[["먼저 뼈대부터:","David has found respect","David는 존경심을 갖게 되었다(find 찾다→갖게 되다)."],["언제부터?","since he was saved by the dolphin","돌고래에게 구조된 이래로(save 구하다)."],["그 일은?","an experience that has changed his life forever","그의 삶을 영원히 바꿔 놓은 경험(change 바꾸다)."],["요약: 돌고래에게 구조된 일이 그의 삶을 바꿔 놓았다."]],
["<b>that 뒤에는 진짜 동사</b>가 필요하다: changing(X) → <b>has changed</b>","<b>현재완료</b>: 과거 일(구조된 경험)이 지금까지 영향을 줄 때 (forever 영원히)"])
D(mk3(),"David는 새로운 존경심을 갖게 되었다.","3형식",me,"David ≠ respect",
[["먼저 뼈대부터:","David has found respect","David는 존경심을 갖게 되었다."],["언제부터?","since he was saved by the dolphin","돌고래에게 구조된 이래로."],["지금은 뭘 해?","and he now volunteers at a center","그리고 그는 지금 센터에서 자원봉사를 한다(volunteer 자원봉사하다)."],["어떤 센터?","a marine wildlife center","해양 야생동물 센터."],["요약: 구조된 David는 지금 센터에서 자원봉사를 한다."]],
["<b>주어가 he(3인칭 단수)</b>이면 현재형 동사에 s: volunteer(X) → <b>volunteers</b>","<b>and he now volunteers</b>: 새 문장이 이어질 때도 주어(he)마다 동사를 따로 맞춘다"])
D(mk3(),"David는 새로운 존경심을 갖게 되었다.","3형식",me,"David ≠ respect",
[["먼저 뼈대부터:","David has found respect","David는 존경심을 갖게 되었다."],["그는 지금 어디서 뭘 해?","he now volunteers at a center","지금 센터에서 자원봉사를 한다."],["어떤 센터?","a marine wildlife center","해양 야생동물 센터."],["그 센터는?","that protects dolphins","돌고래를 보호하는(protect 보호하다)."],["요약: 돌고래를 보호하는 센터에서 자원봉사를 한다."]],
["<b>that 뒤 동사</b>는 선행사에 맞춘다: a center(단수) → protect(X) <b>protects</b>","<b>선행사 찾기</b>: 바로 앞 명사가 dolphins(복수)처럼 보여도 that이 받는 건 center"])
D("When we repeat small errors by making poor decisions, [[our small choices]] [[will eventually add up]] to bad results.","작은 선택들이 쌓일 것이다.","1형식",
[["When we repeat small errors by making poor decisions,","x"],["our small choices","s"],["will eventually add up","v"],["to bad results.","x"]],"",
[["먼저 뼈대부터:","Our choices will add up","우리의 선택들은 쌓일 것이다(add up 쌓이다)."],["언제?","When we repeat small errors","우리가 작은 실수를 반복할 때(repeat 반복하다)."],["어떻게 반복해?","by making poor decisions","잘못된 결정을 내림으로써."],["어떻게 되는데?","to bad results","결국 나쁜 결과로."],["요약: 잘못된 결정이 반복되면 작은 선택들이 나쁜 결과가 된다."]],
["<b>문장에는 진짜 동사(정동사)가 하나는 있어야</b> 한다: adding(X) → <b>will add up</b>","<b>일반적인 앞날의 결과</b>는 will + 동사원형. eventually(결국)는 중간에 들어가는 부사"])
D("According to the design, [[each part]] [[requires]] [[an exact length of wood]].","각 부분은 나무 길이를 필요로 한다.","3형식",
[["According to the design,","x"],["each part","s"],["requires","v"],["an exact length of wood.","o"]],"part ≠ length",
[["먼저 뼈대부터:","Each part requires a length","각 부분은 길이를 필요로 한다(require 필요로 하다)."],["어떤 길이?","an exact length of wood","정확한 길이의 나무."],["무엇에 따르면?","According to the design","설계도에 따르면."],["요약: 설계도는 부품마다 나무 길이를 정확히 요구한다."]],
["<b>each + 단수명사</b>는 단수 취급 → requires(s)","<b>설계도에 적힌 일반적인 내용</b>은 현재시제: required(X) → <b>requires</b>"])
sent3="Since that experience, [[I]] [[have learned]] [[the importance of small processes]] to achieve a good end result, a lesson more valuable than any textbook could teach, and it reminds me to stay careful whenever I start a new project."
me3=[["Since that experience,","x"],["I","s"],["have learned","v"],["the importance of small processes","o"],["to achieve a good end result,","x"],["a lesson more valuable than any textbook could teach,","x"],["and it reminds me to stay careful whenever I start a new project.","x"]]
D(sent3,"나는 중요성을 배웠다.","3형식",me3,"I ≠ importance",
[["먼저 뼈대부터:","I have learned the importance","나는 중요성을 배웠다(learn 배우다)."],["무엇의 중요성?","of small processes","작은 과정들의."],["왜 필요해?","to achieve a good end result","좋은 결과를 얻기 위한(achieve 이루다)."],["어떤 교훈?","a lesson more valuable than any textbook could teach","어떤 교과서도 가르칠 수 없는 더 값진 교훈."],["요약: 그 일 이후 작은 과정의 중요성을 배웠다."]],
["<b>than이 있으면 비교급</b>: valuable(X) → <b>more valuable</b> than. 긴 형용사는 앞에 more","<b>a lesson ...</b>는 앞 내용을 다시 설명해 주는 덧붙임 (콤마로 연결)"])
D(sent3,"나는 중요성을 배웠다.","3형식",me3,"I ≠ importance",
[["먼저 뼈대부터:","I have learned the importance","나는 중요성을 배웠다."],["언제부터?","Since that experience","그 경험 이후로."],["그 교훈은?","a lesson","하나의 교훈."],["그 교훈이 무엇을 해?","it reminds me to stay careful","그것은 내가 조심하도록 상기시켜 준다(remind 상기시키다)."],["요약: 이 교훈 덕에 새 일을 할 때마다 조심하게 된다."]],
["<b>주어 it(= a lesson)은 단수</b>: remind(X) → <b>reminds</b>","<b>remind + 사람 + to 동사원형</b> = ~하라고 상기시키다. 예: remind me to call"])
D("But [[I]] [[thought]] [[small differences wouldn't matter]], so I didn't pay attention to my measurements.","나는 생각했다.","3형식",
[["But","x"],["I","s"],["thought","v"],["small differences wouldn't matter,","o"],["so I didn't pay attention to my measurements.","x"]],"I ≠ that절",
[["먼저 뼈대부터:","I thought (that ~)","나는 ~라고 생각했다(think 생각하다)."],["무엇이라고?","small differences wouldn't matter","작은 차이는 문제 되지 않을 것이라고(matter 중요하다)."],["그래서?","so I didn't pay attention","그래서 주의를 기울이지 않았다(pay attention 주의하다)."],["무엇에?","to my measurements","내 치수 재기에."],["요약: 작은 차이쯤은 괜찮다고 여겨 치수에 신경 쓰지 않았다."]],
["<b>과거 이야기는 시제를 맞춘다</b>: thought, wouldn't, <b>didn't pay</b> (don't pay X)","<b>so</b> = 그래서. 앞 생각의 결과가 뒤에 온다"])
D("[[I]] [[met]] [[her]] a long time ago when we both lived in San Diego.","나는 그녀를 만났다.","3형식",
[["I","s"],["met","v"],["her","o"],["a long time ago when we both lived in San Diego.","x"]],"I ≠ her",
[["먼저 뼈대부터:","I met her","나는 그녀를 만났다(meet 만나다)."],["언제?","a long time ago","오래전에."],["그때 어땠어?","when we both lived in San Diego","우리 둘 다 샌디에이고에 살던 때(live 살다)."],["요약: 둘 다 샌디에이고에 살던 오래전에 그녀를 만났다."]],
["<b>ago</b>가 있으면 과거 시점이 분명 → <b>단순과거</b>: have lived(X) → <b>lived</b>","현재완료(have p.p.)는 ago, yesterday, last year 같은 말과 같이 못 쓴다"])
D("[[We]] [[had been]] [[neighbors]] on the same street for about eight years, but my family moved to Phoenix.","우리는 이웃이었다.","2형식",
[["We","s"],["had been","v"],["neighbors","c"],["on the same street for about eight years,","x"],["but my family moved to Phoenix.","x"]],"We = neighbors",
[["먼저 뼈대부터:","We had been neighbors","우리는 이웃이었었다."],["어디서, 얼마나?","on the same street for about eight years","같은 거리에서 약 8년 동안."],["하지만?","but my family moved to Phoenix","하지만 우리 가족은 피닉스로 이사했다(move 이사하다)."],["요약: 8년 이웃이었지만 우리 가족이 이사를 가면서 끝났다."]],
["<b>과거완료 had p.p.</b> = 과거의 한 일(이사)보다 <b>더 먼저</b> 있었던 일: have been(X) → <b>had been</b>","이웃이던 때가 이사하기 전이라 먼저 → had been"])
sent33="[[We]] [[decided]] [[to meet over lunch last summer]] and have seen each other regularly ever since, a friendship that means more to us than distance ever could, and now both of us hope to meet again soon."
me33=[["We","s"],["decided","v"],["to meet over lunch last summer","o"],["and have seen each other regularly ever since,","x"],["a friendship that means more to us than distance ever could,","x"],["and now both of us hope to meet again soon.","x"]]
D(sent33,"우리는 만나기로 했다.","3형식",me33,"We ≠ to meet",
[["먼저 뼈대부터:","We decided to meet","우리는 만나기로 했다(decide 결정하다)."],["언제, 어떻게?","over lunch last summer","지난여름 점심을 함께하며."],["그 후로는?","and have seen each other regularly ever since","그 뒤로 정기적으로 서로 만나왔다(see 보다)."],["요약: 점심 약속 이후로 쭉 정기적으로 만나고 있다."]],
["<b>동사를 꾸미는 말은 부사</b>: have seen을 꾸미니까 regular(X) → <b>regularly</b>(정기적으로)","<b>ever since</b> = 그 이후로 쭉 → 현재완료(have seen)와 짝꿍"])
D(sent33,"우리는 만나기로 했다.","3형식",me33,"We ≠ to meet",
[["먼저 뼈대부터:","We decided to meet","우리는 만나기로 했다."],["그 후로는?","and have seen each other regularly","정기적으로 서로 만나왔다."],["어떤 우정?","a friendship that means more to us","우리에게 더 큰 의미를 갖는 우정(mean 의미하다)."],["무엇보다?","than distance ever could","거리가 줄 수 있는 것보다."],["요약: 그 우정은 거리보다 우리에게 더 소중하다."]],
["<b>that 뒤 동사</b>는 선행사에 맞춘다: a friendship(단수) → mean(X) <b>means</b>","<b>more ... than</b> = ~보다 더. 비교하는 두 가지를 알아보자 (우정 vs 거리)"])
D(sent33,"우리는 만나기로 했다.","3형식",me33,"We ≠ to meet",
[["먼저 뼈대부터:","We decided to meet","우리는 만나기로 했다."],["그리고 지금은?","and now both of us hope","이제 우리 둘 다 바란다(hope 바라다)."],["무엇을?","to meet again soon","곧 다시 만나기를."],["요약: 우리 둘 다 곧 다시 만나기를 바라고 있다."]],
["<b>both of us는 복수 취급</b>: hopes(X) → <b>hope</b>. 예: Both of them are tall.","<b>hope + to부정사</b>: hope to meet (hope meeting X)"])
D("Since then, [[researchers]] [[have observed]] [[the lifestyle of this fascinating creature]].","연구자들은 생활방식을 관찰해 왔다.","3형식",
[["Since then,","x"],["researchers","s"],["have observed","v"],["the lifestyle of this fascinating creature.","o"]],"researchers ≠ lifestyle",
[["먼저 뼈대부터:","Researchers have observed the lifestyle","연구자들은 생활방식을 관찰해 왔다(observe 관찰하다)."],["언제부터?","Since then","그 이후로."],["누구의?","of this fascinating creature","이 흥미로운 생물의."],["요약: 발견된 뒤로 연구자들은 아델리펭귄의 삶을 계속 관찰해 왔다."]],
["<b>주어가 복수(researchers)</b>면 <b>have</b>: has observed(X) → <b>have observed</b>","<b>Since then</b>(그 이후로)은 지금까지 이어지니 현재완료"])
D("But there are [[seals]] that eat penguins in this icy water.","하지만 물개들이 있다.","1형식",
[["But","x"],["there","x"],["are","v"],["seals","s"],["that eat penguins in this icy water.","x"]],"",
[["먼저 뼈대부터:","there are seals","물개들이 있다."],["어떤 물개?","that eat penguins","펭귄을 잡아먹는(eat 먹다)."],["어디에?","in this icy water","이 차가운 물속에."],["요약: 차가운 바닷속에는 펭귄을 잡아먹는 물개들이 있다."]],
["<b>that 뒤 동사</b>는 선행사에 맞춘다: seals(복수) → eats(X) <b>eat</b>","<b>There are + 복수명사</b> = ~들이 있다. 실제 주어는 are 뒤의 seals"])
sent4="If the first one survives, [[everyone else]] [[will jump]] into the water, a strategy that proves effective for generations, and it shows how instinct guides their survival."
me4=[["If the first one survives,","x"],["everyone else","s"],["will jump","v"],["into the water,","x"],["a strategy that proves effective for generations,","x"],["and it shows how instinct guides their survival.","x"]]
D(sent4,"나머지 모두가 뛰어들 것이다.","1형식",me4,"",
[["먼저 뼈대부터:","Everyone else will jump","나머지 모두가 뛰어들 것이다(jump 뛰어들다)."],["언제?","If the first one survives","첫 번째 펭귄이 살아남으면(survive 살아남다)."],["어떤 전략?","a strategy that proves effective","효과적임이 입증된 전략(prove 입증하다)."],["얼마나?","for generations","여러 세대 동안."],["요약: 첫 펭귄이 살아남으면 모두 뛰어든다. 오랜 세월 통한 전략이다."]],
["<b>that 뒤 동사</b>는 선행사에 맞춘다: a strategy(단수) → prove(X) <b>proves</b>","<b>If ~ 조건절</b>은 미래라도 현재시제(survives)"])
D(sent4,"나머지 모두가 뛰어들 것이다.","1형식",me4,"",
[["먼저 뼈대부터:","Everyone else will jump","나머지 모두가 뛰어들 것이다."],["그 전략은?","a strategy","하나의 전략."],["그것이 무엇을 해?","it shows how instinct guides ...","그것은 본능이 어떻게 ~를 이끄는지 보여준다(show 보여주다)."],["무엇을 이끌어?","their survival","그들의 생존을."],["요약: 이 전략은 본능이 펭귄의 생존을 이끈다는 걸 보여준다."]],
["<b>주어 it(= a strategy)은 단수</b>: show(X) → <b>shows</b>","<b>show + how ~</b>: how 이하(어떻게 ~하는지)가 show의 목적어"])
D(sent4,"나머지 모두가 뛰어들 것이다.","1형식",me4,"",
[["먼저 뼈대부터:","Everyone else will jump","나머지 모두가 뛰어들 것이다."],["그것은 무엇을 보여줘?","it shows how ...","그것은 어떻게 ~인지 보여준다."],["무엇이 이끌어?","instinct guides their survival","본능이 그들의 생존을 이끈다(guide 이끌다)."],["요약: 본능이 펭귄의 생존을 이끈다."]],
["<b>how절 안에서도 주어를 찾자</b>: instinct(단수) → guide(X) <b>guides</b>","<b>instinct</b>(본능)는 셀 수 없는 하나의 개념이라 단수 취급"])
save("ch02-p30-31.html",I)
