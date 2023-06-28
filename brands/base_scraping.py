import requests
import re


class BaseScraping:

    def get_url(self):
        raise NotImplementedError

    def get_headers(self):
        return {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

    def get_data(self):
        response = requests.get(self.get_url(), headers=self.get_headers())
        return response.text

    def parse_data(self, data):
        raise NotImplementedError

    @staticmethod
    def remove_whitespace(text):
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

    def run(self):
        data = self.get_data()
        return self.parse_data(data)
