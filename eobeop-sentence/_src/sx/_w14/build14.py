# -*- coding: utf-8 -*-
import json,os
os.chdir('/home/claude/via/eobeop-sentence/_src/sx')
o=json.load(open('out/ch14.json',encoding='utf-8'))
U={}   # key -> {idx:[markup,memo]}
X={}   # key -> out2 entry
def u(k,**kw): U[k]={int(i[1:]):v for i,v in kw.items()}
def x(k,pt=None,rel=None,st=None):
    d={}
    if pt: d['pt']=pt
    d['rel']=rel or []
    if st: d['st']=st
    X[k]=d

# ---- POINT 1
k='c14p1|예제'
u(k,c1=["{k|there}","!there 도치 : 동사는 뒤의 진짜 주어(a way)에 일치"],c2=["{a|is} a way","there is ~ : ~가 있다"])
x(k,["are","진짜 주어 a way(단수) : is"],[[3,2,"mod","a way 꾸밈"]],
  ["there + be동사 + 주어",["① there is / are + 주어 : 동사는 뒤의 주어에 일치","② there + 일반동사(live, remain)도 같은 어순 : 동사 + 주어"]])
k='c14p1|1'
u(k,c0=["{k|Under the old oak tree}",""],c1=["{a|stood} a boy","!장소 부사구 + 동사 + 주어 : 도치"],c2=["with a worried look on his face.","with + 명사 : ~을 한 채"])
x(k,["a boy stood","장소 부사구가 앞 : stood + 주어(a boy)"],[[2,1,"mod","a boy 설명"]],
  ["장소 부사구 도치",["① 장소·방향 부사구 + 동사 + 주어 : 동사가 주어 앞으로","② 주어가 대명사면 도치 안 함 : Here she came."]])
k='c14p1|2'
u(k,c0=["{k|Important}",""],c1=["{a|was} the work","!보어 도치 : 보어 + 동사 + 주어"])
x(k,["the work was","보어 Important가 앞 : was + the work"],[[2,1,"mod","work 꾸밈"]])
k='c14p1|3'
u(k,c1=["the girl {a|sat}","주어 + 동사 : 평서문 어순"])
x(k,["sat the girl","정답 어순 : 주어 the girl + 동사 sat"],[[2,1,"mod",""]])
k='c14p1|4'
u(k,c1=["{k|there}",""],c2=["{a|are} families","there are + 복수 주어 families"])
x(k,["is","진짜 주어 families(복수) : are"],[[3,2,"mod","families 꾸밈"]])
k='c14p1|5'
u(k,c1=["{a|hang} paintings","!장소 부사구 뒤 도치 : 주어는 복수 paintings"],c2=["by a renowned artist, Pablo Picasso.","Pablo Picasso : artist와 동격"])
x(k,["hangs","주어 paintings(복수) : hang"],[[2,1,"mod","paintings 꾸밈"]],
  ["도치 문장의 수일치",["① 도치되어도 동사는 뒤에 오는 진짜 주어에 일치","② paintings(복수) : hang / a painting(단수) : hangs"]])
k='c14p1|6'
u(k,c0=["{k|Here}","!Here + 대명사 주어 : 도치 안 함"],c3=["【{p|playing} with my friends】.","spend + 시간 + -ing : ~하며 보내다"])
x(k,["spent I","주어가 대명사 I : Here I spent"],[[3,1,"mod","동시 동작"]],
  ["부사 here + 주어",["① Here + 동사 + 명사 주어 : Here comes the bus.","② 주어가 대명사면 도치 안 함 : Here he comes."]])
k='c14p1|7'
u(k,c0=["{k|Remarkably talented}",""],c1=["{a|is} the pianist","!보어 도치 : 보어 + 동사 + 주어"])
x(k,["the pianist is","보어가 앞 : is + 주어(the pianist)"],[[2,1,"mod","pianist 꾸밈"]])
k='c14p1|8'
u(k,c1=["{k|there}",""],c2=["{a|lived} a king","there + 일반동사 : ~가 살았다"])
x(k,["a king lived","there + 동사 + 주어 : lived a king"],[[3,2,"mod","장소"]])
# ---- POINT 2
k='c14p2|예제'
u(k,c0=["{k|Not only}",""],c1=["{a|did} Sarah sell the hair product,","!Not only 뒤 도치 : did + 주어 + 동사원형"],c2=["{c|but} she also {v|trained} women","not only A but also B : 절 두 개 병렬"])
x(k,["Sarah did","Not only 뒤 : did + 주어 + 동사원형"],[[1,2,"par","A but also B"]],
  ["부정어구 앞에 오면 도치",["① Not only / Never / Rarely / Little + 조동사 + 주어 + 동사","② 일반동사 문장은 do / does / did를 써서 도치"]])
