from pydantic import BaseModel, EmailStr


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
