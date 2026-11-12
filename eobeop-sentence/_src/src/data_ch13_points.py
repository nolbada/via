# -*- coding: utf-8 -*-
# CH13 비교구문 : POINT 1~3 (교재 156~157쪽)
P = {}

def D(t, ans, ko, why, st, ex='', **kw):
    d = dict(t=t, ans=ans, ko=ko, why=why, st=st)
    if ex:
        d['ex'] = ex
    d.update(kw)
    return d

# ===== POINT 1 =====
P[1] = dict(
 page='p.156', freq='★★★', title='비교구문의 형태: 원급 vs. 비교급',
 formula=[('c', 'as + 원급 + as'), ('m', '│'), ('c', '비교급 (-er / more·less + 원급) + than')],
 rule='형용사·부사의 <b>원급</b>(원래 모양)은 <b>as ~ as</b>와, <b>비교급</b>은 <b>than</b>과 함께 써요. 끝에 -er이 안 붙는 불규칙 비교급(better, worse, less 등)도 비교급이라서 than이 와요.',
 kinds=['<b>원급 비교</b>(A = B) &nbsp;as old as you (너만큼 나이 든)',
        '<b>비교급 비교</b>(A > B) &nbsp;noisier than ~ (~보다 더 시끄러운), more important than ~, less efficient than ~ (~보다 덜 효율적인)',
        '<b>불규칙 비교급</b>은 원급으로 착각하기 쉬워요 &nbsp;good → better, bad → worse, many/much → more, little → less (모두 than과 함께!)',
        '<b>as, than을 빼고 보면</b> 형용사 자리인지 부사 자리인지 쉬워져요 &nbsp;She moved as graceful(→ gracefully) as a swan. — moved(움직였다)를 꾸미니까 부사!'],
 steps=['as와 than을 잠깐 빼고 읽어서 형용사 자리인지 부사 자리인지 정한다.', '앞에 as + 원급이 있으면 뒤에 as, 비교급(-er, more, less, better 등)이 있으면 뒤에 than을 쓴다.',
        'more / less 뒤에는 형용사·부사의 원래 모양(원급)을 쓴다. (more importantly → more important)'],
 ex=('1_ex', D(
   'We couldn’t have picked a better location for our company [as|than] this warm and inviting city.', 'than',
   '우리는 이 따뜻하고 매력적인 도시보다 우리 회사에 더 좋은 장소를 고를 수가 없었다.',
   '<b>better</b>(더 좋은)는 good의 불규칙 비교급이에요. 비교급 뒤에는 <b>than</b>(~보다)이 와요. as는 as ~ as(원급)일 때 써요.',
   [('c', '비교급', 'better (good의 비교급)'), ('c', '짝', 'than')],
   '<b>couldn’t have picked</b>(pick: 고르다)는 &ldquo;(더 좋은 것을) 고를 수 없었을 것이다&rdquo;라는 뜻이에요. inviting은 &ldquo;매력적인&rdquo;이에요.')),
 groups=[
  ('a', '둘 중 어법에 맞는 것을 고르시오.  (교재 156쪽 1~4번)', [
   (1, D('The car was made 17 years ago, so it’s as <S>old</S> [as|than] you.', 'as',
     '그 차는 17년 전에 만들어져서, 너만큼 나이가 들었다.',
     '앞에 <b>as old</b>(원급)가 있죠? as + 원급 + <b>as</b>의 짝이라서 뒤에도 as가 와요. than은 비교급 뒤에 써요.',
     [('c', '원급', 'as old'), ('c', '짝', 'as')],
     'was made는 &ldquo;만들어졌다&rdquo;(make: 만들다, be + p.p.)예요. 17 years ago는 &ldquo;17년 전에&rdquo;예요.')),
   (2, D('The neighborhood is [noisy|noisier] in the daytime than it is at night.', 'noisier',
     '그 동네는 밤보다 낮에 더 시끄럽다.',
     '뒤에 <b>than</b>이 있어요. than은 비교급과 짝이라서 형용사를 비교급 <b>noisier</b>(더 시끄러운)로 써야 해요.',
     [('c', '짝', 'than'), ('c', '비교급', 'noisier')],
     '<b>in the daytime</b>은 &ldquo;낮에&rdquo;, <b>at night</b>은 &ldquo;밤에&rdquo;예요. than it is at night는 &ldquo;밤에 그런 것보다&rdquo;라는 뜻이에요.')),
   (3, D('Old houses are usually less efficient at storing heat [as|than] modern ones.', 'than',
     '오래된 주택들은 대개 현대식 주택들보다 열을 저장하는 데 덜 효율적이다.',
     '앞에 비교급 <b>less efficient</b>(덜 효율적인)가 있어요. 비교급의 짝은 <b>than</b>이에요. 여기서 ones는 houses를 대신 받는 말이에요.',
     [('c', '비교급', 'less efficient'), ('c', '짝', 'than')],
     '<b>efficient at v-ing</b>는 &ldquo;~하는 데 효율적인&rdquo;이에요. storing → store(저장하다)에 -ing를 붙인 모양이에요.')),
   (4, D('All the other contest participants <C>looked</C> as [uneasy|uneasily] as Zoe.', 'uneasy',
     '다른 모든 대회 참가자들은 Zoe만큼 불안해 보였다.',
     '<b>as ~ as</b>를 빼고 보면 <b>looked</b>(look: ~해 보이다) 뒤 주격보어 자리예요. 부사가 아니라 형용사 <b>uneasy</b>(불안한)가 맞아요.',
     [('v', '동사', 'looked'), ('c', '주격보어(원급)', 'uneasy')],
     'participant는 &ldquo;참가자&rdquo;예요. as uneasy as Zoe는 &ldquo;Zoe만큼 불안한&rdquo;이에요.')),
  ], '정답: 1 as &nbsp; 2 noisier &nbsp; 3 than &nbsp; 4 uneasy'),
  ('b', '밑줄 친 부분이 틀렸다면 바르게 고치시오. 바르면 ○로 표시하시오.  (교재 156쪽 5~8번)', [
   (5, D('We don’t <S>see</S> each other as {{frequently}} as we used to when we were in school.', 'O',
     '우리는 학교에 다닐 때 그랬던 것만큼 서로를 자주 보지 못한다.',
     '<b>as ~ as</b>를 빼고 보면 동사 <b>see</b>(see: 보다)를 꾸미는 자리예요. 동사를 꾸미는 부사 <b>frequently</b>(자주)가 맞아요. 원급이라서 as ~ as가 짝이에요. 고칠 곳이 없어요.',
     [('v', '꾸밈을 받는 말(동사)', 'see'), ('m', '부사(원급)', 'frequently (맞음)')],
     '<b>used to V</b>는 &ldquo;(예전에) V하곤 했다&rdquo;예요. 여기서는 as we used to (see each other)가 줄어든 모양이에요.')),
   (6, D('Recent inventions such as airplanes <C>are</C> surely not more {{importantly}} than ancient ones like the wheel.', 'important',
     '비행기와 같은 최근의 발명품들은 확실히 바퀴와 같은 고대의 발명품들보다 더 중요하지 않다.',
     '<b>than</b>을 빼고 보면 <b>are</b>(be: ~이다) 뒤 주격보어 자리예요. 부사 importantly(중요하게) → 형용사 <b>important</b>(중요한)로 고쳐요. more 뒤에는 원래 모양이 와요.',
     [('v', '동사', 'are'), ('c', '주격보어', 'importantly → important')],
     '<b>ancient ones</b>의 ones는 앞의 inventions를 대신 받는 말이에요. surely는 &ldquo;확실히&rdquo;, ancient는 &ldquo;고대의&rdquo;예요.')),
   (7, D('In this area, you can enjoy <S>scenery</S> as various {{than}} deserts, seas, and mountains.', 'as',
     '이 지역에서, 당신은 사막, 바다, 그리고 산만큼 다양한 풍경을 즐길 수 있다.',
     '앞에 <b>as</b>와 원급 <b>various</b>(다양한)가 있으니 as + 원급 + <b>as</b>예요. than → <b>as</b>로 고쳐요.',
     [('c', '원급', 'as various'), ('c', '짝', 'than → as')],
     '<b>scenery</b>(풍경)는 셀 수 없는 명사예요. as various as ~는 &ldquo;~만큼 다양한&rdquo;이에요.')),
   (8, D('The store is far from my home, but it has <S>more</S> kinds of items {{than}} the store in my town.', 'O',
     '그 가게는 우리 집에서 멀지만, 그것은 우리 동네에 있는 가게보다 더 많은 종류의 물품을 가지고 있다.',
     '앞에 비교급 <b>more</b>(더 많은)가 있으니 짝은 <b>than</b>이에요. 맞아요. 고칠 곳이 없어요.',
     [('c', '비교급', 'more kinds of items'), ('c', '짝', 'than (맞음)')],
     '<b>be far from ~</b>는 &ldquo;~에서 멀다&rdquo;예요. kinds of items는 &ldquo;물품의 종류&rdquo;예요.')),
  ], '정답: 5 ○ (frequently 그대로) &nbsp; 6 important &nbsp; 7 as &nbsp; 8 ○ (than 그대로)'),
 ])

