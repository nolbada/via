# -*- coding: utf-8 -*-
D={}
def A(key,O,pt,rel=(),st=None): D[key]=(O,pt,list(rel),st)

A('c06p1|예제',{0:('{k|It} {v|is} so important','가주어 It : to recognize ~가 진짜 주어'),2:(None,'!목적격 관계대명사 + 불완전한 문장 (have 뒤 목적어 없음)')},
  ['recognizes','진주어는 to부정사 : 동사 자리 아님'],[[2,1,'mod','impacts 꾸밈'],[1,0,'eq','진주어']],
  ['가주어 It과 진주어',['① It is + 형용사 + to V : to V가 진짜 주어 (~하는 것은)','② 진주어 자리에 3인칭 동사(recognizes)는 올 수 없다']])
A('c06p1|1',{1:'병렬 : masks와 gloves 연결',2:(None,'!동사 wear가 이미 있다 : 목적은 to V')},
  ['prevents','본동사 wear가 이미 있다 : 목적은 to V'],[[2,1,'mod','목적']],
  ['한 문장의 본동사',['① 본동사는 접속사 없이 두 개 쓸 수 없다','② 목적(~하기 위해)은 to V로 나타낸다 : wear ~ to prevent']])
A('c06p1|2',{3:'병렬 : swings와 slides 연결'},
  ['playing','문장의 본동사 자리 : -ing는 동사 불가'],[[1,0,'mod','']],
  ['동사 자리 찾기',['① 주어 뒤 전치사구(in the park)를 지우면 동사 자리가 보인다','② 동사 자리에는 시제와 수가 있는 동사(play)를 쓴다','③ -ing나 to V는 혼자서는 동사가 될 수 없다']])
A('c06p1|3',{2:(None,'!pouring은 수식어 : 본동사는 따로 필요'),3:'soak + 목적어 : ~을 흠뻑 적시다'},
  ['soaking','pouring이 수식어라 본동사가 따로 필요'],[[1,0,'mod','']])
A('c06p1|4',{0:(None,'동명사구 : 문장의 주어 (단수 취급)'),1:(None,'!목적격 관계대명사 + 불완전한 문장 (buy 뒤 목적어 없음)')},
  ['restrict','동사 increases가 있다 : 주어는 동명사'],[[1,0,'mod','items 꾸밈']])
A('c06p1|5',{0:(None,'동명사 : 주어 역할 (~하는 것)'),3:'during + 명사 : ~ 동안'},
  ['remember','a helpful way 뒤 : 형용사적 to부정사'],[[2,1,'mod','way 꾸밈']],
  ['명사를 꾸미는 to부정사',['① 명사 + to V : ~할 (명사) (a way to remember : 기억할 방법)','② 명사 바로 뒤에 동사원형이 오면 어법상 틀리다']])
A('c06p1|6',{1:'be proud of + 동명사 : ~을 자랑스러워하다',3:'병렬 : supporting과 giving back 연결'},
  ['support','전치사 of 뒤 : 동명사 (원형 불가)'],[[3,2,'par','병렬']],
  ['전치사 뒤의 형태',['① 전치사 + 동명사 : proud of(자랑스러운) supporting','② 전치사 뒤에 동사원형·to V는 쓰지 않는다']])
A('c06p1|7',{2:(None,'!주어는 복수 diseases : 동사 kill'),4:'병렬 : the fish와 wild fish 연결'},
  ['kills','주어 The diseases가 복수 : s 안 붙임'],[[1,0,'mod',''],[4,3,'par','A뿐 아니라 B도']])
A('c06p1|8',{2:(None,'동명사구 : 보어 역할 (~하는 것)')},
  ['improves','이미 동사 is가 있다 : 보어는 동명사'],[[1,0,'mod','benefit 꾸밈']])
A('c06p2|예제',{0:(None,'조건 부사절 : continue + to V (계속 ~하다)'),3:(None,'!stop + 동명사 : ~하는 것을 멈추다')},
  ['to use','stop + 동명사 : ~하는 것을 멈추다'],[[0,2,'mod','조건']],
  ['stop의 두 가지 목적어',['① stop + 동명사 : ~하는 것을 멈추다 (stop using)','② stop + to V : ~하려고 멈추다 (stop to rest : 쉬려고 멈추다)']])
