#!/usr/bin/env python3

'''
    Module for a function called insert_school
'''


def insert_school(mongo_collection, **kwargs):
    '''
        A function named insert_school that inserts
        a new document in a collection based on
        **kwargs
    '''

    dic = {}
    for k, v in kwargs.items():
        dic.update({k: v})

    new_school = mongo_collection.insert_one(dic)

    return new_school.inserted_id
