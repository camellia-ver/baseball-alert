import requests
import os
import json
from util.create_format_message import format_game_message

def sending_discord(games, game_after=False):
    if not games:
        return
    
    url = os.environ['DISCORD_WEBHOOK_URL']

    response = requests.post(
        url,
        json={'content': format_game_message(games, game_after)}
    )