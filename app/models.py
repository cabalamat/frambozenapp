# models.py = database initilisation for frambozenapp


import bozen
from bozen.butil import *
from bozen import FormDoc, MonDoc
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField, FK, FKeys,
    DateField, DateTimeField)

bozen.setDefaultDatabase('frambozenapp')
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

Author.autopages()

class Book(MonDoc):
    title = StrField()
    yearPublished = IntField()
    authors_ids = FKeys(Author)
    
    @classmethod
    def classLogo(cls):
        return "<i class='fa fa-book'></i> "
    
Book.autopages()


#---------------------------------------------------------------------


#end

