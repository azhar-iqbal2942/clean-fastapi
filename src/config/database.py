from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import config


engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    try:
        yield SessionLocal()
    finally:
        SessionLocal.close_all()


Base = declarative_base()
