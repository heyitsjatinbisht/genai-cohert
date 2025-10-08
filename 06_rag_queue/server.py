from fastapi import FastAPI, Query, Path
from .queue.connection import queue
from .queue.worker import process_query


app = FastAPI()


@app.get("/")
def a():
    return {"status": "Server is up and running"}


@app.post("/")
def chat(
    query: str = Query(..., description="Chat Message"),
):
    job = queue.enqueue(process_query, query)
    return {"status": "Job enqueued", "job_id": job.id}


@app.get("/result/{job_id}")
def get_result(
    job_id: str = Path(..., decription="Job ID")
):
    job = queue.fetch_job(job_id=job)
    result = job.return_value()

    return {"result": result}
