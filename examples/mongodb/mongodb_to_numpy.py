#!/usr/bin/env python3

from pymongo import MongoClient
import pymongo.errors
import numpy as np
import bson
import pickle

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  for data in client['test_db']['numpy_test'].find():
    bindat = data["mat"]
    data_id = data["_id"]
    mat = pickle.loads(bindat)
    print("id: %s" % (str(data_id)))
    print(mat)
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))

