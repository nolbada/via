# -*- coding: utf-8 -*-
# CH09 부사절 접속사와 명사절 접속사 -- 개념 POINT 1~3 (교재 p.106~107)
def I(t, ans, ko, why, st=None, ex='', hard=False, **kw):
    d = dict(t=t, ans=ans, ko=ko, why=why, st=st or [], ex=ex, hard=hard)
    d.update(kw)
    return d
J_ = lambda x: ('c', '접속사', x)
PR_ = lambda x: ('c', '전치사', x)
CL_ = lambda x: ('c', '뒤의 절', x)
NP_ = lambda x: ('c', '명사(구)', x)

P = {}

# ===== POINT 1 =====
P[1] = dict(
 page='p.106', freq='★★☆', title='부사절 접속사 vs. 전치사',
 formula=[('c', 'because / while / although'), ('s', '+ 주어 + 동사'), ('m', '│'), ('c', 'because of / during / despite'), ('s', '+ 명사(구)')],
 rule='뒤에 <b>주어 + 동사가 있는 절</b>이 오면 <b>접속사</b>를, 주어·동사 없이 <b>명사(구)</b>만 오면 <b>전치사</b>를 써요. 뜻이 비슷한 짝으로 외워 두세요.',
 kinds=['<b>~ 때문에</b> &nbsp;because(접속사) + 절 / because of(전치사) + 명사(구)',
        '<b>~ 동안</b> &nbsp;while(접속사) + 절 / during(전치사) + 명사(구)',
        '<b>~에도 불구하고</b> &nbsp;although · (even) though(접속사) + 절 / in spite of · despite(전치사) + 명사(구)',
        '접속사 while은 &ldquo;~인 반면에&rdquo;라는 뜻도 있어요.'],
 steps=['빈칸 바로 뒤를 본다. 「주어 + 동사」가 있는 절인가?', '절이면 접속사(because, while, although/though), 명사(구)뿐이면 전치사(because of, during, despite/in spite of)를 고른다.', '뜻(이유 / 시간 / 양보)이 문맥에 맞는지 마지막으로 확인한다.'],
 ex=('1_ex', dict(
   t='Early humans lost their hair [because|because of] <C>less hair meant</C> effective running.', ans='because',
   ko='초기 인류는 더 적은 털이 효과적인 달리기를 의미했기 때문에 털을 잃었다.',
   why='빈칸 뒤에 <b>less hair(주어) + meant(동사)</b>가 있는 절이 와요. 절 앞에는 접속사 <b>because</b>가 맞아요. because of는 명사(구) 앞에서만 써요. (mean: 의미하다 → 과거 meant)',
   st=[J_('because'), CL_('less hair meant effective running (절)')],
   ex='<b>lost</b>는 lose(잃다)의 과거형이에요. effective running은 &ldquo;효과적인 달리기&rdquo;.')),
 groups=[('a', '둘 중 어법에 맞는 것을 고르시오.  (교재 106쪽 POINT 1 · 1~5번)', [
   (1, I('The concert was canceled [because|because of] a thunderstorm hitting the country.', 'because of',
     '나라를 강타한 폭풍우 때문에 그 콘서트는 취소되었다.',
     '빈칸 뒤 <b>a thunderstorm hitting the country</b>에는 진짜 동사가 없어요. hitting(hit: 강타하다)은 thunderstorm을 꾸미는 분사일 뿐이에요. 그래서 명사구 앞에 쓰는 전치사 <b>because of</b>가 맞아요.',
     [PR_('because of'), NP_('a thunderstorm hitting the country')],
     'hitting이 동사처럼 보여도 &ldquo;강타하는&rdquo;이라고 앞 명사를 꾸미는 말이에요. 「주어 + 동사」 절인지 꼭 구분해요. cancel: 취소하다.')),
   (2, I('The parents sat and enjoyed a conversation [during|while] <C>their children played</C> in the park.', 'while',
     '아이들이 공원에서 놀고 있는 동안 부모들은 앉아서 대화를 즐겼다.',
     '뒤에 <b>their children(주어) + played(동사)</b>가 있는 절이 와요. 절 앞에는 접속사 <b>while</b>(~하는 동안)이 맞아요. during은 전치사라서 안 돼요. (play: 놀다 → 과거 played)',
     [J_('while'), CL_('their children played in the park (절)')],
     '<b>sat and enjoyed</b>는 sit(앉다)의 과거 sat과 enjoy(즐기다)의 과거 enjoyed가 and로 이어졌어요(CH08 동사 병렬).')),
   (3, I('[Despite|Although] heavy traffic on the city roads, Sarah arrived at the meeting on time.', 'Despite',
     '도시 도로의 심한 교통체증에도 불구하고, Sarah는 제때 회의에 도착했다.',
     '빈칸 뒤 <b>heavy traffic on the city roads</b>는 동사가 없는 명사구예요. 명사구 앞에는 전치사 <b>Despite</b>(~에도 불구하고)가 맞아요. Although는 절 앞에 써요.',
     [PR_('Despite'), NP_('heavy traffic on the city roads')],
     '<b>on time</b>은 &ldquo;제때에&rdquo;예요. arrive at ~ = ~에 도착하다.')),
   (4, I('[In spite of|Though] <C>the dog barked</C> loudly, it didn’t bother the neighbors.', 'Though',
     '비록 개가 큰 소리로 짖었을지라도, 그것은 이웃들을 괴롭히지는 않았다.',
     '뒤에 <b>the dog(주어) + barked(동사)</b>가 있는 절이 와요. 절 앞에는 접속사 <b>Though</b>(비록 ~일지라도)가 맞아요. In spite of는 전치사라서 명사(구) 앞에만 써요. (bark: 짖다)',
     [J_('Though'), CL_('the dog barked loudly (절)')],
     '<b>bother</b>는 &ldquo;괴롭히다&rdquo;예요. didn’t bother = 괴롭히지 않았다.')),
   (5, I('Ms. Undset escaped Norway [during|while] the German attack, but she returned after WWII.', 'during',
     'Undset씨는 독일의 공격 동안 노르웨이에서 탈출했지만, 제2차 세계 대전이 끝난 후에 다시 돌아왔다.',
     '빈칸 뒤 <b>the German attack</b>은 동사가 없는 명사구예요. 명사구 앞에는 전치사 <b>during</b>(~ 동안)이 맞아요. while은 절 앞에 써요. (escape: 탈출하다)',
     [PR_('during'), NP_('the German attack')],
     '<b>after WWII</b>의 after는 뒤에 명사구(WWII = 제2차 세계 대전)가 와서 전치사예요. 다음 POINT 2에서 자세히 배워요. returned = return(돌아오다)의 과거.')),
  ], '정답: 1 because of &nbsp; 2 while &nbsp; 3 Despite &nbsp; 4 Though &nbsp; 5 during')])

