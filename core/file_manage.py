import json
import os
from pathlib import Path
from datetime import datetime

PENDING_FILE = 'data/pending_games.json'

def save_games(games):
    os.makedirs(os.path.dirname(PENDING_FILE), exist_ok=True)
    
    with open(PENDING_FILE, 'w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False, indent=2)

def load_games():
    path = Path(PENDING_FILE)
    if not path.exists():
        return []
    
    with open(PENDING_FILE, 'r', encoding='utf-8') as f:
        games = json.load(f)

    today = datetime.today().strftime('%m.%d')

    return [g for g in games if today in g['date']]