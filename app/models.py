# models.py = database initilisation for frambozenapp


import bozen
from bozen.butil import *
from bozen import FormDoc, MonDoc
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField, FK, FKeys,
    DateField, DateTimeField)

import config
bozen.setDefaultDatabase(config.DB_NAME)
import allpages
bozen.notifyFlaskForAutopages(allpages.app, allpages.jinjaEnv)

#---------------------------------------------------------------------
# ...MongoDB collection classes defined here...

class Author(MonDoc):
    name = StrField()
    notes = TextAreaField()
    dateOfBirth = DateField()
    
    @classmethod
    def classLogo(cls):
        return "<i class='fa fa-pencil'></i> "
    
    def myBooks(self) -> Iterable['Book']:
        """ return this author's books """
        return self.getForeignDocs('Book')
    
    def myBooksLinks(self) -> str:
        """ return html giving a list of this author's books,
        with each book being a hyperlink to it.
        I.e. return HTML containing a series of <a href> elements,
        each containing the name of a book and a link to it.
        """
        return ", ".join(bk.a() for bk in self.myBooks())

Author.autopages()

class Book(MonDoc):
    title = StrField()
    yearPublished = IntField()
    authors_ids = FKeys(Author, title="Authors")
    
    @classmethod
    def classLogo(cls):
        return "<i class='fa fa-book'></i> "
    
Book.autopages()


#---------------------------------------------------------------------
# admin site

def createAdminSite():
    """ create admin site """
    import foo
    adminSite = bozen.AdminSite(stub=config.ADMIN_SITE_PREFIX)
    adminSite.runFlask(allpages.app, allpages.jinjaEnv)

if config.CREATE_ADMIN_SITE:
    createAdminSite()

#---------------------------------------------------------------------


#end

