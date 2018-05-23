#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client.test_db
  pycollection = db.pycollection

  pycollection.drop_index('time_1')

  for i in pycollection.list_indexes():
    print(i)

except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
