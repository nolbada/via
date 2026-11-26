# -*- coding: utf-8 -*-
S={};X={}
S['c13p1|예제']={0:("We {v|couldn’t have picked}","!부정어 + 비교급 : 최상급의 뜻"),
 1:("a {k|better} location for our company","better : good의 비교급 (불규칙)"),
 2:("{a|than} this warm and {p|inviting} city.","than : ~보다 / inviting : 매력적인")}
X['c13p1|예제']=dict(pt=["as","비교급 better 뒤 : than (as 아님)"],rel=[[2,1,'mod','비교 대상']],
 st=["부정어 + 비교급 = 최상급",["① couldn’t have p.p. + 비교급 + than : 이보다 더 좋을 수 없다","② 곧 이것이 가장 좋다는 뜻 (최상급 의미)"]])
S['c13p1|1']={0:("The car {v|was made} 17 years ago,","수동태 과거 : 만들어졌다"),
 1:("{c|so} it{v|’s} {a|as} old","so : 그래서 / as ~ as : ~만큼 …한"),
 2:("{c|as} you {o|are}.","생략 : as you (are old)")}
S['c13p1|1'][2]=("{c|as} you {o|are}.","as절 : you 뒤에 are 생략")
X['c13p1|1']=dict(pt=["than","as ~ as 동등 비교 : than 아님"],rel=[[2,1,'eq','~만큼']])
S['c13p1|2']={1:("{v|is} {a|noisier} in the daytime","noisy의 비교급 : y를 i로 바꿔 -er"),
 2:("【{c|than} it {v|is} at night】.","than절 : it = 그 동네")}
X['c13p1|2']=dict(pt=["more noisy","noisy는 -ier형 : more 안 붙임"],rel=[[2,1,'mod','비교 대상']],
 st=["비교급 만들기",["① 1음절 : -er (tall, taller)","② 자음 + y : y를 i로 (noisy, noisier)","③ 3음절 이상 : more + 원급 (more important)"]])
S['c13p1|3']={1:("{v|are} usually {k|less} efficient at {p|storing} heat","less ~ than : 열등 비교 / at + 동명사"),
 2:("{a|than} modern ones.","ones = houses (대신 쓴 말)")}
X['c13p1|3']=dict(pt=["as","less + 원급 + than : as 아님"],rel=[[2,0,'eq','ones = houses']])
S['c13p1|4']={1:("{v|looked} as {a|uneasy}","!look + 형용사 : 부사 uneasily 아님"),
 2:("{c|as} Zoe {o|looked}.","as절 : Zoe 뒤에 looked 생략")}
X['c13p1|4']=dict(pt=["uneasily","look 뒤 보어 : 형용사 uneasy"],rel=[[2,1,'eq','as ~ as']],
 st=["감각동사 + 형용사",["① look, feel, sound, smell, taste + 형용사 보어","② as ~ as 사이도 원급 : as uneasy as Zoe"]])
S['c13p1|5']={0:("We {v|don’t see} each other","each other : 서로 (대명사)"),
 1:("as {a|frequently}","as + 부사 + as : see를 꾸밈"),
 2:("【{c|as} we {v|used to}】","as절 : used to 뒤 see each other 생략"),
 3:("【{c|when} we {v|were} in school】.","when절 : 학교에 다닐 때")}
X['c13p1|5']=dict(pt=["frequent","see(동사)를 꾸밈 : 부사 frequently"],rel=[[2,1,'eq','as ~ as'],[1,0,'mod','']],
 st=["as ~ as 사이의 품사",["① 동사를 꾸미면 부사 (as frequently as)","② be·감각동사 뒤 보어면 형용사 (as old as)"]])
S['c13p1|6']={0:("Recent inventions such as airplanes","such as : ~와 같은 (예시)"),
 1:("{v|are} surely not more {a|important}","!not more ~ than : ~보다 더 …않다"),
 2:("{c|than} ancient ones like the wheel.","ones = inventions (대신 쓴 말)")}
X['c13p1|6']=dict(pt=["importantly","be동사 뒤 보어 : 형용사 important"],rel=[[2,1,'mod','비교 대상']])
S['c13p1|7']={1:("you {v|can enjoy} scenery","can + 동사원형 : ~할 수 있다"),
 2:("{a|as} various","as + 원급 + as : scenery를 꾸밈"),
 3:("{c|as} deserts, seas, {c|and} mountains.","병렬 : deserts, seas, mountains")}
X['c13p1|7']=dict(pt=["so","as ~ as : 앞 as가 짝 (so 아님)"],rel=[[3,2,'eq','~만큼']])
S['c13p1|8']={0:("The store {v|is} far from my home,","far from : ~에서 먼"),
 2:("more kinds of items","more + 명사 : 더 많은 ~"),
 3:("{a|than} the store in my town.","than : ~보다 / in my town이 store 꾸밈")}
X['c13p1|8']=dict(pt=["then","비교급 more 뒤 : than (then 아님)"],rel=[[3,2,'mod','비교 대상']],
 st=["than과 then 구별",["① than : 비교 (more ~ than)","② then : 그때, 그러고 나서 (시간)"]])
S['c13p2|예제']={0:("Many studies {v|have shown}","현재완료 : 보여주었다"),
 1:("【{c|that} {p|drinking} tea {v|is}","that절 : 목적어 / drinking tea가 주어"),
 3:("healthier {c|than} {p|drinking} coffee】.","than 뒤 동명사 : drinking tea와 비교")}
