#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors
from bson.objectid import ObjectId

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client.test_db
  pycollection = db['pycollection']
  pycollection.update_one({'time': 0.01}, {'$inc': {'run': 3}})
  for d in pycollection.find(): print(str(d))
  pycollection.update_one({'time': 0.01}, {'$inc': {'run': -3}})
  print('after...')
  for d in pycollection.find(): print(str(d))
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
