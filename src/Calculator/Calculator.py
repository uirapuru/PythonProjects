from Api import CurrencyDataSource


class Calculator:
    def __init__(self, data_source: CurrencyDataSource):
        self.data_source = data_source

    def calculate(self, data, currency):
        rate = self.data_source.get_exchange_rate(currency)
        # Logika obliczeń
        return rate