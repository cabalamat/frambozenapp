# foo.py = Foo

"""
Foo is a collection class to test frambozenapp. It will
have a field of each type.

The web pages /foos and /foo/{fooId} are defined.
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
    description = TextAreaField(monospaced=True)
    aNumber = IntField(minValue=0, maxValue=100)
    minSpeed = FloatField(title="Minimum Speed, mph", minValue=0.0)
    maxSpeed = FloatField(title="Maximim Speed, mph", minValue=0.0)
    favouriteDrink = ChoiceField(choices=DRINK_CHOICES,
        showNull=True, allowNull=True)
    fruitsLiked = MultiChoiceField(choices=FRUIT_CHOICES,
        desc="tick all fruits this person likes") 
    tickyBox = BoolField()
    aDate = DateField()
    lastSaved = DateTimeField(desc="when this foo was last saved",
        readOnly=True)
    aDateTime = DateTimeField(title="A Date and Time")
    anything = ObjectField(desc="can contain anything",
        default=["any", "thing"])
    favouriteBook = FK(models.Book, allowNull=True, showNull=True)
   
    @classmethod
    def classLogo(self):
        return "<i class='fa fa-star-o'></i> "
        
    def formWideErrorMessage(self):
        if self.minSpeed > self.maxSpeed:
            return "Minimum speed cannot be greater than maximum speed"       
        return "" # no error message, validates OK
    
    def preSave(self):
        self.lastSaved = BzDateTime.now()
        d = self.mongoDict()
        d.pop('anything', "") # remove the anything field
        dpr("d=%r", d)
        self.anything = d
        

#---------------------------------------------------------------------

@app.route('/foos')
def foos():
    count = Foo.count()
    pag = paginate.Paginator(count)
    tem = jinjaEnv.get_template("foos.html")
    h = tem.render(
        count = count,
        pag = pag,
        table = foosTable(pag),
    )
    return h

def foosTable(pag: paginate.Paginator) -> str:
    """ a table of foos """
    h = """<table class='bz-report-table'>
<tr>
    <th>Id</th>
    <th>Name</th>
    <th>Description</th>
    <th>Favourite<br>Drink</th>
    <th>Fruits<br>Liked</th>
    <th>Ticky<br>Box</th>
</tr>    
    """
    fs = Foo.find(
        skip=pag.skip, # skip this number of docs before returning some
        limit=pag.numShow, # max number of docs to return
        sort='name')
    for f in fs:
        h += form("""<tr>
     <td style='background:#fed'><tt>{id}</tt></td>      
     <td>{name}</td>       
     <td>{description}</td>       
     <td>{favouriteDrink}</td>    
     <td>{fruitsLiked}</td>       
     <td>{tickyBox}</td>                  
</tr>""",
            id = htmlEsc(f.id()),
            name = f.a(),
            description = f.asReadableH('description'),
            favouriteDrink = f.asReadableH('favouriteDrink'),
            fruitsLiked = f.asReadableH('fruitsLiked'),
            tickyBox = f.asReadableH('tickyBox'),
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
