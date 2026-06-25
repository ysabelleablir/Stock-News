import unittest
from unittest.mock import Mock, patch
from news import Search

class TestNews(unittest.TestCase):
    @patch("news.requests.get")
    def test_obtain_articles(self, mock_instance):
        marketaux = Mock()
        marketaux.status_code = 200
        marketaux.json.return_value = {
            "meta": {
                "returned": 3
            },
            "data": [
                {
                    "title": "Elon Musk loses trillionaire status as global tech rout hits SpaceX",
                    "url": "https://www.bbc.co.uk/news/articles/c8j2m2p8dgmo?at_medium=RSS&at_campaign=rss"
                },
                {
                    "title": "Tesla Sued After Woman Killed by Car Crashing Into Her House",
                    "url": "https://www.insurancejournal.com/news/southcentral/2026/06/24/875170.htm"
                },
                {
                    "title": "Sunrun Surges 26% on 16-Gigawatt Virtual Power Plant Deal With Tesla and Renew Home",
                    "url": "https://finance.yahoo.com/energy/articles/sunrun-surges-26-16-gigawatt-154738922.html"
                }
            ]
        }
        
        mock_instance.return_value = marketaux
        titles, urls = Search.obtain_articles("ticker", "TSLA")

        assert titles == ["Elon Musk loses trillionaire status as global tech rout hits SpaceX", "Tesla Sued After Woman Killed by Car Crashing Into Her House", "Sunrun Surges 26% on 16-Gigawatt Virtual Power Plant Deal With Tesla and Renew Home"]
        assert urls == ["https://www.bbc.co.uk/news/articles/c8j2m2p8dgmo?at_medium=RSS&at_campaign=rss", "https://www.insurancejournal.com/news/southcentral/2026/06/24/875170.htm", "https://finance.yahoo.com/energy/articles/sunrun-surges-26-16-gigawatt-154738922.html"]

if __name__ == "__main__":
    unittest.main()