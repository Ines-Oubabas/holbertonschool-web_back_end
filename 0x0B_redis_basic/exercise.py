#!/usr/bin/env python3
"""
Redis-based caching utilities with call counting and history replay.

This module defines a `Cache` class that wraps a Redis client to store values,
retrieve them with optional conversion, count method calls, and keep a history
of inputs and outputs. It also provides a `replay` helper to display history.
"""

from __future__ import annotations

from functools import wraps
from typing import Any, Callable, Optional, TypeVar, Union
import uuid

import redis


T = TypeVar("T")


def count_calls(method: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator that counts the number of times `method` is called.

    It uses the method's qualified name as the Redis key and increments it on
    each call, returning the original method's result unchanged.
    """

    @wraps(method)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        self = args[0]
        key: str = method.__qualname__
        # Increment the counter for this method
        self._redis.incr(key)
        return method(*args, **kwargs)

    return wrapper


def call_history(method: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator that records the inputs and outputs of `method` calls.

    Inputs are pushed to a Redis list named "<qualname>:inputs" and outputs to
    "<qualname>:outputs". Arguments are normalized using `str(args)`.
    """

    @wraps(method)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        self = args[0]
        qn: str = method.__qualname__
        in_key: str = f"{qn}:inputs"
        out_key: str = f"{qn}:outputs"

        # Record inputs (ignore kwargs per project requirements)
        self._redis.rpush(in_key, str(args[1:]))

        # Execute and record output
        result: T = method(*args, **kwargs)
        self._redis.rpush(out_key, str(result))
        return result

    return wrapper


class Cache:
    """
    Simple Redis-backed cache with typed retrieval and call history.

    An instance initializes its own Redis client and flushes the current DB.
    """

    def __init__(self) -> None:
        """Initialize the Redis client and flush the database."""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store `data` in Redis under a random UUID key and return that key.

        Args:
            data: The value to store (str, bytes, int, or float).

        Returns:
            The generated key as a string.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], T]] = None
    ) -> Optional[Union[bytes, T]]:
        """
        Retrieve a value from Redis by key, optionally converting it.

        Args:
            key: The Redis key to retrieve.
            fn: Optional single-argument callable that converts the raw bytes
                into the desired type (e.g., int, str decoder, custom parser).

        Returns:
            The raw bytes if no converter is given, the converted value if a
            converter is provided, or None if the key does not exist.
        """
        data: Optional[bytes] = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis, decoding as UTF-8.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The decoded string or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))  # type: ignore[return-value]

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The integer value or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: int(d))  # type: ignore[return-value]


def replay(method: Callable[..., Any]) -> None:
    """
    Display the call history for a decorated method.

    It prints the total call count and each recorded call in the format:
    `QualName(*<inputs>) -> <output>`
    """
    if not hasattr(method, "__self__"):
        return

    redis_client: redis.Redis = getattr(method.__self__, "_redis")  # type: ignore[attr-defined]
    qn: str = method.__qualname__
    in_key: str = f"{qn}:inputs"
    out_key: str = f"{qn}:outputs"

    # Fetch counts and history
    raw_count = redis_client.get(qn)
    count = int(raw_count.decode("utf-8")) if raw_count else 0

    inputs = redis_client.lrange(in_key, 0, -1)
    outputs = redis_client.lrange(out_key, 0, -1)

    print(f"{qn} was called {count} times:")
    for raw_in, raw_out in zip(inputs, outputs):
        in_decoded = raw_in.decode("utf-8")
        out_decoded = raw_out.decode("utf-8")
        print(f"{qn}(*{in_decoded}) -> {out_decoded}")
