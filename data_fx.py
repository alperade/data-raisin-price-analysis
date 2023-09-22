import requests
from forex_python.converter import CurrencyRates


def get_fx():
    c = CurrencyRates()
    exchange_rate = c.get_rate('USD', 'TRY')
    return exchange_rate


if __name__ == '__main__':
    get_fx()
