#!/usr/bin/env python3
"""exercice.py"""

import functools
import redis
import uuid
from typing import Any, Callable, Optional, TypeVar, Union


def count_calls(method: Callable) -> Callable:
    """A system to count how many times methods
    of the Cache class are called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        inp_key = f"{key}:inputs"
        out_key = f"{key}:outputs"
        self._redis.rpush(inp_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(out_key, result)
        return result

    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function"""
    redis_instance = method.__self__._redis

    key = method.__qualname__
    inp_key = f"{key}:inputs"
    out_key = f"{key}:outputs"

    inputs = redis_instance.lrange(inp_key, 0, -1)
    outputs = redis_instance.lrange(out_key, 0, -1)

    print(f"{key} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        inp_str = inp.decode('utf-8') if isinstance(inp, bytes) else inp
        out_str = out.decode('utf-8') if isinstance(out, bytes) else out
        print(f"{key}(*{inp_str}) -> {out_str}")


class Cache:
    """class Cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key, store the input data in Redis
        using the random key and return the key."""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(
            self, key: str, fn: Optional[Callable[[bytes], TypeVar]] = None
    ) -> Optional[Union[bytes, TypeVar]]:
        """take a key string argument and an optional Callable argument
        named fn. This callable will be used to convert
        the data back to the desired format."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Optional[str]:
        """Parametrize Cache.get with the string conversion function."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """parametrize Cache.get with the integer conversion function."""

        return self.get(key, fn=int)
