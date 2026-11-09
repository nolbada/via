# 검수 지침 (어법제대로 데일리 방식 해설)
너는 새로 투입된 검수자다. 담당 key마다 `_tools/base/<key>.json`(문제·바른문장·원 해설: 정답 기준)과 `_tools/daily/<key>.json`(새 해설)을 항목별로 대조해 **오류를 직접 고친다**(daily json만 수정; base는 건드리지 말 것). 형식 규칙은 `_tools/BRIEF_DAILY.md` 참조.
항목마다 확인:
1. 정렬: daily 항목 내용(fm/mp/ex/why)이 그 base 항목의 오류(wr→to, fr)와 같은 포인트를 다루는가? dk 영어 이음 = base correct.
2. 정답·결론이 base explain과 모순되지 않는가. base 자체가 의심스러우면 고치지 말고 보고.
3. 한국어 해석(ko)·dk 한글·tko·exko·altko의 번역 정확성, 쉬운 예/틀린 예/alt 영어 문법(bad는 정말 틀린 문장이어야 하고 alt는 정말 맞는 문장이어야 함), mp 쉬운 예와 이번 조각의 1:1 구조 일치.
4. why가 초등6 눈높이, gist/fm과 중복 없음, 동사는 원형(뜻) 병기, 영어엔 한글 뜻, 이모지 없음, 어색한 한국어.
5. trend 순위가 BRIEF_DAILY 매핑표와 일치(표에 없으면 10위 밖), 숫자 지어내기 금지.
6. d(단어사전) 뜻이 문장 문맥에 맞는지, 어려운 단어 누락.
7. 같은 페이지 안에서 쉬운 예가 지나치게 반복되면(같은 문장 구조·같은 단어) 다양화.
고친 뒤 `cd /home/claude/via/eobeop-jedaero && python3 _tools/check_daily.py <key>` 가 OK여야 한다. build_daily.sh/gc.py/gen_daily.py/git 금지.
보고: 고친 항목 수와 유형별 요약(예: 번역 3, 문법 2…), 고치지 못한 의심 사항(key #번호 + 이유). 오류가 없으면 0이라고 정직하게.
