from fastapi import APIRouter
from app.api.endpoints.user.user import user_module as user_api
from app.api.endpoints.user.auth import auth_module as auth_api

user_router = APIRouter()

user_router.include_router(
    user_api,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

user_router.include_router(
    auth_api,
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