A('c06p2|1',{1:'decide + to V : ~하기로 결정하다',3:'전치사 to + 명사 (to V의 to 아님)'},
  ['going','decide + to V : ~하기로 결정하다'],[],
  ['to V만 취하는 동사',['① decide(결정하다) hope(바라다) plan(계획하다) want(원하다)','② 이 동사 뒤에 동명사는 쓸 수 없다 : decided going (X)']])
A('c06p2|2',{3:(None,'!시간 부사절은 미래 대신 현재형 arrive')},
  ['to clean','finish + 동명사 : ~하는 것을 끝내다'],[[3,1,'mod','']],
  ['동명사만 취하는 동사',['① finish(끝내다) enjoy(즐기다) avoid(피하다) mind(꺼리다)','② give up(포기하다) put off(미루다) consider(고려하다)','③ 이 동사들 뒤에 to V는 쓰지 않는다']])
A('c06p2|3',{1:(None,'refuse + to V : ~하기를 거부하다'),3:(None,'이유 부사절 : ~하기 때문에')},
  ['eating','refuse + to V : ~하기를 거부하다'],[[3,1,'mod','이유']])
A('c06p2|4',{0:('【{o|Being} {p|Based} on a 2019 survey,】','분사구문 : (Being) Based on ~에 근거하면'),4:(None,'시간 부사절 : ~하기 전에')},
  ['to play','quit + 동명사 : ~하기를 그만두다'],[],
  ['그만두다·포기하다 + 동명사',['① quit(그만두다) give up(포기하다) stop(멈추다) + 동명사','② quit to play는 쓰지 않는다 : 그만두는 대상이 동작이기 때문']])
A('c06p2|5',{1:(None,'!stop + to V : ~하기 위해 멈추다 (목적)'),3:(None,'시간 부사절 : before + 주어 + 동사')},
  ['getting','stop to V : ~하려고 멈추다 (목적)'],[[3,1,'mod','']])
A('c06p2|6',{1:'choose + to V : ~하기로 선택하다',3:(None,'rather than : A보다는 B, 뒤 to work는 병렬')},
  ['starting','choose + to V : ~하기로 선택하다'],[[3,2,'par','병렬']])
A('c06p2|7',{2:(None,None),3:'to부정사 (부사적) : 목적 ~하기 위해'},
  ['to renovate','consider + 동명사 : ~을 고려하다'],[[3,1,'mod','목적']],
  ['consider의 목적어',['① consider(고려하다) + 동명사 : ~하는 것을 고려하다','② to V는 뒤에서 목적(~하기 위해)을 나타내는 부사적 용법이다']])
A('c06p2|8',{1:(None,'mind + 동명사 : ~하는 것을 꺼리다'),3:(None,'for A to V : A가 ~하기를 (의미상 주어)')},
  ['to wait','mind + 동명사 : ~을 꺼리다'],[])
A('c06p3|예제',{2:(None,'forget + to V : ~할 것을 잊다'),4:(None,'양보 부사절 : 안에 시간절 when you were born')},
  ['taking','forget + to V : 앞으로 할 일을 잊다'],[[4,2,'mod','양보']],
  ['forget의 두 가지 의미',['① forget + to V : ~할 것을 잊다 (아직 안 한 일)','② forget + 동명사 : ~한 것을 잊다 (이미 한 일)','③ 문장은 사진을 찍지 않았다는 뜻이라 to V']])
A('c06p3|1',{1:(None,'remember + 동명사 : ~한 것을 기억하다'),3:'repeatedly : 반복해서'},
  ['to watch','remember + 동명사 : 이미 한 일을 기억'],[],
  ['remember의 두 가지 의미',['① remember + 동명사 : ~한 것을 기억하다 (이미 한 일)','② remember + to V : ~할 것을 기억하다 (앞으로 할 일)']])
A('c06p3|2',{1:(None,'start : 동명사·to부정사 둘 다 가능')},
  ['plan','start 뒤 : to V나 동명사 (원형 불가)'],[])
