# -*- coding: utf-8 -*-
S={};X={}
S['c13q1|1']={2:("{a|than}","비교급 than any other + 단수 : 최상급 뜻"),
 3:("{k|any other} artist {o|who is} currently on the radio.","!any other + 단수명사 / who is 생략")}
X['c13q1|1']=dict(pt=["that","비교급 more popular 뒤 : than"],rel=[[2,1,'mod','비교 대상']])
S['c13q1|2']={0:("The new recipe {v|is} healthier","healthy의 비교급 : healthier"),
 3:("less sugar","less + 셀 수 없는 명사 : 더 적은 양"),
 4:("{c|than} the previous one】.","one = recipe (같은 명사 대신)")}
X['c13q1|2']=dict(pt=["very","비교급 less : very 강조 불가"],rel=[[2,3,'mod','비교급 강조']],
 st=["less + 비교 대상",["① less + 불가산명사 : less sugar (더 적은 설탕)","② 가산 복수명사는 fewer : fewer dishes","③ 강조 : even less, much less"]])
S['c13q1|3']={0:("【{c|Although} {p|flying}","Although : 양보 / flying : 동명사 주어"),
 1:("{v|may seem}","may seem + 형용사 : ~처럼 보일지 모른다"),
 3:("car accidents {v|happen} more often","more often : 더 자주 (부사의 비교급)")}
X['c13q1|3']=dict(pt=["dangerously","seem 뒤 보어 : 형용사 dangerous"],rel=[[4,3,'mod','비교 대상']],
 st=["seem + 형용사",["① seem, look, become + 형용사 보어","② 부사(dangerously)는 보어 자리에 쓰지 않는다"]])
S['c13q1|4']={0:("No other vehicle on the market {v|is}","No other + 단수 : 다른 어떤 ~도 …않다"),
 3:("{c|as} this sports car {o|is}.","")}
X['c13q1|4']=dict(pt=["faster","as ~ as 사이 : 원급 fast"],rel=[[3,2,'eq','as ~ as']])
S['c13q1|5']={0:("I {v|think} {o|that} 【this navy dress {v|makes} me look","think 뒤 that 생략 / make + O + 원형")}
X['c13q1|5']=dict(pt=["younger","less 뒤 : 원급 young (younger 아님)"],rel=[[3,2,'mod','비교 대상']])
S['c13q1|6']={0:("【{k|The darker}","the + 비교급, the + 비교급 : ~할수록 더"),
 1:("the night sky {v|becomes},】","become + 형용사 : ~해지다"),
 3:("the stars {v|shine}.","shine : 빛나다 (1형식)")}
X['c13q1|6']=dict(pt=["the brightest","the + 비교급 짝 : 최상급 아님"],rel=[[0,2,'par','~할수록 더']],
 st=["비교급이 앞으로 나온다",["① 원래 문장 : the stars shine brighter","② 구문에서는 the brighter를 절 맨 앞에 둔다"]])
S['c13q1|7']={0:("The fitness club {v|is providing} membership plans","is providing : 현재진행형"),
 3:("{c|as} $14.99 a month.","as little as + 수치 : 적게는 ~만큼")}
S['c13q1|7'][2]=("{a|little}","little : 금액·양 (few는 셀 수 있는 명사)")
X['c13q1|7']=dict(pt=["few","금액은 양의 개념 : little (few 아님)"],rel=[[3,2,'eq','as ~ as']])
S['c13q1|8']={1:("an English poet","there be 구문 : be의 주어는 poet"),
 3:("{a|famous}","as + 원급 + as : poet을 꾸밈")}
X['c13q1|8']=dict(pt=["famously","poet을 꾸밈 : 형용사 famous"],rel=[[3,1,'mod','']])
S['c13q1|9']={1:("{a|quite}","not quite + 최상급 : 꼭 ~은 아닌"),
 4:("{c|but} it {v|was} pretty high.","but : 대조 / pretty : 꽤 (원급 강조)")}
X['c13q1|9']=dict(pt=["very","not very ~는 별로 ~않은 : 뜻이 다름"],rel=[[1,2,'mod','강조']])
S['c13q1|10']={2:("{a|as} fiercely","as + 부사 + as : blew를 꾸밈"),
 3:("{c|as} a hurricane {o|blows},","as절 : a hurricane 뒤 blows 생략"),
 4:("{c|so} many trees {v|fell down}.","so : 그래서 / fell down : 쓰러지다")}
X['c13q1|10']=dict(pt=["so","as ~ as 동등 비교 : so ~ as는 옛 표현"],rel=[[3,2,'eq','as ~ as']])
S['c13q1|11']={1:("a {a|more} essential tool for teamwork","a + 비교급 + 형용사 + 명사 어순"),
 2:("{c|than} {k|any other} thing.","!than any other + 단수 : 최상급의 뜻")}
X['c13q1|11']=dict(pt=["most","than 앞 : 비교급 more (most 아님)"],rel=[[2,1,'mod','비교 대상']])
S['c13q1|12']={0:("【{c|Once} groups {v|start} {p|to} do several cooperative activities,】","Once : 일단 ~하면 / start to V"),
 1:("group boundaries {v|melt away}","melt away : 사라지다 (구동사)"),
 4:("【{c|as} they {v|formed}】.","as절 : they = group boundaries")}
X['c13q1|12']=dict(pt=["rapid","melt away(동사)를 꾸밈 : 부사 rapidly"],rel=[[4,3,'eq','as ~ as']])
S['c13q2|1']={0:("The lake {v|has already frozen}","현재완료 : 이미 얼었다"),
 2:("{v|has become}","become + 형용사 : ~해지다")}
