#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client.test_db
  pycollection = db['pycollection']
  data = [{"pipo": i} for i in range(3)]
  pycollection.insert(data)
  for d in pycollection.find(): print(str(d))
  for i in range(3): pycollection.remove({"pipo": i})
  print("after...")
  for d in pycollection.find(): print(str(d))
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
