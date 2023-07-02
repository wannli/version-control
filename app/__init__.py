from fastapi import FastAPI
from app.api import api_router
from app.db import base  # noqa: F401

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router)
    return application

app = create_application()