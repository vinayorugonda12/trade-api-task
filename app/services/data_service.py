import requests

def fetch_market_data(sector: str):
    try:
        url = f"https://duckduckgo.com/?q={sector}+india+market"
        response = requests.get(url, timeout=5)
        return response.text[:100]
    except Exception as e:
        return f"No data available: {str(e)}"