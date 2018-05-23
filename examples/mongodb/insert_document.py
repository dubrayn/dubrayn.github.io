#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client.test_db
  pycollection = db['pycollection']

  for i in range(3):
    data = { "run": 0, "time": 0.01 * i, "norm": 1.0}
    data_id = pycollection.insert_one(data).inserted_id

    print("id: %s" % (str(data_id)))
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
