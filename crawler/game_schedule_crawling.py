from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import re

def parse_teams(team_str):
    pattern = r'([A-Za-z가-힣]+)(\d*)vs(\d*)([A-Za-z가-힣]+)'
    m = re.match(pattern, team_str)

    if m:
        away, away_score, home_score, home = m.groups()
        return {
            'away': away,
            'home': home,
            'away_score': int(away_score) if away_score else None,
            'home_score': int(home_score) if home_score else None,
        }

def get_game_schedule(date=None):
    if date is None:
        date = datetime.today()

    year = date.year
    month = date.month
    url = f"https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0&year={year}&month={month}"

    options = Options()
    options.add_argument("--headless") # 브라우저 창 안 띄움
    options.add_argument("--no-sandbox") # sandbox 비활성화
    options.add_argument("--disable-dev-shm-usage") # 메모리 문제 방지

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)

    try:
        driver.get(url)
    except TimeoutException:
        driver.quit()
        return []

    try:
        rows = driver.find_elements(By.CSS_SELECTOR, "#tblScheduleList tbody tr")

        current_date = ""
        games = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")

            if len(cols) < 8:
                continue

            # 날짜가 있으면 업데이트
            if cols[0].text.strip() and '(' in cols[0].text:
                current_date = cols[0].text.strip()
                offset = 1 # 날짜 컬럼만큼 밀림
            else:
                offset = 0

            teams = parse_teams(cols[1 + offset].text.strip())
            highlight_links = cols[3 + offset].find_elements(By.TAG_NAME, 'a')
            has_highlight = len(highlight_links) > 0
            highlight_url = highlight_links[0].get_attribute('href') if has_highlight else None
            game = {
                'date': current_date,
                'time': cols[0 + offset].text.strip(),
                'away': teams['away'],
                'away_score': teams['away_score'],
                'home': teams['home'],
                'home_score': teams['home_score'],
                'has_highlight': has_highlight,
                'highlight_url': highlight_url,
                'tv': cols[4 + offset].text.strip(),
                'stadium': cols[6 + offset].text.strip(),
                'remarks': cols[7 + offset].text.strip()
            }
            games.append(game)

        return games
    finally:
        driver.quit()