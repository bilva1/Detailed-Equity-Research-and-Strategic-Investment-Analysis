import requests
from bs4 import BeautifulSoup

def get_stock_price(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
        if price_tag:
            return price_tag.text
        else:
            return None
    else:
        return None