k='c14p2|1'
u(k,c0=["{k|Rarely}",""],c1=["{a|could} John express his emotions,","!부정 부사 뒤 도치 : could + 주어 + 동사"],c2=["{c|but} now, true happiness {v|has appeared}","현재완료 : have + p.p. (now와 연결)"])
x(k,["John could","부정 부사 Rarely 뒤 : could + 주어"],[[1,2,"par","대조"]])
k='c14p2|2'
u(k,c0=["Actually, {k|never}",""],c1=["{a|had} we seen a whale so close,","!never 뒤 도치 : had + 주어 + p.p."],c2=["【{c|until} we {v|took} that trip to Alaska】.","until : ~할 때까지 (시간 부사절)"])
x(k,["we had","never 뒤 도치 : had we seen"],[[2,1,"mod","시간"]])
k='c14p2|3'
u(k,c0=["I {v|don’t like} broccoli,",""],c1=["{c|and} {k|neither}","!neither + 조동사 + 주어 : ~도 아니다"],c2=["{a|do} all my family members,","대동사 do : don’t like를 대신함"],c3=["【{c|even if} it{v|’s} good for our health】.","even if : 비록 ~일지라도 (양보절)"])
x(k,["all my family members do","neither 뒤 도치 : do + 주어"],[[2,0,"par","neither ~도"]],
  ["so / neither 도치",["① 긍정문 뒤 : So + 동사 + 주어 / 부정문 뒤 : Neither + 동사 + 주어","② 동사는 앞 문장의 동사에 맞춰 be / do / 조동사 선택"]])
k='c14p2|4'
u(k,c1=["{c|so}","so : 그래서 (뒤는 평서문 어순)"],c2=["she {a|is} having a good time","현재진행형 : is + -ing"])
x(k,["is she","접속사 so 뒤 평서문 어순 : she is"],[[2,0,"par","결과"]])
k='c14p2|5'
u(k,c0=["{k|Only} 【{c|when} Newton {v|placed} two prisms","!Only + 부사절 뒤 : 주절이 도치됨"],c2=["{a|did} he find something new.","did + 주어 + 동사원형 : find (found 아님)"])
x(k,["he found","Only when절 뒤 주절 : did he find"],[],
  ["Only + 부사(구·절) 도치",["① Only + 부사(구·절) + 조동사 + 주어 + 동사원형","② 도치되는 곳은 Only 절이 아니라 뒤의 주절"]])
# ---- POINT 3
k='c14p3|예제'
u(k,c0=["【{c|If} you {v|ask} unhappy people","If절 : ~하면 / ask + 사람 + 의문절"],c1=["【{c|what}","!간접의문문 : what + 주어 + 동사 어순"],c2=["they {a|think} about】】,","what + 불완전한 절 : about의 목적어"])
x(k,["do they think","간접의문문 : 의문사 + 주어 + 동사"],[],
  ["간접의문문 어순",["① 의문사 + 주어 + 동사 : what they think","② 직접 의문문은 의문사 + do + 주어 : what do they think?"]])
k='c14p3|1'
u(k,c0=["I {v|can stop} by your house tomorrow morning,","stop by : ~에 들르다"],c2=["{a|are} you going to be home at that time?","!직접 의문문 : be동사 + 주어 + going to"])
x(k,["you are","직접 의문문 : are + 주어 순서"],[[0,2,"par","but 대조"]])
k='c14p3|2'
u(k,c1=["【{c|if}","if = ~인지 : know의 목적어 (명사절)"],c2=["anyone {a|saw} a $20 bill on the counter","간접의문문 : if + 주어 + 동사 어순"])
x(k,["did anyone see","간접의문문 : 의문문 어순 아님"],[],
  ["if / whether : ~인지",["① 명사절을 이끄는 if / whether : ~인지 아닌지","② 명사절 안은 주어 + 동사 어순 (did 안 씀)"]])
