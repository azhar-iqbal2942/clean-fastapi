from datetime import datetime, timedelta
from jose import jwt, ExpiredSignatureError, JWTError

from config.settings import config
from core.exceptions import UnauthorizedException


class JWTHandler:
    secret_key = config.JWT_SECRET_KEY
    algorithm = config.JWT_ALGORITHM
    expire_minutes = config.JWT_EXPIRE_MINUTES

    @staticmethod
    def encode(payload: dict) -> str:
        expire = datetime.utcnow() + timedelta(minutes=JWTHandler.expire_minutes)
        payload.update({"exp": expire})
        return jwt.encode(
            payload, JWTHandler.secret_key, algorithm=JWTHandler.algorithm
        )

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return jwt.decode(
                token, JWTHandler.secret_key, algorithms=[JWTHandler.algorithm]
            )
        except ExpiredSignatureError as exception:
            # TODO: add logger here
            raise UnauthorizedException("Token Expired")
        except JWTError as exception:
            # TODO: add logger here
            raise UnauthorizedException("Invalid Token")

    @staticmethod
    def decode_expired(token: str) -> dict:
        try:
            return jwt.decode(
                token,
                JWTHandler.secret_key,
                algorithms=[JWTHandler.algorithm],
                options={"verify_exp": False},
            )
        except JWTError as exception:
            raise UnauthorizedException("Invalid Token")
