#!/usr/bin/env python3

'''
    Module for a python script that provides some
    stats about Nginx logs stored in MongoDB
'''

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx
methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
total = nginx_collection.count_documents({})
get_and_path = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'})
dic = {}

for method in methods:
    dic.update({method: nginx_collection.count_documents({'method': method})})
print('{} logs'.format(total))
print('Methods:')
for method in methods:
    print('    method {}: {}'.format(method, dic[method]))

print('{} status check'.format(get_and_path))
