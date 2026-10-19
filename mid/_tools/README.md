# 중등 V시그널 복합형 분석 (M-K 기본 / M-S 심화) — 설계와 제작 순서
중2 동아(윤) 7·8과로 만든 방식. 다른 과·다른 교과서도 같은 순서로 만든다. (학생 화면 이름: "핵심 문장 분석 (기본)/(심화)")

## 두 코스
- 기본(M-K): 한글 어순 맞추기(E의 1단계) → 엑스레이(동사 모두 누르기 → 접착제(문장 둘을 잇는 and/but/so) → 가림판 뺀 뼈대의 닮은꼴(1~5형식) 고르기 → 내 문장 뼈대와 닮은꼴 2번 눌러 선잇기) → 성분 맞추기 → 영어 어순 쌓기 → 마무리 퀴즈. 종속절·준동사는 한 덩어리로 묶어 둠.
- 심화(M-S): 한글 해석 맞추기만 뺌. 엑스레이 뒤에 가려진 덩어리 정체(명사절/형용사절/부사절, to부정사 용법, 동명사, 분사) 고르기 → 그 덩어리 안쪽을 다시 동사·뼈대·선잇기(중첩 가능, 따옴표 안 문장 포함) → 성분 → 어순 → 퀴즈.
- 고등용(H-K/H-S)과 별개. 저장 위치는 via 저장소 `mid/` 아래 (textbook/ 아님).

## 파일
- 앱: `mid/dongah-yun/l7|l8/basic|adv/index.html` (허브 `mid/dongah-yun/index.html`, `l7/index.html`)
- 도구/데이터: `mid/_tools/dongah-yun/` — units.json(문장 목록·일차 배정), data/basic_N.json(분석), data/deep_N.json(안쪽 분석), CONVENTIONS.md / DEEP_CONVENTIONS.md(작성 규칙), validate*.py(검증), build_basic.py(앱 조립: vsignal-e/index.html을 패치), xray_patch.js/xray_handlers.js(엑스레이 단계), test_all.py/test_adv.py(자동 풀이 테스트)
- 스크립트의 경로(/tmp/claude-0/w3, /home/claude/nolbada/via)는 제작 때 환경 기준이라 새 환경에서는 바꿔 쓴다.

## 순서
1. 교재 PDF에서 본문 추출 → 문장 단위로 쪼개 units.json 작성(감탄사 조각 제외, 하루 6~7문장).
2. 기본 데이터: 문장 약 14개씩 나눠 에이전트 병렬 작성 → validate.py → 별도 검토 에이전트로 전수 검토.
3. 심화 데이터: 검토 끝난 기본 데이터를 입력으로 deep 작성 → validate_deep.py → 별도 검토(힌트가 정답을 말하지 않는지 포함).
4. 조립 build_basic.py(rebuild_basic.py / rebuild_deep.py) → test_all.py / test_adv.py 전 일차 자동 풀이(모두 '분석 완료'까지) → via에 push.
## 주의
- 의문문처럼 한 라운드에 같은 역할이 두 번 나오면 선잇기가 안 풀리니 조동사(Can)·가주어(it)는 꾸밈말로 처리.
- 학생 화면에 서열 표현 금지, 앱은 고르기만(쓰기는 종이).
