import os

from Enum.Currency import Currency


def get_currencies(currency_arg):
    if currency_arg:
        currencies = currency_arg.split(',')
        return [Currency[c].value for c in currencies if c in Currency.__members__]
    else:
        currency_data = os.environ.get('CURRENCY')
        if currency_data:
            currencies = currency_data.split(',')
            return [Currency[c].value for c in currencies if c in Currency.__members__]
        else:
            return [c.value for c in Currency]