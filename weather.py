import json
import requests
import os
from keys import OPEN_WEATHER_API_KEY

def get_weather():
    params = {
        "lat": '38.55156276399227',
        "lon": '28.238870626613853',
        "appid": OPEN_WEATHER_API_KEY,
        "units": "metric",
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params=params)
    content = json.loads(response.content)
    try:
        return content["main"]["temp"]
    except:
        return "N/A"
