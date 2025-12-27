import requests

URL = "https://open.er-api.com/v6/latest/USD"


def buscar_moedas():
    response = requests.get(URL, timeout=5)
    response.raise_for_status()

    dados = response.json()

    rates = dados.get("rates", {})

    return {
        "base": dados.get("base_code"),
        "BRL": rates.get("BRL"),
        "EUR": rates.get("EUR"),
        "data": dados.get("time_last_update_utc")
    }