k='c14p3|3'
u(k,c1=["the tourists {a|would} see","see의 목적어가 What : 불완전한 절"],c2=["during their visit to the town】","during + 명사 : ~ 동안"])
x(k,["would the tourists","명사절 안은 주어 + 조동사 어순"],[[2,1,"mod","기간"]])
k='c14p3|4'
u(k,c1=["{c|where}","의문사 : 장소를 묻는다"],c2=["{a|did} you leave it?","!직접 의문문 : 의문사 + did + 주어 + 동사원형"])
x(k,["you left","if절 뒤 주절 : where did you leave"],[[0,2,"mod","조건"]])
k='c14p3|5'
u(k,c1=["they {v|want} 【{p|to} know","want to V : to부정사 (명사적) 목적어"],c3=["it {a|has} a vegetarian menu】】.","whether절 : 평서문 어순 (it has)"])
x(k,["does it have","명사절 whether : 주어 + 동사 순서"],[])
# ---- q1
k='c14q1|1'
u(k,c0=["{k|To the top of the stairs}",""],c1=["{a|climbed} the group","!방향 부사구 뒤 도치 : 동사 + 주어"],c2=["for a picture.","for : ~을 위해 (목적)"])
x(k,["the group climbed","방향 부사구가 앞 : 동사 + 주어(the group)"],[[2,1,"mod","목적"]])
k='c14q1|2'
u(k,c1=["the interviewer {v|may ask}","may : ~일지도 모른다"],c2=["【{c|how}","간접의문문 : ask의 목적어"],c3=["you {a|handle}","!how + 주어 + 동사 : 평서문 어순"])
x(k,["do you handle","간접의문문 : how + 주어 + 동사"],[])
k='c14q1|3'
u(k,c0=["{k|Never}",""],c1=["{a|have} I seen","!never 뒤 도치 : have + 주어 + p.p."],c2=["such an amazing view","such ~ as ... : ...만큼 그렇게 ~한"],c3=["{c|as} the {k|one} from this tower.","!one = view : 앞 명사를 대신 받는 말"])
x(k,["I have","Never 뒤 도치 : have I seen"],[[3,2,"mod","비교 대상"]],
  ["부정어 Never 뒤 도치",["① Never + have / has / had + 주어 + p.p.","② 현재완료·과거완료는 첫 조동사만 주어 앞으로"]])
k='c14q1|4'
u(k,c1=["{k|there}",""],c2=["{a|must be} galaxies","there + must be : ~가 있음이 틀림없다"])
x(k,["must are","조동사 뒤는 동사원형 : must be"],[[3,2,"mod","galaxies 꾸밈"]])
k='c14q1|5'
u(k,c0=["【{c|If} Ms. Bennet {v|went out} to lunch】,","If절 : ~했다면 / went out : 외출했다"],c1=["{c|when} {a|does} she return","!의문사 + does + 주어 : 직접 의문문"])
x(k,["she returns","직접 의문문 : when does she return"],[[0,1,"mod","조건"]])
k='c14q1|6'
u(k,c0=["My parents {v|think}",""],c1=["【{o|that} I {v|should start} {p|doing} ballet every day】,","that 생략 : think의 목적어절"],c2=["{c|and} {k|so}","!so + 동사 + 주어 : ~도 그렇다"],c3=["{a|does} my teacher.","대동사 does : thinks를 대신함"])
x(k,["is my teacher","앞 문장 동사 think : so does + 주어"],[[3,0,"par","so ~도"]])
k='c14q1|7'
u(k,c1=["{k|here}","!here + 대명사 주어 : 도치 안 함"],c3=["【{p|running} down the hill】.","분사구문 : 동시 동작 (she를 꾸밈)"])
x(k,["came she","대명사 주어 she : here she came"],[[3,2,"mod","she 설명"]],
  ["here / there 도치의 조건",["① 주어가 명사 : Here comes the bus.","② 주어가 대명사 : Here she comes. (도치 안 함)"]])
