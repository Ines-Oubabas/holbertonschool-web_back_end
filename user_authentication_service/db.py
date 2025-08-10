#!/usr/bin/env python3
"""DB helper wrapping SQLAlchemy session operations on User."""

from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class encapsulating SQLAlchemy engine and session."""

    def __init__(self) -> None:
        """Initialize a new DB instance with a clean SQLite DB."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session: Session | None = None

    @property
    def _session(self) -> Session:
        """Memoized session object (private)."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password) -> User:
        """Create and persist a new user, then return it."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find first user matching provided fields or raise.

        Raises:
            NoResultFound: if no user matches.
            InvalidRequestError: if invalid columns are provided.
        """
        if not kwargs:
            raise InvalidRequestError("No filter arguments provided")
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise
        except Exception as exc:
            raise InvalidRequestError(str(exc))

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes and commit.

        Raises:
            ValueError: if an unknown attribute is provided.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Invalid field: {key}")
            setattr(user, key, value)
        self._session.commit()
