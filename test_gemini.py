import unittest
from unittest.mock import patch, MagicMock
from GeminiAPI import Gemini

class TestGemini(unittest.TestCase):
    @patch("GeminiAPI.client")
    def test_ask_gemini_return(self, mock_client):
        response = MagicMock()
        response.text = "Prediction"
        mock_client.models.generate_content.return_value = response
        result = Gemini.ask_gemini('TSLA', ['Article 1', 'Article 2', 'Article 3'])
        self.assertEqual(result, "Prediction")