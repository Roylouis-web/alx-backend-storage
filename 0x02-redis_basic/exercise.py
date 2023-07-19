#!/usr/bin/env python3

"""
    Module for a class called Cache
"""

import redis
from uuid import uuid4
from typing import Union


class Cache(object):
    """
        A class called Cache that stores an instance
        of Redis client as a private variable called
        _redis and then flushes the instance
    """

    def __init__(self) -> None:
        """
            Initialises the Cache object
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
           A method that takes data as argument and
           returns a randomly generated string
        """

        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
