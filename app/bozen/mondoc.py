# mondoc.py = the MonDoc class

from typing import *

import pymongo

from .butil import *
from . import bozenutil
from . import formdoc
from . import mongo

#---------------------------------------------------------------------


"""
A MonDoc class has a classInfo variable (which is a Struct) containing:

- fieldNameSet :: set of str
- fieldNameTuple :: [str]
- useCollection

"""

# a dict of the MonDoc subclasses registered. The key is the class name
# (i.e. with upper-case first letter)
# :: dict str: MonDoc subclass
monDocSubclassDict = {}

class MonDocMeta(formdoc.FormDocMeta):
    def __init__(cls, name, bases, dyct):
        super(MonDocMeta, cls).__init__(name, bases, dyct)
        #cls.classInfo = Struct()
        #formdoc.initialiseClass(cls, dyct)
        initialiseMonDocClass(cls, dyct)

def initialiseMonDocClass(cls, dyct):
    """
    This contains additional initialisation for a MonDoc subcluass,
    over and above what is defined in `formdoc.initialiseClass`.
    """
    global monDocSubclassDict
    monDocSubclassDict[cls.__name__] = cls
    setCollection(cls, dyct)

def setCollection(cls, dyct):
    """ Set the pymongo collection into cls.classInfo.useCollection
    """
    if cls.__name__ == 'MonDoc': return
          
    useCollectionName = cls.__name__
    dpr("Class %s doesn't define a _collection, using %s",
        cls.__name__, useCollectionName)    
    db = mongo.getDefaultDatabase()
    if not db:
        raise Exception("No database defined, so can't initialise "
            "%s's collection"
            % (cls.__name__,))
    useCollection = db[useCollectionName]
    cls.classInfo.useCollection = useCollection



#---------------------------------------------------------------------

class MonDoc(formdoc.FormDoc, metaclass=MonDocMeta):
    """ an abstraction over a Mongo Document """

    def __init__(self, **kwargs):
        """ Create a new MonDoc.
        :param dict kwargs: these arguments can be used to give initial
            values to the fields in the MonDoc
        """
        super(MonDoc, self).__init__(**kwargs)
        
    def __repr__(self):
        s = "<%s" % (self.__class__.__name__,)
        if self.__dict__.has_key('_id'):
            s += " %s" % (self.id(),)
        showFields = self.classInfo.fieldNameTuple[:5]
        for fn in showFields:
            fv = self[fn]
            s += " %s=%r" % (fn, fv)
        #//for
        s += ">"
        return s

    def __str__(self):
        return self.__repr__()
    
    #========== class methods ==========
    
    @classmethod
    def count(cls, *args, **kwargs)->int:
        """ return a count of documents in this class.
        The args and kwargs arguments are the same as for
            pymongo.collection.Collection.find()

        :return the number of documents satisfying the criteria
        """
        cursor = cls.col().find(*args, **kwargs)
        return cursor.count()

    @classmethod
    def col(cls)->pymongo.collection.Collection:
        """ return a document's collection """
        return cls.classInfo.useCollection

#---------------------------------------------------------------------


#end
