from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import api_router
from app.core import config
from app.db import base, session

def create_application() -> FastAPI:
    application = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    application.include_router(api_router, prefix=config.API_PREFIX)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in config.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application

app = create_application()

@app.on_event("startup")
async def startup_event():
    base.Base.metadata.create_all(bind=session.engine)

@app.on_event("shutdown")
async def shutdown_event():
    await session.close_db_connection()