#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors
import numpy as np
import bson
import pickle

username, password, host, dbname = 'user0', 'pwd0', '127.0.0.1', 'test_db'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  for i in range(3):
    mat = np.eye(3) * i
    bindat = bson.binary.Binary(pickle.dumps(mat, protocol = 2))
    data_id = client['test_db']['numpy_test'].insert_one({'mat': bindat}).inserted_id
    print("id: %s" % (str(data_id)))
    print(mat)
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
