# -*- coding: utf-8 -*-
# CH08 등위·상관접속사와 병렬구조 -- 개념 POINT 1~3 (교재 p.94~95)
def I(t, ans, ko, why, st=None, ex='', hard=False, **kw):
    d = dict(t=t, ans=ans, ko=ko, why=why, st=st or [], ex=ex, hard=hard)
    d.update(kw)
    return d
A_ = lambda x: ('s', '짝 A', x)
B_ = lambda x: ('s', '짝 B', x)
C_ = lambda x: ('s', '짝 C', x)
J_ = lambda x: ('c', '접속사', x)
N_ = lambda x: ('m', '참고', x)

P = {}

# ===== POINT 1 : 동사 병렬 =====
P[1] = dict(
 page='p.94', freq='★★☆', title='동사 병렬',
 formula=[('v', '동사'), ('c', '+ and / but / (n)or +'), ('v', '동사')],
 rule='<b>and / but / or</b>는 <b>같은 모양끼리</b> 이어 주는 말이에요. 동사는 <b>동사끼리</b>만 이어지고, 동사와 -ing·to 같은 준동사(동사에서 나온 다른 모양)는 이을 수 없어요.',
 kinds=['<b>조동사 뒤 동사원형끼리</b> &nbsp;can start ~ and receive ~ (can 뒤에 동사원형이 두 개)',
        '<b>시제 맞추기</b> &nbsp;accepted, asked, or refused (과거 동사는 과거 동사끼리)',
        '<b>수 일치 맞추기</b> &nbsp;watches ~ or walks ~ (주어가 한 명이면 -s 동사끼리)',
        '<b>명령문끼리</b> &nbsp;Cut ~ and start ~ (동사원형으로 시작하는 문장 두 개)'],
 steps=['and / but / or에 동그라미를 친다.', '접속사 앞에서 같은 역할을 하는 동사를 찾아 짝을 맞춘다. (뜻으로 묶이는 덩어리 구분!)', '짝이 된 동사의 모양(원형 / 시제 / -s)을 똑같이 맞춘다.'],
 ex=('1_ex', dict(
   t='You can <S>start</S> working a month earlier <C>and</C> [receive|receiving] a larger bonus for doing so.', ans='receive',
   ko='당신은 한 달 일찍 일하는 것을 시작하고 그렇게 하는 것에 대해 더 큰 보너스를 받을 수 있다.',
   why='조동사 <b>can</b> 뒤에 동사원형 <b>start</b>(start: 시작하다)가 있고, and가 이 start와 짝이 될 동사를 이어 줘요. 그래서 동사원형 <b>receive</b>(receive: 받다)가 맞아요. receiving은 동사가 아니라 준동사라서 start와 짝이 될 수 없어요.',
   st=[A_('start'), J_('and'), B_('receive (동사원형)')],
   ex='<b>working a month earlier</b>의 working은 start 뒤에 온 목적어(~하는 것)예요. receive의 짝은 working이 아니라 start예요. 이렇게 <b>무엇과 무엇이 짝인지</b> 덩어리를 가려내는 게 중요해요. <b>for doing so</b>는 &ldquo;그렇게 하는 것에 대해&rdquo;.')),
 groups=[
  ('a', '둘 중 어법에 맞는 것을 고르시오.  (교재 94쪽 1~4번)', [
   (1, I('I could <S>see</S> the fireworks from the roof of my building <C>and</C> [take|taking] pictures of them.', 'take',
     '나는 내 건물 지붕에서 불꽃놀이를 보고 사진을 찍을 수 있었다.',
     '<b>could</b> 뒤에 동사원형 <b>see</b>(see: 보다)가 있고, and 뒤의 동사도 같은 could에 이어져요. 그래서 동사원형 <b>take</b>(take: (사진을) 찍다)가 맞아요. taking은 준동사라서 동사 see와 짝이 될 수 없어요.',
     [A_('see'), J_('and'), B_('take (동사원형)')],
     '<b>take pictures</b>는 &ldquo;사진을 찍다&rdquo;예요. pictures of them의 them은 fireworks(불꽃놀이)를 가리켜요.')),
   (2, I('After an important exam, Tim usually either <S>gets</S> some rest <C>or</C> [go|goes] downtown to meet his friends.', 'goes',
     '중요한 시험 후에, Tim은 보통 휴식을 취하거나 친구들을 만나러 시내에 간다.',
     '<b>either A or B</b>(A와 B 둘 중 하나)에서 A는 <b>gets</b>(get: 취하다)예요. 주어 Tim은 한 명이라서 동사에 -s가 붙은 단수동사예요. 그래서 B도 단수동사 <b>goes</b>(go: 가다)로 맞춰요.',
     [A_('gets (단수동사)'), J_('either ~ or'), B_('goes (단수동사)')],
     '<b>to meet his friends</b>는 &ldquo;친구들을 만나러&rdquo;(목적)라는 뜻이에요. downtown은 &ldquo;시내에&rdquo;.')),
   (3, I('The groups of workers <S>accepted</S> the new policy, <S>asked</S> the company to change it, <C>or</C> [refuse|refused] it.', 'refused',
     '노동자 집단들은 새 정책을 받아들이거나, 회사에 그것을 바꾸라고 요청하거나, 그것을 거부했다.',
     '<b>accepted</b>(accept: 받아들이다)와 <b>asked</b>(ask: 요청하다)가 둘 다 과거 동사예요. or 뒤에도 과거 동사 <b>refused</b>(refuse: 거부하다)로 시제를 맞춰요. 세 개를 나열할 때는 마지막 앞에 and / or를 써요.',
     [A_('accepted (과거)'), B_('asked (과거)'), J_('or'), C_('refused (과거)')],
     '<b>ask A to V</b>는 &ldquo;A에게 V하라고 요청하다&rdquo;예요. asked the company to change it = 회사에 그것을 바꾸라고 요청했다.')),
   (4, I('Brown lines <S>run</S> along the backs of the amazing lizards <C>and</C> [continue|continuing] down their tails.', 'continue',
     '갈색 선들이 그 놀라운 도마뱀들의 등을 따라 이어지고, 꼬리로 계속 내려간다.',
     '주어 <b>Brown lines</b>(복수)의 동사는 <b>run</b>(run: 이어지다, 뻗다)이에요. and로 이어지는 동사도 같은 주어의 동사라서 복수 현재 동사 <b>continue</b>(continue: 계속되다)가 맞아요. continuing은 동사가 될 수 없어요.',
     [A_('run (복수 동사)'), J_('and'), B_('continue (복수 동사)')],
     '<b>down their tails</b>는 &ldquo;꼬리 쪽으로 내려가며&rdquo;라는 방향을 말하는 꾸밈말이에요.')),
  ], '정답: 1 take &nbsp; 2 goes &nbsp; 3 refused &nbsp; 4 continue'),
  ('b', '밑줄 친 부분이 틀렸다면 바르게 고치시오. 바르면 ○로 표시하시오.  (교재 94쪽 5~8번)', [
   (5, I('A person usually <S>makes</S> a number of mistakes in life <C>and</C> {{learn}} lessons from them.', 'learns',
     '사람은 보통 삶에서 많은 실수를 하고 그것들로부터 교훈을 배운다.',
     '주어 <b>A person</b>은 한 명이라서 <b>makes</b>(make: 하다)처럼 -s가 붙은 단수동사를 써요. and 뒤 동사도 같은 주어의 동사라서 <b>learn → learns</b>(learn: 배우다)로 고쳐요.',
     [A_('makes (단수동사)'), J_('and'), B_('learn → learns')],
     '<b>a number of mistakes</b>의 a number of는 &ldquo;많은&rdquo;이라는 뜻이에요. 이 안의 mistakes(복수)는 동사의 수와 상관없어요.')),
   (6, I('Some children do not <S>speak</S> often <C>but</C> {{express}} themselves clearly when they do.', 'O',
     '어떤 아이들은 자주 말을 하지는 않지만 할 때는 스스로를 분명하게 표현한다.',
     '<b>do not speak</b>에서 not 뒤에는 동사원형 <b>speak</b>(speak: 말하다)이 와요. but으로 이어진 <b>express</b>(express: 표현하다)도 같은 자리의 동사원형이라서 맞아요. 고칠 곳이 없어요.',
     [A_('speak (동사원형)'), J_('but'), B_('express (동사원형, 맞음)')],
     '<b>when they do</b>에서 do는 앞의 동사(speak)를 대신 받는 말이에요. 뜻은 &ldquo;말을 할 때는&rdquo;.')),
   (7, I('Serene quickly <S>turned</S> on one foot in front of her friends <C>but</C> {{to fall}} to the floor.', 'fell',
     'Serene은 친구들 앞에서 재빨리 한 발로 돌았지만 바닥에 넘어졌다.',
     '앞의 동사 <b>turned</b>(turn: 돌다)가 과거 동사예요. but 뒤에도 과거 동사가 와야 해서 to부정사 <b>to fall</b>을 과거 동사 <b>fell</b>(fall: 넘어지다)로 고쳐요. fall은 과거형이 fell인 불규칙 동사예요.',
     [A_('turned (과거)'), J_('but'), B_('to fall → fell (과거)')],
     '<b>turn on one foot</b>은 &ldquo;한 발로 서서 돌다&rdquo;라는 뜻이에요.')),
   (8, I('<S>Cut</S> unnecessary expenses <C>and</C> {{start}} saving if you want to achieve your financial goals more quickly.', 'O',
     '당신의 재정적인 목표를 더 빨리 달성하기를 원한다면 불필요한 비용을 줄이고 저축을 시작해라.',
     '동사원형으로 시작하는 문장은 &ldquo;~해라&rdquo;(명령문)예요. <b>Cut</b>(cut: 줄이다)과 and로 이어진 <b>start</b>(start: 시작하다)도 동사원형이라서 맞아요. 고칠 곳이 없어요.',
     [A_('Cut (명령문 동사원형)'), J_('and'), B_('start (동사원형, 맞음)')],
     '<b>start saving</b>은 &ldquo;저축하기 시작하다&rdquo;(start + -ing)예요. 이 saving은 start의 목적어라서 병렬과는 상관없어요.')),
  ], '정답: 5 learns &nbsp; 6 ○ (express 그대로) &nbsp; 7 fell &nbsp; 8 ○ (start 그대로)'),
 ])

