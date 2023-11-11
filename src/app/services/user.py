from typing import Annotated
from fastapi import Depends
from app.repositories.user import UserRepository


class UserService:
    def __init__(
        self, user_repository: Annotated[UserRepository, Depends(UserRepository)]
    ):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all()

    def create_user(self, user):
        return self.user_repository.create(user=user)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_by_email(email=email)

    def get_user_by_id(self, id: int):
        return self.user_repository.get_by_id(id=id)
