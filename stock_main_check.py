import requests

NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = "TW5KKAOQ88DMY1XG"

stock_params = {
    "apikey": API_KEY,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": NAME
}


response = requests.get(STOCK_ENDPOINT, params = stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_close = data_list[0]['4. close']
print(yesterday_close)