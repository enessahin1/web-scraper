class StarterStrategy:
    def start(self):
        pass


class Starter:
    def __init__(self, strategy: StarterStrategy):
        self._strategy = strategy

    def execute(self):
        self._strategy.start()
