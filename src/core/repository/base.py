from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session

from config.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Base class for data repositories."""

    def __init__(self, model: Type[ModelType], db_session: Session):
        self.session = db_session
        self.model_class: Type[ModelType] = model
