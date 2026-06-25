import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import requests
import sqlalchemy as db 
import os

from getstockapi import(
    fetch_most_active_stocks,
    fetch_ohlcv,
    create_engine,
    save_to_database,
    main
)
#To run :python -m unittest Stock_Unit_test.TestFetchMostActiveStocks -v

class TestFetchMostActiveStocks(unittest.TestCase):
    @patch('getstockapi.requests.get')
    def test_sucessful_fetch(self,mock_get):
        mock = MagicMock()
        
        mock.json.return_value = {
            'most_actives':[
                {'symbol': 'AAPL', 'volume': 1000000},
                {'symbol': 'MSFT', 'volume': 900000},
                {'symbol': 'GOOGL', 'volume': 800000}
            ]
        }

        mock_get.return_value = mock

        result = fetch_most_active_stocks(top=3)

        self.assertEqual(result,['AAPL','MSFT','GOOGL'])