# ===== POINT 2 : 동명사와 to부정사 병렬 =====
P[2] = dict(
 page='p.95', freq='★★☆', title='동명사와 to부정사 병렬',
 formula=[('s', 'v-ing / to + 동사원형'), ('c', '+ and / but / (n)or +'), ('s', 'v-ing / (to) 동사원형')],
 rule='<b>동명사(-ing)</b>는 동명사끼리, <b>to부정사(to + 동사원형)</b>는 to부정사끼리 이어요. 단, 뒤에 이어지는 to부정사의 <b>to는 생략</b>할 수 있어요.',
 kinds=['<b>동명사 + 동명사</b> &nbsp;by telling ~ or showing ~ (전치사 by 뒤에는 동명사)',
        '<b>to부정사 + to부정사</b> &nbsp;not only to take ~, but to get ~',
        '<b>뒤의 to는 생략 가능</b> &nbsp;to understand, remember, and review (remember, review 앞의 to가 빠진 모양)',
        '<b>짝 접속사</b>(both A and B / not only A but also B 등)도 A와 B의 모양을 똑같이 맞춰요.'],
 steps=['접속사 앞 짝(A)이 -ing인지 to부정사인지 확인한다. (앞에 전치사가 있으면 -ing!)', '짝(B)도 같은 모양으로 맞춘다. to부정사 뒤쪽은 to를 생략해도 된다.', '짝이 아닌 덩어리(목적을 나타내는 to 등)에 속지 않는다.'],
 ex=('2_ex', dict(
   t='An advertisement cannot meet its goal to create an appealing image by <S>telling</S> too many stories <C>or</C> [showing|to show] everything.', ans='showing',
   ko='광고는 너무 많은 이야기를 하는 것이나 모든 것을 보여주는 것에 의해 매력적인 이미지를 만들어 내는 목표를 달성할 수 없다.',
   why='<b>by</b>는 전치사라서 뒤에 동명사가 와요. 그래서 A는 동명사 <b>telling</b>(tell: 말하다)이에요. or 뒤의 B도 같은 동명사 <b>showing</b>(show: 보여주다)으로 맞춰요. to show는 to부정사라서 안 돼요.',
   st=[A_('telling (by의 목적어, 동명사)'), J_('or'), B_('showing (동명사)')],
   ex='<b>to create an appealing image</b>는 goal(목표)을 꾸며 주는 to부정사예요. &ldquo;매력적인 이미지를 만들어 내는&rdquo;이라는 뜻이고, telling / showing과는 다른 덩어리예요.')),
 groups=[('a', '둘 중 어법에 맞는 것을 고르시오.  (교재 95쪽 POINT 2 · 1~5번)', [
   (1, I('Kevin gave the old man enough money <C>not only</C> <S>to take</S> a bus, <C>but</C> [getting|to get] a warm meal.', 'to get',
     'Kevin은 그 노인에게 버스를 탈 뿐만 아니라 따뜻한 식사를 할 충분한 돈을 주었다.',
     '<b>not only A but (also) B</b>에서 A가 to부정사 <b>to take</b>(take: (차를) 타다)예요. 그래서 B도 to부정사 <b>to get</b>(get: 얻다, 먹다)으로 맞춰요. 둘 다 &ldquo;enough money(충분한 돈)&rdquo;를 꾸며 줘요.',
     [A_('to take (to부정사)'), J_('not only ~ but'), B_('to get (to부정사)')],
     '<b>gave the old man enough money</b>는 &ldquo;그 노인에게 충분한 돈을 주었다&rdquo;예요. give A B(A에게 B를 주다) 모양이에요.')),
   (2, I('To reduce paper waste, digital reports are preferred instead of <S>printing</S> them <C>or</C> [making|to make] copies of them.', 'making',
     '종이 낭비를 줄이기 위해, 인쇄하는 것이나 복사본을 만드는 것 대신에 디지털 보고서가 선호된다.',
     '<b>instead of</b>의 of는 전치사라서 뒤에 동명사가 와요. 그래서 A가 동명사 <b>printing</b>(print: 인쇄하다)이고, or 뒤 B도 동명사 <b>making</b>(make: 만들다)이 맞아요.',
     [A_('printing (동명사)'), J_('or'), B_('making (동명사)')],
     '<b>To reduce paper waste</b>는 &ldquo;종이 낭비를 줄이기 위해&rdquo;(목적)라는 문장 앞 꾸밈말이에요. reduce: 줄이다.')),
   (3, I('Taking notes is a good way <S>to understand</S>, <S>remember</S>, <C>and</C> [review|reviewing] important information better.', 'review',
     '노트 필기를 하는 것은 중요한 정보를 더 잘 이해하고, 기억하고, 복습하기 위한 좋은 방법이다.',
     'way(방법)를 꾸미는 to부정사 <b>to understand</b>(understand: 이해하다)와 <b>(to) remember</b>(remember: 기억하다)가 이어지고 있어요. 뒤쪽 to는 생략할 수 있어서 세 번째도 동사원형 <b>review</b>(review: 복습하다)가 맞아요.',
     [A_('to understand'), B_('(to) remember (to 생략)'), J_('and'), C_('(to) review (to 생략)')],
     '<b>Taking notes</b>(노트 필기를 하는 것)는 동명사 주어라서 단수동사 is가 와요(CH01에서 배웠어요).')),
   (4, I('Judy wakes up early in the morning <C>both</C> <S>to drink</S> a cup of tea <C>and</C> [doing|to do] yoga.', 'to do',
     'Judy는 차를 한 잔 마시는 것과 요가를 하는 것 둘 다 하기 위해 아침에 일찍 일어난다.',
     '<b>both A and B</b>(A와 B 둘 다)에서 A가 to부정사 <b>to drink</b>(drink: 마시다)예요. 그래서 B도 to부정사 <b>to do</b>(do: 하다)로 맞춰요.',
     [A_('to drink (to부정사)'), J_('both ~ and'), B_('to do (to부정사)')],
     '<b>wakes up</b>(wake up: 일어나다)은 주어 Judy에 맞춘 단수동사예요. 목적을 나타내는 to부정사 두 개가 &ldquo;~하기 위해&rdquo;로 이어졌어요.')),
   (5, I('I love <S>cooking</S> dishes with new flavors, <C>and</C> [sharing|to share] meals with my family to create happy memories.', 'sharing',
     '나는 새로운 맛의 요리를 하는 것과, 행복한 기억을 만들기 위해 가족들과 식사를 함께 하는 것을 좋아한다.',
     '<b>love</b>(love: 좋아하다)의 목적어로 동명사 <b>cooking</b>(cook: 요리하다)이 왔어요. and로 이어지는 B도 같은 동명사 <b>sharing</b>(share: 함께 나누다)으로 맞춰요.',
     [A_('cooking (동명사)'), J_('and'), B_('sharing (동명사)')],
     '맨 끝의 <b>to create happy memories</b>는 &ldquo;행복한 기억을 만들기 위해&rdquo;라는 목적이에요. 병렬의 짝이 아니라서 신경 쓰지 않아도 돼요.')),
  ], '정답: 1 to get &nbsp; 2 making &nbsp; 3 review &nbsp; 4 to do &nbsp; 5 sharing')])

