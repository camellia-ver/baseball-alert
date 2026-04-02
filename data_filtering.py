import yaml
from datetime import datetime
from constants import TV_MAPPING

def load_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
    
def filtering_games(games, today=None, after_game=False):
    if today is None:
        today = datetime.today()
    today = today.strftime("%m.%d")

    config = load_config()
    team = config['team']
    broadcast = config['broadcast']

    filtered = []
    for game in games:
        is_today = game['date'].startswith(today)
        is_target_team = is_target_team = game['away'] == team or game['home'] == team
        is_tv_broadcast = after_game if after_game else (TV_MAPPING.get(game['tv'], game['tv']) in broadcast)

        if is_today and is_target_team and is_tv_broadcast:
            filtered.append(game)

    return filtered