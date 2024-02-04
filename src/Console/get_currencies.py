import os

from Enum.Currency import Currency


def get_currencies(currency_arg):
    """
    Zwraca listę wartości walut na podstawie podanego argumentu lub zmiennej środowiskowej.

    Jeśli podany jest argument `currency_arg`, funkcja przetwarza ten ciąg, rozdzielając go
    przecinkami, i zwraca listę odpowiadających mu wartości z enumeracji `Currency`,
    o ile nazwy walut znajdują się w enumeracji. Jeśli argument nie jest podany, funkcja próbuje
    odczytać listę walut z zmiennej środowiskowej `CURRENCIES`. Jeżeli ani argument, ani zmienna
    środowiskowa nie są dostępne, zwracana jest lista wszystkich wartości z enumeracji `Currency`.

    Args:
        currency_arg (str, optional): Ciąg zawierający nazwy walut rozdzielone przecinkami.

    Returns:
        list: Lista wartości walut odpowiadających podanym nazwom w `currency_arg` lub
              zdefiniowanych w zmiennej środowiskowej `CURRENCIES`, lub lista wszystkich
              dostępnych walut, jeśli żadne dane wejściowe nie są dostępne.
    """
    if currency_arg:
        currencies = currency_arg.split(',')
        return [Currency[c].value for c in currencies if c in Currency.__members__]
    else:
        currency_data = os.environ.get('CURRENCIES')
        if currency_data:
            currencies = currency_data.split(',')
            return [Currency[c].value for c in currencies if c in Currency.__members__]
        else:
            return [c.value for c in Currency]