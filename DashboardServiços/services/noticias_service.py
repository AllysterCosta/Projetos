import os
import requests

API_KEY = os.getenv("NEWS_API_KEY")
URL = "https://newsapi.org/v2/everything"


def buscar_noticias(limite=5):
    if not API_KEY:
        return {"erro": "API KEY de notícias não configurada"}

    params = {
        "q": "tecnologia",
        "language": "pt",
        "pageSize": limite,
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get(URL, params=params, timeout=5)

    if response.status_code != 200:
        return {"erro": response.text}

    dados = response.json()

    noticias = []
    for item in dados.get("articles", []):
        noticias.append({
            "titulo": item.get("title"),
            "fonte": item.get("source", {}).get("name"),
            "url": item.get("url")
        })

    return noticias
