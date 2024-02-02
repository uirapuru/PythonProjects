from abc import ABC, abstractmethod


class CurrencyDataSource(ABC):
    @abstractmethod
    def get_average_currency_rate(self, currency, date):
        pass
