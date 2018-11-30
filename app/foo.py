# foo.py = Foo

"""
Foo is a collection class to test frambozenapp. It will
have a field of each type.

The web pages /foos and /foo/{fooId} are defined.
"""

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, form, htmlEsc
from bozen import FormDoc, MonDoc, BzDate
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField,
    DateField)

import ht

#---------------------------------------------------------------------

DRINK_CHOICES = [
    ('beer', "Beer"),    
    ('beer-lager', "Lager"),   
    ('beer-frambozen', "Frambozen"), 
    ('wine', "Wine"),         
    ('spirits-whisky', "Whisky"),   
    ('spirits-gin', "Gin"), 
] 
FRUIT_CHOICES = [
    ('apple', "Apple"),
    ('banana', "Banana"),
    ('strawberry', "Strawberry"),
    ('raspberry', "Raspberry"),
]   

class Foo(MonDoc):
    name = StrField()
    aNumber = IntField(minValue=0, maxValue=100)
    favouriteDrink = ChoiceField(choices=DRINK_CHOICES,
        showNull=True, allowNull=True)
    fruitsLiked = MultiChoiceField(choices=FRUIT_CHOICES,
        desc="tick all fruits this person likes") 
    tickyBox = BoolField()
    dateOfBirth = DateField()
    dateOfDeath = DateField()
    
    def logo(self):
        """ use different logs depending on whether alive/dead """
        if self.dateOfDeath:
            return "<i class='fa fa-star-o'></i> "
        else:
            return "<i class='fa fa-star'></i> "
        
    def formWideErrorMessage(self):
        if self.dateOfBirth and self.dateOfDeath:
            if self.dateOfDeath < self.dateOfBirth:
                return "Date Of Death cannot be before Date Of Birth"
        
        return "" # no error message, validates OK

#---------------------------------------------------------------------

@app.route('/foos')
def foos():
    count = Foo.count()
    tem = jinjaEnv.get_template("foos.html")
    h = tem.render(
        count = count,
        table = foosTable(),
    )
    return h

def foosTable() -> str:
    """ a table of foos """
    h = """<table class='bz-report-table'>
<tr>
    <th>Name</th>
    <th>Favourite<br>Drink</th>
    <th>Ticky Box</th>
    <th>Date of<br>Birth</th>
    <th>Date of<br>Death</th>
</tr>    
    """
    fs = Foo.find(sort='name')
    for f in fs:
        h += form("""<tr>
     <td>{name}</td>       
     <td>{favouriteDrink}</td>       
     <td>{tickyBox}</td>       
     <td>{dateOfBirth}</td>       
     <td>{dateOfDeath}</td>                
</tr>""",
            name = f.a(),
            favouriteDrink = f.asReadableH('favouriteDrink'),
            tickyBox = f.asReadableH('tickyBox'),
            dateOfBirth = f.asReadableH('dateOfBirth'),
            dateOfDeath = f.asReadableH('dateOfDeath'),
        )     
    #//for f
    h += "</table>"
    return h
    
    
#---------------------------------------------------------------------
  
@app.route('/foo/<id>', methods=['POST', 'GET'])
def foo(id):
    if id=='NEW':
        doc = Foo()
    else:    
        doc = Foo.getDoc(id)
    msg = ""    
    
    if request.method=='POST':
        doc = doc.populateFromRequest(request)
        if request.form.get('delete', "0") == "1":
            # delete the foo
            doc.delete()
            return redirect("/foos", code=302)
        else:
            if doc.isValid():
                doc.save()
                msg = "Saved document"
            #//if    
    #//if    
        
    tem = jinjaEnv.get_template("foo.html")
    h = tem.render(
        doc = doc,
        id = id,
        msg = ht.goodMessageBox(msg),
    )
    return h
    
    
    
#---------------------------------------------------------------------


#end