# ===== POINT 3 : 분사 병렬 =====
P[3] = dict(
 page='p.95', freq='★☆☆', title='분사 병렬',
 formula=[('s', '분사 / 형용사'), ('c', '+ and / but / (n)or +'), ('s', '분사 / 형용사')],
 rule='<b>분사</b>(-ing / -ed 모양)는 분사끼리 이어요. 분사는 형용사처럼 쓰이기 때문에 <b>분사와 형용사도 서로 이을 수 있어요</b>. 하지만 동사나 to부정사와는 이을 수 없어요.',
 kinds=['<b>분사 + 분사</b> &nbsp;tired but excited (피곤하지만 신난)',
        '<b>분사 + 형용사</b> &nbsp;relaxed or confident / very new and interesting',
        '<b>감정을 느끼면 -ed, 감정을 주면 -ing</b> &nbsp;excited(신난), interesting(흥미로운)',
        '<b>꾸미는 말 자리도 같아요</b> &nbsp;useful and encouraging advice (조언을 꾸미는 말끼리)'],
 steps=['접속사 앞뒤 중 이미 정해진 쪽(형용사/분사)을 본다.', '반대쪽도 형용사 역할을 하는 분사(-ing / -ed)로 맞춘다.', '-ing인지 -ed인지는 꾸밈받는 말이 감정을 &ldquo;주는지 / 느끼는지&rdquo;로 정한다.'],
 ex=('3_ex', dict(
   t='You can train your brain to become [relaxed|to relax] <C>or</C> <S>confident</S> by repeating experiences.', ans='relaxed',
   ko='당신은 경험을 반복함으로써 당신의 뇌가 편안하거나 자신감 있게 되도록 훈련시킬 수 있다.',
   why='<b>become</b>(become: ~이 되다) 뒤에는 상태를 말하는 보어가 와요. or 뒤의 <b>confident</b>(자신감 있는)가 형용사라서 앞도 형용사 역할을 하는 분사 <b>relaxed</b>(relax: 편안하게 하다 → 편안해진)가 맞아요. to relax는 동사 모양이라 형용사와 이을 수 없어요.',
   st=[A_('relaxed (분사)'), J_('or'), B_('confident (형용사)')],
   ex='<b>by repeating experiences</b>는 &ldquo;경험을 반복함으로써&rdquo;(방법)예요. by 뒤에는 동명사 repeating(repeat: 반복하다)이 왔어요.')),
 groups=[('a', '밑줄 친 부분이 틀렸다면 바르게 고치시오. 바르면 ○로 표시하시오.  (교재 95쪽 POINT 3 · 1~5번)', [
   (1, I('You look a little <S>tired</S> <C>but</C> {{excited}} after starting the project.', 'O',
     '그 프로젝트를 시작한 이후로 너는 약간 피곤하지만 신나 보인다.',
     '<b>look</b>(look: ~해 보이다) 뒤에 보어가 와요. <b>tired</b>(피곤한)와 but으로 이어진 <b>excited</b>(excite: 신나게 하다 → 신난)도 같은 분사라서 맞아요. 사람이 신나는 감정을 &ldquo;느끼니까&rdquo; -ed예요. 고칠 곳이 없어요.',
     [A_('tired (분사)'), J_('but'), B_('excited (분사, 맞음)')],
     '<b>after starting the project</b>는 &ldquo;프로젝트를 시작한 후에&rdquo;예요. after 뒤에 동명사 starting이 왔어요.')),
   (2, I('Close friends can provide comfort to {{discourage}} <C>or</C> <S>unhappy</S> teenagers.', 'discouraged',
     '가까운 친구들은 낙담하거나 불행한 십 대들에게 위안을 제공할 수 있다.',
     'or 뒤의 <b>unhappy</b>(불행한)는 teenagers(십 대들)를 꾸미는 형용사예요. 앞의 discourage도 teenagers를 꾸며야 하므로 분사가 와야 해요. 십 대들이 낙담을 &ldquo;느끼는&rdquo; 쪽이라서 과거분사 <b>discouraged</b>(discourage: 낙담시키다 → 낙담한)로 고쳐요.',
     [A_('discourage → discouraged'), J_('or'), B_('unhappy (형용사)')],
     '<b>provide comfort to ~</b>는 &ldquo;~에게 위안을 주다&rdquo;예요. provide: 제공하다.')),
   (3, I('The team’s research topic is very <S>new</S> <C>and</C> {{interests}}, so it is receiving a lot of attention.', 'interesting',
     '그 팀의 연구 주제가 매우 새롭고 흥미로워서, 그것은 많은 관심을 받고 있다.',
     '<b>is</b> 뒤의 보어 <b>new</b>(새로운)는 형용사예요. and 뒤에도 형용사 역할을 하는 분사가 와야 해요. interests는 동사(interest: 흥미를 끌다)의 -s 모양이라 안 돼요. 연구 주제가 흥미를 &ldquo;주는&rdquo; 쪽이라서 현재분사 <b>interesting</b>(흥미로운)으로 고쳐요.',
     [A_('new (형용사)'), J_('and'), B_('interests → interesting')],
     '<b>so it is receiving a lot of attention</b>은 &ldquo;그래서 많은 관심을 받고 있다&rdquo;(결과)예요. receive: 받다.')),
   (4, I('Noam will join a tennis club even though he is <C>neither</C> <S>drawn</S> to sports <C>nor</C> {{skilled}} at them.', 'O',
     'Noam은 스포츠에 끌리거나 능숙한 것 둘 다 아니지만 테니스 클럽에 가입할 것이다.',
     '<b>neither A nor B</b>(A도 B도 아닌)에서 A가 <b>drawn</b>(draw: 끌어당기다 → 끌리는)이라는 과거분사예요. 그래서 B도 분사 <b>skilled</b>(능숙한)로 맞아요. 고칠 곳이 없어요.',
     [A_('drawn (과거분사)'), J_('neither ~ nor'), B_('skilled (분사, 맞음)')],
     '<b>even though</b>는 &ldquo;비록 ~일지라도&rdquo;라는 뜻의 접속사예요(CH09에서 자세히 배워요). be drawn to ~ = ~에 끌리다.')),
   (5, I('Before I went up on stage to speak, Ms. Miller gave me {{to encourage}} <C>and</C> <S>useful</S> advice.', 'encouraging',
     '내가 연설하기 위해 무대에 오르기 전에, Miller씨는 나에게 힘을 북돋아 주고 유용한 조언을 해주었다.',
     'and 뒤의 <b>useful</b>(유용한)은 advice(조언)를 꾸미는 형용사예요. 그래서 앞도 advice를 꾸미는 분사가 와야 해요. 조언이 힘을 &ldquo;북돋아 주는&rdquo; 쪽이라서 현재분사 <b>encouraging</b>(encourage: 북돋우다 → 힘을 북돋아 주는)으로 고쳐요. to encourage는 안 돼요.',
     [A_('to encourage → encouraging'), J_('and'), B_('useful (형용사)')],
     '<b>went up on stage to speak</b>에서 to speak는 &ldquo;연설하기 위해&rdquo;(목적)예요. go up: 올라가다.')),
  ], '정답: 1 ○ (excited 그대로) &nbsp; 2 discouraged &nbsp; 3 interesting &nbsp; 4 ○ (skilled 그대로) &nbsp; 5 encouraging')])

SUMMARY = [
 (1, '동사는 동사끼리: 조동사 뒤 동사원형, 시제, -s(수)를 똑같이 맞춘다', 'can start ~ and receive ~ / watches ~ or walks ~'),
 (2, '동명사는 동명사끼리, to부정사는 to부정사끼리 (뒤의 to는 생략 가능)', 'by telling ~ or showing ~ / to understand, remember, and review'),
 (3, '분사는 분사 또는 형용사끼리: 감정을 느끼면 -ed, 감정을 주면 -ing', 'tired but excited / useful and encouraging advice'),
]
