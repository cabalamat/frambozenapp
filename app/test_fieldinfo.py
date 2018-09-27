# test_fieldinfo.py = test <fieldinfo.py>


from bozen.butil import *
from bozen import lintest

from bozen import fieldinfo
from bozen.fieldinfo import titleize, StrField


#---------------------------------------------------------------------

class T_functions(lintest.TestCase):  
    
    def test_titleize(self):
        r = titleize("theFieldName123")
        sb = "The Field Name 123"
        self.assertSame(r, sb)
        r = titleize("theFieldName123x")
        sb = "The Field Name 123 x"
        self.assertSame(r, sb)  
    
#---------------------------------------------------------------------
   
class T_StrField(lintest.TestCase):
    """ test the StrField class """
    
    def test_basicMethods(self):
        sf = StrField()
        r = sf.defaultDefault()
        self.assertSame(r, "")
    
    
#---------------------------------------------------------------------

dpr("friendly debugging message here")

group = lintest.TestGroup()
group.add(T_functions)
group.add(T_StrField)

if __name__=='__main__': group.run()

#end
