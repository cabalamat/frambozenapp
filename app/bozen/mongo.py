# mongo.py = interface to MongoDB

from typing import *

import pymongo

#---------------------------------------------------------------------

mongoClient = None
defaultDB = None

def setDefaultDatabase(dbName: str, host="localhost", port=27017):
    global mongoClient, defaultDB, idInc
    mongoClient = pymongo.MongoClient(host, port)
    defaultDB = mongoClient[dbName]
    
def getDefaultDatabase()->Optional[pymongo.collection.Collection]:
    """ return the default database, if this has been set """
    return defaultDB

#---------------------------------------------------------------------

#end
