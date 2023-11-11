from fastapi import APIRouter, Depends

from app.schemas.user import CreateUserRequest, UserResponse
from app.models.user import User
from core.models import Message
from app.handlers.user import UserHandler
from core.dependencies.authentication import AuthenticationRequired
from core.dependencies.current_user import get_current_user


user_router = APIRouter()


@user_router.get(
    "/me",
    response_model=UserResponse,
    dependencies=[Depends(AuthenticationRequired)],
    status_code=200,
)
def get_users(user: User = Depends(get_current_user)):
    return user


@user_router.post(
    "/",
    response_model=UserResponse,
    responses={400: {"model": Message}},
    status_code=201,
)
def register_user(
    register_user_request: CreateUserRequest,
    user_handler: UserHandler = Depends(UserHandler),
):
    return user_handler.handle_create_user(register_user_request)
