#!/usr/bin/env python3

"""
    Module for a class called Cache
"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional


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

    def get(key: str, fn=None: Optional[Callable]) ->
    Union[bytes, str, int, float]:

        """
            A method that takes a key string as
            argument and an optional Callable
        """

        value = self._redis.get(key)

        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
            A method that automatically
            parametrizes Cache.get
        """

        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """
            A method that automatically
            parametrizes Cache.get
        """

        value = self._redis.get(key)

        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
