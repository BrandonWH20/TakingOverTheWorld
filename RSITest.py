import json

import requests

""" TODO: write a program that Buys a stock when the RSI goes from <32 to >54 within 24 hours.  """

def rsitest(ticker = "TRUP"):

    request = "https://www.alphavantage.co/query?function=RSI&symbol=Ticker&interval=weekly&time_period=10&series_type=open&apikey=2U2M12W6VQ47QS0J"
    request.replace("Ticker", ticker)

    data = requests.get(request)
    string = json.loads(data.text)
    print(string)