# test_mondoc.py = Test the MonDoc class

import traceback

import bozen
from bozen.butil import *
from bozen import lintest, MonDoc
from bozen.fieldinfo import StrField
from bozen.numberfield import IntField
from bozen.keychoicefield import FK
from bozen.multichoicefield import FKeys
from bozen import mondoc
from bozen.nulldoc import NullDoc

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
        dpr("f=%r", f)
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
    

class T_FK(lintest.TestCase):
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
        
    def test_accessForeignFields_b1(self):
        grrm = Author.find_one({'name': "George R. R. Martin"})
        
        #>>>>> Book "A Game of Thrones"
        b1 = Book.find_one({'yearPublished': 1996})
        self.assertSame(b1.title, "A Game of Thrones")
        self.assertSame(b1.author_id, grrm._id, 
            "Author id of A Game of Thrones")
        b1keys = sorted(list(b1.__dict__.keys()))
        dpr("b1 has keys: %r", b1keys)
        
        self.assertSame(b1.author.name, "George R. R. Martin", 
            "Author of A Game of Thrones")
        
        # make sure b1 doesn't write .author field 
        b1.save()
        b1dict = Book.col().find_one({'yearPublished': 1996})
        dpr("b1 (from pymongo) %r", b1dict)
        b1keys = list(b1dict.keys())
        self.assertTrue("_id" in b1keys, "b1dict has _id")
        self.assertTrue("title" in b1keys, "b1dict has title")
        self.assertTrue("yearPublished" in b1keys,
            "b1dict has yearPublished")
        self.assertTrue("author_id" in b1keys, 
            "b1dict has author_id")
        self.assertFalse("author" in b1keys, 
            "b1dict doesn't have author field")
        
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
            
            
    def test_accessForeignFields_b3(self):
        go = Author.find_one({'name': "George Orwell"})
        
        #>>>>> Book "Animal Farm"
        b3 = Book.find_one({'yearPublished': 1945}) 
        self.assertSame(b3.title, "Animal Farm")
        self.assertSame(b3.author_id, go._id, 
            "Author id of Animal Farm")
        self.assertSame(b3.author.name, "George Orwell", 
            "Author of Animal Farm")   
        
    def test_no_FK_so_NullDoc(self):
        """ when FK cannot be deferenced, return a NullDoc """
        b4 = Book(title="The C Programming Language",
            yearPublished=1988)
        b4.save()
        
        b4load = Book.find_one({'title':"The C Programming Language"})
        r = b4load.title
        self.assertSame(r, "The C Programming Language", "Title correct")
        r = b4load.yearPublished
        self.assertSame(r, 1988, "Year correct")
        r = b4load.author_id
        self.assertSame(r, None, "author_id correct")
        r = b4load.author
        self.assertTrue(isinstance(r, NullDoc),
            "author is a NullDoc")   
        self.assertSame(r.fakeClass, Author,
            "the NullDoc is pretending to be an Author")   
        r = b4load.author.name
        self.assertSame(r, "", "No author, so field gets default value")
        
    def test_getForeignFieldNames(self):
        """ the getForeignFieldNames() function """
        r = Book.getForeignFieldNames(Author)
        self.assertSame(r, ['author_id'], 
            "Book has foreign field to Author of author_id")
            
     
#---------------------------------------------------------------------

class AuthorM(MonDoc):
    name = StrField()

class BookM(MonDoc):
    title = StrField()
    authors_ids = FKeys(AuthorM)
    

