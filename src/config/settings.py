from enum import Enum
from environs import Env
from pydantic_settings import BaseSettings
from pydantic import Field

env = Env()
env.read_env()


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class Settings(BaseSettings):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    SQLALCHEMY_DATABASE_URL: str = Field(env("SQLALCHEMY_DATABASE_URL"))
    JWT_SECRET_KEY: str = "123"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 10
    # POOL_SIZE = 5
    # MAX_OVERFLOW = 1
    # POOL_PRE_PING = True
    # ECHO = True
    # POOL_RECYCLE_IN_SECONDS = 3600
    # ECHO_POOL = False
    # POOL_RESET_ON_RETURN = "rollback"
    # POOL_TIMEOUT_IN_SECONDS = 30
    # POOL = "~sqlalchemy.pool.QueuePsool"


config: Settings = Settings()  # type: ignore
