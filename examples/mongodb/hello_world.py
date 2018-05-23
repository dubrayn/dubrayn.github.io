#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors

username, password, host, dbname = 'admin0', 'pwd0', '127.0.0.1', 'admin'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  print(client.database_names()) # list databases

  db = client['test_db']
  print(db.collection_names()) # list collections

except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
