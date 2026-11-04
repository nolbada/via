from gen import *
I=[]
I.append(mk("[[Gloria]] [[will take]] [[a break]] and relax after she finishes her work for the day, which she considers quite exhausting.",
"Gloria는 휴식을 취할 것이다.","3형식",
[["Gloria","s"],["will take","v"],["a break","o"],["and relax","x"],["after she finishes her work for the day,","x"],["which she considers quite exhausting.","x"]],"Gloria ≠ break",
[["먼저 뼈대부터:","Gloria will take a break","Gloria는 휴식을 취할 것이다(take 취하다)."],["또 무엇을?","and relax","그리고 쉴 것이다(relax 쉬다)."],["언제?","after she finishes her work for the day","하루 일을 마친 후에(finish 끝내다)."],["그 일은?","which she considers quite exhausting","그녀가 꽤 힘들다고 생각하는(consider 생각하다)."],["요약: 하루 일을 마치면 쉬겠다. 그 일은 꽤 힘들다."]],
["<b>관계절 안에서도 주어를 찾자</b>: which she considers의 주어는 she(3인칭 단수) → consider(X) <b>considers</b>","<b>after ~ 시간 부사절</b>은 미래라도 현재시제(finishes)"]))
I.append(mk("After locking the door, [[I]] [[realized]] [[that I had left the key inside]], feeling embarrassed in front of my neighbors.",
"나는 깨달았다.","3형식",
[["After locking the door,","x"],["I","s"],["realized","v"],["that I had left the key inside,","o"],["feeling embarrassed in front of my neighbors.","x"]],"I ≠ that절",
[["먼저 뼈대부터:","I realized (that ~)","나는 ~을 깨달았다(realize 깨닫다)."],["언제?","After locking the door","문을 잠근 후에(lock 잠그다)."],["무엇을?","that I had left the key inside","열쇠를 안에 두고 나왔다는 것을(leave 두고 오다)."],["어떤 기분으로?","feeling embarrassed in front of my neighbors","이웃들 앞에서 부끄러움을 느끼며."],["요약: 열쇠를 안에 두고 문을 잠근 걸 깨닫고 이웃 앞에서 민망했다."]],
["<b>감정 분사</b>: 내가 느끼면 <b>-ed</b>. 내가 민망한 거니까 embarrassing(X) → <b>embarrassed</b>","<b>had p.p.</b>: 깨달은 때보다 열쇠를 두고 온 게 더 먼저 → had left"]))
I.append(mk("[[The use of smartphones]] [[has become]] [[widespread]] since their introduction in the early 2000s, a trend that reflects changing lifestyles.",
"스마트폰 사용이 널리 퍼졌다.","2형식",
[["The use of smartphones","s"],["has become","v"],["widespread","c"],["since their introduction in the early 2000s,","x"],["a trend that reflects changing lifestyles.","x"]],"use = widespread",
[["먼저 뼈대부터:","The use has become widespread","사용이 널리 퍼졌다(become ~가 되다)."],["무엇의 사용?","of smartphones","스마트폰의."],["언제부터?","since their introduction in the early 2000s","2000년대 초 도입된 이래로."],["그 흐름은?","a trend that reflects changing lifestyles","변화하는 생활방식을 반영하는(reflect 반영하다) 흐름."],["요약: 스마트폰은 도입 이후 널리 퍼졌고, 생활방식의 변화를 보여 준다."]],
["<b>that 뒤 동사</b>는 선행사에 맞춘다: a trend(단수) → reflect(X) <b>reflects</b>","<b>주어 찾기</b>: The use of smartphones에서 주어는 use(단수). of ~는 꾸밈이라 has become"]))
I.append(mk("[[We]] [[will keep]] [[checking when the concert tickets will go on sale]], hoping to get good seats.",
"우리는 계속 확인할 것이다.","3형식",
[["We","s"],["will keep","v"],["checking when the concert tickets will go on sale,","o"],["hoping to get good seats.","x"]],"We ≠ checking",
[["먼저 뼈대부터:","We will keep checking","우리는 계속 확인할 것이다(keep ~ing 계속 ~하다)."],["무엇을?","when the concert tickets will go on sale","콘서트 표가 언제 판매를 시작하는지(go on sale 판매되다)."],["무엇을 바라며?","hoping to get good seats","좋은 자리를 얻기를 바라며(hope 바라다, get 얻다)."],["요약: 표 판매일을 계속 확인하며 좋은 자리를 노린다."]],
["<b>hope + to부정사</b>: hoping to get(O) / hoping getting(X). 예: hope to win","<b>when ~</b>가 check(확인하다)의 목적어 = 언제 ~인지(명사절) → 미래 will go 그대로"]))
I.append(mk("[[The first automobile]] [[was invented]] in 1886 by Karl Benz, a German engineer whose design influenced the entire industry.",
"최초의 자동차가 발명되었다.","3형식",
[["The first automobile","s"],["was invented","v"],["in 1886 by Karl Benz,","x"],["a German engineer whose design influenced the entire industry.","x"]],"",
[["먼저 뼈대부터:","The first automobile was invented","최초의 자동차가 발명되었다(invent 발명하다)."],["언제, 누구에 의해?","in 1886 by Karl Benz","1886년에 Karl Benz에 의해."],["그는 누구?","a German engineer","독일인 엔지니어."],["어떤 점이?","whose design influenced the entire industry","그의 설계는 업계 전체에 영향을 미쳤다(influence 영향을 주다)."],["요약: 독일 엔지니어 벤츠가 1886년 최초의 자동차를 발명했다."]],
["<b>whose + 명사</b> = ~의 (소유). whose design = 그의 설계. <b>who's</b>는 who is의 줄임말이라 뒤에 명사가 오면 틀림","<b>was invented</b> = 발명되었다 (be p.p. 수동) — 자동차는 '발명되는' 쪽"]))
I.append(mk("[[The beach]] [[will turn into]] a big party spot when the summer season arrives, attracting tourists from every corner of the country.",
"해변이 변할 것이다.","1형식",
[["The beach","s"],["will turn into","v"],["a big party spot","x"],["when the summer season arrives,","x"],["attracting tourists from every corner of the country.","x"]],"",
[["먼저 뼈대부터:","The beach will turn into a spot","해변은 장소로 변할 것이다(turn into ~로 변하다)."],["어떤 장소?","a big party spot","큰 파티 장소."],["언제?","when the summer season arrives","여름 시즌이 오면(arrive 도착하다)."],["그래서?","attracting tourists from every corner of the country","전국 각지에서 관광객들을 끌어모으며(attract 끌어모으다)."],["요약: 여름이면 해변이 파티 장소가 되어 관광객이 몰려든다."]],
["<b>셀 수 있는 명사</b>는 하나냐 여럿이냐를 -s로 보여 준다. 여러 관광객 → tourist(X) <b>tourists</b>","<b>every corner of the country</b>처럼 '여러 곳에서 온 사람들'은 복수를 생각하면 쉽다"]))
I.append(mk("When Martin reached the empty bus stop, [[he]] [[found]] [[that he had missed the bus]], which left him standing there alone and frustrated.",
"그는 알게 되었다.","3형식",
[["When Martin reached the empty bus stop,","x"],["he","s"],["found","v"],["that he had missed the bus,","o"],["which left him standing there alone and frustrated.","x"]],"he ≠ that절",
[["먼저 뼈대부터:","he found (that ~)","그는 ~을 알게 되었다(find 알게 되다)."],["언제?","When Martin reached the empty bus stop","Martin이 텅 빈 정류장에 도착했을 때(reach 도착하다)."],["무엇을?","that he had missed the bus","버스를 놓쳤다는 것(miss 놓치다)."],["그 일이?","which left him standing there alone and frustrated","그를 그곳에 홀로 좌절한 채 서 있게 만들었다(leave 남겨 두다)."],["요약: 버스를 놓친 걸 알고 정류장에 홀로 서서 좌절했다."]],
["<b>and는 같은 모양끼리 연결</b>: alone(형용사) and <b>frustrated</b>(형용사 역할). 그가 좌절한 거니까 -ing(X) → <b>-ed</b>","<b>감정 분사</b>: 사람이 느끼면 -ed(frustrated 좌절한)"]))
I.append(mk("[[The students]] [[visited]] [[the museum]] last month to see famous works of art, most of which were created centuries ago.",
"학생들은 박물관을 방문했다.","3형식",
[["The students","s"],["visited","v"],["the museum","o"],["last month to see famous works of art,","x"],["most of which were created centuries ago.","x"]],"students ≠ museum",
[["먼저 뼈대부터:","The students visited the museum","학생들은 박물관을 방문했다(visit 방문하다)."],["언제, 왜?","last month to see famous works of art","지난달에 유명한 미술 작품을 보려고."],["그 작품들은?","most of which were created centuries ago","그것들 대부분은 수세기 전에 만들어졌다(create 만들다)."]  ,["요약: 박물관에서 본 작품 대부분은 아주 오래전에 만들어졌다."]],
["<b>most of which + 동사</b>: of 뒤(which = works of art, 복수)에 맞춘다 → was(X) <b>were</b>","<b>were created</b> = 만들어졌다 (be p.p. 수동)"]))
I.append(mk("[[This restaurant]] [[is]] [[popular]] because it has served customers high-quality dishes for over 10 years, a reputation earned through hardly any complaints.",
"이 식당은 인기가 있다.","2형식",
[["This restaurant","s"],["is","v"],["popular","c"],["because it has served customers high-quality dishes for over 10 years,","x"],["a reputation earned through hardly any complaints.","x"]],"restaurant = popular",
[["먼저 뼈대부터:","This restaurant is popular","이 식당은 인기가 있다."],["왜?","because it has served customers high-quality dishes","고객들에게 고급 요리를 제공해 왔기 때문에(serve 제공하다)."],["얼마나?","for over 10 years","10년 넘게."],["그 평판은?","a reputation earned through hardly any complaints","불만이 거의 없이 얻어진 평판(earn 얻다)."],["요약: 10년간 불만 없이 좋은 요리를 내서 인기가 있다."]],
["<b>명사 뒤에서 꾸미는 분사</b>: 명사가 '~되는' 쪽이면 <b>-ed(수동)</b>. 평판은 '얻어지는' 것 → earning(X) <b>earned</b>","<b>hardly any</b> = 거의 없는. 예: hardly any money = 돈이 거의 없다"]))
I.append(mk("[[The car]] [[will run]] smoothly as long as you change the engine oil regularly, a habit as important as checking the tires.",
"차는 달릴 것이다.","1형식",
[["The car","s"],["will run","v"],["smoothly","x"],["as long as you change the engine oil regularly,","x"],["a habit as important as checking the tires.","x"]],"",
[["먼저 뼈대부터:","The car will run smoothly","차는 부드럽게 달릴 것이다(run 달리다)."],["언제까지 그럴 조건?","as long as you change the engine oil regularly","엔진 오일을 정기적으로 교체하는 한(change 바꾸다)."],["그 습관은?","a habit as important as checking the tires","타이어를 점검하는 것만큼 중요한 습관(check 점검하다)."],["요약: 오일을 제때 갈아 주면 차가 잘 달린다. 타이어 점검만큼 중요하다."]],
["<b>동사를 꾸미는 말은 부사</b>: change(바꾸다)를 꾸미니까 regular(X) → <b>regularly</b>(정기적으로)","<b>as 형용사 as</b> = ~만큼 …한. 예: as important as (~만큼 중요한)"]))
I.append(mk("Since they first appeared, [[communities]] [[have used]] [[dance]] to remember major events like birth and death, ceremonies that continue to this day.",
"공동체들은 춤을 사용해 왔다.","3형식",
[["Since they first appeared,","x"],["communities","s"],["have used","v"],["dance","o"],["to remember major events like birth and death,","x"],["ceremonies that continue to this day.","x"]],"communities ≠ dance",
[["먼저 뼈대부터:","Communities have used dance","공동체들은 춤을 사용해 왔다(use 사용하다)."],["언제부터?","Since they first appeared","처음 등장한 이래로(appear 나타나다)."],["왜?","to remember major events like birth and death","탄생과 죽음 같은 중요한 사건을 기리려고(remember 기억하다)."],["그 의식은?","ceremonies that continue to this day","오늘날까지 계속되는(continue 계속되다)."],["요약: 사람들은 오래전부터 춤으로 중요한 일을 기려 왔고 지금도 이어진다."]],
["<b>that 뒤에는 진짜 동사</b>가 필요하다: continuing(X) → <b>continue</b>. 선행사 ceremonies가 복수라서 s 없는 모양","<b>Since ~ + have p.p.</b>: ~한 이래로 지금까지 → 현재완료"]))
I.append(mk("[[The road]] [[was closed]] because an accident had occurred earlier on the same day, leaving drivers to find another route.",
"도로가 폐쇄되었다.","3형식",
[["The road","s"],["was closed","v"],["because an accident had occurred earlier on the same day,","x"],["leaving drivers to find another route.","x"]],"",
[["먼저 뼈대부터:","The road was closed","그 도로는 폐쇄되었다(close 닫다)."],["왜?","because an accident had occurred earlier","앞서 사고가 발생했기 때문에(occur 일어나다)."],["그래서?","leaving drivers to find another route","운전자들이 다른 경로를 찾아야 하게 하며(find 찾다)."],["요약: 사고로 도로가 막혀 운전자들은 다른 길을 찾아야 했다."]],
["<b>leave + 목적어 + to부정사</b> = ~가 …하도록 두다. leaving drivers <b>to find</b> (found X: find의 과거형)","<b>had occurred</b>: 사고가 난 건 도로가 폐쇄된 때보다 먼저 → 과거완료"]))
save("ch02-p27.html",I)
