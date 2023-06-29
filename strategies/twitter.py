from brands.twitter import TwitterIntegration
from strategies.base_starter_strategy import StarterStrategy


class TwitterFirstDataStrategy(StarterStrategy):
    def start(self):
        twitter_integration = TwitterIntegration()
        twitter_first_data = twitter_integration.execute("get_first_data")
        print(twitter_first_data)
