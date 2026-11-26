# -*- coding: utf-8 -*-
S={};X={}
S['c13s1|1-(A)']={0:("【{c|As} one of my friends {v|recommended},】","As절 : ~한 대로 (접속사)"),
 2:("a brighter color","brighter : bright의 비교급"),
 4:("{a|than} the dark blue.","brighter ~ than : ~보다 더 밝은")}
X['c13s1|1-(A)']=dict(pt=["as","비교급 brighter 뒤 : than"],rel=[[4,2,'mod','비교 대상']])
S['c13s1|1-(B)']={1:("【{o|that} it {v|is} more (B)","that 생략 : think의 목적어절")}
S['c13s1|1-(B)'][2]=("{a|practical},","more + 원급 : 3음절 형용사 비교")
X['c13s1|1-(B)']=dict(pt=["practically","be동사 보어 : 형용사 practical"],rel=[[2,1,'eq','보어']])
S['c13s1|2-(A)']={0:("【{c|Although} a {p|balanced} diet {c|and} rest {v|are} factors","양보 / and : diet와 rest 병렬"),
 1:("as (A) {a|great}","as + 원급 + as : factors를 꾸밈"),
 2:("{c|as} exercise {o|is}","as절 : exercise 뒤 is 생략")}
X['c13s1|2-(A)']=dict(pt=["greatly","factors 꾸밈 : 형용사 great"],rel=[[2,1,'eq','~만큼']])
S['c13s1|2-(B)']={1:("{v|must be followed} as (B) {a|necessarily}","조동사 + 수동태 / 부사 necessarily"),
 2:("as {p|staying} active","as + 동명사 : 활동적으로 유지하는 것만큼")}
S['c13s1|2-(B)'][2]=("{c|as} {p|staying} active","as + 동명사 : 활동적으로 유지하는 것만큼")
X['c13s1|2-(B)']=dict(pt=["necessary","followed(동사) 꾸밈 : 부사 necessarily"],rel=[[2,1,'eq','as ~ as']])
S['c13s1|3-(A)']={3:("{v|are used} (A) {a|far} more frequently","수동태 / far : 비교급 more 강조")}
X['c13s1|3-(A)']=dict(pt=["very","비교급 more frequently : very 불가"],rel=[[4,3,'mod','비교 대상'],[2,1,'mod','']])
S['c13s1|3-(B)']={0:("Similarly, 【{k|the taller} the buildings {c|or} towers in a city {v|are},】","the + 비교급, the + 비교급 / or : 병렬"),
 1:("the (B) {a|more} crowded they {v|become}","become + 형용사 : 더 붐비게 되다")}
X['c13s1|3-(B)']=dict(pt=["most","the + 비교급 짝 : most 아님"],rel=[[0,1,'par','~할수록 더']])
S['c13s1|4-①']={0:("The park in Irvine","in Irvine : park을 꾸밈"),
 2:("{c|as} the one in Tustin {o|is},","the one = the park (대신 쓴 말)")}
X['c13s1|4-①']=dict(pt=["closer","not as ~ as 사이 : 원급 close"],rel=[[2,1,'eq','~만큼']],
 st=["not as ~ as",["① A is not as 원급 as B : A는 B만큼 ~않다","② 같은 뜻 : A is less 원급 than B"]])
S['c13s1|4-②']={1:("【{o|that} the one in Santa Ana","that 생략 : think의 목적어절"),
 3:("better","better : good의 비교급 (불규칙)")}
X['c13s1|4-②']=dict(pt=["very","비교급 better : very 강조 불가"],rel=[[2,3,'mod','비교급 강조']])
S['c13s1|5-①']={0:("An image {v|has} a {k|much} larger impact","much : 비교급 larger 강조"),
 2:("{a|than} words.","비교급 + than : ~보다 더 …한")}
X['c13s1|5-①']=dict(pt=["as","비교급 larger 뒤 : than"],rel=[[2,0,'mod','비교 대상']])
S['c13s1|5-②']={0:("The nerves from the eye to the brain","from A to B : A에서 B까지"),
 2:("{c|as} the nerves from the ear to the brain {o|are}.","")}
X['c13s1|5-②']=dict(pt=["thicker","배수사 + as + 원급 + as : thick"],rel=[[2,1,'eq','배수 비교']])
S['c13s1|6-①']={0:("Leslie’s family {v|went} on vacation to the beach,","go on vacation : 휴가를 가다")}
X['c13s1|6-①']=dict(pt=["so","as much as + 수치 : as ~ as 짝"],rel=[])
S['c13s1|6-②']={0:("【{c|As} they {v|left} the hotel","As : ~하면서 (시간)"),
 1:("after only {p|playing} board games","전치사 + 동명사 : after playing"),
 3:("Leslie’s six-year-old daughter {v|said},","six-year-old : 하이픈 뒤 year는 단수")}
