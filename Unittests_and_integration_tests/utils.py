#!/usr/bin/env python3
"""
Utility helpers:
- access_nested_map: safely access nested mappings by a path of keys.
- get_json: fetch JSON from an HTTP endpoint.
- memoize: cache method results per-instance (like a simple property cache).
"""

from typing import Any, Mapping, Tuple, Dict
import requests
from functools import wraps


def access_nested_map(nested_map: Mapping[str, Any],
                      path: Tuple[str, ...]) -> Any:
    """
    Access a nested mapping using an ordered tuple of keys.

    Args:
        nested_map: Nested dictionary-like mapping.
        path: Tuple of keys to traverse in order.

    Returns:
        The value found at the given path.

    Raises:
        KeyError: If any key in the path is missing.
    """
    current: Any = nested_map
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            raise KeyError(key)
        current = current[key]
    return current


def get_json(url: str) -> Dict[str, Any]:
    """
    Perform a GET request and return JSON payload as a dictionary.

    Args:
        url: HTTP endpoint.

    Returns:
        Parsed JSON payload as a dictionary.
    """
    response = requests.get(url)
    return response.json()


def memoize(method):
    """
    Decorator that caches the result of an instance method with no arguments.

    The cached value is stored on the instance using a private attribute,
    so subsequent calls return the cached value without re-invoking the method.
    """
    attr_name = f"_{method.__name__}_cached"

    @wraps(method)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)
    return wrapper
