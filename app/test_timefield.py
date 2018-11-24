# test_timefield.py = test the <timefield.py> module

import traceback
import datetime

from bozen.butil import *
from bozen import lintest

from bozen import timefield
from bozen.timefield import BzDate

#---------------------------------------------------------------------

class T_BzDate(lintest.TestCase):
    """ test the BzDate class """
    
    def test_creation(self):
        d = BzDate("20171231")
        self.assertSame(d, "20171231")
        self.assertSame(str(d), "20171231")
       
    def test_creation_exception(self):
        try:
            d = BzDate("2017123")
        except: 
            exStr = traceback.format_exc()
            self.passed("correctly throws exception for bad value, "
                "exception is:\n-----begin-----\n%s-----end-----"
                % (exStr,)) 
        else:
            self.failed("incorrectly doesn't throw exception for "
                "bad value")  
        
    def test_creation_from_date(self):    
        date = datetime.date(1998, 12, 13)
        d = BzDate(date)
        dpr("d=%r:%s", d, type(d))
        dpr("str(d)=%r", str(d))
        self.assertSame(d, "19981213")
        
    def test_actsAsStr(self):   
        d = BzDate("20060709")
        mm = d[4:6]
        self.assertSame(mm, "07", "extracted month")
        self.assertTrue(isinstance(d, BzDate), "d is a BzDate")
        
        ds = str(d)
        self.assertFalse(isinstance(ds, BzDate), "ds isn't a BzDate")
        self.assertTrue(isinstance(ds, str), "ds is a str")
         
    def test_repr(self):
        d = BzDate("20060709")
        r = repr(d)
        self.assertSame(r, "BzDate('20060709')", "repr of a BzDate")
        
    def test_toTuple(self):
        d = BzDate("20041202")
        year, month, day = d.toTuple()
        self.assertSame(year, 2004, "year")
        self.assertSame(month, 12, "month")
        self.assertSame(day, 2, "day")
        
    def test_to_date(self):
        d = BzDate("20040924")
        pyd = d.to_date()
        self.assertSame(pyd.year, 2004, "year")
        self.assertSame(pyd.month, 9, "month")
        self.assertSame(pyd.day, 24, "day")
        
    def test_to_datetime(self):
        d = BzDate("20010109")
        pyd = d.to_datetime()
        self.assertSame(pyd.year, 2001, "year")
        self.assertSame(pyd.month, 1, "month")
        self.assertSame(pyd.day, 9, "day")
        self.assertSame(pyd.hour, 0, "hour")
        self.assertSame(pyd.minute, 0, "minute")
        self.assertSame(pyd.second, 0, "second")
        
    def test_addDays(self):
        d = BzDate("20010109")
        dpr("d=%r:%s", d, type(d))
        d2 = d.addDays(4)
        dpr("d2=%r:%s", d2, type(d2))
        self.assertSame(d2, "20010113", "added 4 days")
        
        d3 = d.addDays(365)
        dpr("d3=%r:%s", d3, type(d3))
        self.assertSame(d3, "20020109", "added 365 days")
        
        d4 = d.addDays(-10)
        dpr("d4=%r:%s", d4, type(d4))
        self.assertSame(d4, "20001230", "subtract 10 days")
        
        
        
    
#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_BzDate)

if __name__=='__main__': group.run()

#end