X['c13s1|6-②']=dict(pt=["better","one of the + 최상급 : best (better 아님)"],rel=[[5,4,'eq','']])
S['add13|1-1']={0:("Many","Many : 많은 사람들 (대명사)"),
 1:("{v|are wearing}","현재진행형 : 입고 있다"),
 3:("with temperatures {a|as} low {c|as} 3 degree Celsius","as low as + 수치 : 낮게는 ~만큼")}
X['add13|1-1']=dict(pt=["so","as low as + 수치 : as ~ as 짝"],rel=[])
S['add13|1-2']={1:("{v|has traveled}","현재완료 : 여행해 왔다"),
 2:("to {a|more} places","more + 복수명사 : 더 많은 장소들")}
X['add13|1-2']=dict(pt=["most","than이 있으므로 비교급 more"],rel=[[4,2,'mod','비교 대상']])
S['add13|1-3']={1:("of the ocean","of the ocean : surface를 꾸밈"),
 3:("as {a|smooth} {c|as} a mirror","as + 원급 + as : ~만큼 매끄러운")}
X['add13|1-3']=dict(pt=["smoothly","look 뒤 보어 : 형용사 smooth"],rel=[[3,2,'eq','보어']])
S['add13|1-4']={1:("{v|like} big trucks,","like : 좋아하다 (동사)"),
 3:("{k|more} {a|than} small cars.","like A more than B : B보다 A를 더")}
X['add13|1-4']=dict(pt=["then","비교 : more than (then 아님)"],rel=[[3,1,'mod','비교 대상']])
S['add13|1-5']={0:("【{c|As} people {v|get} older,】","As : ~함에 따라 / get + 형용사"),
 2:("{v|do not learn}","do not + 동사원형"),
 3:("as {a|efficiently} {c|as}","as + 부사 + as : learn을 꾸밈")}
X['add13|1-5']=dict(pt=["efficient","learn(동사) 꾸밈 : 부사 efficiently"],rel=[[3,2,'mod',''],[4,1,'eq','those = brains']])
S['add13|2-1']={4:("{c|than} cars {o|are}.","")}
X['add13|2-1']=dict(pt=["very","비교급 safer : very 강조 불가"],rel=[[4,3,'mod','비교 대상']])
S['add13|2-2']={0:("For the second year in a row,","in a row : 연속으로"),
 4:("in the North America.","in + 장소 : 최상급의 범위")}
X['add13|2-2']={}
S['add13|2-3']={1:("{v|are feeling}","feel + 형용사 : ~하게 느끼다"),
 2:("{a|very} sad","very : 원급 sad 강조")}
X['add13|2-3']=dict(pt=["much","원급 sad : much 강조 불가"],rel=[[4,3,'par','병렬']])
S['add13|2-4']={}
X['add13|2-4']=dict(pt=["very","비교급 worse : very 강조 불가"],rel=[[3,2,'mod','비교 대상']])
S['add13|2-5']={1:("{v|has enjoyed}","현재완료 : since와 함께"),
 2:("a clearer mind, more energy,","clearer : clear의 비교급")}
X['add13|2-5']=dict(rel=[[3,2,'par','병렬']])
S['add13|3-1']={0:("【{k|The sooner}","the + 비교급, the + 비교급 : ~할수록 더 …"),
 4:("the {a|earlier}","early의 비교급 : y를 i로 바꿔 -er"),
 6:("{v|can all leave}","all : we를 가리킴 (조동사 뒤 all)")}
X['add13|3-1']=dict(pt=["more early","early는 -ier형 : more 안 붙임"],rel=[[0,4,'par','~할수록 더']])
S['add13|3-2']={0:("According to one of my friends Keith,","동격 : Keith = one of my friends"),
 3:("{a|than} {k|any other} game","!than any other + 단수 : 최상급의 뜻"),
 4:("on the market right now.","on the market : game을 꾸밈")}
X['add13|3-2']=dict(pt=["as","비교급 more fun 뒤 : than"],rel=[[3,2,'mod','비교 대상']])
S['add13|3-3']={0:("Currently, the amount","the amount of + 불가산 : 단수 취급"),
 3:("{v|is}","is : 주어 the amount에 맞춤")}
X['add13|3-3']=dict(pt=["larger","배수사 + as + 원급 + as : large"],rel=[[2,1,'mod',''],[5,0,'eq','that = amount']])
S['add13|3-4']={2:("【{c|which} {v|makes} it {k|one of the smallest} animals","계속적 용법 : 앞 내용 전체 설명"),
 3:("in the world】.","one of the + 최상급 + 복수명사")}
X['add13|3-4']=dict(rel=[[2,1,'mod','앞 내용 전체']])
S['add13|3-5']={0:("No other island","No other + 단수 : 다른 어떤 ~도 …않다"),
 4:("in the Atlantic Ocean.","in the Atlantic Ocean : island를 꾸밈")}
X['add13|3-5']=dict(pt=["more","no other ~ as 원급 as : more 아님"],rel=[[1,0,'mod','']])
