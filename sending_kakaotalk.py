import requests
import os
import json
from constants import TV_MAPPING

ACCESS_TOKEN = os.environ['KAKAO_ACCESS_TOKEN']
REST_API_KEY = os.environ['KAKAO_REST_API_KEY']
CLIENT_SECRET = os.environ['KAKAO_CLIENT_SECRET']

def sending_kakaotalk(games):
    if not games:
        return
    
    message = "⚾ 오늘의 삼성 라이온즈 경기 안내\n\n"
    
    for game in games:
        message += f"📅 {game['date']}\n"
        message += f"⏰ {game['time']}\n"
        message += f"🏟️ {game['stadium']}\n"
        message += f"📺 {TV_MAPPING.get(game['tv'], game['tv'])}\n"
        message += f"🆚 {game['away']} vs {game['home']}\n"
        message += "\n"

    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }

    data = {
        'template_object': json.dumps({
            'object_type': 'text',
            'text': message,
            'link': {}
        })
    }

    response = requests.post(url, headers=headers, data=data)