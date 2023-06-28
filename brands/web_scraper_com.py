from bs4 import BeautifulSoup
from brands.base_scraping import BaseScraping


class WebScraperComGetFirstData(BaseScraping):

    def get_url(self):
        return 'https://webscraper.io/test-sites'

    def parse_data(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        lead_text = soup.find('div', class_='col-md-7 pull-right')
        return self.remove_whitespace(lead_text.get_text(strip=True))


class WebScraperComGetAllList(BaseScraping):

    def get_url(self):
        return 'https://webscraper.io/test-sites'

    def parse_data(self, data):
        description_list = []
        soup = BeautifulSoup(data, 'html.parser')
        tags = soup.find_all('div', class_='col-md-7 pull-right')
        for tag in tags:
            lead_text = tag.find('p', class_='lead')
            description_list.append(self.remove_whitespace(lead_text.get_text(strip=True)))
        return description_list


class WebScraperComIntegration:
    actions = {
        "get_first_data": WebScraperComGetFirstData,
        "get_all_list": WebScraperComGetAllList
    }

    def execute(self, action_name):
        action = self.actions.get(action_name)
        if action:
            return action().run()
        else:
            raise Exception("Action not found")
