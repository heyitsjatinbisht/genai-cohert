from fastapi import FastAPI, Query
from .queue.connection import queue
from .queue.worker import process_query

app = FastAPI()


@app.get("/")
def chat():
    return {"status": "Server is up and running"}


@app.post("/")
def chat(
    query: str = Query(..., description="Chat Message"),
):
    job = queue.enqueue(process_query, query)
    return {"status": "Job enqueued", "job_id": job.id}