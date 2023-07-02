from fastapi import APIRouter

from app.api.endpoints import users, superusers, resolutions, suggestions

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(superusers.router, prefix="/superusers", tags=["superusers"])
api_router.include_router(resolutions.router, prefix="/resolutions", tags=["resolutions"])
api_router.include_router(suggestions.router, prefix="/suggestions", tags=["suggestions"])