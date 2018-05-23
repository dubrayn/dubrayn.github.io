#!/usr/bin/env python

from pymongo import MongoClient
import pymongo.errors
from bson.objectid import ObjectId
import hashlib
import gridfs

def hash_content(content):
  m = hashlib.md5()
  m.update(content)
  return m.hexdigest()

username, password, host, dbname = 'admin0', 'pwd0', '127.0.0.1', 'admin'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

try:
  db = client['test_gridfs']
  gridfs = gridfs.GridFS(db)
  filename = 'toto'
  content = '12f18481bh192d0 08 d h2j011jp'
  print(hash_content(content))
  # save content as a GridFS file
  gridfs.put(content, filename = filename)
  # load content from a GridFS file
  fp = gridfs.get_last_version(filename = filename)
  print(hash_content(fp.read()))
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))
