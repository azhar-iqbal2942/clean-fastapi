from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from config.database import get_session
from core.exceptions import DuplicateValueException


class UserRepository:
    """
    User repository provides all the database operations for the User model.
    """

    def __init__(self, session: Annotated[Session, Depends(get_session)]) -> None:
        self.session = session

    def create(self, user):
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
            self.session.add(user)
            self.session.commit()
            return user
        except IntegrityError as e:
            self.session.rollback()
            raise DuplicateValueException("This email is already exist.")

    def get_all(self):
        """
        The function retrieves all users from the database using the provided session.

        :param session: The `session` parameter is an instance of the SQLAlchemy `Session` class. It
        represents a database session and is used to interact with the database
        :type session: Session
        :return: a list of all the User objects in the database.
        """
        users = self.session.query(User).all()
        return users

    def get_by_email(self, email: str):
        """
        The function get_by_email retrieves a user from the database based on their email.

        :param email: The email parameter is a string that represents the email address of the user you
        want to retrieve from the database
        :type email: str
        :return: the user object that matches the given email address.
        """
        user = self.session.query(User).filter(User.email == email).first()
        return user

    def get_by_id(self, id: int):
        """
        The function get_user_by_id retrieves a user from the database based on their ID.

        :param id: The `id` parameter is an integer that represents the unique identifier of a user
        :type id: int
        :return: The method is returning a User object that matches the given id.
        """
        return self.session.query(User).filter(User.id == id).first()
