from game_schedule_crawling import get_game_schedule
from data_filtering import filtering_games
from sending_kakaotalk import sending_kakaotalk

# def main():
#     games = get_game_schedule()
#     filtered = filtering_games(games)
#     sending_kakaotalk(filtered)

from datetime import datetime

def main():
    test_date = datetime(2026, 3, 29)
    games = get_game_schedule(test_date)  # 경기 있었던 날짜
    print(f"수집된 경기 수: {len(games)}")
    for game in games:
        print(game)
    
    filtered = filtering_games(games, today=test_date)
    print(f"필터링된 경기 수: {len(filtered)}")
    sending_kakaotalk(filtered)

if __name__ == '__main__':
    main()