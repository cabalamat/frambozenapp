# models.py = database initilisation for frambozenapp


import bozen
from bozen.butil import *
from bozen import FormDoc, MonDoc
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField,
    DateField)

bozen.setDefaultDatabase('frambozenapp')

#---------------------------------------------------------------------
# ...MongoDB collection classes defined here...


#---------------------------------------------------------------------


#end

