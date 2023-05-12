#!/usr/bin/env python3
"""
Redis exercise
"""
from typing import Callable
import redis


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

    @staticmethod
    def store(data: str) -> str:
        """
        Store data in cache
        """
        key = str(uuid.uuid4())
        Cache._redis.set(key, data)
        return key

# Implement call_history decorator here
def call_history(method: Callable) -> Callable:
    """
    call_history decorator
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function
        """
        # Get input and output list keys
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Append input arguments to input list
        Cache._redis.rpush(input_key, str(args))

        # Execute wrapped function to get output
        output = method(*args, **kwargs)

        # Append output to output list
        Cache._redis.rpush(output_key, str(output))

        # Return output
        return output

    # Return wrapper function
    return wrapper

# Decorate Cache.store with call_history
Cache.store = call_history(Cache.store)
