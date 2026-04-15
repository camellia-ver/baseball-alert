import yaml
from datetime import datetime
from core.constants import TV_MAPPING
from core.file_manage import save_games

def load_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
    
def filtering_games(games, today=None, after_game=False):
    if today is None:
        today = datetime.today().strftime("%m.%d")

    config = load_config()
    team = config['team']
    broadcast = config['broadcast']

    filtered = []
    save_data = []
    for game in games:
        is_today = game['date'].startswith(today)
        is_target_team = game['away'] == team or game['home'] == team
        is_tv_broadcast = True if after_game else any(
            TV_MAPPING.get(tv, tv) in broadcast for tv in game['tv']
        )
        
        if is_today and is_target_team:
            save_data.append(game)
            if is_tv_broadcast:
                filtered.append(game)

    save_games(save_data)

    return filtered