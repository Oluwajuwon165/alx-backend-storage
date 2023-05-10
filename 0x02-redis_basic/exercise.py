#!/usr/bin/env python3
"""
Cache module
"""

import uuid
import redis


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
