#!/usr/bin/env python3

'''
    A script that prints some stats about
    an nginx collection
'''

from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    total = nginx_collection.count_documents({})
    get_and_path = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    method_dict = {}

    for method in methods:
        method_dict.update(
            {method: nginx_collection.count_documents({'method': method})})
    print('{} logs'.format(total))
    print('Methods:')
    for method in methods:
        print('\tmethod {}: {}'.format(method, method_dict[method]))

    print('{} status check'.format(get_and_path))

    print('IPs:')
    for res in nginx_collection.aggregate(
            [{'$sortByCount': '$ip'}, {'$limit': 10}]):
        print("\t{}: {}".format(res['_id'], res['count']))
