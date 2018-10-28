# test_mondoc.py = Test the MonDoc class

import traceback

import bozen
from bozen.butil import *
from bozen import lintest
from bozen.fieldinfo import StrField
from bozen.numberfield import IntField
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
        self.db.drop_collection("Foo")
        numFoos = Foo.count()
        self.assertSame(numFoos, 0, "there should be no Foos")

    def test_createFoo(self):
        f = Foo()
        dpr("f.__class__=%r", f.__class__)
        dpr("f.__class__.classInfo=%r", f.__class__.classInfo)
        dpr("f.__dict__=%r", f.__dict__)
        self.assertSame(f.name, "no name", "accessing f.name field")
        self.assertSame(f.address, "xxx", "accessing f.address field")
        self.assertSame(f.y, "", "accessing f.y field")
        self.assertSame(f.howMany, 42, "accessing f.howMany field")

    def test_createFoo_withArguments(self):
        f = Foo(name="Jon Snow", address="The Wall")
        self.assertBool(isinstance(f, Foo), "(f) is a Foo")
        self.assertSame(f.name, "Jon Snow", "f.name value")
        self.assertSame(f.address, "The Wall", "f.address value")

        #>>>>> test manually setting _id works
        f2 = Foo(_id="qwerty")

        pr("f2.__dict__=%r", f2.__dict__)
        self.assertSame(f2._id, "qwerty", "f._id value")
        self.assertSame(f2.id(), "qwerty", "access _id using f.id()")

        #>>>>> test non-existant field throws exception

        try:
            f3 = Foo(fieldDoesNotExist=1579)
        except:
            exStr = traceback.format_exc()
            self.passed("correctly throws exception for non-existant field, "
                "exception is:\n-----begin-----\n%s-----end-----"
                % (exStr,))
        else:
            self.failed("incorrectly doesn't throw exception for "
                "non-existant field")

    def test_save(self):
        f = Foo()
        f.name = "Bran Stark"
        f.address = "up north"
        f.y = "Why?"
        f.howMany = -333
        f.save()
        numFoos = Foo.count()
        self.assertSame(numFoos, 1, "there should be exactly 1 Foo")

        id = f.id()
        dpr("f.id()=%r", id)
    
#---------------------------------------------------------------------

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_create_save_delete)

if __name__=='__main__': group.run()



#end
