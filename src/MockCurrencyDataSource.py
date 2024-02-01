from src.CurrencyDataSource import CurrencyDataSource


class MockCurrencyDataSource(CurrencyDataSource):
    def get_exchange_rate(self, currency):
        # Zwraca zaszyte wartości do testów
        return {"USD": 3.8, "EUR": 4.5}.get(currency, None)