# ===== POINT 2 =====
P[2] = dict(
 page='p.106', freq='★★★', title='부사절 접속사와 전치사 둘 다로 쓰이는 단어',
 formula=[('c', 'before / after / until / since / as / like'), ('s', '+ 절 (접속사)'), ('m', '또는'), ('s', '+ 명사(구) (전치사)')],
 rule='before, after, until, since, as, like는 <b>접속사도 되고 전치사도 돼요</b>. 뒤에 절이 올 수도, 명사(구)가 올 수도 있어서 <b>각각의 뜻</b>을 알고 문맥에 맞는지 확인해야 해요.',
 kinds=['<b>before / after</b> &nbsp;접속사: ~하기 전에 / ~한 후에 · 전치사: ~ 전에 / ~ 후에',
        '<b>until / till</b> &nbsp;접속사: ~할 때까지 · 전치사: ~까지',
        '<b>since</b> &nbsp;접속사: ~한 이래로, ~이기 때문에 · 전치사: ~ 이래로',
        '<b>as</b> &nbsp;접속사: ~하듯이, ~함에 따라, ~할 때, ~하면서, ~이기 때문에 · 전치사: ~로서, ~만큼, ~처럼',
        '<b>like</b> &nbsp;접속사: ~하듯이, ~하는 것처럼 · 전치사: (예를 들어) ~ 같은, ~와 같이',
        '<b>alike</b>는 &ldquo;비슷한 / 비슷하게&rdquo;라는 형용사·부사예요. 전치사 like와 헷갈리지 마세요. (예: The twins dressed alike. 쌍둥이는 비슷하게 입었다.)'],
 steps=['뒤가 「주어 + 동사」 절인지, 명사(구)인지 먼저 본다.', '절이면 접속사의 뜻, 명사(구)면 전치사의 뜻으로 해석해 본다.', '그 뜻이 문장에 자연스러운지 확인한다. (뜻이 안 맞으면 다른 단어로 고친다)'],
 ex=('2_ex', dict(
   t='When rice prices fall, people have more money for items [since|like] <C>meat and dairy</C>, changing their spending.', ans='like',
   ko='쌀 가격이 떨어질 때, 사람들은 고기와 유제품 같은 제품들을 살 더 많은 돈을 가지게 되어, 그들의 소비를 바꾼다.',
   why='빈칸 뒤 <b>meat and dairy</b>는 동사가 없는 명사구라서 전치사가 와야 해요. since도 전치사가 될 수 있지만 뜻이 &ldquo;~ 이래로&rdquo;라서 안 맞아요. &ldquo;고기와 유제품 같은&rdquo;이라는 뜻은 전치사 <b>like</b>예요.',
   st=[PR_('like (~ 같은)'), NP_('meat and dairy')],
   ex='<b>changing their spending</b>은 앞 내용의 결과를 덧붙이는 분사구문(&ldquo;그래서 소비를 바꾼다&rdquo;)이에요. dairy: 유제품.')),
 groups=[('a', '밑줄 친 부분이 틀렸다면 바르게 고치시오. 바르면 ○로 표시하시오.  (교재 106쪽 POINT 2 · 1~5번)', [
   (1, I('I moved to this city in 2010, and {{as}} that year, I have witnessed its remarkable growth.', 'since',
     '나는 2010년에 이 도시로 이사를 왔고, 그해 이래로 그것의 놀랄 만한 성장을 목격해 왔다.',
     '<b>that year</b>는 동사가 없는 명사구라서 전치사가 와야 해요. 뜻이 &ldquo;그해 이래로&rdquo;이고 have witnessed(witness: 목격하다)와 어울리니까 전치사 <b>since</b>가 맞아요. as(~로서, ~처럼)는 뜻이 안 맞아서 <b>as → since</b>로 고쳐요.',
     [PR_('as → since'), NP_('that year')],
     '<b>have witnessed</b>는 &ldquo;(지금까지) 목격해 왔다&rdquo;(현재완료)예요. since가 이런 현재완료와 잘 어울려요. remarkable: 놀랄 만한.')),
   (2, I('The students celebrated by going out for dinner {{after}} <C>they finished</C> the college entrance exams.', 'O',
     '학생들은 대학 입학시험을 마친 후에 저녁 식사를 하러 나감으로써 축하했다.',
     '뒤에 <b>they(주어) + finished(동사)</b>가 있는 절이 와요. 절 앞에서 &ldquo;~한 후에&rdquo;라는 뜻이니까 접속사 <b>after</b>가 맞아요. 고칠 곳이 없어요.',
     [J_('after (~한 후에)'), CL_('they finished the college entrance exams (절)')],
     '<b>celebrated by going out</b>은 &ldquo;나감으로써 축하했다&rdquo;예요. celebrate: 축하하다, finish: 끝내다.')),
   (3, I('With the same green eyes and red hair, Natalie looks {{alike}} her mother.', 'like',
     '똑같은 초록색 눈과 빨간 머리를 가지고 있어서, Natalie는 그녀의 엄마와 같이 보인다.',
     '<b>her mother</b>는 명사(구)이고, &ldquo;엄마와 같이&rdquo;라는 뜻이니까 전치사 <b>like</b>가 맞아요. alike는 &ldquo;비슷한 / 비슷하게&rdquo;라는 형용사·부사라서 뒤에 명사를 바로 받을 수 없어요. <b>alike → like</b>로 고쳐요.',
     [PR_('alike → like'), NP_('her mother')],
     '<b>look like ~</b>는 &ldquo;~처럼 보이다&rdquo;예요. alike는 The twins dressed alike처럼 문장 끝에 단독으로 써요.')),
   (4, I('We worked hard {{until}} the late hours of the night to complete the project successfully.', 'O',
     '우리는 프로젝트를 성공적으로 마치기 위해 밤늦은 시간까지 열심히 일했다.',
     '<b>the late hours of the night</b>는 동사가 없는 명사구예요. &ldquo;밤늦은 시간까지&rdquo;라는 뜻이니까 전치사 <b>until</b>(~까지)이 맞아요. 고칠 곳이 없어요.',
     [PR_('until (~까지)'), NP_('the late hours of the night')],
     '<b>to complete the project successfully</b>는 &ldquo;프로젝트를 성공적으로 마치기 위해&rdquo;(목적)예요. worked = work(일하다)의 과거.')),
   (5, I('People naturally get used to things around them {{like}} <C>time passes</C>.', 'as (또는 after)',
     '사람들은 시간이 지남에 따라 자연스럽게 그들 주변의 것들에 익숙해진다.',
     '뒤의 <b>time(주어) + passes(동사)</b>는 절이에요. like도 접속사로 &ldquo;~하듯이&rdquo;라고 쓰이지만 이 문장에는 뜻이 안 맞아요. &ldquo;시간이 지남에 따라&rdquo;라는 뜻은 접속사 <b>as</b>(~함에 따라)예요(&ldquo;시간이 지난 후에&rdquo;로 보면 after도 가능). <b>like → as</b>로 고쳐요.',
     [J_('like → as (또는 after)'), CL_('time passes (절)')],
     '<b>get used to ~</b>는 &ldquo;~에 익숙해지다&rdquo;예요. 이 to는 전치사라서 뒤에 명사(things)가 와요. pass: 지나가다.')),
  ], '정답: 1 since &nbsp; 2 ○ (after 그대로) &nbsp; 3 like &nbsp; 4 ○ (until 그대로) &nbsp; 5 as (또는 after)')])

