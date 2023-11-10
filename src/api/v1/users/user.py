from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import CreateUserRequest, UserResponse
from app.models.user import User
from config.database import get_session
from core.models import Message
from app.handlers.user import UserHandler
from core.dependencies.authentication import AuthenticationRequired


user_router = APIRouter()


@user_router.get(
    "/",
    response_model=list[UserResponse],
    dependencies=[Depends(AuthenticationRequired)],
    status_code=200,
)
def get_users(db: Session = Depends(get_session)):
    return db.query(User).all()


@user_router.post(
    "/",
    response_model=UserResponse,
    responses={400: {"model": Message}},
    status_code=201,
)
def register_user(
    register_user_request: CreateUserRequest, db: Session = Depends(get_session)
):
    user_handler = UserHandler()
    return user_handler.handle_create_user(register_user_request, db)
