from fastapi import APIRouter

from .auth import jwt_router

auth_router = APIRouter()
auth_router.include_router(jwt_router, tags=["Auth"])

__all__ = ["auth_router"]