# ===== POINT 2 =====
P[2] = dict(
 page='p.157', freq='★★☆', title='비교급 · 최상급 강조 부사',
 formula=[('c', 'much / even / far / still / a lot'), ('s', '+ 비교급'), ('m', '│'), ('c', 'by far / quite'), ('s', '+ 최상급'), ('m', '│'), ('c', 'very'), ('s', '+ 원급')],
 rule='<b>비교급</b> 앞에는 &ldquo;훨씬&rdquo;이라는 뜻의 <b>much / even / far / still / a lot</b>, <b>최상급</b> 앞에는 &ldquo;단연코&rdquo;라는 뜻의 <b>by far / quite</b>이 와요. <b>very</b>는 원급만 강조하고, 비교급·최상급은 강조하지 못해요.',
 kinds=['<b>much / even / far / still / a lot + 비교급</b> &nbsp;much healthier (훨씬 더 건강한)',
        '<b>by far / quite + 최상급</b> &nbsp;by far the worst (단연코 최악인), quite the longest (단연코 가장 긴)',
        '<b>very + 원급</b> &nbsp;very similar (매우 비슷한) — very better, very the worst는 틀려요!'],
 steps=['강조하는 말 뒤에 오는 단어가 원급인지, 비교급인지, 최상급인지 본다.', '비교급이면 much / even / far / still / a lot, 최상급이면 by far / quite을 쓴다.', 'very는 원급 앞에서만 쓴다.'],
 ex=('2_ex', D(
   'Many studies have shown that drinking tea is [much|very] healthier than drinking coffee.', 'much',
   '많은 연구들이 차를 마시는 것이 커피를 마시는 것보다 훨씬 더 건강하다는 것을 보여주었다.',
   '<b>healthier</b>(더 건강한)는 비교급이에요. 비교급 앞에는 &ldquo;훨씬&rdquo;이라는 뜻의 <b>much</b>가 와요. very는 비교급을 강조할 수 없어요.',
   [('c', '강조 부사', 'much'), ('c', '비교급', 'healthier')],
   '<b>drinking tea</b>(차를 마시는 것)는 동명사구 주어라서 단수 is예요(CH01 복습). have shown은 show(보여 주다)의 현재완료예요.')),
 groups=[
  ('a', '둘 중 어법에 맞는 것을 고르시오.  (교재 157쪽 POINT 2 · 1~5번)', [
   (1, D('With proper training, my public-speaking skills have become [far|very] <S>better</S> over time.', 'far',
     '적절한 훈련 덕에, 나의 대중 연설 기술은 시간이 지나면서 훨씬 더 좋아졌다.',
     '<b>better</b>(더 좋은)는 good의 비교급이에요. 비교급 앞에는 &ldquo;훨씬&rdquo;이라는 뜻의 <b>far</b>가 와요. very는 비교급 앞에 못 써요.',
     [('c', '비교급', 'better'), ('c', '강조 부사', 'far (훨씬)')],
     'have become(become: ~해지다) + better는 &ldquo;더 좋아졌다&rdquo;예요. proper는 &ldquo;적절한&rdquo;, over time은 &ldquo;시간이 지나면서&rdquo;예요.')),
   (2, D('The two apartments look [much|very] <S>similar</S>, but one is slightly bigger than the other.', 'very',
     '두 아파트는 매우 비슷해 보이지만, 하나가 다른 것보다 약간 더 크다.',
     '<b>similar</b>(비슷한)는 원급이에요. 원급을 강조하는 건 <b>very</b>(매우)예요. much는 비교급 앞에 써요. (뒤의 bigger than은 비교급이고, slightly(약간)가 그것을 꾸며요.)',
     [('c', '원급', 'similar'), ('c', '강조 부사', 'very (매우)')],
     'look + 형용사(similar)는 &ldquo;~해 보이다&rdquo;예요(CH12 복습). one ~ the other는 &ldquo;하나는 ~, 다른 하나는&rdquo;이에요.')),
   (3, D('The storm last night was [by far|very] <S>the worst</S> we’ve experienced in years.', 'by far',
     '어젯밤의 폭풍은 우리가 몇 년간 경험한 것 중 단연코 최악이었다.',
     '<b>the worst</b>(가장 나쁜)는 최상급이에요. 최상급 앞에는 &ldquo;단연코&rdquo;라는 뜻의 <b>by far</b>가 와요. very는 최상급 앞에 못 써요.',
     [('c', '최상급', 'the worst'), ('c', '강조 부사', 'by far (단연코)')],
     '<b>we’ve experienced</b>는 we have experienced(experience: 경험하다)의 줄임말(현재완료)이에요. in years는 &ldquo;몇 년간&rdquo;이에요.')),
   (4, D('In 2014, Internet usage time on mobile phones was [even|very] <S>greater</S> than that on desktops or laptops.', 'even',
     '2014년에, 휴대폰에서 인터넷을 사용한 시간이 데스크톱 컴퓨터나 노트북 컴퓨터에서 인터넷을 사용한 시간보다 훨씬 더 많았다.',
     '<b>greater</b>(더 큰, 더 많은)는 비교급이에요. 비교급 앞에는 &ldquo;훨씬&rdquo;이라는 뜻의 <b>even</b>이 와요.',
     [('c', '비교급', 'greater'), ('c', '강조 부사', 'even (훨씬)')],
     '<b>that on desktops or laptops</b>의 that은 앞의 usage time(사용 시간)을 대신 받는 말이에요.')),
   (5, D('Even if the bridge is very long, it is not [quite|very] <S>the longest</S> in the world.', 'quite',
     '비록 그 다리가 매우 길지라도, 그것이 세계에서 단연코 가장 길지는 않다.',
     '<b>the longest</b>(가장 긴)는 최상급이에요. 최상급 앞에는 &ldquo;단연코&rdquo;라는 뜻의 <b>quite</b>이 와요. (앞의 very long은 원급 long을 강조하는 very라서 맞아요.)',
     [('c', '최상급', 'the longest'), ('c', '강조 부사', 'quite (단연코)')],
     '<b>Even if ~</b>는 &ldquo;비록 ~일지라도&rdquo;예요. not quite the longest는 &ldquo;단연코 가장 길지는 않다&rdquo;라는 뜻이에요.')),
  ], '정답: 1 far &nbsp; 2 very &nbsp; 3 by far &nbsp; 4 even &nbsp; 5 quite'),
 ])

