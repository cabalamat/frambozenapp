# formdoc.py = FormDoc class, etc for bozen

import collections

from .butil import *
from . import bozenutil
from .fieldinfo import FieldInfo

#from butil import *
#import bozenutil
#from fieldinfo import FieldInfo

#---------------------------------------------------------------------

class FormDocMeta(type):
    def __init__(cls, name, bases, dyct):
        dpr("!!!! in FormDocMeta init method !!!!")
        super(FormDocMeta, cls).__init__(name, bases, dyct)
        cls.classInfo = Struct()
        initialiseClass(cls, dyct)
        
  
def initialiseClass(cls, dyct):
    """ Initialise a subclass of FormDoc
    :param class cls: the class we are initialising
    :param dict dict: a dictionary containing class variables
    """
    dpr("cls=%r __name__=%r", cls, cls.__name__)
    cls.classInfo.fieldNameSet = set()
    cls.classInfo.fieldNameTuple = []
    dpr("fieldNameTuple=%r", cls.classInfo.fieldNameTuple)
    for fieldName, fieldInfo in dyct.items():
        dpr("fieldName=%r fieldInfo=%r", fieldName, fieldInfo)
        if not isinstance(fieldInfo, FieldInfo): continue
        fieldInfo.setFieldName(fieldName)
        fieldInfo.setDocClass(cls)
        dpr("%s fieldName=%s",
            fieldInfo.__class__.__name__,
            fieldName)
        cls.classInfo.fieldNameSet.add(fieldName)
        cls.classInfo.fieldNameTuple.append(fieldName)
        #dpr("fieldNameTuple=%r", cls.classInfo.fieldNameTuple)
    #//for
    def keyFn(fieldName):
        return dyct[fieldName].index
    cls.classInfo.fieldNameTuple = tuple(
        sorted(cls.classInfo.fieldNameTuple,
               key= keyFn))
    checkForMissingIndex(cls, dyct)

def checkForMissingIndex(cls, dyct):
    #print "Checking class %s for duplicate fields..." % (cls.__name__,)
    indexes = [dyct[fieldName].index
               for fieldName in cls.classInfo.fieldNameTuple]
    if len(indexes)<2: return # array to small to check
    for at,fix in enumerate(indexes):
        fn = cls.classInfo.fieldNameTuple[at] #::str
        fi = dyct[fn] #::FieldInfo
        dpr("at={} fix={} fn=%s", at, fix, fn)
        if at>0:
            if prev+1 != fix:
                # found an error
                fn = cls.classInfo.fieldNameTuple[at] #::str
                fi = dyct[fn] #::FieldInfo
                raise Exception(
                    "In class %s, duplicate field definition before %s,"
                    " at %s:%d"
                    % (cls.__name__, fn, fi.definedFile, fi.definedLine))
        prev = fix
    #//for      
        
        
#---------------------------------------------------------------------

class FormDoc(metaclass=FormDocMeta):
    """ an collection of fields, for use in an html form

    Instance variables:

    displayErrors (bool) = do we display errors on outputting this form
    """

    def __init__(self, **kwargs):
        """ Create a new FormDoc.
        :param dict kwargs: these arguments can be used to give initial
            values to the fields in the FormDoc
        """
        self.displayErrors = False
        self.populateFields()
        allowedFieldNames = self.allowedFieldNameSet()
        for k, v in kwargs.items():
            if k not in allowedFieldNames:
                raise NameError("'%s' is not a valid field name for %s"
                    % (k, self.__class__.__name__))
            self.__dict__[k] = v
            
 
    def allowedFieldNameSet(self):
        """ Return allowed field names for this class
        @return::set str
        """
        return self.classInfo.fieldNameSet           
        
    def populateFields(self):
        """ populate the fields defined in the subclass's definition.
        """
        classDict = dict(type(self).__dict__)
        for con, co in classDict.items():
            if con[:1] == "_": continue
            if isinstance(co, FieldInfo):
                self.__dict__[con] = co.createWithInitialValue()
        #//for
    

    def __repr__(self):
        """
        Show a string representation of me
        :rtype str
        """
        s = "<%s" % (self.__class__.__name__,)
        showFields = self.classInfo.fieldNameTuple[:5]
        dpr("showFields=%r", showFields)
        for fn in showFields:
            fv = self[fn]
            s += " %s=%r" % (fn, fv)
        #//for
        s += ">"
        return s
       

    #========== make it work like a dict ==========

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def keys(self):
        return self.__dict__.keys()

    def __iter__(self):
        for item in self.__dict__:
            yield item

    def __len__(self):
        return len(self.__dict__)

    def get(self, key, defaultValue=None):
        if self.__dict__.has_key(key):
            return self.__dict__[key]
        else:
            return defaultValue
        
    #========== rendering an html form ==========

    def buildForm(self, **kwargs):
        """ Build an html form containing all the fields in the FormDoc.
        Includes enclosing '<table>' tags.
        """
        h = form("<table class='form-table'>{}</table>",
            self.buildFormLines(**kwargs))
        return h

    def buildFormLines(self, **kwargs):
        """ Build an html form containing all the fields in the FormDoc.
        Doesn't include enclosing '<table>' tags.
        """
        h = ""
        for fieldName in self.classInfo.fieldNameTuple:
            fi = self.getFieldInfo(fieldName)
            if fi.displayInForm:
                h += self.formLine(fieldName, **kwargs)
        #//for
        return h

    def formLine(self, fn, **kwargs):
        """ Build a line of an html form
        :param str fn: field name
        """
        errCssClass = ""
        errMsg2 = ""
        fi = self.getFieldInfo(fn)
        v = self[fn] # field value
        if self.displayErrors:
            errMsg = fi.errorMsg(v)
            if errMsg:
                errMsg2 = ("<br>\n<i class='fa fa-exclamation-triangle'></i> "
                    + errMsg)
                errCssClass = "form-error-line"

        h = form("""<tr class='{fn}_line {errCssClass}'>
    <th class='form-title'>
      <label for="id_{fn}" title="{desc}">{title}</label></th>
    <td>{ff} {errMsg2}</td>
</tr>""",
            fn = fn,
            desc = fi.desc,
            title = fi.title,
            ff = self.formField(fn, **kwargs),
            errCssClass = errCssClass,
            errMsg2 = errMsg2,
        )
        return h
    
    def formField(self, fn, **kwargs):
        """ Build a field of an html form
        :param str fn: field name
        """
        fi = self.getFieldInfo(fn)
        v = self[fn] # value in the field
        #prvars("fn kwargs fi v")
        h = fi.formField(v, **kwargs)
        #pr("type(h)=%s", type(h))
        #prvars("h")
        return h
    
    #========== utility functions ==========

    @classmethod
    def getFieldInfo(cls, fieldName):
        """ Get the FieldInfo object for a field in a FormDoc subclass.
        :param string fieldName:
        :rtype FieldInfo
        """
        return cls.__dict__[fieldName]


#---------------------------------------------------------------------





#end
