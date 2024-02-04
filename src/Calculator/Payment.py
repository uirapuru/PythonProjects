class Payment:
    """
    Klasa reprezentująca płatność, zawierająca informacje o kwocie, walucie i dacie dokonania płatności.

    Atrybuty:
        amount (float): Kwota płatności.
        currency (str): Waluta płatności.
        date (str): Data dokonania płatności, w formacie zgodnym z ISO 8601 (np. "YYYY-MM-DD").
    """
    def __init__(self, amount, currency, date):
        """
        Inicjalizuje nową instancję klasy Payment.

        Args:
            amount (str, float): Kwota płatności. Jeśli podano jako string, zostanie przekonwertowana na float.
            currency (str): Kod waluty płatności, zgodny ze standardem ISO 4217 (np. "USD", "EUR").
            date (str): Data dokonania płatności, w formacie "YYYY-MM-DD".

        Raises:
            ValueError: Jeśli wartość `amount` nie może być przekonwertowana na float.
        """
        self.amount = float(amount)
        self.currency = currency
        self.date = date
