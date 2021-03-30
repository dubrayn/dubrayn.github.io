#!/usr/bin/env python3

import sys
from pymongo import MongoClient
import pymongo.errors

def list_db(client):
  try:
    database_names = client.list_database_names()
    for database_name in database_names:
      db = client[database_name]
  
      lusers = db.command('usersInfo')

      users = [] 
      for document in lusers['users']:
        user = document['user']
        roles = [role['role'] for role in document['roles']]
        users.append(user)

      print("%s (%s)" % (database_name, str(users)))

      for collection_name in db.list_collection_names():
        print(" + %s" % (collection_name))

        nb_documents = db[collection_name].count()

        if database_name not in ["admin", "local"]:
          for document in db[collection_name].find():
            print("   + %s" % (str(document)))
        else:
          print("   + %d documents" % (nb_documents))
 
  except pymongo.errors.OperationFailure as e:
    print("ERROR: %s" % (e))

def clean_db(client):
  try:
    database_names = client.database_names()
    for database_name in database_names:
      db = client[database_name]
  
      users = db.command('usersInfo')
      nbUsers = len(users['users'])
  
      for document in users['users']:
        user = document['user']
        roles = [role['role'] for role in document['roles']]
        if user != 'admin0':
          db.command('dropUser', user)
  
      if database_name != 'admin' and database_name != 'local': 
        client.drop_database(database_name)
    
  except pymongo.errors.OperationFailure as e:
    print("ERROR: %s" % (e))

def init_db(client):
  clean_db(client)
  db = client['test_db']
  db.create_collection('MusicRecords')
  db.command('createUser', 'user0', pwd = 'pwd0', roles = ['readWrite'])
  db['MusicRecords'].insert_one({'band':'Pink Floyd', 'song':'Wish You Were Here'})
  db['MusicRecords'].insert_one({'band':'Pink Floyd', 'song':'Have a Cigar', 'year': 1975})
  
if __name__ == '__main__':
  username, password, host, dbname = 'admin0', 'pwd0', '127.0.0.1', 'admin'
  client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))

  if len(sys.argv) > 1:
    if sys.argv[1] == 'init':
      print("INIT")
      init_db(client)
      sys.exit()
    elif sys.argv[1] == 'clean':
      print("CLEAN")
      clean_db(client)
      sys.exit()

  list_db(client)