k='c14q1|8'
u(k,c0=["The food of the restaurant {v|is} delicious,",""],c1=["{c|but} {k|even} more excellent","!even + 비교급 : 훨씬 더 (비교급 강조)"],c2=["{a|is} the interior.","!보어 도치 : 보어 + 동사 + 주어"])
x(k,["the interior is","보어가 앞 : is + the interior"],[[1,0,"par","대조"]])
k='c14q1|9'
u(k,c0=["{k|Hardly}",""],c1=["{a|had} I walked","!Hardly 뒤 도치 : had + 주어 + p.p."],c3=["【{c|when} it {v|began} {p|to} rain】.","Hardly ~ when ... : ~하자마자 ...했다"])
x(k,["I had","Hardly 뒤 : had I walked"],[[1,3,"par","Hardly ~ when"]],
  ["Hardly ~ when 구문",["① Hardly + had + 주어 + p.p. ~ when + 과거 : ~하자마자 ...했다","② No sooner ~ than 도 같은 뜻 (than을 씀)"]])
k='c14q1|10'
u(k,c0=["{k|It} {v|is} not clear","!가주어 it : 진짜 주어는 뒤의 if절"],c1=["【{c|if}","if = ~인지 : 명사절 (whether)"],c2=["the new product {a|will be}","if절 안 : 주어 + will be 순서"])
x(k,["will the new product be","if절 안 : 주어 + will be 순서"],[])
k='c14q1|11'
u(k,c1=["{a|sat} a traveler,","!장소 부사구 뒤 도치 : 동사 + 주어"],c2=["【{p|being} tired of heat and thirst】.","분사구문 : 이유 (a traveler를 설명)"])
x(k,["a traveler sat","장소 부사구가 앞 : sat + a traveler"],[[2,1,"mod","분사구문"]])
k='c14q1|12'
u(k,c0=["{k|Not only}",""],c1=["{a|does} motivation create energy,","!Not only 뒤 도치 : does + 주어 + 동사원형"],c2=["{c|but} it also {v|helps}","not only A but also B : 병렬"])
x(k,["motivation creates","Not only 뒤 : does + 주어 + 동사원형"],[[1,2,"par","A but also B"]],
  ["not only A but also B",["① A와 B는 문법적으로 같은 형태 (병렬)","② Not only가 문장 앞이면 A 부분만 도치 : does + 주어"]])
