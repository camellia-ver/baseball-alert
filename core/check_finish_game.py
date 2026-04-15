def is_game_finished(game):
    if game['remarks'] != '-':  # 취소
        return True
    
    if game['has_review']:   # 정상 종료
        return True
    
    return False
