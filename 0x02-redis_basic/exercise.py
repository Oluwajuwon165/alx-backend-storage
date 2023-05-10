#!/usr/bin/env python3
"""
Cache module
"""

import uuid
import redis
from typing import Callable, Union


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Initialize a new instance of the Cache class.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key and store the input data in Redis using the key.
        Return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) \
            -> Union[str, bytes, int, float]:
        """
        Retrieve the data stored at the given key in Redis.
        If a fn callable is provided, use it to convert the
        data back to the desired format.
        Return the data.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve the data stored at the given key in Redis as a string.
        Return the data as a string.
        """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve the data stored at the given key in Redis as an integer.
        Return the data as an integer.
        """
        return self.get(key, fn=lambda x: int(x))
