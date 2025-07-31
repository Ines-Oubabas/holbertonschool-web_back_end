#!/usr/bin/env python3
"""File contening Auth class"""
import os
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth Class methods"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path is authorized"""
        if path is None:
            return True
        if not excluded_paths:
            return True
        if not path.endswith("/"):
            path += "/"
        for excluded in excluded_paths:
            if excluded == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header value from request"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """to be implemented"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(cookie_name)