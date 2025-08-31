from openai import OpenAI;

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

text = "Hello i am jatin bisht"

result = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
)

print(result)