import re

from Enum.Currency import Currency


def validate_date(date_text):
    if not re.match(r"\d{4}-\d{2}-\d{2}", date_text):
        raise ValueError("Data musi być w formacie RRRR-MM-DD.")

def validate_currency(currency_code):
    if currency_code not in Currency.__members__:
        raise ValueError("Nieobsługiwana waluta.")

def validate_amount(amount):
    try:
        return float(amount)
    except ValueError:
        raise ValueError("Kwota musi być liczbą.")


def validate_output(output):
    if output:
        if not output.endswith('.txt') and not output.endswith('.csv'):
            raise ValueError("Plik musi mieć rozszerzenie .txt lub .csv")