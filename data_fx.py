import requests

def get_fx():
    url = 'https://api.exchangerate.host/latest'
    params = {
        "base": 'USD',
        "symbols": 'TRY'
    }
    response = requests.get(url, params=params)
    data = response.json()
    try:
        return data['rates']['TRY']
    except:
        return "N/A"

if __name__ == '__main__':
    get_fx()
