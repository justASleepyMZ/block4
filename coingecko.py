import requests

def get_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "price": data["market_data"]["current_price"]["usd"],
            "market_cap": data["market_data"]["market_cap"]["usd"],
            "rank": data["market_cap_rank"]
        }
    return None
