import json
from pathlib import Path

PENDING_FILE = 'pending_games.json'

def save_games(games):
    with open(PENDING_FILE, 'w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False, indent=2)