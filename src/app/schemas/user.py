# pylint: disable=all
# type: ignore
import re
from pydantic import BaseModel, EmailStr, constr, validator


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=64)
    is_active: bool

    @validator("password")
    def password_must_contain_special_characters(cls, v):
        if not re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Password must contain special characters")
        return v

    class Config:
        orm_mode = True
