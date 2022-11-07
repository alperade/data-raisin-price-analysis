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
       data = response.json()
       return data['rates']['TRY']
    except requests.HTTPError as e:
        print(f"Exception caught: {e}")



if __name__ == '__main__':
    get_fx()
