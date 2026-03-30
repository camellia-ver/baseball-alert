import yaml
from datetime import datetime

TV_MAPPING = {
    "S-T": "SBS",
    "M-T": "MBC",
    "K-2T": "KBS2",
    "SPO-T": "SPOTV",
    "SPO-2T": "SPOTV2",
    "MS-T": "MBC Sports+",
    "SS-T": "SBS Sports",
    "KN-T": "KBS N Sports",
}

def load_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
    
def filtering_games(games):
    config = load_config()
    team = config['team']
    broadcast = config['broadcast']
    today = datetime.today().strftime('%m.%d')

    filtered = []
    for game in games:
        is_today = game['date'].startwith(today)
        is_target_team = is_target_team = game['away'] == team or game['home'] == team
        is_tv_broadcast = TV_MAPPING.get(game['tv'], game['tv']) in broadcast

        if is_today and is_target_team and is_tv_broadcast:
            filtered.append(game)

    return filtered