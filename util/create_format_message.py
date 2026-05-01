from core.constants import TV_MAPPING

def format_game_message(games, game_after=False):
    title = '⚾ 오늘의 삼성 라이온즈 경기 결과 안내\n\n' if game_after else '⚾ 오늘의 삼성 라이온즈 경기 안내\n\n'

    game_message = []
    for game in games:
        tv_display = ', '.join(TV_MAPPING.get(tv, tv) for tv in game['tv'])
        lines = [
            f"📅 {game['date']}",
            f"⏰ {game['time']}",
            f"🏟️ {game['stadium']}",
            f"📺 {tv_display}",
        ]

        if game_after:
            if game['remarks'] == '-':
                lines.append(f"🆚 {game['away']} {game['away_score']} vs {game['home_score']} {game['home']}\n")
            else:
                lines.append(f"🆚 {game['away']} vs {game['home']}\n")
                lines.append(f"📝 {game['remarks']}")

            if game['highlight_url'] is not None: 
                lines.append(f"🎬 하이라이트: {game['highlight_url']}") 
        else:
            lines.append(f"🆚 {game['away']} vs {game['home']}\n")

        game_message.append('\n'.join(lines))

    return title + '\n\n'.join(game_message)
