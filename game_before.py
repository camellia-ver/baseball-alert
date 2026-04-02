from game_schedule_crawling import get_game_schedule
from data_filtering import filtering_games
from sending_kakaotalk import sending_kakaotalk
from token_manager import ensure_valid_token
from file_manage import save_games

def main():
    print('ensure_valid_token start')
    ensure_valid_token() # 토큰 유효성 확인 및 갱신
    print('ensure_valid_token end')
    print('get_game_schedule start')
    games = get_game_schedule()
    print('get_game_schedule end')
    print('filtering_games start')
    filtered = filtering_games(games)
    print('filtering_games end')
    print('sending_kakaotalk start')
    sending_kakaotalk(filtered)
    print('sending_kakaotalk end')
    print('save_games start')
    save_games(filtered)
    print('save_games end')

if __name__ == '__main__':
    main()