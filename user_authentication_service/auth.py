#!/usr/bin/env python3
"""Authentication service: registration, login, sessions, resets."""

import uuid
from typing import Optional

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password) -> bytes:
    """Return a salted bcrypt hash of the given password."""
    if not isinstance(password, str):
        password = str(password)
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Return a new UUID as a string."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        """Initialize Auth with a DB instance."""
        self._db = DB()

    def register_user(self, email, password) -> User:
        """Register a new user or raise if email already exists."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hashed.decode())
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email, password) -> bool:
        """Validate credentials with bcrypt.checkpw."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        stored = user.hashed_password.encode("utf-8")
        return bcrypt.checkpw(password.encode("utf-8"), stored)

    def create_session(self, email) -> Optional[str]:
        """Create a new session for the user and return the session_id."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id) -> Optional[User]:
        """Return user linked to session_id, or None."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id) -> None:
        """Invalidate a user's session."""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email) -> str:
        """Create and store a reset token for a user, return the token."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User not found")
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token, password) -> None:
        """Update user's password using a valid reset token."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid reset token")
        hashed = _hash_password(password).decode()
        self._db.update_user(user.id, hashed_password=hashed, reset_token=None)
