from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path =Path(__file__).parent / "annual.pdf"


# loading

loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

# Chunking

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
    )


split_docs = text_splitter.split_documents(documents=docs)


# Vector Embedding

embedding_modal = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

# using embedding modal create embeddings of split_docs and store in db

vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url="http://localhost:6333",
    collection_name="learning_vectors",
    embedding=embedding_modal
)

print("Indexing of documents done...")