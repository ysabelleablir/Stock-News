import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

gemini_key = os.getenv('Gemini_Key')
#ticker = input('ticker symbol ')


client = genai.Client(
  api_key=gemini_key,
)
class Gemini:
  @staticmethod
  def ask_gemini(ticker, articles):
    if len(articles) < 3:
      raise ValueError("Expected at least 3 articles")

    prompt = f"""
    Stock ticker: {ticker}

    News articles:

    Article 1:
    {articles[0]}

    Article 2:
    {articles[1]}

    Article 3:
    {articles[2]}

    you are a wall street financial analyst trying to predict a stock's response.
    Based on the above articles given to you Predict:
    weather the stock will go up or down tomorrow.
    """



    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return (response.text)
