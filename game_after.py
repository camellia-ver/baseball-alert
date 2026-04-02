from crawler.game_schedule_crawling import get_game_schedule
from core.data_filtering import filtering_games
from kakao.sending_kakaotalk import sending_kakaotalk
from kakao.token_manager import ensure_valid_token
from core.file_manage import load_games, save_games
import time

def is_game_finished(game):
    if game['remarks'] != '-':  # 취소
        return True
    if game['has_highlight']:   # 정상 종료
        return True
    
    return False

def main():
    ensure_valid_token() # 토큰 유효성 확인 및 갱신
    filtered = load_games()

    if not filtered:
        return

    games = get_game_schedule()
    filtered = filtering_games(games, after_game=True)

    if all(is_game_finished(g) for g in filtered):
        sending_kakaotalk(filtered, game_after=True)    
        save_games([])

if __name__ == '__main__':
    main()