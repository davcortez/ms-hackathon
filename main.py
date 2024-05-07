from fastapi import FastAPI
from routers import job_matcher
from internal.config import get_settings
from fastapi.middleware.cors import CORSMiddleware


settings = get_settings()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_http_methods,
    allow_headers=settings.cors_headers,
)


app.include_router(job_matcher.router)
