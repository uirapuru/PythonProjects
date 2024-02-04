class Invoice:
    """
    Klasa reprezentująca fakturę, zawierająca informacje o kwocie, walucie i dacie wystawienia.

    Attributes:
        amount (float): Kwota faktury.
        currency (str): Waluta faktury.
        date (str): Data wystawienia faktury, w formacie zgodnym z ISO 8601 (np. "YYYY-MM-DD").
    """
    def __init__(self, amount, currency, date):
        """
        Inicjalizuje nową instancję klasy Invoice.

        Args:
            amount (str, float): Kwota faktury. Jeśli podano jako string, zostanie przekonwertowana na float.
            currency (str): Kod waluty faktury, zgodny ze standardem ISO 4217 (np. "USD", "EUR").
            date (str): Data wystawienia faktury, w formacie "YYYY-MM-DD".

        Raises:
            ValueError: Jeśli wartość `amount` nie może być przekonwertowana na float.
        """
        self.amount = float(amount)
        self.currency = currency
        self.date = date
