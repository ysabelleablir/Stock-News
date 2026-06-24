import requests
import os
from dotenv import load_dotenv
from datetime import date,timedelta

load_dotenv()
NEWS_KEY = os.getenv("NEWS_KEY")
BASE_URL = 'https://api.marketaux.com/v1/'
SEARCH_PREFS = {
    'ticker': 'symbols',
    'industry': 'industries',
    'asset class': 'entity_types'
}

class Search:
    @staticmethod
    def obtain_articles(preference, value):
        parameters = {
            "api_token": NEWS_KEY,
            "published_after": date.today() - timedelta(days=7)
        }
        parameters[SEARCH_PREFS[preference]] = value

        # Parsing the response
        response = requests.get(BASE_URL + 'news/all', params=parameters)
        articles = response.json()["data"]
        article_titles = [article["title"] for article in articles]
        article_urls = [article["url"] for article in articles]

        return (article_titles, article_urls)