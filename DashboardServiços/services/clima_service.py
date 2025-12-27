import requests
import os

API_KEY = os.getenv("OPENWEATHER_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"


def buscar_clima(cidade="São Paulo"):
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(URL, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()

    return {
        "cidade": cidade,
        "temp": data["main"]["temp"],
        "descricao": data["weather"][0]["description"]
    }
