# from forex_python.converter import CurrencyRates
import requests
from keys import TWELVEDATA_API_KEY


def get_fx():
    # c = CurrencyRates()
    # exchange_rate = c.get_rate('USD', 'TRY')
    # Define the API endpoint and parameters
    api_key = TWELVEDATA_API_KEY
    url = f'https://api.twelvedata.com/price?symbol=USD/TRY&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    exchange_rate = float(data['price'])
    return exchange_rate


if __name__ == '__main__':
    get_fx()
