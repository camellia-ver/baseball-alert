from datetime import datetime
import zoneinfo
from core.constants import TV_MAPPING
from core.file_manage import save_games
    
def filtering_games(games, config, today=None, after_game=False):
    if today is None:
        today = datetime.now(zoneinfo.ZoneInfo('Asia/Seoul')).strftime("%m.%d")

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