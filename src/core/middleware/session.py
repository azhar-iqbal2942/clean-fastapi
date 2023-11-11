from sqlalchemy.orm import sessionmaker
from starlette.middleware.base import BaseHTTPMiddleware

from config.database import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class SessionMiddleware(BaseHTTPMiddleware):
    def dispatch(self, request, call_next):
        request.state.db = SessionLocal()
        response = call_next(request)

        # Close the session after the request is handled
        request.state.db.close()
        return response
