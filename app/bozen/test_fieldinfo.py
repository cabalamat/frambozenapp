# test_fieldinfo.py = test <fieldinfo.py>


from butil import *
import lintest

import fieldinfo

#---------------------------------------------------------------------

class T_functions(lintest.TestCase):
    
    def test_titleize(self):
        r = fieldinfo.titleize("theFieldName123")
        sb = "The Field Name 123"
        self.assertSame(r, sb)
        r = fieldinfo.titleize("theFieldName123x")
        sb = "The Field Name 123 x"
        self.assertSame(r, sb)
    
    
    
#---------------------------------------------------------------------

dpr("friendly debugging message here")

group = lintest.TestGroup()
group.add(T_functions)

if __name__=='__main__': group.run()

#end
