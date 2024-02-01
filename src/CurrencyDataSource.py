from abc import ABC, abstractmethod


class CurrencyDataSource(ABC):
    @abstractmethod
    def get_exchange_rate(self, currency):
        pass
