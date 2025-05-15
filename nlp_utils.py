import requests

RU_COIN_SYNONYMS = {
    "биткоин": "bitcoin",
    "эфириум": "ethereum",
    "солана": "solana"
}

def load_coin_list():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    if response.status_code == 200:
        return {c["id"]: c["symbol"] for c in response.json()}
    return {}

def extract_coin_name(user_input, coin_list):
    user_input = user_input.lower()

    # Сначала проверим по синонимам
    for ru, coin_id in RU_COIN_SYNONYMS.items():
        if ru in user_input:
            return coin_id

    # Затем обычное сравнение с ID
    for coin_id in coin_list:
        if coin_id in user_input:
            return coin_id
    return None

def classify_query(user_input):
    lowered = user_input.lower()
    if "цена" in lowered or "price" in lowered:
        return "price"
    elif "капитализация" in lowered or "market cap" in lowered or "рейтинг" in lowered:
        return "market"
    elif "новости" in lowered or "news" in lowered:
        return "news"
    elif "думаешь" in lowered or "прогноз" in lowered or "через" in lowered:
        return "summary"
    else:
        return "summary"
