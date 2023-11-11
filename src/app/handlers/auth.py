from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.auth import UserLoginRequest
from app.services.user import UserService
from app.schemas.extras.token import Token
from core.exceptions import BadRequestException
from core.jwt import JWTHandler
from core.security.password import PasswordHandler


class AuthHandler:
    def __init__(
        self, user_service: Annotated[UserService, Depends(UserService)]
    ) -> None:
        self.user_service = user_service

    def login(self, user_credentials: UserLoginRequest):
        user = self.user_service.get_user_by_email(user_credentials.email)

        if not user:
            raise BadRequestException("Invalid credentials")

        if not PasswordHandler.verify(user.hashed_password, user_credentials.password):
            raise BadRequestException("Invalid credentials")

        return Token(
            access_token=JWTHandler.encode(payload={"id": user.id}),
            refresh_token=JWTHandler.encode(payload={"sub": "refresh_token"}),
        )
