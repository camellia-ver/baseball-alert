import requests
import os
import json
from util.create_format_message import format_game_message

def sending_kakaotalk(games, game_after=False):
    if not games:
        return

    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

    access_token = os.environ['KAKAO_ACCESS_TOKEN']
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    data = {
        'template_object': json.dumps({
            'object_type': 'text',
            'text': format_game_message(games, game_after),
            'link': {}
        })
    }

    response = requests.post(url, headers=headers, data=data)