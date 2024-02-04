from enum import Enum


class Currency(Enum):
    """
    Enumeracja reprezentująca obsługiwane waluty.

    Atrybuty:
        EUR (str): Euro.
        USD (str): Dolar amerykański.
        GBP (str): Funt brytyjski.
    """
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'
