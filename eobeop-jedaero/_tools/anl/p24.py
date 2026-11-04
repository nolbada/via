from gen import *
I=[]
I.append(mk("We have solved many interesting puzzles together since joining the [[puzzle club]], which meets every Saturday afternoon.".replace("[[puzzle club]]","puzzle club").replace("We have solved many interesting puzzles","[[We]] [[have solved]] [[many interesting puzzles]]"),
"우리는 퍼즐들을 풀어왔다.","3형식",
[["We","s"],["have solved","v"],["many interesting puzzles","o"],["together since joining the puzzle club, which meets every Saturday afternoon.","x"]],"We ≠ puzzles",
[["먼저 뼈대부터:","We have solved puzzles","우리는 퍼즐들을 풀어왔다."],["어떤 퍼즐?","many interesting puzzles","많은 흥미로운 퍼즐들."],["언제부터?","since joining the puzzle club","그 퍼즐 동아리에 가입한 이래로."],["어떤 동아리?","which meets every Saturday afternoon","매주 토요일 오후에 모이는(meet 모이다)."],["요약: 매주 토요일에 모이는 퍼즐 동아리에 들어간 뒤로 퍼즐을 많이 풀었다."]],
["<b>관계대명사 which 뒤 동사</b>는 앞 명사(선행사)에 맞춘다: 단수 club → meet(모이다)이 아니라 <b>meets</b>","<b>since ~ing</b> = ~한 이래로 → 지금까지 이어지니 현재완료(have solved)와 짝꿍"]))
I.append(mk("Lisa visited her grandparents last summer before they moved to a different city, which made her feel sad.".replace("Lisa visited her grandparents","[[Lisa]] [[visited]] [[her grandparents]]"),
"Lisa는 조부모님을 방문했다.","3형식",
[["Lisa","s"],["visited","v"],["her grandparents","o"],["last summer before they moved to a different city, which made her feel sad.","x"]],"Lisa ≠ grandparents",
[["먼저 뼈대부터:","Lisa visited her grandparents","Lisa는 조부모님을 방문했다."],["언제?","last summer before they moved to a different city","그분들이 다른 도시로 이사하기 전인 지난여름에."],["그리고 어땠어?","which made her feel sad","그것(이사)은 그녀가 슬프게 느끼게 만들었다 (make 만들다, feel 느끼다)."],["요약: 조부모님이 이사 가시기 전에 찾아뵈었는데, 그 일이 그녀를 슬프게 했다."]],
["<b>feel + 형용사</b> = ~하게 느끼다 → sadly(슬프게, 부사)가 아니라 <b>sad</b>(슬픈). 예: I feel happy.","<b>, which</b>는 앞 내용 전체를 받는다 (여기서는 '이사한 일')"]))
I.append(mk("The young man has worked on his novel for several months now, feeling excited about the progress he has made.".replace("The young man has worked","[[The young man]] [[has worked]]"),
"그 청년은 일해왔다.","1형식",
[["The young man","s"],["has worked","v"],["on his novel for several months now,","x"],["feeling excited about the progress he has made.","x"]],"",
[["먼저 뼈대부터:","The young man has worked","그 청년은 일해왔다(work 일하다)."],["무엇에?","on his novel for several months now","지금까지 몇 달 동안 자기 소설에."],["어떤 마음으로?","feeling excited","신이 나서(feel 느끼다)."],["무엇 때문에?","about the progress he has made","자신이 이룬 진전에 대해(make 만들다→이루다)."],["요약: 몇 달째 소설을 쓰고 있고, 진전이 있어서 신이 난다."]],
["<b>감정 분사</b>: 내가 그 감정을 <b>느끼면 -ed</b>(excited 신난), 감정을 <b>일으키면 -ing</b>(exciting 신나게 하는). 사람이 신난 거니까 excited","<b>for + 기간 + now</b>(지금까지 ~ 동안)는 현재완료(has worked)와 잘 어울린다"]))
I.append(mk("Ms. Spadler purchased a toaster only three weeks ago, but it's already not working, which frustrated her a lot.".replace("Ms. Spadler purchased a toaster","[[Ms. Spadler]] [[purchased]] [[a toaster]]"),
"Spadler 씨는 토스터를 샀다.","3형식",
[["Ms. Spadler","s"],["purchased","v"],["a toaster","o"],["only three weeks ago, but it's already not working, which frustrated her a lot.","x"]],"Ms. Spadler ≠ toaster",
[["먼저 뼈대부터:","Ms. Spadler purchased a toaster","Spadler 씨는 토스터를 샀다(purchase 구입하다)."],["언제?","only three weeks ago","겨우 3주 전에."],["그런데?","but it's already not working","하지만 벌써 작동하지 않는다."],["그래서?","which frustrated her a lot","그것은 그녀를 많이 짜증 나게 했다(frustrate 좌절시키다)."],["요약: 산 지 3주 된 토스터가 벌써 고장 나서 짜증이 났다."]],
["<b>콤마(,) 뒤 which</b>(앞 내용 전체를 받아 덧붙여 설명)는 <b>that으로 못 바꾼다</b>. 예: , which = O / , that = X","<b>three weeks ago</b>처럼 분명한 과거 시점이 있으면 단순과거(purchased)"]))
I.append(mk("In the Old Stone Age, [[groups of 20 to 60 people]] [[wandered]] from place to place to find food, and they must search for days without success.",
"무리가 떠돌아다녔다.","1형식",
[["In the Old Stone Age,","x"],["groups of 20 to 60 people","s"],["wandered","v"],["from place to place","x"],["to find food,","x"],["and they must search for days without success.","x"]],"",
[["먼저 뼈대부터:","Groups wandered","무리들이 떠돌아다녔다(wander 떠돌다)."],["언제?","In the Old Stone Age","구석기 시대에."],["왜?","to find food","식량을 찾으려고(find 찾다)."],["그리고?","and they must search for days without success","그들은 성과 없이 며칠을 찾아다녀야 했다(search 찾다)."],["요약: 구석기 사람들은 식량을 찾아 떠돌았고 며칠씩 헤매기도 했다."]],
["<b>조동사 뒤에는 동사원형</b>: must + search(찾다). must searched(X). 예: can go, will eat","<b>접속사 and</b> 앞뒤에 각각 주어·동사가 있는 두 문장이 나란히 이어져 있다"]))
I.append(mk("[[We]]'[[re]] so [[excited]] although we have waited in line for the sale to start for hours, hoping to get good deals.",
"우리는 신이 나 있다.","2형식",
[["We","s"],["'re","v"],["so excited","c"],["although we have waited in line for the sale to start for hours,","x"],["hoping to get good deals.","x"]],"We = excited",
[["먼저 뼈대부터:","We are excited","우리는 신이 나 있다."],["얼마나?","so excited","매우 신이 난."],["비록 어땠지만?","although we have waited in line ... for hours","몇 시간 동안 줄 서서 기다려 왔지만(wait 기다리다)."],["무엇을 바라며?","hoping to get good deals","좋은 물건을 사기를 바라며(hope 바라다, get 얻다)."],["요약: 몇 시간 줄 서 기다렸지만, 좋은 물건 살 기대에 신이 난다."]],
["<b>문장에 동사가 이미 있고</b> 접속사 없이 동사를 또 못 붙인다 → <b>-ing(분사)</b>로 덧붙인다: hoped(X) → <b>hoping</b>","<b>주어 We</b> 하나가 '신난다'와 '바란다'를 모두 한다 (분사구문의 주어 = 주절 주어)"]))
I.append(mk("[[He]] [[has been]] [[interested in stars]] since he saw his first shooting star last year, although he was very young.",
"그는 별에 관심이 있어 왔다.","2형식",
[["He","s"],["has been","v"],["interested in stars","c"],["since he saw his first shooting star last year,","x"],["although he was very young.","x"]],"He = interested",
[["먼저 뼈대부터:","He has been interested","그는 관심이 있어 왔다."],["무엇에?","in stars","별에."],["언제부터?","since he saw his first shooting star last year","작년에 처음 별똥별을 본 이래로(see 보다)."],["비록 어땠지만?","although he was very young","비록 매우 어렸지만."],["요약: 어린 나이였지만 별똥별을 본 뒤로 쭉 별에 관심을 가져왔다."]],
["<b>although / even though + 주어 + 동사</b>(절) = 비록 ~지만. <b>despite + 명사</b>(구). 예: although he was young / despite his age","<b>be interested in</b> = ~에 관심이 있다 (interested는 상태를 설명하는 보어)"]))
I.append(mk("[[I]] [[closed]] [[the window]] when I felt a cold breeze coming in, feeling colder than before.",
"나는 창문을 닫았다.","3형식",
[["I","s"],["closed","v"],["the window","o"],["when I felt a cold breeze coming in,","x"],["feeling colder than before.","x"]],"I ≠ window",
[["먼저 뼈대부터:","I closed the window","나는 창문을 닫았다(close 닫다)."],["언제?","when I felt a cold breeze coming in","찬 바람이 들어오는 것을 느꼈을 때(feel 느끼다)."],["그때 기분은?","feeling colder than before","전보다 더 춥게 느끼며."],["요약: 찬 바람이 들어와서 창문을 닫았다."]],
["<b>1음절 형용사의 비교급은 -er</b>: cold → colder. <b>more와 -er을 같이 쓰면 안 된다</b> (more colder X)","<b>긴 단어</b>는 more를 쓴다: more beautiful. 한 단어에 비교 표시는 하나만!"]))
save("ch02-p24.html",I)
