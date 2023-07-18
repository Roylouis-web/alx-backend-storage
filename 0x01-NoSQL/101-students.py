#!/usr/bin/env python3

'''
    Module for a function named top_students
'''


def top_students(mongo_collection):
    '''
        A function that returns all students sorted
        by average score
    '''

    return mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}])
