#!/usr/bin/env python3

'''
    Module for a function named schools_by_topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
        A Python function that returns the list
        of school having a specific topic
    '''

    return mongo_collection.find(
            {"topics": {"$in": [topic]}})
