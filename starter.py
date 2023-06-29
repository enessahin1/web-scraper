from strategies.base_starter_strategy import Starter
from strategies.twitter import TwitterFirstDataStrategy
from strategies.web_scraper_com import WebScraperFirstDataStrategy, WebScraperGetAllDataStrategy

if __name__ == '__main__':
    starter = Starter(WebScraperFirstDataStrategy())
    starter.execute()
    starter = Starter(WebScraperGetAllDataStrategy())
    starter.execute()
    starter = Starter(TwitterFirstDataStrategy())
    starter.execute()
