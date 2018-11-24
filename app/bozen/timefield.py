# timefield.py = date and time fields

from typing import *
import datetime

from . import butil
from .butil import *
from . import bozenutil

from .fieldinfo import fieldIndex, FieldInfo

#---------------------------------------------------------------------

class BzDate(str):
    """ the Bozen date class """
    
    def __new__(cls, s):
        dpr("s=%r:%s", s, type(s))
        if isinstance(s, str):
            dpr("s=%r is str", s)
            if len(s)>=8:
                return super().__new__(cls, s[:8])
            else:    
                errMsg = form("String %r wrongly formatted for BzDate," 
                    "should be 'yyyymmdd'", s)
                raise ValueError(errMsg)
        elif isinstance(s, datetime.date):
            dpr("s=%r is date", s)
            s2 = "%04d%02d%02d" % (s.year, s.month, s.day)
            dpr("s2=%r" % (s2,))
            return super().__new__(cls, s2)
        else:
            s = ""
        
            
    def __repr__(self) -> str:
        r = "BzDate(%r)" % (str(self),)
        return r
    
    def toTuple(self) -> (int,int,int):
        """ to tuple of year, month, day """
        y = butil.exValue(lambda: int(self[0:4]), 2000)
        mon = butil.exValue(lambda: int(self[4:6]), 1)
        day = butil.exValue(lambda: int(self[6:8]), 1)
        return (y, mon, day)
    
    def to_date(self) -> datetime.date:
        """ convert to datetime.date """
        y, m, d = self.toTuple()
        return datetime.date(y, m ,d)
        
        
    def to_datetime(self) -> datetime.datetime:
        """ convert to datetime.datetime """
        y, m, d = self.toTuple()
        return datetime.datetime(y, m ,d)
    
    def addDays(self, numDays: int) -> 'BzDate':
        dt = self.to_date() 
        dpr("dt=%r:%s", dt, type(dt))
        dt2 = dt + datetime.timedelta(numDays)
        dpr("dt2=%r:%s", dt2, type(dt2))
        bd2 = BzDate(dt2)
        dpr("bd2=%r:%s", bd2, type(bd2))
        return bd2
        
        
    @classmethod
    def today(cls) -> 'BzDate':
        """ TODO """    

#---------------------------------------------------------------------

#end
