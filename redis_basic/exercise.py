#!/usr/bin/env python3
"""
Redis
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache
    """

    def __init__(self):
        """
        Redis
        """
        # Store the redis client as a private variable
        self._redis = redis.Redis()
        # Clear all keys in the current database
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Redis
        """
        # Generate a unique random key using uuid4
        random_key = str(uuid.uuid4())

        # Save the data to Redis under the generated key
        self._redis.set(random_key, data)

        # Return the key so the user can retrieve the data later
        return random_key
