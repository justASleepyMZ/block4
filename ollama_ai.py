import requests

def generate_response(coin_name, data, intent, news_list=None):
    news_formatted = "\n".join([f"- {n}" for n in news_list]) if news_list else ""
    prompt = f"""
User is asking about {coin_name}.

Intent: {intent}
Data:
- Price: ${data.get('price')}
- Market Cap: ${data.get('market_cap')}
- Rank: {data.get('rank')}
News Headlines:
{news_formatted}

Generate a human-like answer that summarizes the above information and addresses the user's intent.
"""
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]