X['c13q2|1']=dict(pt=["colder","as ~ as 사이 : 원급 cold"],rel=[[4,3,'eq','as ~ as']])
S['c13q2|2']={1:("【{c|that} she {v|trains}","so ~ that : 너무 ~해서 …")}
S['c13q2|2'][0]=("Helen {v|loves} {p|to} exercise {k|so} much","to부정사 (명사적) : loves의 목적어")
X['c13q2|2']=dict(pt=["harder","as ~ as 사이 : 원급 hard"],rel=[[3,2,'eq','as ~ as']],
 st=["hard와 hardly",["① hard : 열심히 (형용사·부사 같은 모양)","② hardly : 거의 ~않다 (뜻이 전혀 다름)"]])
S['c13q2|3']={0:("The company {v|offers}","offer : 제시하다 / 목적어는 prices"),
 2:("{a|than}","more ~ than : ~보다 더 …한"),
 3:("its rivals {o|offer} in the market.","생략 : its rivals (offer)")}
S['c13q2|3'][3]=("its rivals in the market.","its rivals (offer) in the market 의미")
X['c13q2|3']=dict(pt=["that","비교급 more 뒤 : than (that 아님)"],rel=[[2,1,'mod','비교 대상']])
S['c13q2|4']={0:("Douglas {v|has been feeling}","현재완료 진행형 : 느끼고 있다"),
 1:("{a|much}","much : 비교급 happier 강조"),
 2:("happier","feel + 형용사 : ~하게 느끼다"),
 3:("{c|and} more stable","병렬 : happier와 more stable")}
X['c13q2|4']=dict(pt=["very","비교급 happier : very 강조 불가"],rel=[[1,2,'mod','비교급 강조'],[3,2,'par','병렬']])
S['c13q2|5']={0:("The second movie in the series {v|is}","in the series : movie를 꾸밈"),
 2:("in some aspects such as special effects","such as : ~와 같은 (예시)"),
 3:("{a|than}","better ~ than : ~보다 더 나은"),
 4:("the first one.","one = movie (같은 명사 대신)")}
X['c13q2|5']=dict(pt=["that","비교급 better 뒤 : than"],rel=[[3,1,'mod','비교 대상']])
S['c13q2|6']={0:("The Grand Canyon {v|is considered}","수동태 : 여겨진다"),
 1:("one of the","one of the + 최상급 + 복수명사"),
 3:("natural wonders in the world.","wonders : 복수명사 (one of 뒤)")}
X['c13q2|6']=dict(pt=["more impressive","one of the + 최상급 : most impressive"],rel=[[2,3,'mod','']],
 st=["긴 형용사의 최상급",["① 3음절 이상 : the most + 원급 (most impressive)","② 짧은 형용사 : the + -est (the tallest)"]])
S['c13q2|7']={0:("This new medicine {v|works}","work on : ~에 작용하다"),
 1:("{a|more effectively}","동사 works를 꾸밈 : 부사 비교급"),
 3:("{c|than} anything else 【{c|that} I{v|’ve tried}】.","목적격 관계대명사절 : anything else 꾸밈")}
X['c13q2|7']=dict(pt=["more effective","동사 works 꾸밈 : 부사 effectively"],rel=[[1,0,'mod',''],[3,1,'mod','비교 대상']])
S['c13q2|8']={1:("our relationship {v|will get}","get + 형용사 : ~해지다"),
 2:("{a|closer and closer}.","비교급 and 비교급 : 점점 더 ~")}
X['c13q2|8']=dict(pt=["close and close","비교급 and 비교급 : closer and closer"],rel=[[2,1,'eq','보어']])
S['c13q2|9']={0:("The painter {v|thought} 【{c|that} creativity {v|was}","that절 : thought의 목적어"),
 1:("{a|more valuable}","value 형용사 비교급 : more valuable"),
 3:("{c|than} {k|any other} skill】.","!than any other + 단수 : 최상급의 뜻")}
X['c13q2|9']=dict(pt=["most valuable","than이 있으므로 비교급 more valuable"],rel=[[3,1,'mod','비교 대상']])
S['c13q2|10']={1:("as {a|early}","as + 원급 + as possible"),
 3:("【{p|to} prevent the disease from {p|getting} worse】.","to부정사 (부사적) : 목적 / from + 동명사")}
S['c13q2|10'][0]=("The doctor {v|suggested} {p|starting} treatment","suggest + 동명사 : ~하는 것을 제안하다")
S['c13q2|10'][2]=("{c|as} possible","as ~ as possible : 가능한 한 ~하게")
X['c13q2|10']=dict(pt=["earlier","as ~ as 사이 : 원급 early"],rel=[[2,1,'eq','as ~ as']],
 st=["suggest + 동명사",["① suggest + 동명사 : ~하는 것을 제안하다","② suggest + to V는 쓰지 않는다"]])
S['c13q2|11']={0:("{p|Reading} this book {v|will give} you","동명사 주어 : 동사는 단수 취급"),
 1:("a more {a|complete}","a + more + 형용사 + 명사 어순"),
 4:("{c|than} that short article.","that = explanation")}
X['c13q2|11']=dict(pt=["completely","명사 explanation 꾸밈 : 형용사 complete"],rel=[[4,1,'mod','비교 대상']])
S['c13q2|12']={0:("Students 【{c|who} {v|formed} one positive habit】","주격 관계대명사절 : Students 꾸밈"),
 1:("{v|reported} less stress,","report : 보고하다 / 목적어 세 개"),
 3:("shorter","shorter : short의 비교급"),
 4:("hours of {p|watching} TV, {c|and} fewer dirty dishes.","병렬 : 보고한 세 가지 연결")}
X['c13q2|12']=dict(pt=["very","비교급 shorter : very 강조 불가"],rel=[[2,3,'mod','비교급 강조']])
