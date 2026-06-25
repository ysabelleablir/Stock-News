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
    print("Getting Gemini Response...")

    prompt = f"""
    Stock ticker: {ticker}

    News articles:
    {articles}

    you are a wall street financial analyst trying to predict a stock's response
    based on the potential articles and the stock data provided to you. If there
    are no articles, just go based on the stock data; otherwise, explain analysis
    in relation to the stock. Predict: whether the stock will go up or down tomorrow.
    """



    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print("Got Gemini Response!")
    return (response.text)