# ---- q2
k='c14q2|1'
u(k,c0=["【{c|As} the hikers {v|walked}","As + 절 : ~하면서 (동시 진행)"],c1=["deeper and deeper into the forest】,","비교급 and 비교급 : 점점 더 ~"],c3=["【{c|where}","간접의문문 : wondered의 목적어"],c4=["the trail {a|would} lead】.","!where + 주어 + 동사 : 평서문 어순"])
x(k,["would the trail","간접의문문 : where + 주어 + would lead"],[])
k='c14q2|2'
u(k,c1=["{k|there}",""],c2=["{a|remain} boxes","!there + 일반동사 : 주어는 복수 boxes"],c3=["full of old memories","형용사구 : boxes를 꾸밈"],c4=["such as diaries, letters, and pictures.","such as A, B, and C : 예시 나열 (병렬)"])
x(k,["remains","주어 boxes(복수) : remain"],[[3,2,"mod","boxes 꾸밈"]])
k='c14q2|3'
u(k,c0=["{k|Only} 【{c|when} the sun {v|sets}】","!Only + 부사절 뒤 : 주절 도치"],c1=["{a|does} the city come","come alive : 활기를 띠다"],c2=["alive with bright lights","with A and B : A와 B로 (병렬)"])
x(k,["the city comes","Only when절 뒤 : does the city come"],[[3,2,"par","lights/people"]])
k='c14q2|4'
u(k,c0=["{k|Very skilled}",""],c1=["{a|was} the magician,","!보어 도치 : 보어 + 동사 + 주어"])
x(k,["the magician was","보어가 앞 : was + the magician"],[[1,2,"par","원인과 결과"]])
k='c14q2|5'
u(k,c0=["【{c|Before} you {v|transfer} to another college】,","Before + 절 : ~하기 전에"],c1=["{a|have} you","!의문문 : have + 주어 + p.p. (현재완료)"],c2=["considered {p|changing} your major instead?","consider + 동명사 : ~을 고려하다"])
x(k,["you have","의문문 : 조동사 have가 주어 앞으로"],[])
k='c14q2|6'
u(k,c1=["{c|so}","so : 그래서 (결과)"],c2=["he {a|hates}","so 뒤 : 평서문 어순"])
x(k,["hates he","접속사 so 뒤 평서문 어순 : he hates"],[[3,2,"mod",""]])
k='c14q2|7'
u(k,c0=["{k|Little}","!Little : 거의 ~않다 (부정어)"],c1=["{a|did} Robert realize","!Little 뒤 도치 : did + 주어 + 동사원형"],c2=["【{c|that} his simple act of kindness","that절 : realize의 목적어 (명사절)"],c3=["{v|would have} a great impact","have an impact on : ~에 영향을 미치다"])
x(k,["Robert realized","Little 뒤 : did + 주어 + 동사원형"],[])
k='c14q2|8'
u(k,c1=["{a|lie} creatures","!장소 부사구 뒤 도치 : 주어는 복수 creatures"],c2=["【{c|that} {v|feed} on dead plants and animals","주격 관계대명사절 : creatures를 꾸밈"],c3=["{c|and} {v|keep} the forest clean】.","병렬 : feed와 keep / keep + O + 형용사"])
x(k,["lies","주어 creatures(복수) : lie"],[[2,1,"mod","creatures 꾸밈"],[2,3,"par","병렬"]])
k='c14q2|9'
u(k,c1=["the client {a|received} Rebecca’s email】","whether + 주어 + 동사 : 평서문 어순"],c2=["{v|is} uncertain 【{c|because} she {v|didn’t receive} any reply】.","because절 : 이유 (부사절)"])
x(k,["did the client receive","whether절 : 주어 + 동사 순서"],[])
k='c14q2|10'
u(k,c1=["two drivers {a|were} having","과거진행형 : 주어(복수) + were + -ing"])
x(k,["were two drivers","진행형은 주어 + were + -ing 어순"],[])
k='c14q2|11'
u(k,c0=["{k|Rarely}",""],c1=["{a|can} I reach","!Rarely 뒤 도치 : can + 주어 + 동사원형"],c2=["Melissa over the phone,","over the phone : 전화로"],c3=["{c|so} I usually {v|send} her a text message.","send + 간접목적어 + 직접목적어 (4형식)"])
x(k,["I can","Rarely 뒤 : can + 주어 + 동사원형"],[[1,3,"par","결과"]])
k='c14q2|12'
u(k,c0=["【{c|When} you {v|face} difficult challenges】,","When + 절 : ~할 때"],c2=["with yourself about your weaknesses?","honest with A about B : A에게 B에 솔직한"])
x(k,["you are","의문문 : be동사 + 주어"],[[0,1,"mod","시간"]])
# ---- s1
k='c14s1|1-(A)'
u(k,c0=["【{c|If} you {v|could move} to any city in the world】,","가정법 과거 : If + 과거, 조동사 과거"],c1=["{c|where} (A)","의문사 : 장소를 묻는다"],c2=["{a|would} you go?","!의문사 + would + 주어 + 동사원형"])
x(k,["you would","직접 의문문 : where would + 주어 + go"],[[0,2,"mod","조건"]])
k='c14s1|1-(B)'
u(k,c0=["{k|Little} (B)","Little : 거의 ~않다 (부정어)"],c1=["{a|do} some people know","!Little 뒤 도치 : do + 주어 + 동사원형"])
x(k,["some people do","Little 뒤 : do + 주어 + 동사원형"],[])
k='c14s1|2-(A)'
u(k,c0=["{k|So embarrassed} (A)",""],c1=["{a|was} Catherine","!보어 도치 : So + 형용사 + 동사 + 주어"])
x(k,["Catherine was","So embarrassed 뒤 : was + 주어"],[[2,1,"mod","때"]],
  ["So + 형용사 문두 도치",["① So + 형용사 + 동사 + 주어 : 매우 ~해서","② 보어(형용사)가 문장 앞으로 나가면 동사와 주어가 뒤바뀐다"]])
