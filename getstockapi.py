import requests
import pandas as pd
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET = os.getenv("SECRET")

#Gets most active stocks
#DOCS: https://docs.alpaca.markets/us/reference/mostactives-1
url_active = "https://data.alpaca.markets/v1beta1/screener/stocks/most-actives"

#Get OCHLV for individual stocks
#DOCS: https://docs.alpaca.markets/us/reference/stockbars
url_stock = "https://data.alpaca.markets/v2/stocks/AAPL/bars"


params = {
    "by": "volume",
    "top": 100
}

response = requests.get(url_active, params = params, auth = (API_KEY, SECRET))
data = response.json()

print(data)




