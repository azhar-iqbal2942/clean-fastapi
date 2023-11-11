# type: ignore
from starlette.authentication import AuthenticationBackend, AuthCredentials
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.requests import HTTPConnection

from app.schemas.extras.current_user import CurrentUser
from core.jwt import JWTHandler


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection):
        """
        The `authenticate` function checks the authorization header of an HTTP connection, decodes a JWT
        token, and returns authentication credentials and the current user if the token is valid.

        :param conn: HTTPConnection - an object representing the HTTP connection
        :type conn: HTTPConnection
        :return: The authenticate function returns a tuple containing two values:
        AuthCredentials(["authenticated"]) and current_user.
        """
        current_user = CurrentUser()
        authorization: str = conn.headers.get("Authorization")

        if not authorization:
            return

        try:
            scheme, token = authorization.split()
            if scheme.lower() != "bearer":
                return
        except ValueError:
            return

        if not token:
            return
        try:
            payload = JWTHandler.decode(token=token)
        except Exception as e:
            return False, current_user

        if payload:
            current_user = CurrentUser(id=payload.get("id"))
            return AuthCredentials(["authenticated"]), current_user

        return


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
