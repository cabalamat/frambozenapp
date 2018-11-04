# test_fieldinfo.py = test <fieldinfo.py>


from bozen.butil import *
from bozen import lintest

from bozen import fieldinfo
from bozen.fieldinfo import titleize, cssClasses, StrField


#---------------------------------------------------------------------

class T_functions(lintest.TestCase):  
    
    def test_titleize(self):
        r = titleize("theFieldName123")
        sb = "The Field Name 123"
        self.assertSame(r, sb)
        r = titleize("theFieldName123x")
        sb = "The Field Name 123 x"
        self.assertSame(r, sb)  
        
    def test_cssClasses(self):
        r = cssClasses()
        self.assertSame(r, "")
        r = cssClasses('')
        self.assertSame(r, '')
        r = cssClasses('foo', 'bar')
        self.assertSame(r, ' class="foo bar"')
        r = cssClasses(['foo', 'bar'])
        self.assertSame(r,  ' class="foo bar"')
        r = cssClasses('foo', False, 'bar')
        self.assertSame(r, ' class="foo bar"')
        r = cssClasses('foo', '', 'bar') 
        self.assertSame(r, ' class="foo bar"')
        r = cssClasses('foo', True and 'monospace')
        self.assertSame(r, ' class="foo monospace"')
        r = cssClasses('bar', False and 'monospace')
        self.assertSame(r, ' class="bar"')
        r = cssClasses('bar', 'should=fail', 'qwerty-56')
        self.assertSame(r, ' class="bar qwerty-56"')
    
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
