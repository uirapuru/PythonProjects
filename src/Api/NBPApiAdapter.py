from datetime import datetime, timedelta

from Api.CurrencyDataSource import CurrencyDataSource
from Enum.Currency import Currency
import requests


class NBPApiAdapter(CurrencyDataSource):
    """
    Adapter do API Narodowego Banku Polskiego (NBP), implementujący interfejs CurrencyDataSource
    dla pobierania średnich kursów walut.

    Attributes:
        api_url (str): Podstawowy adres URL API NBP.
    """

    def __init__(self):
        self.api_url = "http://api.nbp.pl/api/"

    def get_average_currency_rate(self, currency, date):
        """
        Pobiera średni kurs wymiany dla podanej waluty i daty z API NBP.

        Metoda wykonuje zapytanie do API NBP, aby uzyskać średni kurs wymiany dla określonej waluty
        na podaną datę. Jeśli waluta nie jest obsługiwana lub kurs nie może być pobrany po 3 próbach,
        metoda zgłasza wyjątek.

        Args:
            currency (str): Kod waluty, dla której ma zostać pobrany średni kurs.
            date (str): Data, na którą ma zostać pobrany średni kurs, w formacie "YYYY-MM-DD".

        Returns:
            float: Średni kurs waluty na podaną datę.

        Raises:
            ValueError: Jeśli podana waluta nie jest obsługiwana lub nie można znaleźć kursu dla podanej daty.
            Exception: W przypadku innych błędów związanych z komunikacją z API NBP.
        """

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
