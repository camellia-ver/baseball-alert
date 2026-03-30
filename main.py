from game_schedule_crawling import get_game_schedule
from data_filtering import filtering_games
from sending_kakaotalk import sending_kakaotalk

def main():
    games = get_game_schedule()
    filtered = filtering_games(games)
    sending_kakaotalk(filtered)

if __name__ == '__main__':
    main()