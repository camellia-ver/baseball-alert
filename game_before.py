from crawler.game_schedule_crawling import get_game_schedule
from core.data_filtering import filtering_games
from discord.send_discord import sending_discord
from kakao.sending_kakaotalk import sending_kakaotalk
from kakao.token_manager import ensure_valid_token
from util.load_config import load_config

def main():
    config = load_config()
    channel = config['notification']['channel']

    if channel == 'kakao':
        ensure_valid_token()  # 카카오 토큰 유효성 확인 및 갱신
        games = get_game_schedule()
        filtered = filtering_games(games, config)
        sending_kakaotalk(filtered)

    elif channel == 'discord':
        games = get_game_schedule()
        filtered = filtering_games(games, config)
        sending_discord(filtered)

    else:
        raise ValueError(f"지원하지 않는 채널입니다: {channel}")

if __name__ == '__main__':
    main()