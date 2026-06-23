import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

gemini_key = os.getenv('Gemini_Key')

client = genai.Client(
  api_key=gemini_key,
)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    system_instruction=(
      "you are a wall street financial analyst trying to predict a "
      "stock's response based on news articles given to you."
      ),
    input="What are the advantages of pair programming?",
)

print(interaction.output)
