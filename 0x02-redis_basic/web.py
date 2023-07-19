#!/usr/bin/env python3

'''
    Web cache and tracker
'''

import requests
import redis
from functools import wraps
from typing import Callable


store = redis.Redis()


def count_url_access(method: Callable) -> Callable:
    '''
        Decorator to count the number of times
        an https request was made to a url
    '''

    @wraps(method)
    def wrapper(url):
        ''' Wrapper decorator '''

        cached_key = 'cached:' + url
        cached_data = store.get(cached_key)

        if cached_dat:
            return cached_data.decode('utf-8')

        count_key = 'count:' + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    res = requests.get(url)
    return res.text
