#!/usr/bin/env python3

'''
    Module for a function named update_topics
'''


def update_topics(mongo_collection, name, topics):
    '''
        A function that changes all topics of a school
        based on the name
    '''

    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}})