# ===== POINT 3 =====
P[3] = dict(
 page='p.157', freq='★☆☆', title='비교구문 관련 표현',
 formula=[('c', 'as + 원급 + as possible'), ('m', '│'), ('c', 'get + 비교급 and 비교급'), ('m', '│'), ('c', 'the + 비교급 ~, the + 비교급 …'), ('m', '│'), ('c', 'one of the + 최상급 + 복수명사')],
 rule='비교구문에는 <b>정해진 짝(관용 표현)</b>이 있어요. 모양이 맞게 쓰였는지 짝으로 확인하세요.',
 kinds=['<b>원급 표현</b> &nbsp;as + 원급 + 명사 + as …(…만큼 ~한 명사) / <b>as + 원급 + as possible</b>(가능한 한 ~하게) / twice·three times + as + 원급 + as …(…의 몇 배만큼 ~한) / <b>no (other) + 단수명사 + as + 원급 + as …</b>(어떤 ~도 …만큼 ~하지 않다)',
        '<b>비교급 표현</b> &nbsp;<b>get + 비교급 (and 비교급)</b>(점점 더 ~해지다) / <b>the + 비교급 ~, the + 비교급 …</b>(더 ~할수록, 더 …하다) / <b>no (other) + 단수명사 + 비교급 + than …</b>(어떤 ~도 …보다 더 ~하지 않다) / <b>비교급 + than any other + 단수명사</b>(다른 어떤 ~보다 더 ~하다)',
        '<b>최상급 표현</b> &nbsp;<b>one of the + 최상급 + 복수명사</b>(가장 ~한 ~ 중 하나)'],
 steps=['문장 속 표현이 위 관용 표현 중 하나인지 알아본다.', '그 표현의 정해진 모양(원급 / 비교급 / 최상급)에 맞는지 확인한다.', '틀렸으면 정해진 모양으로 고친다. (as fastest as possible → as fast as possible)'],
 ex=('3_ex', D(
   'The older the male Chuckwallas lizards grow, the [light|lighter] their body colors become.', 'lighter',
   '수컷 척왈라 도마뱀은 더 나이가 들수록, 몸 색깔이 더 밝아진다.',
   '앞쪽에 <b>the older</b>(더 나이 든)가 있어요. <b>the + 비교급 ~, the + 비교급 …</b>(더 ~할수록 더 …하다) 짝이라서 뒤에도 비교급 <b>lighter</b>(더 가벼운)가 와요.',
   [('c', '앞 절', 'the older ~ grow'), ('c', '뒤 절', 'the lighter ~ become')],
   '<b>grow</b>(grow: ~해지다) 뒤의 older는 보어예요. become(become: ~해지다) 뒤의 lighter도 보어예요. male은 &ldquo;수컷의&rdquo;, lizard는 &ldquo;도마뱀&rdquo;이에요.')),
 groups=[
  ('a', '밑줄 친 부분이 틀렸다면 바르게 고치시오. 바르면 ○로 표시하시오.  (교재 157쪽 POINT 3 · 1~5번)', [
   (1, D('My friends and I <S>ran</S> as {{fastest}} as possible to get to the movie on time.', 'fast',
     '내 친구들과 나는 제시간에 영화관에 도착하기 위해 가능한 한 빠르게 달렸다.',
     '<b>as ~ as possible</b>(가능한 한 ~하게)은 사이에 원급이 와요. fastest(가장 빠르게) → <b>fast</b>(빠르게)로 고쳐요.',
     [('c', '표현', 'as ~ as possible'), ('m', '원급 자리', 'fastest → fast')],
     'ran → run(달리다)의 과거형이에요. <b>get to ~</b>는 &ldquo;~에 도착하다&rdquo;, <b>on time</b>은 &ldquo;제시간에&rdquo;예요.')),
   (2, D('When people learn from their mistakes, they <C>get</C> {{wiser}} and wiser at making decisions.', 'O',
     '사람들이 그들의 실수로부터 배울 때, 그들은 결정을 내리는 데 있어서 점점 더 현명해진다.',
     '<b>get + 비교급 and 비교급</b>은 &ldquo;점점 더 ~해지다&rdquo;예요. get(get: ~해지다) 뒤에 wiser(더 현명한) and wiser가 와서 맞아요. 고칠 곳이 없어요.',
     [('c', '표현', 'get + 비교급 and 비교급'), ('m', '비교급', 'wiser (맞음)')],
     '<b>learn from ~</b>은 &ldquo;~로부터 배우다&rdquo;예요. at making decisions는 &ldquo;결정을 내리는 데 있어&rdquo;예요.')),
   (3, D('This painting is {{oldest}} than any other artwork in this museum.', 'older',
     '이 그림은 이 박물관 안의 다른 어떤 예술 작품보다 더 오래되었다.',
     '<b>비교급 + than any other + 단수명사</b>(다른 어떤 ~보다 더 ~한)는 비교급과 함께 써요. oldest(가장 오래된) → 비교급 <b>older</b>(더 오래된)로 고쳐요.',
     [('c', '표현', '비교급 + than any other + 단수명사'), ('m', '비교급 자리', 'oldest → older')],
     '<b>any other</b> 뒤에는 단수명사(artwork)가 와요. than 앞에는 최상급이 아니라 비교급이에요!')),
   (4, D('Face-to-face <S>conversation</S> is one of the {{best}} ways to develop new thinking and ideas.', 'O',
     '대면 대화는 새로운 사고와 아이디어를 개발하는 가장 좋은 방법들 중 하나이다.',
     '<b>one of the + 최상급 + 복수명사</b>(가장 ~한 ~ 중 하나)예요. best(가장 좋은) + ways(방법들)가 와서 맞아요. 고칠 곳이 없어요.',
     [('c', '표현', 'one of the + 최상급 + 복수명사'), ('m', '최상급', 'best (맞음)')],
     '<b>Face-to-face conversation</b>(마주 보고 하는 대화)은 단수 주어라서 is예요. <b>to develop ~</b>는 ways를 꾸미는 &ldquo;개발하는&rdquo;이에요.')),
   (5, D('No other animal on the earth <C>is</C> as {{smarter}} as the orangutan.', 'smart',
     '지구상의 다른 어떤 동물도 오랑우탄만큼 똑똑하지 않다.',
     '<b>no other + 단수명사 ~ as + 원급 + as …</b>(어떤 ~도 …만큼 ~하지 않다) 모양이에요. as와 as 사이에는 원급이 와서 smarter(더 똑똑한) → <b>smart</b>(똑똑한)로 고쳐요.',
     [('c', '표현', 'no other + 단수명사 ~ as 원급 as …'), ('m', '원급 자리', 'smarter → smart')],
     '<b>No other animal</b>은 &ldquo;다른 어떤 동물도 ~않다&rdquo;예요. animal이 단수라서 동사는 is예요.')),
  ], '정답: 1 fast &nbsp; 2 ○ (wiser 그대로) &nbsp; 3 older &nbsp; 4 ○ (best 그대로) &nbsp; 5 smart'),
 ])

SUMMARY = [
 (1, '원급은 as ~ as, 비교급은 than과 짝 (불규칙 비교급 better·worse·less도 than!)', 'as old as you / better than this city'),
 (2, '비교급 강조: much·even·far·still·a lot / 최상급 강조: by far·quite / very는 원급만', 'much healthier / by far the worst / very similar'),
 (3, '관용 표현의 정해진 모양: as 원급 as possible · get 비교급 and 비교급 · the 비교급, the 비교급 · one of the 최상급 복수명사 · no other 단수명사 as 원급 as / 비교급 than', 'as fast as possible / wiser and wiser / the older, the lighter'),
]
