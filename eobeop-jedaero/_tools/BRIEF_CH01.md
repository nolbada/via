# CH01 빠진 해설 제작 브리프 (p.12~p.18)

배경: 해커스 어법 제대로 CHAPTER 1 변형문제(원문: _tools/src/ch1_byunhyung_p12-15.txt, ch1_byunhyung_p16-18.txt).
선생님이 직접 만든 해설 일부(p.12 전체 8문항, p.13 1~4번)는 _tools/src/ch1_haeseol_partial_p12-13.txt — 이 내용(바른문장·해석·해설)은 선생님 원본이니 그대로 살려 쓴다(문장 다듬기만, 뜻 바꾸지 말 것). 나머지는 새로 쓴다.

## 1) 내용 JSON → 페이지 생성
- /home/claude/via/eobeop-jedaero/_tools/content/<key>.json 작성 (형식: _tools/gen_page.py 맨 위 docstring 참고; 예시는 ch02-p24.html 한 카드)
- sentence: 변형문제 원문 그대로, 오류 부분을 <w>…</w> 로 감싼다. from/to: 틀린 표현 → 바른 표현. correct: 바른 문장 전체. interp: 자연스러운 한국어 해석.
- ch: 두 자리 챕터(예 "12"), badge: "챕터 POINT 이름 (Chapter 12 POINT 2)" — 이름은 /root/.claude/skills/synced/*/haekeoseu-eobeop-jedaero/references/chapter_points.md 표를 그대로 사용, 반드시 "(Chapter N POINT M)" 형태 포함(그래머콕 링크가 이걸 읽음).
- explain: 해설 HTML(<b>만 사용). 기존 ch02-p24.html 카드 문체 참고: 왜 틀렸는지 + 맞는 이유 + 문장 속 다른 포인트(추가 어법 포인트)를 짧게. 학생용: 쉬운 한국어, 영어에는 한글 뜻, 동사는 원형+뜻 병기.
- 선생님 원본 해설을 쓸 때도 위 형식으로 옮기되, 선생님이 단 '어법 유형'은 가장 가까운 Chapter/POINT로 매핑해 badge에 쓴다.
- 문항 수는 원문 번호와 정확히 일치(★ 표시는 번호 앞 ★ 무시하고 sentence에 넣지 않음). 지문(p.18)은 groups를 지문별로 나눈다(bar: "p.18 · 1번 지문 정답 및 해설"), 한 지문에 오류가 1~2개 → 각 오류가 한 item(문장 단위: 그 오류가 든 문장 하나가 sentence), 같은 문장에 오류 2개면 item 2개. tag는 쓰지 않음.
- prev/next: 순서는 ch01-p12 → p13 → p14 → p15 → p16 → p17 → p18 → ch01-p20-21a. 라벨은 "p.13 ▶" 식, 이전은 ["ch01-p12","p.12"] (gen_page가 "◀ " 붙임). p12는 prev null, p18 next ["ch01-p20-21a","p.20~21 ①"].
- 실행: cd /home/claude/via/eobeop-jedaero && python3 _tools/gen_page.py _tools/content/<key>.json

## 2) 문장 분석 JSON (노트정리)
_tools/BRIEF.md 의 규칙 전부 그대로(JSON 스키마·닮은꼴 고정값·문체). 각 answerline(=오류 하나)마다 1개, 문서 순서대로 → _tools/anl/<key>.html.json, 그리고
 python3 _tools/inject.py <key>.html _tools/anl/<key>.html.json  (eobeop-jedaero 폴더에서) → 'ok'
 python3 _tools/gc.py  는 마지막에 내가 한 번 돌리니 너는 돌리지 말 것.
수동태 문장은 form "3형식", merel "수동태".

## 3) 규칙
- git 건드리지 말 것. 담당 key 파일 외 수정 금지(특히 index.html, ch02~ 파일).
- 정확성 최우선: 바른문장이 정말 문법적으로 맞는지, 오류 판정이 맞는지(예: 변형문제에 오류가 없어 보이는 문장이나 오류가 둘로 보이는 문장은 보고) 스스로 한 번 전수 검산.
- 끝나면 짧게 보고: 페이지·항목 수, 애매한 항목(원문 오류 의심 포함).
