from app.schemas.user import CreateUserRequest
from sqlalchemy.orm import Session

from app.models.user import User
from app.services.user import UserService
from core.security.password import PasswordHandler


class UserHandler:
    def handle_create_user(self, register_user_request: CreateUserRequest, db: Session):
        user = User(
            email=register_user_request.email,
            hashed_password=PasswordHandler.hash(register_user_request.password),
            is_active=register_user_request.is_active,
        )
        service = UserService()
        user = service.create_user(db, user)
        return user

    def handle_fetch_all_users(self, db: Session):
        users = UserService().get_all_users(session=db)
        return users
