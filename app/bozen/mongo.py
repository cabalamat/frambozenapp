# mongo.py = interface to MongoDB

import pymongo

#---------------------------------------------------------------------
mongoClient = None
defaultDB = None

def setDefaultDatabase(dbName: str, host="localhost", port=27017):
    global mongoClient, defaultDB, idInc
    mongoClient = pymongo.MongoClient(host, port)
    database = mongoClient[dbStr]
    
def getDefaultDatabase():

#---------------------------------------------------------------------

#end
