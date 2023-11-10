from typing import List

from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import router
from config.settings import config
from core.middleware.authentication import AuthBackend
from core.exceptions import CustomException


def init_routers(app: FastAPI) -> None:
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        print("Exception occured")
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


# def init_cache() -> None:
#     Cache.init(backend=RedisBackend(), key_maker=CustomKeyMaker())


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        # Middleware(
        #     AuthenticationMiddleware,
        #     backend=AuthBackend(),
        #     on_error=on_auth_error,
        # ),
        # Middleware(AuthBackend),
        # Middleware(ResponseLoggerMiddleware),
    ]
    return middleware


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Template",
        description="FastAPI Template by @azhar-iqbal2942",
        version="1.0.0",
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        # redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )

    # Main router for the API.
    init_routers(app=app)
    init_listeners(app=app)

    return app


app = create_app()
