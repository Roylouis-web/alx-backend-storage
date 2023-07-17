#!/usr/bin/env python3

'''
    Module for a Python function called list_all
'''


def list_all(mongo_collection):
    '''
        A Python function that lists all
        document in a collection
    '''

    if mongo_collection is None:
        return []

    return mongo_collection.find()
