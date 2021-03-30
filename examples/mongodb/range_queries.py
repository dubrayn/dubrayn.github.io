#!/usr/bin/env python3

from pymongo import MongoClient
import pymongo.errors

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client.test_db
  pycollection = db.pycollection

  for document in pycollection.find({"time": {"$lt": 0.015}}).sort('time'):
    print(document)

except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
