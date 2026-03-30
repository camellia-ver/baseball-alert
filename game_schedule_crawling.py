from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import re

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

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    driver.implicitly_wait(5)

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

            teams = cols[1 + offset].text.strip()
            parts = re.split(r'\d*vs\d*', teams)
            game = {
                'date': current_date,
                'time': cols[0 + offset].text.strip(),
                'away': parts[0].strip(),
                'home': parts[1].strip() if len(parts) > 1 else '',
                'tv': cols[4 + offset].text.strip(),
                'stadium': cols[6 + offset].text.strip(),
            }
            games.append(game)

        return games
    finally:
        driver.quit()