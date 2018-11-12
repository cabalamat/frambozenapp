# test_mondoc.py = Test the MonDoc class

import traceback

import bozen
from bozen.butil import *
from bozen import lintest, MonDoc
from bozen.fieldinfo import StrField
from bozen.numberfield import IntField
from bozen.keychoicefield import FK
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
    
    def test_find(self):
        """ the find() function """
        f = list(Foo.find({'name': "Bran Stark"}))
        self.assertSame(len(f), 1, "there is only one Bran Stark")

    def test_find_one(self):
        """ the find_one() function """
        r = Foo.find_one({'name': "Bran Stark"})
        self.assertSame(type(r), Foo, "returned a Foo")
        self.assertSame(r.address, "up north", "address is correct")

        r = Foo.find_one({'name': "doesn't exist"})
        self.assertSame(r, None, "no record returned")

    def test_getDoc(self):
        """ test the getDoc() function """
        f = Foo.find_one({'name': "Bran Stark"})
        fid = f.id()
        pr("fid=%r", fid)
        f2 = Foo.getDoc(fid)
        self.assertSame(f2.address, "up north",
            "address got by getDoc() is correct")

        f3 = Foo.getDoc("this shouldn't exist")
        self.assertSame(f3, None, "f3 correctly doesn't exist")
        
    def test_delete(self):
        """ test the delete() method """
        f = Foo.find_one({'name': "Bran Stark"})
        f.delete()
        fs = list(Foo.find({'name': "Bran Stark"}))
        self.assertSame(len(fs), 0, "Bran Stark has been deleted")
        
#---------------------------------------------------------------------

class T_urls(lintest.TestCase):
    """ test a, url, logo, getName functions """

    def test_url(self):
        self.db = bozen.getDefaultDatabase()
        self.db.drop_collection("foo")
        numFoos = Foo.count()
        self.assertSame(numFoos, 0, "there should be no Foos")

        # make a foo
        foo = Foo(name="Onion Knight", address="Seaworth")
        foo.save()
        id = foo.id()

        u = foo.url()
        urlSb = "/foo/" + id
        self.assertSame(u, urlSb, "foo's url is correct")

        self.assertSame(foo.logo(), "", "foo doesn't have a logo")

        self.assertSame(foo.getName(), "Onion Knight", "foo.getName()")

        # put it all together
        a = foo.a()
        aSb = form("<a href='{}'>Onion Knight</a>", urlSb)
        self.assertSame(a, aSb, "foo.a()")

#---------------------------------------------------------------------

class Author(MonDoc):
    name = StrField()

class Book(MonDoc):
    title = StrField()
    yearPublished = IntField()
    author_id = FK(Author)
    

class T_foreignKeys(lintest.TestCase):
    """ test the FK (foreign key) field and associated functionality """
    
    def setUpAll(self):
        """ run once before all the tests, to set up the system """
        self.db = bozen.getDefaultDatabase()
        
        self.db.drop_collection("Author")
        numAuthors = Author.count()
        self.assertSame(numAuthors, 0, "there should be no Authors")
        
        self.db.drop_collection("Book")
        numBooks = Book.count()
        self.assertSame(numBooks, 0, "there should be no Authors")

    def test_create_data(self):
        a1 = Author(name="George R. R. Martin")
        a1.save()
        a2 = Author(name="George Orwell")
        a2.save()
        numAuthors = Author.count()
        self.assertSame(numAuthors, 2, "there should be 2 Authors")
        
        b1 = Book(title="A Game of Thrones", yearPublished=1996)
        b1.author_id = a1._id
        b1.save()
        
        b2 = Book(title="A Clash of Kings", yearPublished=1999)
        b2.author_id = a1._id
        b2.save()
        
        b3 = Book(title="Animal Farm", yearPublished=1945)
        b3.author_id = a2._id
        b3.save()
        
        numBooks = Book.count()
        self.assertSame(numBooks, 3, "there should be 3 Books")
        
    def test_accessForeignFields(self):
        grrm = Author.find_one({'name': "George R. R. Martin"})
        go = Author.find_one({'name': "George Orwell"})
        
        #>>>>> Book "A Game of Thrones"
        b1 = Book.find_one({'yearPublished': 1996})
        self.assertSame(b1.title, "A Game of Thrones")
        self.assertSame(b1.author_id, grrm._id, 
            "Author id of A Game of Thrones")
        self.assertSame(b1.author.name, "George R. R. Martin", 
            "Author of A Game of Thrones")
        try:
            r = b1.foo
        except KeyError:
            exStr = traceback.format_exc()
            self.passed("correctly throws exception for non-existant field, "
                "exception is:\n-----begin-----\n%s-----end-----"
                % (exStr,))
        else:
            self.failed("incorrectly doesn't throw exception for "
                "non-existant field")
            
        #>>>>> Book "Animal Farm"
        b3 = Book.find_one({'yearPublished': 1945}) 
        self.assertSame(b3.title, "Animal Farm")
        self.assertSame(b3.author_id, go._id, 
            "Author id of Animal Farm")
        self.assertSame(b3.author.name, "George Orwell", 
            "Author of Animal Farm")   
            
                  
                  
    
#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_create_save_delete)
group.add(T_urls)
group.add(T_foreignKeys)

if __name__=='__main__': group.run()



#end
