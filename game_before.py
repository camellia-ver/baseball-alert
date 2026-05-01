from crawler.game_schedule_crawling import get_game_schedule
from core.data_filtering import filtering_games
from discord.send_discord import sending_discord
from kakao.sending_kakaotalk import sending_kakaotalk
from kakao.token_manager import ensure_valid_token
from util.load_config import load_config

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

    games = get_game_schedule()
    filtered = filtering_games(games, config)
    send_fn(filtered)

if __name__ == '__main__':
    main()