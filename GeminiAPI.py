import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

gemini_key = os.getenv('Gemini_Key')
#ticker = ___
#articles = ___

client = genai.Client(
  api_key=gemini_key,
)

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

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    system_instruction=(
    #input=prompt,
)

print(interaction.output)