# ===== POINT 3 =====
P[3] = dict(
 page='p.107', freq='★★★', title='명사절 접속사: 완전한 절 앞 vs. 불완전한 절 앞',
 formula=[('c', 'that / whether·if / when·where·why·how'), ('s', '+ 완전한 절'), ('m', '│'), ('c', 'what / which / who(m)'), ('s', '+ 불완전한 절')],
 rule='명사절 접속사는 뒤 절이 <b>완전한지 불완전한지</b>로 골라요. <b>완전한 절</b>(주어·목적어·보어가 다 있음) 앞에는 that, whether/if, when·where·why·how를, <b>불완전한 절</b>(주어나 목적어가 빠짐) 앞에는 what, which, who(m)를 써요.',
 kinds=['<b>완전한 절 앞</b>: that(~라는 것) · whether / if(~인지 아닌지) · when / where / why / how(언제 / 어디서 / 왜 / 어떻게 ~하는지)',
        '<b>불완전한 절 앞</b>: what / which(무엇이 / 어떤 것이 ~하는지) · who(m)(누가 / 누구를 ~하는지)',
        '완전한 절 예: I heard that you won first prize. (주어 you, 동사 won, 목적어 first prize가 다 있어요)',
        '불완전한 절 예: I heard what was reported on the news. (was reported의 주어가 빠졌어요)'],
 steps=['접속사 뒤 절에 주어·목적어·보어가 다 있는지 센다.', '다 있으면(완전) that / whether / if / when / where / why / how, 빠졌으면(불완전) what / which / who를 고른다.', '완전한 절 중에서는 뜻으로 고른다. (~라는 것: that / ~인지 아닌지: whether·if / 언제·어디서·왜·어떻게: when·where·why·how)'],
 ex=('3_ex', dict(
   t='When you enjoy music, just forget [what|whether] <C>you have musical talent</C>.', ans='whether',
   ko='음악을 즐길 때, 당신이 음악적인 재능을 가지고 있는지를 그냥 잊어버려라.',
   why='빈칸 뒤 <b>you(주어) + have(동사) + musical talent(목적어)</b>는 빠진 게 없는 <b>완전한 절</b>이에요. what은 불완전한 절 앞에 쓰니까 안 맞고, &ldquo;~인지 아닌지&rdquo;라는 뜻의 <b>whether</b>가 맞아요.',
   st=[J_('whether (~인지 아닌지)'), CL_('you have musical talent (완전한 절)')],
   ex='<b>forget whether ~</b>는 &ldquo;~인지 아닌지를 잊다&rdquo;예요. 맨 앞 When you enjoy music은 &ldquo;음악을 즐길 때&rdquo;라는 부사절이에요.')),
 groups=[
  ('a', '둘 중 어법에 맞는 것을 고르시오.  (교재 107쪽 POINT 3 · 1~4번)', [
   (1, I('Duke asked Morris [when|what] <C>the meeting would end</C>, as he needed to go to the restroom.', 'when',
     '화장실에 갈 필요가 있었기 때문에, Duke는 Morris에게 회의가 언제 끝나는지 물었다.',
     '뒤에 <b>the meeting(주어) + would end(동사)</b>가 있고 end(끝나다)는 목적어가 필요 없는 동사라서 <b>완전한 절</b>이에요. 그래서 <b>when</b>(언제)이 맞아요. what은 불완전한 절 앞에 써요.',
     [J_('when (언제 ~하는지)'), CL_('the meeting would end (완전한 절)')],
     '<b>as he needed to go to the restroom</b>의 as는 &ldquo;~하기 때문에&rdquo;라는 부사절 접속사예요(POINT 2). need: 필요하다.')),
   (2, I('Considering the world market, we can only guess [that|which] <C>our business will suffer for a while</C>.', 'that',
     '세계 시장을 고려하면, 우리 사업이 한동안 나빠질 것이라고 추측할 수밖에 없다.',
     '뒤에 <b>our business(주어) + will suffer(동사)</b>가 있는 <b>완전한 절</b>이에요. &ldquo;~라고&rdquo;라는 뜻의 <b>that</b>이 맞아요. which는 불완전한 절 앞에 써요. (suffer: 나빠지다, 고통받다)',
     [J_('that (~라고)'), CL_('our business will suffer for a while (완전한 절)')],
     '<b>Considering the world market</b>은 &ldquo;세계 시장을 고려하면&rdquo;이라는 문장 앞 꾸밈말이에요. can only guess = 추측할 수밖에 없다.')),
   (3, I('I was curious about [why|who] <C>made</C> Maya change her mind at the last moment.', 'who',
     '나는 누가 마지막 순간에 Maya가 마음을 바꾸게 만들었는지 궁금했다.',
     '<b>made</b>(make: 만들다) 앞에 주어가 없는 <b>불완전한 절</b>이에요. 사람이 주어이니까 <b>who</b>(누가)가 맞아요. why는 완전한 절 앞에 써요.',
     [J_('who (누가 ~하는지)'), CL_('(주어 없음) made Maya change her mind (불완전한 절)')],
     '<b>make A V</b>는 &ldquo;A가 V하게 만들다&rdquo;예요. change her mind = 마음을 바꾸다.')),
   (4, I('She wanted to know [if|what] <C>her grandmother had ever actually seen an angel</C>.', 'if',
     '그녀는 할머니가 실제로 천사를 본 적이 있는지 아닌지 알기를 원했다.',
     '뒤에 <b>her grandmother(주어) + had seen(동사) + an angel(목적어)</b>가 다 있는 <b>완전한 절</b>이에요. &ldquo;~인지 아닌지&rdquo;라는 뜻의 <b>if</b>가 맞아요. what은 불완전한 절 앞에 써요. (see: 보다 → 본 적 있다는 had seen)',
     [J_('if (~인지 아닌지)'), CL_('her grandmother had ever actually seen an angel (완전한 절)')],
     '<b>want to know ~</b>는 &ldquo;~을 알기를 원하다&rdquo;예요. ever는 &ldquo;지금까지, 한 번이라도&rdquo;.')),
  ], '정답: 1 when &nbsp; 2 that &nbsp; 3 who &nbsp; 4 if'),
  ('b', '밑줄 친 부분이 틀렸다면 바르게 고치시오. 바르면 ○로 표시하시오.  (교재 107쪽 POINT 3 · 5~8번)', [
   (5, I('Mr. Williams was unaware of {{whether}} <C>his family was planning for his birthday</C>.', 'what',
     'Williams씨는 그의 가족이 그의 생일에 무엇을 계획하고 있는지 알지 못했다.',
     '뒤 절의 <b>was planning</b>(plan: 계획하다)에는 목적어가 빠져 있어요. 그래서 <b>불완전한 절</b>이라서 whether는 안 맞고 &ldquo;무엇을&rdquo;이라는 뜻의 <b>what</b>이 맞아요. <b>whether → what</b>으로 고쳐요.',
     [J_('whether → what'), CL_('(목적어 없음) his family was planning for his birthday (불완전한 절)')],
     '<b>be unaware of ~</b>는 &ldquo;~을 알지 못하다&rdquo;예요. of는 전치사지만 뒤에 명사절이 올 수 있어요.')),
   (6, I('One of the most essential decisions we can make is {{how}} <C>we should invest our time every day</C>.', 'O',
     '우리가 내릴 수 있는 가장 중요한 결정 중 하나는 우리가 매일 우리의 시간을 어떻게 투자해야 하는지이다.',
     '뒤에 <b>we(주어) + should invest(동사) + our time(목적어)</b>가 다 있는 <b>완전한 절</b>이에요. &ldquo;어떻게&rdquo;라는 뜻의 <b>how</b>가 맞아요. 고칠 곳이 없어요.',
     [J_('how (어떻게 ~하는지)'), CL_('we should invest our time every day (완전한 절)')],
     '<b>One of the most essential decisions ... is</b>에서 주어는 One(하나)이라서 단수동사 is예요(CH01). <b>we can make</b>는 decisions를 꾸며요. invest: 투자하다.')),
   (7, I('I really wonder {{what}} <C>they found such a wonderful sofa for their living room</C>.', 'where (또는 how)',
     '나는 그들이 거실을 위한 그렇게 멋진 소파를 어디에서(또는 어떻게) 찾았는지 정말 궁금하다.',
     '뒤에 <b>they(주어) + found(동사) + such a wonderful sofa(목적어)</b>가 다 있는 <b>완전한 절</b>이에요. what은 불완전한 절 앞에 쓰니까 안 되고, &ldquo;어디에서&rdquo;라는 <b>where</b>(또는 how)가 맞아요. <b>what → where</b>로 고쳐요. (find: 찾다 → 과거 found)',
     [J_('what → where (또는 how)'), CL_('they found such a wonderful sofa for their living room (완전한 절)')],
     '<b>wonder ~</b>는 &ldquo;~인지 궁금해하다&rdquo;예요. such a wonderful sofa = 그렇게 멋진 소파.')),
   (8, I('Close your eyes and imagine {{if}} <C>you are standing on top of a mountain</C>.', 'that',
     '눈을 감고 네가 산꼭대기에 서 있다고 상상해 봐라.',
     '뒤에 <b>you(주어) + are standing(동사: stand, 서다)</b>가 있는 <b>완전한 절</b>이에요. 상상하는 내용을 &ldquo;~라고&rdquo; 이으니까 <b>that</b>이 맞아요. if는 &ldquo;~인지 아닌지&rdquo;라서 뜻이 안 맞아요. <b>if → that</b>으로 고쳐요.',
     [J_('if → that'), CL_('you are standing on top of a mountain (완전한 절)')],
     '<b>Close your eyes and imagine ~</b>은 명령문 두 개가 and로 이어진 문장이에요(CH08). close: 감다, imagine: 상상하다.')),
  ], '정답: 5 what &nbsp; 6 ○ (how 그대로) &nbsp; 7 where (또는 how) &nbsp; 8 that'),
 ])

SUMMARY = [
 (1, '절 앞(주어 + 동사)은 접속사, 명사(구) 앞은 전치사', 'because + 절 / because of + 명사(구) · while / during · although / despite'),
 (2, 'before · after · until · since · as · like는 접속사도 전치사도 됨 → 뜻으로 확인', 'since that year(전치사) / as time passes(접속사)'),
 (3, '완전한 절 앞: that · whether/if · when·where·why·how / 불완전한 절 앞: what · which · who', 'know whether you have talent / know what was reported'),
]
