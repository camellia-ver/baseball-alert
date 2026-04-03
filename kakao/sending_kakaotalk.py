import requests
import os
import json
from core.constants import TV_MAPPING

def format_game_message(games, game_after=False):
    title = '⚾ 오늘의 삼성 라이온즈 경기 결과 안내\n\n' if game_after else '⚾ 오늘의 삼성 라이온즈 경기 안내\n\n'

    game_message = []
    for game in games:
        lines = [
            f"📅 {game['date']}",
            f"⏰ {game['time']}",
            f"🏟️ {game['stadium']}",
            f"📺 {TV_MAPPING.get(game['tv'], game['tv'])}",
        ]

        if game_after:
            if game['remarks'] == '-':
                lines.append(f"🆚 {game['away']} {game['away_score']} vs {game['home_score']} {game['home']}\n")
            else:
                lines.append(f"🆚 {game['away']} vs {game['home']}\n")
                lines.append(f"📝 {game['remarks']}")

            if game['has_highlight']: 
                lines.append(f"🎬 하이라이트: {game['highlight_url']}") 
        else:
            lines.append(f"🆚 {game['away']} vs {game['home']}\n")

        game_message.append('\n'.join(lines))

    return title + '\n\n'.join(game_message)

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