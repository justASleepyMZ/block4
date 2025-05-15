from nlp_utils import extract_coin_name, classify_query, load_coin_list
from coingecko import get_coin_data
from newsapi import get_crypto_news
from ollama_ai import generate_response

coin_list = load_coin_list()

def process_user_query(user_input):
    coin_id = extract_coin_name(user_input, coin_list)
    if not coin_id:
        return "The cryptocurrency in your request could not be recognized."

    intent = classify_query(user_input)
    data = get_coin_data(coin_id)
    if not data:
        return "Error retrieving coin data."

    news = get_crypto_news(coin_id) if intent in ["news", "summary"] else None
    answer = generate_response(coin_id, data, intent, news)
    return answer
