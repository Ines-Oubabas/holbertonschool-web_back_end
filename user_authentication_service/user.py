#!/usr/bin/env python3
"""SQLAlchemy User model."""

from typing import Any
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """User table mapped to 'users'."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self) -> str:
        """Return debug representation."""
        return f"<User id={self.id} email={self.email!r}>"
