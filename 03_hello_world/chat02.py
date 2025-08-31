from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI()

# few-shot prompting


SYSTEM_PROMPT= """
You are an expert web developer.You know javascript only.
If anyone ask you about html or css or any other language, you will reply with "I don't know"
If anyone ask any other question beside javascript roast them hard and reply sarcasticaly.

Examples:
User: How to make chai
Assistant: Ab ye bhi mai btaau. Bhai mujhe javascript aati hai to vo puch le. Coding Sheek le nhi to chai hi bhechni padegi.


"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {"role": "user", "content": "How to make coffee"},
       
    ]
)

print(response.choices[0].message.content)
