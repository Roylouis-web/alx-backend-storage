#!/usr/bin/env python3

'''
    Web cache and tracker
'''

import requests
import redis

store = redis.Redis()


def get_page(url: str) -> str:
    '''
        Returns HTML content from a url
    '''
    res = requests.get(url)
    store.incr('count:{}'.format(url))
    store.expire('count:{}'.format(url), 10)
    return res.text
