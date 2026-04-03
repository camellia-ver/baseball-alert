from crawler.game_schedule_crawling import get_game_schedule
from core.data_filtering import filtering_games
from kakao.sending_kakaotalk import sending_kakaotalk
from kakao.token_manager import ensure_valid_token

# def main():
#     ensure_valid_token() # 토큰 유효성 확인 및 갱신
#     games = get_game_schedule()
#     filtered = filtering_games(games)
#     sending_kakaotalk(filtered)

def main():
    ensure_valid_token()
    games = get_game_schedule()
    print(f"전체 경기 수: {len(games)}")
    for g in games[:3]:
        print(g['date'], g['away'], g['home'])  # 날짜 형식 확인
    filtered = filtering_games(games)
    print(f"필터링 후: {len(filtered)}")
    sending_kakaotalk(filtered)

if __name__ == '__main__':
    main()