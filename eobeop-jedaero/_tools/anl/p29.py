from gen import *
I=[]
I.append(mk("[[They]] also [[wonder]] [[when humans will find the perfect cure for this disease]], which frustrates researchers worldwide.",
"그들은 궁금해한다.","3형식",
[["They","s"],["also","x"],["wonder","v"],["when humans will find the perfect cure for this disease,","o"],["which frustrates researchers worldwide.","x"]],"They ≠ when절",
[["먼저 뼈대부터:","They wonder (when ~)","그들은 ~이 궁금하다(wonder 궁금해하다)."],["무엇이 궁금?","when humans will find the perfect cure","인간이 언제 완벽한 치료법을 찾을지(find 찾다)."],["어떤 병에 대한?","for this disease","이 질병에 대한."],["그 일은?","which frustrates researchers worldwide","전 세계 연구자들을 좌절시킨다(frustrate 좌절시키다)."],["요약: 사람들은 암 치료법이 언제 나올지 궁금해하고, 연구자들은 답답하다."]],
["<b>which 뒤에는 진짜 동사</b>가 필요하다: frustrating(X) → <b>frustrates</b> (선행사 this disease는 단수라 s)","같은 지문 끝 문장도 같은 원리: that easier(X) → that <b>is easier</b> (관계절에는 동사 is가 있어야 한다)"]))
I.append(mk("And by the time I left college at the age of 22, [[I]] [[had also learned]] [[tennis, golf, and basketball]], skills which are useful in my daily life even now.",
"나는 테니스, 골프, 농구를 배운 상태였다.","3형식",
[["And by the time I left college at the age of 22,","x"],["I","s"],["had also learned","v"],["tennis, golf, and basketball,","o"],["skills which are useful in my daily life even now.","x"]],"I ≠ sports",
[["먼저 뼈대부터:","I had learned tennis, golf, and basketball","나는 테니스, 골프, 농구를 배운 상태였다(learn 배우다)."],["언제쯤?","by the time I left college at the age of 22","22살에 대학을 떠날 무렵에는(leave 떠나다)."],["그 운동들은?","skills","기술들."],["어떤 기술?","which are useful in my daily life even now","지금도 내 일상에서 유용한."],["요약: 대학을 떠날 때쯤 세 종목을 배웠고, 그 기술은 지금도 쓸모 있다."]],
["<b>콤마(,) 뒤 관계대명사는 which</b>: , that(X) → , <b>which</b>","<b>관계절에도 동사</b>가 있어야 한다. skills(복수) → useful만(X) <b>are useful</b>"]))
save("ch02-p29.html",I)
