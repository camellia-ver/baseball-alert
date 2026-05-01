from crawler.game_schedule_crawling import get_game_schedule
from core.data_filtering import filtering_games
from kakao.sending_kakaotalk import sending_kakaotalk
from kakao.token_manager import ensure_valid_token
from discord.send_discord import sending_discord
from core.file_manage import load_games, save_games
from core.check_finish_game import is_game_finished
from util.load_config import load_config
import time

def main():
    config = load_config()
    channel = config['notification']['channel']
    
    channel_handlers = {
        'discord': (None, sending_discord),
        'kakao': (ensure_valid_token, sending_kakaotalk)
    }
    ensure_token, send_fn = channel_handlers[channel]

    if ensure_token:
        ensure_token() # 토큰 유효성 확인 및 갱신

    filtered = load_games()
    if not filtered:
        return

    games = get_game_schedule()
    filtered = filtering_games(games, config, today= filtered[0]['date'], after_game=True)

    pending = None
    if len(filtered) > 2:
        pending = filtered.pop()

    if all(is_game_finished(g) for g in filtered):        
        send_fn(filtered, game_after=True)  
        save_games([pending] if pending else [])

if __name__ == '__main__':
    main()