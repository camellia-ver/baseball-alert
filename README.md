# ⚾ Samsung Baseball Alert

KBO 경기 일정을 수집하여 삼성 라이온즈 경기 중 TV 중계가 있는 날만  
당일 오전 9시에 카카오톡으로 자동 전송하는 프로그램입니다.

## 🛠 기술 스택

- **Language**: Python
- **Crawling**: Selenium
- **Automation**: GitHub Actions
- **Notification**: Kakao Talk API

## 📁 프로젝트 구조

```
samsung-baseball-alert/
├── .github/
│   └── workflows/
│       └── schedule.yml       # 매일 오전 9시 자동 실행
├── main.py                    # 전체 흐름 통합
├── game_schedule_crawling.py  # KBO 경기 일정 수집
├── data_filtering.py          # 삼성 + TV 중계 필터링
├── sending_kakaotalk.py       # 카카오톡 전송
├── token_manager.py           # 토큰 자동 재발급
├── constants.py               # TV 방송국 매핑 테이블
├── config.yaml                # 설정값
└── requirements.txt           # 라이브러리 목록
```

## ⚙️ 동작 방식

```
1. 매일 오전 9시 GitHub Actions 자동 실행
2. KBO 공식 사이트에서 경기 일정 크롤링
3. 삼성 라이온즈 + TV 중계 경기 필터링
4. 카카오톡 나와의 채팅으로 경기 정보 전송
```

## 🔒 GitHub Secrets 설정

| Name | 설명 |
|---|---|
| `KAKAO_ACCESS_TOKEN` | 카카오 액세스 토큰 |
| `KAKAO_REFRESH_TOKEN` | 카카오 리프레시 토큰 |
| `KAKAO_REST_API_KEY` | 카카오 REST API 키 |
| `KAKAO_CLIENT_SECRET` | 카카오 클라이언트 시크릿 |

## 📬 카카오톡 메시지 예시

```
⚾ 오늘의 삼성 라이온즈 경기 안내

📅 03.29(일)
⏰ 14:00
🏟️ 대구삼성라이온즈파크
📺 MBC Sports+
🆚 롯데 vs 삼성
```