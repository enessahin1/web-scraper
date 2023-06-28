from brands.web_scraper_com import WebScraperComIntegration
from brands.twitter import TwitterIntegration

if __name__ == '__main__':
    integration = WebScraperComIntegration()
    my_first_data = integration.execute("get_first_data")
    print(my_first_data)
    my_all_list = integration.execute("get_all_list")
    print(my_all_list)
    twitter_integration = TwitterIntegration()
    twitter_first_data = twitter_integration.execute("get_first_data")
    print(twitter_first_data)