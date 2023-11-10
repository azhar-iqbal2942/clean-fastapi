from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import UserLoginRequest
from app.handlers.auth import AuthHandler
from config.database import get_session


jwt_router = APIRouter()


@jwt_router.post("/login", status_code=201)
def login_user(
    login_user_request: UserLoginRequest, db: Session = Depends(get_session)
):
    return AuthHandler().login(db, login_user_request)
