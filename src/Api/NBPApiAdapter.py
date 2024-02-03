from datetime import datetime, timedelta

from Api.CurrencyDataSource import CurrencyDataSource
from Enum.Currency import Currency
import requests


class NBPApiAdapter(CurrencyDataSource):
    def __init__(self):
        self.api_url = "http://api.nbp.pl/api/"

    def get_average_currency_rate(self, currency, date):
        if currency.upper() not in Currency.__members__:
            raise ValueError(f"Nieobsługiwana waluta: {currency}")

        attempts = 0
        while attempts < 3:
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                url = f"{self.api_url}exchangerates/rates/a/{currency.lower()}/{date}/?format=json"
                # print(url)
                response = requests.get(url)
                if response.status_code == 404:
                    raise ValueError("404 Not Found")
                response.raise_for_status()
                data = response.json()
                return data['rates'][0]['mid']
            except ValueError as e:
                # print(e)
                attempts += 1
                date_obj -= timedelta(days=1)
                date = date_obj.strftime("%Y-%m-%d")
            except Exception as e:
                raise Exception(f"Błąd API: {e}")

        raise Exception("Nie udało się pobrać kursu po 3 próbach.")