class T_FKeys(lintest.TestCase):
    """ test the FKeys (foreign keys) field and associated functionality """
                 
    
    def setUpAll(self):
        """ run once before all the tests, to set up the system """
        self.db = bozen.getDefaultDatabase()
        
        self.db.drop_collection("AuthorM")
        numAuthors = AuthorM.count()
        self.assertSame(numAuthors, 0, "there should be no Authors")
        
        self.db.drop_collection("BookM")
        numBooks = BookM.count()
        self.assertSame(numBooks, 0, "there should be no Authors")

    def test_create_data(self):
        a1 = AuthorM(name="Brian Kernighan")
        a1.save()
        a2 = AuthorM(name="Dennis Ritchie")
        a2.save()
        a3 = AuthorM(name="Rob Pike")
        a3.save()
        numAuthors = AuthorM.count()
        self.assertSame(numAuthors, 3, "there should be 3 Authors")
        
        b1 = BookM(title="The C Progranmming Language")
        b1.authors_ids = [a1._id, a2._id]
        b1.save()
        
        b2 = BookM(title="The Practice of Programming")
        b2.authors_ids = [a1._id, a3._id]
        b2.save()
        
        b3 = BookM(title="The Unix Programming Environment")
        b3.authors_ids = [a1._id, a3._id]
        b3.save()
        
        numBooks = BookM.count()
        self.assertSame(numBooks, 3, "there should be 3 Books")
        
    def test_load(self):
        """ load all the books and authors into instance variables """
        self.a1 = AuthorM.find_one({'name': "Brian Kernighan"})
        self.assertSame(self.a1.name, "Brian Kernighan")    
        
        self.a2 = AuthorM.find_one({'name': "Dennis Ritchie"})
        self.assertSame(self.a2.name, "Dennis Ritchie")   
        
        self.a3 = AuthorM.find_one({'name': "Rob Pike"})
        self.assertSame(self.a3.name, "Rob Pike")
        
        self.b1 = BookM.find_one({'title': "The C Progranmming Language"})
        self.assertSame(self.b1.authors_ids, [self.a1._id, self.a2._id],
            "authors for b1")
        
        self.b2 = BookM.find_one({'title': "The Practice of Programming"})
        self.assertSame(self.b2.authors_ids, [self.a1._id, self.a3._id],
            "authors for b2")
        
        self.b3 = BookM.find_one({'title': "The Unix Programming Environment"})
        self.assertSame(self.b3.authors_ids, [self.a1._id, self.a3._id],
            "authors for b3")
        
    def test_dereference(self):
        """ dereferencing an FKeys field """
        r = self.b1.authors
        self.assertSame(len(r), 2, "b1 has 2 authors")
        authorNames = ", ".join(au.name for au in self.b1.authors)
        self.assertSame(authorNames, "Brian Kernighan, Dennis Ritchie",
            "authors for b1")
        
        r3 = self.b3.authors
        self.assertSame(len(r3), 2, "b3 has 2 authors")
        authorNames = ", ".join(au.name for au in self.b3.authors)
        self.assertSame(authorNames, "Brian Kernighan, Rob Pike",
            "authors for b3")
        
    def test_getForeignFieldNames(self):
        """ the getForeignFieldNames() function """
        r = BookM.getForeignFieldNames(AuthorM)
        self.assertSame(r, ['authors_ids'], 
            "BookM has foreign field to AuthorM of authors_ids")
        
        r = AuthorM.getForeignFieldNames(BookM)
        self.assertSame(r, [], 
            "AuthorM has no foreign fields to BookM")
        
    def test_getForeignIds(self):
        """ FKeys reverse lookup -- get ids """
        bookIds = list(self.a1.getForeignIds(BookM, 'authors_ids'))
        dpr("bookIds for a1 (Brian Kernighan): %r", bookIds)
        self.assertSame(len(bookIds), 3, 
             "Brian Kernighan has authored 3 books in database")
        self.assertTrue(self.b1._id in bookIds, 
            "bookIds contains 'The C Progranmming Language'")
        self.assertTrue(self.b2._id in bookIds, 
            "bookIds contains 'The Practice of Programming'")
        self.assertTrue(self.b3._id in bookIds, 
            "bookIds contains 'The Unix Programming Environment'")
        
    def test_getForeignIds_colStr(self):   
        """ Test the getForeignIds() method using a string for the collection 
        name.
        """
        bookIds = list(self.a2.getForeignIds('BookM', 'authors_ids'))
        dpr("bookIds for a2 (Dennis Ritchie): %r", bookIds)
        self.assertSame(len(bookIds), 1, 
             "Dennis Ritchie has authored 1 book in database")
        self.assertTrue(self.b1._id in bookIds, 
            "bookIds contains 'The C Progranmming Language'") 
               
    def test_getForeignDocs(self):  
        """ FKeys reverse lookup -- get documents """
        books = list(self.a3.getForeignDocs(BookM, 'authors_ids'))
        dpr("books for a3 (Rob Pike): %r", books)
        self.assertSame(len(books), 2, 
             "Rob Pike has authored 2 books in database")
        titles = ",".join(book.title for book in books)
        dpr("book titles = %r", titles)
        self.assertTrue("The Practice of Programming" in titles,
            "Books includes: The Practice of Programming")
        self.assertTrue("The Unix Programming Environment" in titles,
            "Books includes: The Unix Programming Environment")
        
    def test_getForeignDocs_no_field(self): 
        books = list(self.a3.getForeignDocs(BookM))
        dpr("books for a3 (Rob Pike): %r", books)
        self.assertSame(len(books), 2, 
             "Rob Pike has authored 2 books in database") 
        titles = ",".join(book.title for book in books)
        dpr("book titles = %r", titles)
        self.assertTrue("The Practice of Programming" in titles,
            "Books includes: The Practice of Programming")
        self.assertTrue("The Unix Programming Environment" in titles,
            "Books includes: The Unix Programming Environment")
        
     
#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_create_save_delete)
group.add(T_urls)
group.add(T_FK)
group.add(T_FKeys)

if __name__=='__main__': group.run()



#end
