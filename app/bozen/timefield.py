# timefield.py = date and time fields

"""
Fields for time and date representation.


The date and timer formats used here are based on ISO8601 and especially 
on RFC3339 which defines a subset of ISO8601.

Dates are stored like this: "1985-04-12"
Instances in time are stored like this: "1985-04-12T23:20:50"
Time-of-day is stored like this: "23:59:00"

"""

from typing import *
import datetime
import re

from . import butil
from .butil import *
from . import bozenutil

from .fieldinfo import fieldIndex, FieldInfo, cssClasses

#---------------------------------------------------------------------

validDate=re.compile("[0-9]{4}-[0-1][0-9]-[0-3][0-9]")

def isValidDate(s: str) -> bool:
    return bool(validDate.fullmatch(s[:10]))

validDate8=re.compile("[0-9]{4}[0-1][0-9][0-3][0-9]")

def isValidDate8(s: str) -> bool:
    return bool(validDate8.fullmatch(s[:8]))

validDateTime=re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}"
    "T[0-2][0-9]:[0-5][0-9]:[0-5][0-9]")

def isValidDateTime(s: str) -> bool:
    return bool(validDateTime.fullmatch(s))

validTod=re.compile("[0-2][0-9]:[0-5][0-9]:[0-5][0-9]")

def isValidTod(s: str) -> bool:
    return bool(validTod.fullmatch(s))


class BzDate(str):
    """ the Bozen date class """
    
    def __new__(cls, s):
        dpr("s=%r:%s", s, type(s))
        if isinstance(s, str):
            if isValidDate(s): # yyyy-mm-dd
                return super().__new__(cls, s[:10])
            if isValidDate8(s): # yyyymmdd
                s2 = "%s-%s-%s" % (s[0:4], s[4:6], s[6:8])
                return super().__new__(cls, s2)
            else:    
                errMsg = form("String %r wrongly formatted for BzDate," 
                    "should be 'yyyy-mm-dd'", s)
                raise ValueError(errMsg)
        elif isinstance(s, datetime.date):
            s2 = "%04d-%02d-%02d" % (s.year, s.month, s.day)
            return super().__new__(cls, s2)
        else:
            s = ""
        
            
    def __repr__(self) -> str:
        r = "BzDate(%r)" % (str(self),)
        return r
    
    def toTuple(self) -> Tuple[int,int,int]:
        """ to tuple of year, month, day """
        y = butil.exValue(lambda: int(self[0:4]), 2000)
        mon = butil.exValue(lambda: int(self[5:7]), 1)
        day = butil.exValue(lambda: int(self[8:10]), 1)
        return (y, mon, day)
    
    def to_date(self) -> datetime.date:
        """ convert to datetime.date """
        y, m, d = self.toTuple()
        return datetime.date(y, m ,d)
        
    def to_datetime(self) -> datetime.datetime:
        """ convert to datetime.datetime """
        y, m, d = self.toTuple()
        return datetime.datetime(y, m ,d)
    
    def formatDate(self, formatStr:str) -> str:
        dt = self.to_date()
        s = dt.strftime(formatStr)
        return s
    
    def addDays(self, numDays: int) -> 'BzDate':
        dt = self.to_date() 
        dt2 = dt + datetime.timedelta(numDays)
        return BzDate(dt2)        
        
    @classmethod
    def today(cls) -> 'BzDate':
        today = datetime.date.today()
        return BzDate(today)

#---------------------------------------------------------------------
""" 
The default format for a date to look like in a from field 
"""
DEFAULT_DATE_SCREEN_FORMAT = "%Y-%b-%d"

class DateField(FieldInfo):
    """ a field that contains a date """

    def readArgs(self, **kwargs):
        super(DateField, self).readArgs(**kwargs)
        self.fieldLen = kwargs.get('fieldLen', 13)
        self.dateFormat = kwargs.get('dateFormat', 
            DEFAULT_DATE_SCREEN_FORMAT)
        self.required = kwargs.get('required', False)

    def defaultDefault(self):
        return ""

    def convertValue(self, vStr: str) -> Union[BzDate,str]:
        """ Convert a value coming back from an html form into a format
        correct for the database (either a BzDate or "")
        """
        vStr = vStr.strip()
        if not vStr: return ""
    
        try:
            bzd = BzDate(vStr)
        except ValueError:
            return ""
        return bzd
    
    

    def convertToScreen(self, v:Union[str,BzDate]) -> str:
        """ Convert the internal value in Python (v) to a readable
        value (i.e. a string or unicode that could de displayed in a form
        or elsewhere).
        """
        dpr("v=%r:%s", v, type(v))
        if not v: return ""
        if isinstance(v,BzDate):
            s = v.formatDate(self.dateFormat)
            return s
        else:
            raise ShouldntGetHere

    def formField_rw(self, v, **kwargs) -> str:
        """
        Create a form field (an <input> tag).

        :param v: this is the value of the field in the FormDoc
        :param kwargs: these arguments may include
            - readOnly :: bool (default False) = the form is read only
        :type kwargs: dict str:Any
        :return html containing the field
        :rtype str
        """
        vStr = self.convertToScreen(v)
        h = form("""<input{cc} id="id_{fn}"
            name="{fn}"
            type="text" value="{v}" size={fieldLen}>""",
            cc = cssClasses(
                "bz-input",
                "bz-DateField",
                self.monospaced and "monospace"),
            fn = self.fieldName,
            v = attrEsc(vStr),
            fieldLen = self.fieldLen)
        return h

    def formField_ro(self, v, **kwargs) -> str:
        vStr = self.convertToScreenH(v)
        if not vStr: vStr = "&nbsp;"
        h = form("""<span class='bz-read-only'>{}</span>""",
            vStr)
        return h

    def errorMsg(self, v) -> str:
        if self.required and not v:
            return "This field is required."


#---------------------------------------------------------------------

#---------------------------------------------------------------------

#end
