# test_mondoc.py = Test the MonDoc class


import bozen
from bozen.butil import *
from bozen import lintest
from bozen import mondoc

bozen.setDefaultDatabase('test_bozen')

#---------------------------------------------------------------------

class Foo(mondoc.MonDoc):
    name = StrField(default = "no name")
    address = StrField(default = "xxx")
    y = StrField() # defaults to ""
    howMany = IntField(default = 42)
    
    
class T_create_save_delete(lintest.TestCase):
    """ test creating and saving a Foo in the database """

    def setUpAll(self):
        """ run once before all the tests, to set up the system """
        self.db = bozen.getDefaultDatabase()
        self.db.drop_collection("foo")
        numFoos = Foo.count()
        self.assertSame(numFoos, 0, "there should be no Foos")

    
#---------------------------------------------------------------------

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_create_save_delete)

if __name__=='__main__': group.run()



#end
