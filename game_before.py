from game_schedule_crawling import get_game_schedule
from data_filtering import filtering_games
from sending_kakaotalk import sending_kakaotalk
from token_manager import ensure_valid_token

def main():
    ensure_valid_token() # 토큰 유효성 확인 및 갱신
    games = get_game_schedule()
    filtered = filtering_games(games)
    sending_kakaotalk(filtered)

if __name__ == '__main__':
    main()