# 문장 구조 분석(sx) 작성 브리프

작업 폴더: /home/claude/via/eobeop-sentence/_src/sx  (이 폴더 밖은 건드리지 말 것)
- 입력: in/chNN.json (내 챕터 NN 하나만). 항목마다 key, title(POINT 제목), chunks=[[영어,한글,종류(S/M/V/C/'')]...], tr(전체 해석), ans(정답 말).
- 출력: out/chNN.json 하나. {key: [[마크업, 메모], ...]} — chunks와 같은 개수·같은 순서. 메모가 없으면 "".
- 검사: `python3 mk_sx.py NN` → errors=0 될 때까지 고친다. 완료 보고는 3줄 이내(문항 수, 남긴 의문점, 불확실한 항목 key).
- 모든 key를 빠짐없이 작성(누락 금지). 스크립트로 대충 자동 생성하지 말고 문장마다 직접 읽고 분석한다(보조 스크립트로 JSON을 조립하는 것은 괜찮음).

## 하는 일
각 문장을 아이카식 '문장 전체 구조 분석'으로 표시한다. 기존 분석(S/M/V 칩)은 정답 중심이고, 이것은 문장 속 **모든** 동사·접속사·절·준동사를 보여 주는 보충이다.
덩어리(chunk)별로 영어 마크업과 초록 메모를 쓴다. 영어 글자는 한 글자도 바꾸지 않는다(태그와 【 】만 추가 — mk_sx.py가 영어를 대조한다).

## 마크업 태그
- `{v|…}` 동사(구). 모든 절의 동사를 표시한다: 본동사, 관계사절·종속절 안의 동사, 조동사+동사 한 덩어리(will be done, have solved, would like to ask 의 would like), 병렬 동사(and 뒤 동사 포함).
  준동사(to부정사·동명사·분사)는 {v}가 아니라 {p}.
- `{a|…}` 정답이 들어 있는 말(ans). 문항당 보통 하나. 동사가 정답이면 그 동사를 {v} 대신 {a}로. 정답이 동사가 아니면(시간 표현, 접속사, 대명사 등) 그 말에 {a}. 동사가 정답인 문항에서도 문장 속 다른 동사는 {v}.
  ans가 '○'이거나 여러 말이면 가장 핵심인 말 하나에 {a}, 없으면 {a} 생략 가능(그 경우 mk_sx 정답 검사는 '○'만 면제).
- `{c|…}` 접속사·관계사·의문사·접속부사(and, but, or, that, which, who, when, because, if, whether, as, while, although, however, so …)를 상자로. 등위접속사 and/but/or도 포함(병렬 구조 표시).
- `{p|…}` 준동사 표지: to부정사의 to, 동명사·분사의 -ing/-ed 형태 단어(수식하는 분사 포함). 해당 단어 하나만 감싼다. 
- `【 】` 종속절·관계사절·준동사구·삽입구의 시작과 끝을 표시. 여러 덩어리에 걸쳐도 되지만 한 문장 안에서 짝이 정확히 맞아야 한다. 중첩 가능하나 2단계까지만.
  관계사절 = 【{c|that} {v|has} …】, 분사구 = 【{p|climbing} up the mountain】, to부정사구 = 【{p|to} make new friends】, 명사절 = 【{c|what} you {v|watch} …】, 종속절 = 【{c|When} couples {v|get} married today,】.
- 가능하면 덩어리 경계에서 괄호가 열리고 닫히게 쓰되, 덩어리 안에서 열고 닫아도 된다.
- 주어는 표시하지 않는다(기존 칩이 있음). 전치사구·명사구에는 태그를 달지 않는다.

## 메모(초록 글씨) 규칙
- 40자 이하(검사). 한 문장에서 메모는 1~4개, 구조가 어려운 곳에만. 다는 곳: 절·준동사의 종류와 수식 대상, 병렬 구조, 숙어·구동사·고정 표현, 전치사+동명사, 도치·생략·삽입, 접속사의 뜻 등.
- 예: "to부정사 (형용사적) : way를 꾸밈", "주격 관계대명사절 : a house를 꾸밈", "계속적 용법 : Insects 보충 설명", "병렬 : 동사 두 개 연결", "전치사 + 동명사", "현재분사구 : hikers를 꾸밈", "look like + 명사 : ~처럼 보이다", "접속사 + 분사구문", "so ~ that 구문".
- 화살표(→, ➔, ->) 금지. 이모지 금지. 학생이 읽는 쉬운 말. 영어 단어를 쓰면 같은 덩어리·문장에 보이는 단어로 한정하고 필요하면 한글 뜻을 붙인다(문법 용어 자체는 한글).
- 이미 기존 칩 라벨(lab)에 있는 정답 수일치 설명을 반복하지 말고, 그 문장의 나머지 구조(절·준동사·병렬)를 보충한다. 구조가 아주 단순한 문장은 메모가 0~1개여도 된다.
- 문법적으로 틀린 말을 쓰지 말 것. 확신이 안 서면 메모를 달지 않는다. 원본 해석(tr)과 한글 덩어리와 어긋나는 구조 분석 금지.

## 문장 종류별 주의
- 틀린 곳 고치기(fix) 문항의 chunks는 '고친 정답 문장'이다. 그 정답 문장 기준으로 분석한다.
- 배열·서술형 힌트가 있었던 문항도 chunks(완성된 정답 문장) 기준.
- 문장 앞 'Typically,' 같은 부사어, 쉼표 삽입은 태그 없이 둔다.
- be동사(is, are, was)·have·do도 동사이므로 {v}. 'be going to'는 {v|is going to} 처럼 한 덩어리(to는 {p} 아님).
- would like to ask: {v|would like} {p|to} {v|ask}가 아니라 to ask는 {p|to} ask (ask는 준동사 일부라 태그 없음). 즉 준동사의 동사원형/분사는 태그 없이 두고 표지(to, -ing)만 {p}.
  동명사·분사는 -ing/-ed 단어 자체가 {p}.

## 모범 (CH01 추가문제, in 형식 → out 형식)
A good way / to make new friends / is / to join a social group / with people your age.
 → ["A good way",""], ["【{p|to} make new friends】","to부정사 (형용사적) : way를 꾸밈"], ["{a|is}",""], ["{p|to} join a social group","to부정사 (명사적) : 보어"], ["with people 【your age】.","people (who are) your age"]  ← (필요하면 이런 생략 설명도 가능)
Typically, / a house / that has a swimming pool / costs / a lot of money.
 → ["Typically,",""],["a house",""],["【{c|that} {v|has} a swimming pool】","주격 관계대명사절 : a house를 꾸밈"],["{a|costs}","본동사"],["a lot of money.","cost + 목적어 : 돈이 ~ 든다"]
Insects, / which normally serve a useful purpose in nature, / are in danger / due to climate change.
 → ["Insects,",""],["【{c|which} normally {a|serve}","계속적 용법 : Insects 보충 설명"],["a useful purpose in nature】,",""],["{v|are} in danger","본동사"],["due to climate change.","due to + 명사 : ~ 때문에"]
