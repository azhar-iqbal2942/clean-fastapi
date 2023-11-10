from starlette.types import ASGIApp, Receive, Scope, Send
from starlette.authentication import AuthenticationBackend

__all__ = ["AuthBackend"]


class AuthBackend:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        print("AuthBackend Middleware called")
