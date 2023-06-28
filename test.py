from unittest import TestCase, mock

from brands.twitter import TwitterIntegration
from brands.web_scraper_com import WebScraperComIntegration
from test_data import test_twitter_data, web_scraping_first_data


class ScrapingTestCases(TestCase):
    def setUp(self) -> None:
        self.twitter_integration = TwitterIntegration()
        self.web_scraper_com_integration = WebScraperComIntegration()

    @mock.patch('selenium.webdriver.remote.webdriver.WebDriver.get')
    @mock.patch('selenium.webdriver.support.wait.WebDriverWait')
    @mock.patch('selenium.webdriver.support.wait.WebDriverWait.until')
    @mock.patch('selenium.webdriver.remote.webdriver.WebDriver.page_source', new=test_twitter_data)
    def test_twitter_get_first_data(self, get_mock, web_driver_mock, until_mock):
        first_data = self.twitter_integration.execute("get_first_data")
        self.assertEquals(first_data, "Galatasaray")

    @mock.patch('requests.get')
    @mock.patch('brands.base_scraping.BaseScraping.get_data', return_value=web_scraping_first_data)
    def test_web_scraper_com_get_first_data(self, mock, mock2):
        first_data = self.web_scraper_com_integration.execute("get_first_data")
        self.assertEquals(first_data, "E-commerce site")
