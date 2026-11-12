# 어법 제대로 문장분석 앱·PDF 설계 (261113)

- 앱: eobeop-sentence/index.html (챕터 목록 → POINT → 문장 풀이). 챕터 데이터는 d/chNN.js. 학생 진도 저장 키 eobeop-sent-v2 (CH01 POINT 1~3은 예전 id p1~p3 유지).
- 데이터 흐름: src/data_chNN_points.py(원본 정답·해석·해설) + author/chNN.py(덩어리·한글 직독직해·성분·정답 쌍·노트) → `python3 mk.py NN` → data/chNN.json → build_app.py(앱) / build_pdf.py(PDF).
- 자동 검수: validate.py (덩어리 영어 이어붙인 것 = 정답 문장, 해석·해설·구조 칩 원본 일치, 정답이 V 덩어리에 있는지, 누르기 대상 존재 등).
- 새 문장 추가·수정: author/chNN.py만 고치고 mk.py → build_app.py. 앱을 갱신하면 sw 캐시 이름(build_app.py 2번째 인자)을 올린다.
- 누르기 단계(taps): POINT마다 핵심 종류(S 주어/선행사, M 건너뛸 수식어, C 단서)를 학생이 먼저 눌러 찾는다.
