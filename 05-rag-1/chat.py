from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_vectors",
    embedding=embedding_model
)
# Take user query

query = input("> ")

# Vector similarity search in DB

search_results = vector_db.similarity_search(
    query=query
)



context = "\n\n".join(
    [
        f"Page content: {result.page_content}\nPage number: {result.metadata.get('page_number')}\nFile Location: {result.metadata.get('source')}\n"
        for result in search_results
    ]
)


SYSTEM_PROMPT = f"""
You are a helpful Ai Assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number.

You should only answer the user based on the following context and navigate the user to open the right page number to know more.

Context:
{context}
"""


chat_completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query},
    ]
)

print(chat_completion.choices[0].message.content)