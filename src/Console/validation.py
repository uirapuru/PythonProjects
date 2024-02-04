import re
from Enum.Currency import Currency

def validate_date(date_text):
    """
    Sprawdza, czy podana data jest w poprawnym formacie RRRR-MM-DD.

    Args:
        date_text (str): Data do sprawdzenia.

    Raises:
        ValueError: Jeśli data nie jest w formacie RRRR-MM-DD.
    """
    if not re.match(r"\d{4}-\d{2}-\d{2}", date_text):
        raise ValueError("Data musi być w formacie RRRR-MM-DD.")

def validate_currency(currency_code):
    """
    Sprawdza, czy podany kod waluty jest obsługiwany.

    Args:
        currency_code (str): Kod waluty do sprawdzenia.

    Raises:
        ValueError: Jeśli waluta nie jest obsługiwana.
    """
    if currency_code not in Currency.__members__:
        raise ValueError("Nieobsługiwana waluta.")

def validate_amount(amount):
    """
    Próbuje przekonwertować podaną kwotę na typ float.

    Args:
        amount (str): Kwota do walidacji.

    Returns:
        float: Kwota przekonwertowana na typ float.

    Raises:
        ValueError: Jeśli kwota nie jest liczbą.
    """
    try:
        return float(amount)
    except ValueError:
        raise ValueError("Kwota musi być liczbą.")

def validate_output(output):
    """
    Sprawdza, czy nazwa pliku wyjściowego ma poprawne rozszerzenie (.txt lub .csv).

    Args:
        output (str): Nazwa pliku do walidacji.

    Raises:
        ValueError: Jeśli plik nie ma rozszerzenia .txt lub .csv.
    """
    if output:
        if not output.endswith('.txt') and not output.endswith('.csv'):
            raise ValueError("Plik musi mieć rozszerzenie .txt lub .csv")