k='c14s1|2-(B)'
u(k,c2=["nobody {a|had} informed her","why + 주어 + 동사 : 평서문 어순"],c3=["about the sudden change in the schedule】.","inform + 사람 + about : ~에 대해 알리다"])
x(k,["had nobody","간접의문문 : why + 주어 + 동사 순서"],[])
k='c14s1|3-(A)'
u(k,c1=["oil {a|is} imported","수동태 : be + p.p. (수입되다)"])
x(k,["is oil","수동태 평서문 : 주어 oil + is imported"],[[2,1,"mod","from"]])
k='c14s1|3-(B)'
u(k,c1=["{k|so} (B)","!so + 동사 + 주어 : ~도 그렇다"],c2=["{a|does} the price","대동사 does : goes up을 대신함"])
x(k,["the price does","so 뒤 도치 : so does + 주어"],[[2,0,"par","so ~도"]])
k='c14s1|4-①'
u(k,c1=["{a|stood} a {p|locked} door,","!장소 부사구 뒤 도치 : 동사 + 주어"],c2=["【{p|leaving} Edgar curious】.","분사구문 : 결과 (leave + O + 형용사)"])
x(k,["a locked door stood","장소 부사구 뒤 : stood + 주어"],[[2,1,"mod","분사구문"]])
k='c14s1|4-②'
u(k,c2=["his sister {a|knew}","whether + 주어 + 동사 : 평서문 어순"])
x(k,["did his sister know","whether절 : 주어 + 동사 순서"],[])
k='c14s1|5-①'
u(k,c1=["{k|not only}",""],c2=["{a|does} it become","!not only 뒤 도치 : does + 주어 + 동사원형"],c3=["easier, {c|but} you {v|can do} other things more easily as well.","not only A but B : A뿐 아니라 B도"])
x(k,["it becomes","not only 뒤 : does + 주어 + 동사원형"],[[2,3,"par","A but B"]])
k='c14s1|5-②'
u(k,c1=["{k|there}",""],c3=["of achievement 【{c|as} you {v|experience} the positive impact of this one habit on various aspects of your life】.","as : ~함에 따라 (시간 부사절)"])
x(k,["can been","조동사 can 뒤에는 동사원형 be"],[])
k='c14s1|6-1'
u(k,c0=["My friends {c|and} I","병렬 : My friends와 I (주어 두 개)"])
x(k,["drive up","last summer(과거) : 과거형 drove"],[])
k='c14s1|6-①'
u(k,c0=["{k|Only} 【{c|when} we {v|got} to the top of the mountain】","!Only + 부사절 뒤 : 주절 도치"],c1=["{a|did} I remember","did + 주어 + 동사원형 : remember"],c2=["【{c|that} I {v|had been} there before】.","that절 : remember의 목적어 (대과거)"])
x(k,["I remembered","Only when절 뒤 : did + 주어 + 동사원형"],[])
k='c14s1|6-3'
u(k,c1=["the last time {o|when} 【I {v|was} at the mountain】,","!관계부사 when 생략 : the last time 꾸밈"],c2=["it","비인칭 주어 it : 날씨·계절"])
x(k,["is","지난번(과거)의 일 : 과거형 was"],[[1,3,"mod","때"]])
k='c14s1|6-②'
u(k,c1=["{k|there}","!부사 there + 대명사 주어 : 도치 안 함"],c3=["snow for the very first time in my life.","the very first time : 처음으로"])
x(k,["saw I","대명사 주어 I : there I saw"],[])
# ---- add
k='add14|1-1'
u(k,c1=["{a|traveled}","!장소 부사구 뒤 도치 : 동사 + 주어"],c3=["from across Asia {c|and} Europe,","전치사구 : people을 꾸밈 (병렬)"])
x(k,["people traveled","장소 부사구 뒤 : 동사 + 주어"],[[3,2,"mod","people 꾸밈"],[4,2,"mod","people 꾸밈"]],
  ["장소 부사구 + 자동사",["① 장소 부사구 + 자동사(travel, live, stand) + 주어","② 주어가 길면 뒤로 보내 문장이 읽기 쉬워진다"]])
