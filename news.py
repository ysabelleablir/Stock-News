import requests
import os
from dotenv import load_dotenv

from datetime import date,timedelta
# from getstockapi import ticker # TODO: find out where the variable actually is

load_dotenv()

NEWS_KEY = os.getenv("NEWS_KEY")
BASE_URL = 'https://api.marketaux.com/v1/'

"""
Obtain preferences for parameters
- Do we want to simply find a specific ticker?
- Should we also prompt for industries?
- Observe articles up to when?
"""
# ticker = input("Enter the stock ticker: ") # TESTING PROMPT
prev_date = date.today() - timedelta(days=7)

parameters = {
    "api_token": NEWS_KEY,
    "symbols": ticker,
    "published_after": prev_date
}

# Parsing the response
response = requests.get(BASE_URL + 'news/all', params=parameters)
articles = response.json()["data"]
article_urls = [article["url"] for article in articles]