X['c13p2|예제']=dict(pt=["very","비교급 healthier : very 강조 불가"],rel=[[2,3,'mod','비교급 강조']],
 st=["비교급 강조 부사",["① much, far, even, still, a lot + 비교급","② very, so, too는 원급 강조 : very healthy"]])
S['c13p2|1']={1:("my public-speaking skills {v|have become}","become + 보어 : ~해지다 / 현재완료"),
 3:("better over time.","better : good의 비교급 (불규칙)")}
X['c13p2|1']=dict(pt=["very","비교급 better : very 강조 불가"],rel=[[2,3,'mod','비교급 강조']])
S['c13p2|2']={0:("The two apartments {v|look}","look + 형용사 : ~해 보이다"),
 1:("{a|very}","very : 원급(similar) 강조"),
 3:("{c|but} one {v|is} {k|slightly} bigger {c|than} the other.","!slightly + 비교급 : 약간 더 ~한")}
X['c13p2|2']=dict(pt=["much","원급 similar : much 강조 불가"],rel=[[1,2,'mod','원급 강조']],
 st=["원급 강조 vs 비교급 강조",["① 원급 : very, so, quite (very similar)","② 비교급 : much, far, even, still, a lot, slightly"]])
S['c13p2|3']={0:("The storm last night {v|was}","last night : 어젯밤 (부사구)"),
 2:("the worst {o|that} 【we{v|’ve experienced} in years】.","목적격 관계대명사 생략 : worst를 꾸밈")}
X['c13p2|3']=dict(pt=["very","by far : 최상급 강조 (very와 자리 다름)"],rel=[[1,2,'mod','최상급 강조']])
S['c13p2|4']={0:("In 2014, Internet usage time on mobile phones {v|was}","on mobile phones : time을 꾸밈"),
 2:("greater {c|than} that on desktops {c|or} laptops.","that = usage time / or : 병렬")}
X['c13p2|4']=dict(pt=["very","비교급 greater : very 강조 불가"],rel=[[1,2,'mod','비교급 강조']])
S['c13p2|5']={0:("【{c|Even if} the bridge {v|is} very long,】","Even if : 양보 / very : 원급 강조"),
 3:("the longest in the world.","최상급 the longest : 범위는 in the world")}
X['c13p2|5']=dict(pt=["very","not very ~는 별로 ~않은 : 뜻이 다름"],rel=[[2,3,'mod','강조']])
S['c13p3|예제']={0:("【{k|The older} the male Chuckwallas lizards {v|grow},】","the + 비교급, the + 비교급 : ~할수록 더 …"),
 1:("the {a|lighter} their body colors {v|become}.","become + 비교급 : 더 ~해지다")}
X['c13p3|예제']=dict(pt=["lightest","the + 비교급 짝 : 최상급 아님"],rel=[[0,1,'par','~할수록 더']],
 st=["the + 비교급, the + 비교급",["① The + 비교급 + S + V, the + 비교급 + S + V","② 두 비교급 모두 the 바로 뒤에 둔다","③ 최상급(the lightest)이 아니라 비교급(the lighter)"]])
S['c13p3|1']={0:("My friends {c|and} I {v|ran}","병렬 : 주어 My friends와 I"),
 2:("{c|as} possible","as ~ as possible : 가능한 한 ~하게"),
 3:("【{p|to} get to the movie on time】.","to부정사 (부사적) : 목적 (~하기 위해)")}
S['c13p3|1'][1]=("as {a|fast}","fast : 부사도 형태 같음 (fastly 없음)")
X['c13p3|1']=dict(pt=["fastly","fast는 형용사·부사 같은 모양"],rel=[[2,1,'eq','as ~ as']],
 st=["as ~ as possible",["① as + 원급 + as possible = as + 원급 + as + 주어 + can","② ran을 꾸미므로 원급은 부사 fast"]])
S['c13p3|2']={0:("【{c|When} people {v|learn} from their mistakes,】","When절 : 시간 (~할 때)"),
 1:("they {v|get}","get + 형용사 : ~해지다")}
X['c13p3|2']=dict(pt=["wise and wise","비교급 and 비교급 : 원급 반복 아님"],rel=[[2,1,'eq','보어']],
 st=["점점 더 ~해지다",["① 비교급 and 비교급 : wiser and wiser","② 3음절 이상 : more and more important"]])
S['c13p3|3']={1:("{v|is} {a|older}","old의 비교급 : older"),
 2:("{c|than} {k|any other} artwork in this museum.","!than any other + 단수 : 최상급의 뜻")}
X['c13p3|3']=dict(pt=["oldest","than이 있으므로 비교급 older"],rel=[[2,1,'mod','비교 대상']])
S['c13p3|4']={1:("{v|is} one of the","!one of the + 최상급 + 복수명사"),
 3:("ways 【{p|to} develop new thinking {c|and} ideas】.","to부정사 (형용사적) : ways 꾸밈 / and : 병렬")}
X['c13p3|4']=dict(pt=["better","one of the + 최상급 : better 아님"],rel=[[2,3,'mod','']],
 st=["one of the + 최상급",["① one of the + 최상급 + 복수명사 : 가장 ~한 것들 중 하나","② 동사는 one에 맞춘다 : is"]])
S['c13p3|5']={0:("No other animal on the earth {v|is}","No other + 단수명사 : 다른 어떤 ~도 …않다"),
 1:("as {a|smart}","부정어 + as 원급 as : 최상급의 뜻"),
 2:("{c|as} the orangutan {o|is}.","")}
X['c13p3|5']=dict(pt=["smarter","as ~ as 사이 : 원급 smart"],rel=[[2,1,'eq','as ~ as']])
