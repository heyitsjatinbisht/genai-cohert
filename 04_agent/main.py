from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


client = OpenAI()

def getWeather(city:str):
    return "42 degree C"

SYSTEM_PROMPT= """
       You are a helpful ai assistant.

       Today date is {datetime.now()}
"""


response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role": "user", "content": "What is the date and time now?"},
    ]
)

print(response.choices[0].message.content)