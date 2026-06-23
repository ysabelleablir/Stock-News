import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
#from news import article_urls

load_dotenv()

gemini_key = os.getenv('Gemini_Key')
ticker = input('ticker symbol ')
articles = ['https://financefeeds.com/bnb-faces-a-make-or-break-moment-before-june-ends/', 
'https://www.pb.pl/technologiczne-spolki-tanieja-w-usa-ale-wiekszosc-pozostalych-drozeje-1263324',
'https://www.investorideas.com/news/2026/renewable-energy/06231-tesla-natpower-battery-storage-deal.asp']

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



response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
