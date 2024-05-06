from fastapi import FastAPI
from routers import job_matcher


app = FastAPI()

app.include_router(job_matcher.router)
