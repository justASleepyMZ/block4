import os
import requests
from dotenv import load_dotenv
load_dotenv()

def get_crypto_news(coin_name):
    api_key = os.getenv("NEWSAPI_KEY")
    url = f"https://newsapi.org/v2/everything?q={coin_name}&language=en&pageSize=3&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return [f"{a['title']} ({a['source']['name']})" for a in response.json()["articles"]]
    return []
