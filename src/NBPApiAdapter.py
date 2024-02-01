from CurrencyDataSource import CurrencyDataSource


class NBPApiAdapter(CurrencyDataSource):
    def __init__(self):
        self.api_url = "http://api.nbp.pl/api/"

    def get_exchange_rate(self, currency):
        pass
