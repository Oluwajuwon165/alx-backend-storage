#!/usr/bin/env python3
"""
Main file
"""
import redis
from uuid import uuid4
from typing import Union, Callable


def call_history(method: Callable) -> Callable:
    """
    Store history of input and output for function
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function
        """
        key = method.__qualname__
        input_key = key + ":inputs"
        output_key = key + ":outputs"

        r = redis.Redis()
        r.rpush(input_key, str(args))
        result = method(*args, **kwargs)
        r.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Constructor method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None) -> Union[str, bytes, int, float, None]:
        """
        Get method
        """
        data = self._redis.get(key)
        if fn is not None and data is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Get string method
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Get int method
        """
        return self.get(key, lambda x: int(x))

    def get_str_list(self, key: str) -> list:
        """
        Get string list method
        """
        data = self._redis.lrange(key, 0, -1)
        return [item.decode('utf-8') for item in data]