k='add14|1-2'
u(k,c1=["{v|arrived} in Salt Lake Valley in 1847,",""],c2=["{c|and} {k|here}","!부사 here + 대명사 주어 : 도치 안 함"])
x(k,["built they","대명사 주어 they : here they built"],[])
k='add14|1-3'
u(k,c2=["{a|waited}","wait for : ~을 기다리다"],c3=["for hours","for + 기간 : ~ 동안"])
x(k,["waited fans","문장 어순 : 주어 fans + 동사 waited"],[[4,2,"mod",""]])
k='add14|1-4'
u(k,c1=["{k|there}",""],c4=["with a long neck {c|and} tail.","전치사구 : dinosaur를 꾸밈 (병렬)"])
x(k,["lives","Over 200 million years ago : 과거형 lived"],[[4,3,"mod","dinosaur 꾸밈"]])
k='add14|1-5'
u(k,c0=["{k|Incredibly skilled}",""],c1=["{a|were}","!보어 도치 : 보어 + 동사 + 주어(the pilots)"],c3=["thanks to their training","thanks to + 명사 : ~ 덕분에"])
x(k,["was","주어 the pilots(복수) : were"],[[4,3,"mod","training 꾸밈"]])
k='add14|2-1'
u(k,c5=["{k|neither}","!neither + 조동사 + 주어 : ~도 아니다"],c6=["{a|could}","대동사 could : could not go out 대신"],c7=["ours.","ours = our boats (소유대명사)"])
# note: indices below fixed after check
x(k,["ours could","neither 뒤 도치 : could + 주어(ours)"],[[6,2,"par","neither ~도"]])
k='add14|2-2'
u(k,c0=["{k|Hardly}","!Hardly 뒤 도치 : have + 주어 + p.p."],c1=["{a|have}","현재완료 : have + p.p."],c4=["【{c|since} she {v|started} a job in the city】.","since절 : ~한 이래로"])
x(k,["we have","Hardly 뒤 도치 : have we seen"],[[4,3,"mod","시작 시점"]])
k='add14|2-3'
u(k,c2=["{c|so}","so : 그래서 (결과)"],c4=["{a|closes}","!so 뒤 평서문 어순 : 도치 아님"],c5=["it most afternoons.","most afternoons : 대부분의 오후에"])
x(k,["does he close","접속사 so 뒤 평서문 어순 : he closes"],[[4,1,"par","결과"]])
k='add14|2-4'
u(k,c0=["{k|Never}","!Never 뒤 도치 : did + 주어 + 동사원형"])
x(k,None,[[4,3,"mod","think 목적어"]],
  ["Never + did + 주어 + 동사원형",["① 일반동사 문장의 Never 도치 : did + 주어 + 동사원형","② 시제는 did가 나타낸다 : think (thought 아님)"]])
k='add14|2-5'
u(k,c1=["{a|will}","!주절 도치 : will + 주어 + 동사원형"],c3=["{v|allow} the students",""],c4=["【{p|to} plan a camping trip】.","!allow + O + OC(to V) : 허락의 5형식"])
x(k,["the school will","Only if절 뒤 : will + 주어 + 동사원형"],[[4,3,"eq","목적격 보어"]],
  ["Only if 조건절 도치",["① Only if + 절 + 조동사 + 주어 + 동사원형","② Only if절 자체는 평서문 어순 : their parents agree"]])
k='add14|3-1'
u(k,c3=["{v|was}","보어 자리에 명사절 how절이 온다"],c4=["【{c|how}","간접의문문 : was의 보어"],c6=["get home】.","get home : 집에 도착하다"])
x(k,["would we","간접의문문 : how + 주어 + would + 동사"],[[4,3,"eq","보어"]])
k='add14|3-2'
u(k,c1=["【{c|whether}","명사절 : wondering의 목적어 (~인지)"],c3=["a towel {o|that} 【I {v|could borrow}】】,","!목적격 관계대명사 that 생략 : towel 꾸밈"])
x(k,["do you have","whether절 : 주어 + 동사 순서"],[])
k='add14|3-3'
u(k,c0=["【{c|If} you{v|’re going away} this weekend】,","go away : 떠나다"],c2=["{a|should}","!의문사 + should + 주어 : 직접 의문문"])
x(k,["I should","직접 의문문 : when should + 주어 + 동사"],[[0,2,"mod","조건"]])
k='add14|3-4'
u(k,c2=["{v|asked} the hotel manager","ask + 사람 + 의문절 : 4형식"],c4=["he {a|might}","!what + 주어 + 동사 : 평서문 어순"])
x(k,["might he","간접의문문 : what + 주어 + might + 동사"],[])
k='add14|3-5'
u(k,c0=["【{c|Until} there {v|is} an announcement】,","Until절 : ~할 때까지"],c5=["{c|as} {o|it is} scheduled】.","!as 뒤 '주어 + be' 생략 : as (it is) scheduled"])
x(k,["does the event start","if절 : 주어 + 동사 어순 (직접 의문문 아님)"],[])

for key,d in U.items():
    assert key in o,key
    for i,v in d.items(): o[key][i]=v
json.dump(o,open('out/ch14.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
os.makedirs('out2',exist_ok=True)
json.dump(X,open('out2/ch14.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(U),len(X))
