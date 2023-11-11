from typing import Annotated
from fastapi import Depends
from app.schemas.user import CreateUserRequest

from app.models.user import User
from app.services.user import UserService
from core.security.password import PasswordHandler


class UserHandler:
    def __init__(
        self, user_service: Annotated[UserService, Depends(UserService)]
    ) -> None:
        self.user_service = user_service

    def handle_create_user(self, register_user_request: CreateUserRequest):
        user = User(
            email=register_user_request.email,
            hashed_password=PasswordHandler.hash(register_user_request.password),
            is_active=register_user_request.is_active,
        )
        user = self.user_service.create_user(user=user)
        return user

    def handle_get_user_by_id(self, id: int):
        return self.user_service.get_user_by_id(id=id)
