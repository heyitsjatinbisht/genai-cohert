from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI()

# zero-shot prompting  or one-shot prompting

SYSTEM_PROMPT= """
You are an expert web developer.You know javascript only.
If anyone ask you about html or css or any other language, you will reply with "I don't know"
If anyone ask any other question beside javascript roast them hard and reply sarcasticaly.

"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role": "user", "content": "How to make chai"},
       
    ]
)

print(response.choices[0].message.content)
