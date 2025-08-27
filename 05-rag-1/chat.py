from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

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

print("Search results: ",search_results)
