from brands.web_scraper_com import WebScraperComIntegration
from strategies.base_starter_strategy import StarterStrategy


class WebScraperFirstDataStrategy(StarterStrategy):
    def start(self):
        integration = WebScraperComIntegration()
        my_all_list = integration.execute("get_all_list")
        print(my_all_list)


class WebScraperGetAllDataStrategy(StarterStrategy):
    def start(self):
        integration = WebScraperComIntegration()
        my_all_list = integration.execute("get_all_list")
        print(my_all_list)