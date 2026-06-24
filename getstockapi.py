import requests
import pandas as pd
import os
import json
from dotenv import load_dotenv
import sqlalchemy as db

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET = os.getenv("ALPACA_SECRET")

#Gets most active stocks
#DOCS: https://docs.alpaca.markets/us/reference/mostactives-1
url_active = "https://data.alpaca.markets/v1beta1/screener/stocks/most-actives"

params_active = {
    "by": "volume",
    "top": 50
}

response_top = requests.get(url_active, params = params_active, auth = (API_KEY, SECRET))
data_top = response_top.json()['most_actives']


#Getting just the tickers from the data
ticker_symbols = []

for stock in data_top:
    ticker_symbols.append(stock['symbol'])

#Get OCHLV for individual stocks
#DOCS: https://docs.alpaca.markets/us/reference/stockbars
url_tick_ex = "https://data.alpaca.markets/v2/stocks/AAPL/bars"

params_tick = {
    "timeframe":"1Day",
}

"""
c: Close price.
h: High price.
l: Low price.
o: Open price.
v: Volume (number of shares traded).
vw: Volume Weighted Average Price (VWAP).
n: Number of trades (transactions) in that specific bar period.
t: Timestamp (in ISO 8601 format, with Z indicating UTC).
"""

#Inputting values into dictionary for pandas
keys = ["symbol","close","high","low","open","time","volume","volume-weighted"]
ochlv = {key: [] for key in keys}

for ticker in ticker_symbols:
    url_tick = f"https://data.alpaca.markets/v2/stocks/{ticker}/bars"
    response_tick = requests.get(url_tick, params = params_tick, auth = (API_KEY, SECRET))
    
    data_tick = response_tick.json()
    bars = response_tick.json()['bars'][0]

    symbol = data_tick['symbol']
    ochlv['symbol'].append(symbol)
    
    ochlv['close'].append(bars['c'])
    ochlv['high'].append(bars['h'])
    ochlv['low'].append(bars['l'])
    ochlv['open'].append(bars['o'])
    ochlv['time'].append(bars['t'])
    ochlv['volume'].append(bars['v'])
    ochlv['volume-weighted'].append(bars['vw'])


df = pd.DataFrame(ochlv)









