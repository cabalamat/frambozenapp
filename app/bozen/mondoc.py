# mondoc.py = the MonDoc class

from typing import *

import pymongo

from .butil import *
from . import bozenutil
from .bztypes import DbId, DisplayValue, DbValue, HtmlStr
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
        
    def allowedFieldNameSet(self)->Set[str]:
        """ Return allowed field names for this class. Valid fields
        are all the ones defined, and _id. This overrides the method in
        FormDoc, which doesn't allow '_id'.
        """
        return self.classInfo.fieldNameSet | set(["_id"])
        
    def __repr__(self):
        s = "<%s" % (self.__class__.__name__,)
        if '_id' in self.__dict__:
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
    def count(cls, *args, **kwargs) -> int:
        """ return a count of documents in this class.
        The args and kwargs arguments are the same as for
            pymongo.collection.Collection.find()

        :return the number of documents satisfying the criteria
        """
        cursor = cls.col().find(*args, **kwargs)
        return cursor.count()


    @classmethod
    def find(cls, *args, **kwargs) -> Iterator:
        """ a wrapper round the pymongo find() method. This method
        is an iterator; each value returned is an instance of the relevant
        MonDoc subclass.
        """
        kwargs = cls.fixKwargs(kwargs)
        cursor = cls.col().find(*args, **kwargs)
        for item in cursor:
            ins = cls.transform(item)
            yield ins
            
    @classmethod
    def find_one(cls, *args, **kwargs) -> Union['MonDoc',None]:
        """ a wrapper round the pymongo find_one() method. The value
        returned is an instance of the relevant MonDoc subclass.
        """
        kwargs = cls.fixKwargs(kwargs)
        doc = cls.col().find_one(*args, **kwargs)
        if doc==None: return None
        ins = cls.transform(doc)
        return ins
    
    @classmethod
    def delete_many(cls, spec=None):
        """ Delete all the documents in this table
        :param spec: Optional MongoDB search specification. If included,
            only records complying with the specification will be deleted.
        :type spec: dict or None
        """
        cls.col().delete_many(spec)
        
    @classmethod
    def getDoc(cls, id: DbId) -> Union['MonDoc',None]:
        """ get a document from the collection given its id.
        If it doesn't exist, return None
        :param id:
        :ptype id: str or ObjectId
        :param bool createIfNotExist: if the document doesn't exist,
            create a new one and set its _id to be id.
        :rtype MonDoc subclass, or None
        """
        id = mongo.normaliseId(id)
        result = cls.col().find_one({'_id': id})
        if result==None:
            return None
        ins = cls.transform(result)
        return ins

    @classmethod
    def transform(cls, mongoDoc: Dict) -> 'MonDoc':
        """ Transform a document as returned by pymongo into a MonDoc-subclass
        document.
        @param dict mongoDoc: a document as returned from pymongo. This
            is a dict with the keys being strings and the values being
            json values converted to the equivalent Python type.
        """
        instance = cls()
        for k, v in mongoDoc.items():
            instance.__dict__[k] = v
        instance.postLoad()
        return instance
    
    @classmethod
    def col(cls) -> pymongo.collection.Collection:
        """ return a document's collection """
        return cls.classInfo.useCollection
    
    #========== saving ==========
    
    def save(self):
        """ save this document """
        if not self.hasId():
            self._id = "%s-%s" % (
                self.__class__.__name__, 
                mongo.idInc.getNewIndexB36())
            self.preCreate()
            
        self.preSave()
        self.col().save(self.mongoDict())
        self.postSave()   
        
    def delete(self):
        """ Delete this document from the database """
        if self.hasId():
            self.col().delete_one({'_id': self._id})
    remove = delete
 
    def preSave(self):
        """ The user can over-ride this with a method to be called
        immediately before the document is saved.
        """
        pass

    def postSave(self):
        """ The user can over-ride this with a method to be called
        immediately after the document is saved.
        """
        pass

    def preCreate(self):
        """ The user can over-ride this with a method to be called
        immediately before the document is created in the database
        (but just after its future _id has been assigned).
        """
        pass
    
    def postLoad(self):
        """ The user can over-ride this with a method to be called
        immediately after the document is loaded.
        """
        pass
    
    def mongoDict(self):
        """ return a dictionary for the current document,
        in the format wanted by pymongo. Only include fields
        defined in the class definition.
        :rtype dict
        """
        d = {}
        for fn in (self.classInfo.fieldNameTuple + ('_id',)):
            if not fn in self.__dict__: continue
            d[fn] = self[fn]
        #//for
        #prvars("d")
        return d
    
    

    #========== functions for rendering as html ==========

    def a(self, urlStub=None, includeLogo=True) -> HtmlStr:
        """Get an a-href for a document.
        :param urlStub: if this parameter is given, then the urlStub is
            the url before the id(), e.g. if id()="foo-12" and urlStub="/abc/"
            then the whole url is "/abc/foo-12"
        """
        if urlStub:
            url = urlStub + self.id()
            #prvars("url")
        else:
            url = self.url()
            #prvars("url")
        if includeLogo:
            logo = self.logo()
        else:
            logo = ""
        h = "<a href='%s'>%s%s</a>" % (attrEsc(url),
            logo, self.getNameH())
        return h


    def url(self) -> str:
        """
        The URL at which this document can be accessed in the web app.
        By convention this is /{collectionName}/{documentId} ; this can be
        over-ridden if desired.
        """
        n = self.__class__.__name__
        collectionName = n[:1].lower() + n[1:]
        u = form("/{}/{}", collectionName, self.id())
        return u

    @classmethod
    def classLogo(cls) -> HtmlStr:
        """
        A logo for all documents in the collection, for example using
        Font Awesome or a similar web logo collection. If a logo is used,
        insert a space after it unless you want it to be right next to
        the text describing the document.
        """
        return ""

    def logo(self) -> HtmlStr:
        """
        A logo for the document, for example using Font Awesome or a
        similar web logo collection. If a logo is used, insert a space after
        it unless you want it to be right next to the text describing
        the document.
        """
        return self.classLogo()

    def getName(self) -> str:
        """ Returns a string that is used to descibe the document.
        The default implementation here is the contents of the first
        FieldInfo field defined for the MonDoc.
        """
        if len(self.classInfo.fieldNameTuple)==0:
            return ""
        fn0 = self.classInfo.fieldNameTuple[0]
        if fn0.endswith("_id"): return self.id()
        return self.asReadable(fn0)

    def getNameH(self) -> HtmlStr:
        """ Returns an html-escpaed string that is used to descibe the document.
        The default implementation here is the contents of the first
        FieldInfo field defined for the MonDoc.
        """
        return htmlEsc(self.getName())

    
    #========== misc methods

    def id(self) -> str:
        """ return this docment's _id, converted to a string,
        or "" if no _id.
        """
        if self.hasId():
            return str(self._id)
        else:
            return ""

    def hasId(self) -> bool:
        """ does this document have an _id field? """
        return '_id' in self.__dict__
    
    #========== utility functions ==========
    
    @staticmethod
    def fixKwargs(kwargs):
        """ Normalise the kwargs to the `find()` method.
        :param dict kwargs: this is the keyword arguments to the find()
            method or similar methods
        :return the same kwargs but with the sort parameter normalised
        :rtype dict
        """
        if 'sort' in kwargs:
            kwargs['sort'] = MonDoc.fixSort(kwargs['sort'])
        return kwargs

    @staticmethod
    def fixSort(sortArg) -> List[Tuple[str,int]]:
        """ Normalise sort argument.

        This puts the sort argument into a form that pymongo requires. See:
        <http://api.mongodb.org/
        python/current/api/pymongo/cursor.html#pymongo.cursor.Cursor.sort>

        Examples:

        'foo' -> [('foo', 1)]
        ('bar',-1) -> [('bar', -1)]
        [('foo',-1), 'bar'] -> [('foo', -1), ('bar', 1)]

        @return = the sort argument in te way that pymongo requires it
        """
        if isinstance(sortArg, (str,tuple)):
            sortArg = [sortArg]
        newSortArg = [term if isinstance(term, tuple)
                           else (term, 1)
                      for term in sortArg]
        return newSortArg

    
    
    
#---------------------------------------------------------------------


#end
