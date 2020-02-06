# filex.py = File Example

"""
Filex is an example that allows users to upload/download files.

The web pages /fileExamples and /fileExample/{id} are defined.
"""

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, form, htmlEsc
from bozen import FormDoc, MonDoc, BzDate, BzDateTime
from bozen import paginate
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField, ObjectField, FK,
    DateField, DateTimeField)

import ht
import models

#---------------------------------------------------------------------

class FileExample(MonDoc):
    name = StrField()
    description = TextAreaField()
    timestamp = DateTimeField(desc="when this filex was last altered",
        readOnly=True)
   
    @classmethod
    def classLogo(self):
        return "<i class='fa fa-file'></i> "
        
    def preSave(self):
        self.timestamp = BzDateTime.now()
  
FileExample.autopages()  
  
#---------------------------------------------------------------------
