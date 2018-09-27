# fieldinfo.py = information about fields

import inspect
import os.path

from . import butil
from .butil import *
from . import bozenutil

#import butil
#from butil import *
#import bozenutil

#---------------------------------------------------------------------
# utility functions


def titleize(fn: str)->str:
    """ Convert a field name into a title
    :param string fn: a field name
    :rtype string
    """
    if fn[-3:]=="_id" and len(fn)>3:
        # remove trailing _id
        fn = fn[:-3]
    fn = fn[:1].capitalize() + fn[1:]
    r = ""
    insideNumber = False
    for ch in fn:
        if ch.isupper() or (ch.isdigit() != insideNumber):
            r += " "
        r += ch
        insideNumber = ch.isdigit()
    return r.strip()


#---------------------------------------------------------------------
"""
Things a field index (fi) must do:

fi.formField() = return a form field

fi.errorMsg() = return an error message (or "" if no errors)

fi.convertValue(fv) = convert from a form-value into a value that can be
    stored in a database field.
    
fi.convertToReadable(dbv)->str = convert from a db-valuer into a string

fi.convertToReadableH(dbv)->str = convert from a db-value into an html
    marked up string

"""


fieldIndex = bozenutil.Incrementor()

class FieldInfo:
    """ superclass for Bozen fields """

    def __init__(self, **kwargs):
        self.index = fieldIndex()
        self.desc = ""
        self.readArgs(**kwargs)

        caller = inspect.stack()[1]
        pan = caller[1]
        self.definedFile = os.path.basename(pan)
        self.definedLine = caller[2]

        dpr("%s:{} [%r] create %s, kwargs=%r",
            self.definedFile, self.definedLine,
            self.index, str(self.__class__.__name__), kwargs)


    def __repr__(self):
        r = "<%s %s>" % (self.__class__.__name__,
            butil.exValue(lambda: self.fieldName, "(name unknown)"))
        return r

    def createWithInitialValue(self):
        return self.defaultValue

    #========== html output to form ==========

    def xxxformBox(self, v, **kwargs):
        return self.formField(v, **kwargs)

    def formField(self, v, **kwargs):
        """
        Create a form field (typically an <input> tag).
        This method will be over-ridden by most subclasses.

        :param v: this is the value of the field in the FormDoc
        :param kwargs: these arguments may include
            - readOnly :: bool (default False) = the form is read only
        :type kwargs: dict str:Any
        :return html containing the field
        :rtype str
        """
        readOnly = kwargs.get('readOnly', self.readOnly)
        if readOnly:
            return self.formField_ro(v, **kwargs)
        else:
            return self.formField_rw(v, **kwargs)


    def formField_rw(self, v, **kwargs):
        vStr = self.convertToReadable(v)
        h = form("""<input class='gin{monospace}' id="id_{fn}"
            name="{fn}"
            type="text" value="{v}" size={fieldLen}>""",
            monospace = self.monospaceClass(),
            fn = self.fieldName,
            v = attrEsc(vStr),
            fieldLen = self.fieldLen)
        return h

    def formField_ro(self, v, **kwargs):
        vStr = htmlEsc(self.convertToReadable(v))
        if vStr.strip() == "": vStr = "&nbsp;"
        h = form("<span class='read-only{monospace}' "
                 "id='id_{fn}'>{v}</span>",
            fn = self.fieldName,
            v = vStr,
            monospace = self.monospaceClass(),
        )
        return h

    def monospaceClass(self):
        """ returns text for the monospace CSS class.
        :rtype str
        """
        if self.monospaced:
            return " monospace"
        else:
            return ""

    #========== error message for field

    def errorMsg(self, v):
        """ Calculate an error message for this field
        :param v: data for this field (in format as it goes in the
            database)
        :return an error message for this field,
            or "" if there are no errors
        :rtype str
        """
        retVal = ""
        #pr("v=%r self.minValue=%r", v, self.minValue)
        if (self.minValue is not None) and v < self.minValue:
            retVal += "Value %s must be >=%s.\n" % (v, self.minValue)
        if (self.maxValue is not None) and v > self.maxValue:
            retVal += "Value %s must be <=%s.\n" % (v, self.maxValue)

        return retVal


    #========== subclasses should re-implement these ==========

    def readArgs(self, **kwargs):
        """ Reads the keyword arguments when the FieldInfo was created.
        Subclasses of FieldInfo may wish to call this using super and
        then add their own keyword arguments.
        """
        #pr("FieldInfo:readArgs kwargs=%r", kwargs)
        self.defaultValue = kwargs.get('default', self.defaultDefault())
        if 'desc' in kwargs:
            self.desc = kwargs['desc']
        if 'title' in kwargs:
            self.title = kwargs['title']
        if 'columnTitle' in kwargs:
            self.columnTitle =  kwargs['columnTitle']

        self.fieldLen = kwargs.get("fieldLen", 20)
        self.formatStr = kwargs.get("formatStr", "{}")
        self.readOnly = kwargs.get('readOnly', False)
        self.monospaced = kwargs.get('monospaced', False)
        self.minValue = kwargs.get('minValue', None)
        self.maxValue = kwargs.get('maxValue', None)
        self.displayInForm = kwargs.get('displayInForm', True)
        self.convertF = kwargs.get('convertF', None)

    def defaultDefault(self):
        """ return the default value for the default value of the
        object.
        """
        return None

    def convert(self, v):
        """ Convert a value from something got from a form to a value
        that can be stored in the database for that field. uses the
        (convertF) parameter if it is set, otherwise uses the FieldInfo
        subclass's convertValue() method
        The return type necessarily depends on what field type it is.
        :param string v:
        """
        v2 = butil.ascStr(v)
        #prvars("v2")
        if self.convertF:
            return self.convertF(v2)
        else:
            return self.convertValue(v2)

    def convertValue(self, v):
        """ Convert a value from something got from a form to a value
        that can be stored in the database for that field.
        The return type necessarily depends on what field type it is.
        :param string v:
        """
        raise ImplementedBySubclass

    def convertToReadableH(self, v):
        """ Convert the internal value in the database (v) to a readable
        value (i.e. a string or unicode that could de displayed in a form
        or elsewhere). This method is the opposite of the convertValue()
        method.

        :param v: value from database
        :return readable html based (v)
        :rtype str containing html
        """
        h = htmlEsc(self.convertToReadable(v))
        return h

    def convertToReadable(self, v):
        """ Convert the internal value in the database (v) to a readable
        value (i.e. a string or unicode that could de displayed in a form
        or elsewhere). This method is the opposite of the convertValue()
        method.

        :param v: value from database
        :rtype str or unicode
        """
        s = self.formatStr.format(v)
        return s


    #========== helper functions

    def setFieldName(self, fieldName):
        """
        This is called from formdoc.initialiseClass() to set the
        fieldName to be whatever the class variable name is in the
        class definition.
        :param fieldName: the field name
        :type fieldName: str
        """
        dpr("setting field name to %r", fieldName)
        self.fieldName = fieldName
        if not hasattr(self, 'title'):
            self.title = titleize(self.fieldName)
        if not hasattr(self, 'columnTitle'):
            self.columnTitle = self.title
        return self.title

    def setDocClass(self, docClass):
        """
        This is called from formdoc.initialiseClass() to set the
        docClass to the class for which this is a field.
        :param docClass: the class of this FieldInfo
        :type docClass: a subclass of FormDoc or MonDoc
        """
        self.docClass = docClass

    def classFieldName(self):
        """ Text giving the class and fieldname of the FieldInfo, e.g.
        "Customer.phoneNumber". May be useful for debugging.
        @return::str
        """
        return "%s.%s" % (self.docClass.__name__, self.fieldName)


#---------------------------------------------------------------------


class StrField(FieldInfo):
    """ a field holding a Python str """

    def readArgs(self, **kwargs):
        super(StrField, self).readArgs(**kwargs)
        self.minLength = kwargs.get('minLength', None)
        self.maxLength = kwargs.get('maxLength', None)
        self.charsAllowed = kwargs.get('charsAllowed', None)
        self.required = kwargs.get('required', False)


    def defaultDefault(self):
        """ return the default value for the default value of the
        object.
        """
        return ""

    def convertValue(self, v):
        return butil.myStr(v)


    def errorMsg(self, v):
        if self.required and not v:
            return "This field is required."

        msg = "Value '{}' ".format(v)

        if self.minLength!=None and len(v)<self.minLength:
            msg += "must be at least %d characters long"%self.minLength
            return msg

        if self.maxLength!=None and len(v)>self.maxLength:
            msg += "must be no longer than %d characters"%self.maxLength
            return msg

        if self.charsAllowed!=None:
            for ch in v:
                if ch not in self.charsAllowed:
                    msg += ("may only contain chars in: %s"
                            % self.charsAllowed)
                    return msg

        return ""




#---------------------------------------------------------------------





#end
