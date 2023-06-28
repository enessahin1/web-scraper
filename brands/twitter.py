from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from brands.base_scraping import BaseScraping
from selenium import webdriver


class TwitterFirstData(BaseScraping):
    WAIT_TIME = 40

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        )

    def run(self):
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get(self.get_url())
        wait = WebDriverWait(driver, self.WAIT_TIME)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-kzbkwu")))
        data = driver.page_source
        driver.close()
        driver.quit()
        return self.parse_data(data)

    def get_url(self):
        return 'https://twitter.com/?lang=en'

    def parse_data(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        load_data = soup.find('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
        return self.remove_whitespace(load_data.text)


class TwitterIntegration:
    actions = {
        "get_first_data": TwitterFirstData
    }

    def execute(self, action_name):
        action = self.actions.get(action_name)
        if action:
            return action().run()
        else:
            raise Exception("Action not found")
