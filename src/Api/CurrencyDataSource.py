from abc import ABC, abstractmethod


class CurrencyDataSource(ABC):
    """
    Abstrakcyjna klasa źródła danych walutowych definiująca interfejs dla różnych implementacji
    dostarczających średni kurs waluty.

    Klasa ta służy jako szablon dla klas potomnych, które muszą dostarczyć konkretną implementację
    metody `get_average_currency_rate`, umożliwiającą pobieranie średniego kursu waluty na podaną datę.
    """
    @abstractmethod
    def get_average_currency_rate(self, currency, date):
        """
        Metoda abstrakcyjna, która powinna być zaimplementowana przez klasy potomne,
        aby dostarczyć mechanizm pobierania średniego kursu waluty.

        Args:
            currency (str): Kod waluty, dla której ma zostać pobrany średni kurs.
            date (str): Data, na którą ma zostać pobrany średni kurs waluty, w formacie zgodnym z ISO 8601 (np. "YYYY-MM-DD").

        Returns:
            float: Średni kurs waluty na podaną datę.

        Raises:
            NotImplementedError: Jeśli metoda nie zostanie zaimplementowana przez klasę potomną.
        """
        pass
