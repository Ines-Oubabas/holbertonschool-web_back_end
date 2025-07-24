#!/usr/bin/env python3
"""
This module provides utilities for password hashing and validation using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed version.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plaintext password to validate.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
