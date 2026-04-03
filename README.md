# ⚾ Baseball Alert

KBO 경기 일정을 수집하여 삼성 라이온즈 경기 중 TV 중계가 있는 날만  
당일 오전 9시에 카카오톡으로 자동 전송하는 프로그램입니다.  
경기 종료 후에는 최종 결과(스코어, 하이라이트 링크)도 자동으로 전송합니다.

<br>

## 🛠 기술 스택

| 항목 | 내용 |
|------|------|
| Language | Python |
| Crawling | Selenium |
| Automation | GitHub Actions |
| Notification | Kakao Talk API |

<br>

## 📁 프로젝트 구조

```
baseball-alert/
├── .github/
│   └── workflows/
│       └── schedule.yml          # GitHub Actions 자동 실행 스케줄
│
├── crawler/
│   └── game_schedule_crawling.py # KBO 공식 사이트 경기 일정 크롤링
│
├── core/
│   ├── data_filtering.py         # 팀 / TV 중계 필터링
│   ├── file_manage.py            # pending_games.json 읽기 · 쓰기
│   └── constants.py              # TV 방송국 매핑 테이블
│
├── kakao/
│   ├── sending_kakaotalk.py      # 메시지 포맷 생성 및 카카오톡 전송
│   └── token_manager.py          # 액세스 토큰 유효성 검사 및 자동 갱신
│
├── data/
│   └── pending_games.json        # 경기 전 저장된 당일 경기 정보 (런타임 생성)
│
├── game_before.py                # 진입점 1 — 경기 전 알림 (오전 9시)
├── game_after.py                 # 진입점 2 — 경기 후 결과 전송 (경기 종료 후)
├── config.yaml                   # 필터링 설정 (팀명, 중계 채널 목록)
├── requirements.txt              # 의존 라이브러리
└── .gitignore
```

<br>

## ⚙️ 동작 방식

### 경기 전 알림 (`game_before.py`)
```
1. 매일 오전 9시 GitHub Actions 자동 실행
2. KBO 공식 사이트에서 당일 경기 일정 크롤링
3. 삼성 라이온즈 경기 중 TV 중계 있는 경기만 필터링
4. 필터링된 경기 정보를 pending_games.json에 저장
5. 카카오톡 나와의 채팅으로 경기 정보 전송
```

### 경기 후 결과 (`game_after.py`)
```
1. 경기 종료 예상 시간에 GitHub Actions 자동 실행
2. pending_games.json에서 당일 경기 정보 로드
3. 경기 종료 여부 확인 (하이라이트 등록 또는 취소 여부)
4. 모든 경기가 종료되면 스코어 · 하이라이트 링크 전송
5. pending_games.json 초기화
```

<br>

## 🔒 GitHub Secrets 설정

| Secret 이름 | 설명 |
|---|---|
| `KAKAO_ACCESS_TOKEN` | 카카오 액세스 토큰 |
| `KAKAO_REFRESH_TOKEN` | 카카오 리프레시 토큰 |
| `KAKAO_REST_API_KEY` | 카카오 REST API 키 |
| `KAKAO_CLIENT_SECRET` | 카카오 클라이언트 시크릿 |
| `GH_TOKEN` | GitHub Personal Access Token (Secrets 자동 갱신용) |
| `GH_REPO` | 레포지토리 이름 (예: `username/baseball-alert`) |

<br>

## 📬 카카오톡 메시지 예시

**경기 전 알림**
```
⚾ 오늘의 삼성 라이온즈 경기 안내

📅 03.29(일)
⏰ 14:00
🏟️ 대구삼성라이온즈파크
📺 MBC Sports+
🆚 롯데 vs 삼성
```

**경기 후 결과**
```
⚾ 오늘의 삼성 라이온즈 경기 결과 안내

📅 03.29(일)
⏰ 14:00
🏟️ 대구삼성라이온즈파크
📺 MBC Sports+
🆚 롯데 3 vs 5 삼성

🎬 하이라이트: https://...
```