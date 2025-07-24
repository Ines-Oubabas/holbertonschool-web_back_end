#!/usr/bin/env python3
"""Encrypting passwords and Check valid password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash the password using bcrypt and return the salted hash."""
    pass_encoded = password.encode()
    pass_hashed = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return pass_hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    valid = False
    pass_encoded = password.encode()
    if bcrypt.checkpw(pass_encoded, hashed_password):
        return True
    return False