#!/usr/bin/env python3

'''
    Web cache and tracker
'''

import requests
import redis
from functools import wraps
from typing import Callable

store = redis.Redis()


def count_url_access(method: Callable[[str], str]) -> Callable:
    '''
        Decorator to count the number of times
        an https request was made to a url
    '''

    @wraps(method)
    def wrapper(url: str) -> str:
        ''' Wrapper decorator '''

        count_key = 'count:' + url
        html = method(url)

        store.incr(count_key)
        store.expire(count_key, 10)
        return html.text
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    '''
        Returns HTML content from a url
    '''
    res = requests.get(url)
    return res.text
