from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

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
            if cols[0].text.strip():
                current_date = cols[0].text.strip()

            game = {
                "date": current_date,
                "time": cols[1].text.strip(),
                "away": cols[2].text.strip(),
                "home": cols[4].text.strip(),
                "tv": cols[7].text.strip(),
                "stadium": cols[9].text.strip(),
            }
            games.append(game)

        return games
    finally:
        driver.quit()