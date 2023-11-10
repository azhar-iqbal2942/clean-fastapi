from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from core.exceptions import DuplicateValueException


class UserRepository:
    """
    User repository provides all the database operations for the User model.
    """

    def create(self, session: Session, user):
        """
        The above function creates a new user in the database using the provided session and returns the
        created user.

        :param session: The "session" parameter is an instance of the SQLAlchemy Session class. It
        represents a database session and is used to interact with the database
        :type session: Session
        :param user: The "user" parameter is an instance of a user object that you want to create and
        add to the session
        :return: The `user` object is being returned.
        """
        try:
            session.add(user)
            session.commit()
            return user
        except IntegrityError as e:
            session.rollback()
            raise DuplicateValueException("This email is already exist.")

    def get_all(self, session: Session):
        """
        The function retrieves all users from the database using the provided session.

        :param session: The `session` parameter is an instance of the SQLAlchemy `Session` class. It
        represents a database session and is used to interact with the database
        :type session: Session
        :return: a list of all the User objects in the database.
        """
        users = session.query(User).all()
        return users

    def get_by_email(self, session: Session, email: str):
        user = session.query(User).filter(User.email == email).first()
        return user
