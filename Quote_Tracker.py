import requests

def get_stock_price(symbol):
    # You need an API key for a real API; this is a placeholder URL
    url = f"https://api.example.com/stocks/{symbol}"
    response = requests.get(url)
    data = response.json()
    return data['price']

symbol = input("Enter the stock symbol: ")
price = get_stock_price(symbol)
print(f"Current price of {symbol}: ${price:.2f}")
