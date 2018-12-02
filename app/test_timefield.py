# test_timefield.py = test the <timefield.py> module

import traceback
import datetime

from bozen.butil import *
from bozen import lintest

from bozen import timefield
from bozen.timefield import BzDate, BzDateTime

#---------------------------------------------------------------------

class T_BzDate(lintest.TestCase):
    """ test the BzDate class """
    
    def test_creation(self):
        d = BzDate("2017-12-31")
        self.assertSame(d, "2017-12-31")
        self.assertSame(str(d), "2017-12-31")
        
        d2 = BzDate("20130908")
        self.assertSame(d2, "2013-09-08")
        
        d3 = BzDate("2013-09-08and irrelevant stuff here")
        self.assertSame(d3, "2013-09-08")
       
    def test_creation_exception(self):
        try:
            d = BzDate("2017-12-3")
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
        self.assertSame(d, "1998-12-13")
        
    def test_creation_from_BzDate(self):
        d = BzDate("2011-09-22")
        d2 = BzDate(d)
        self.assertSame(d2, "2011-09-22")
        
    def test_actsAsStr(self):   
        d = BzDate("2006-07-09")
        mm = d[5:7]
        self.assertSame(mm, "07", "extracted month")
        self.assertTrue(isinstance(d, BzDate), "d is a BzDate")
        
        ds = str(d)
        self.assertFalse(isinstance(ds, BzDate), "ds isn't a BzDate")
        self.assertTrue(isinstance(ds, str), "ds is a str")
         
    def test_repr(self):
        d = BzDate("2006-07-09")
        r = repr(d)
        self.assertSame(r, "BzDate('2006-07-09')", "repr of a BzDate")
        
    def test_toTuple(self):
        d = BzDate("2004-12-02")
        year, month, day = d.toTuple()
        self.assertSame(year, 2004, "year")
        self.assertSame(month, 12, "month")
        self.assertSame(day, 2, "day")
        
    def test_to_date(self):
        d = BzDate("2004-09-24")
        pyd = d.to_date()
        self.assertSame(pyd.year, 2004, "year")
        self.assertSame(pyd.month, 9, "month")
        self.assertSame(pyd.day, 24, "day")
        
    def test_to_datetime(self):
        d = BzDate("2001-01-09")
        pyd = d.to_datetime()
        self.assertSame(pyd.year, 2001, "year")
        self.assertSame(pyd.month, 1, "month")
        self.assertSame(pyd.day, 9, "day")
        self.assertSame(pyd.hour, 0, "hour")
        self.assertSame(pyd.minute, 0, "minute")
        self.assertSame(pyd.second, 0, "second")
        
    def test_addDays(self):
        d = BzDate("2001-01-09")
        dpr("d=%r:%s", d, type(d))
        d2 = d.addDays(4)
        dpr("d2=%r:%s", d2, type(d2))
        self.assertSame(d2, "2001-01-13", "added 4 days")
        
        d3 = d.addDays(365)
        dpr("d3=%r:%s", d3, type(d3))
        self.assertSame(d3, "2002-01-09", "added 365 days")
        
        d4 = d.addDays(-10)
        dpr("d4=%r:%s", d4, type(d4))
        self.assertSame(d4, "2000-12-30", "subtract 10 days")
        
    def test_today(self):
        t = BzDate.today()
        dpr("Today's date: %r", t)
        year, month, day = t.toTuple()
        self.assertTrue(year >= 2018, 
            "(assumes we are not testing in the past)")
        self.assertTrue(month >= 1)
        self.assertTrue(month <= 12)
        self.assertTrue(day >= 1)
        self.assertTrue(day <= 31)
        
  
#---------------------------------------------------------------------

class T_BzDateTime(lintest.TestCase):
    """ test the BzDateTime class """
    
    def test_creation_allDigits(self):
        """ create a BzDateTime using all-digit format """
        d = BzDateTime("20171231")
        self.assertSame(d, "2017-12-31T00:00:00")
        self.assertSame(str(d), "2017-12-31T00:00:00")
        
        d = BzDateTime("19870615")
        self.assertSame(d, "1987-06-15T00:00:00")
        
        d = BzDateTime("1989061521")
        self.assertSame(d, "1989-06-15T21:00:00")
        
        d = BzDateTime("199106152153")
        self.assertSame(d, "1991-06-15T21:53:00")
        
        d = BzDateTime("199106152153somenonsensehere")
        self.assertSame(d, "1991-06-15T21:53:00")
        
        d = BzDateTime("19920615215301")
        self.assertSame(d, "1992-06-15T21:53:01")
              
    def test_creation_bzFormat(self):
        """ create a BzDateTime using variations of bz format, 
        e.g. "2017-12-31T23:59:58"
        """
        d = BzDateTime("2012-06-04")
        self.assertSame(d, "2012-06-04T00:00:00")
        
        d = BzDateTime("2012-05-04T07")
        self.assertSame(d, "2012-05-04T07:00:00")
        
        d = BzDateTime("2012-04-04T07:35")
        self.assertSame(d, "2012-04-04T07:35:00")
        
        d = BzDateTime("2011-04-04T07:35:51")
        self.assertSame(d, "2011-04-04T07:35:51")
        
        d = BzDateTime("2011-04-04  07:35:51")
        self.assertSame(d, "2011-04-04T07:35:51")
        
    def test_creation_from_BzDate(self):
        """ create a BzDateTime from a BzDate or BzDateTime """
        d = BzDate("2012-06-04")
        d2 = BzDateTime(d)
        self.assertSame(d2, "2012-06-04T00:00:00")
        
    
#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_BzDate)
group.add(T_BzDateTime)

if __name__=='__main__': group.run()

#end
