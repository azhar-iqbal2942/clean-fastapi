from fastapi import APIRouter, Depends

from app.schemas.auth import UserLoginRequest
from app.handlers.auth import AuthHandler


jwt_router = APIRouter()


@jwt_router.post("/login", status_code=201)
def login_user(
    login_user_request: UserLoginRequest,
    auth_handler: AuthHandler = Depends(AuthHandler),
):
    return auth_handler.login(login_user_request)
