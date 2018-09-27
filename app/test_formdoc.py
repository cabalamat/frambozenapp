# test_formdoc.py = tests <formdoc.py>

from bozen.butil import *
from bozen import lintest

from bozen.fieldinfo import StrField
from bozen import formdoc

#---------------------------------------------------------------------

class Customer(formdoc.FormDoc):
    name = StrField(
        desc="the full name of the customer",
        title="Customer Name",
        default="no name")
    address = StrField(default = "xxx")
    y = StrField() # defaults to ""
    z = StrField(default="zzz.zz") # defaults to "zzz.zz"

class T_FormDoc(lintest.TestCase):
    """ test operations on a a Customer form """
    
    def test_creation1(self):
        c = Customer()
        self.assertSame(c.name, "no name")
        self.assertSame(c.address, "xxx")
        self.assertSame(c.y, "")
        self.assertSame(c.z, "zzz.zz")
        
    def test_creation2(self):
        c = Customer(
            name="Bella",
            address="1290 Short Lane",
            y="wise",
            z="asleep")
        self.assertSame(c.name, "Bella")
        self.assertSame(c.address, "1290 Short Lane")
        self.assertSame(c.y, "wise")
        self.assertSame(c.z, "asleep")
        
    def test_buildForm(self):
        c = Customer(
            name="Bella",
            address="1290 Short Lane",
            y="wise",
            z="asleep")
        formH = c.buildForm()
        dpr("formH:\n%s", formH)

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_FormDoc)

if __name__=='__main__': group.run()


#end
