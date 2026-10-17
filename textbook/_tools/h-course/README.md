# 고교 교과서 코스 앱 제작 도구 (H-K코스 / H-S코스)

- build_hk.py : H-K코스(V시그널 E '오늘 7문장' 방식) 앱 생성. vsignal-e/index.html 의 DATA 를 교체하고 gq_patch.js(마스킹테이프·닮은꼴·절 종류 질문)를 끼워 넣음. 문장 데이터(D 리스트)와 GQ(절/형식 정답)를 고쳐 쓰면 다른 과·문장에도 재사용.
- gq_patch.js : 마스킹테이프(꾸밈말 '가림', 절 'who ...') → 닮은꼴(1~5형식) → 절 종류 질문 코드.
- build_hs.py : H-S코스(Y xray 심화 방식) 앱 생성. vsignal-y/xray.html 의 S 배열을 교체. add(...) 항목 형식은 파일 안 예시 참고.
- test_hk.py / test_hs.py : 헤드리스 크롬으로 끝까지 자동 풀이(결과 화면 확인). 멈추면 STALL 로 보고.
- 원본 vsignal-e, vsignal-y 는 읽기 전용(수정 금지). 출력은 textbook/<학교>/<과>/e/ , y/ .
- 경로(SRC/OUT)는 파일 상단에서 바꿔 쓴다.
