from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.exceptions import UnauthorizedException
from core.jwt import JWTHandler


class AuthenticationRequired:
    def __init__(
        self,
        token: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
    ) -> None:
        if not token:
            raise UnauthorizedException("Authentication required")

        # this will check if token is valid. If not raise exception
        JWTHandler.decode(token=token.credentials)
