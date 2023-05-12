#!/usr/bin/env python3
"""Cache module"""

import redis
import functools


def count_calls(method: callable) -> callable:
    """Decorator to count the number of calls to a method"""
    @functools.wraps(method)
    def wrapped(self, *args, **kwargs):
        """Wrapped function that increments count and returns result"""
        key = method.__qualname__
        self.redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapped


class Cache:
    """Cache class that stores data in Redis"""
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)

    @count_calls
    def store(self, data: bytes) -> str:
        """Store the data in the cache and return its key"""
        key = self.redis.get('cache_key')
        if key is None:
            key = 1
        else:
            key = int(key) + 1
        self.redis.set(key, data)
        self.redis.set('cache_key', key)
        return str(key)

    def get(self, key: str) -> bytes:
        """Retrieve the data stored in the cache for the given key"""
        return self.redis.get(key)
