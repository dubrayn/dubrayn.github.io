#!/usr/bin/env python3

from pymongo import MongoClient
import pymongo.errors
from bson.objectid import ObjectId

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client.test_db
  pycollection = db['pycollection']
  pycollection.replace_one({'time': 0.01}, {'toto': 'tutu'})
  for d in pycollection.find(): print(str(d))
  pycollection.replace_one({'toto': 'tutu'}, {'run': '0000', 'time': 0.01, 'norm': 1.0})
  print('after...')
  for d in pycollection.find(): print(str(d))
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
