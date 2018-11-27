# testform.py = the /testForm page

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, form, htmlEsc
from bozen import FormDoc, BzDate
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField,
    DateField)

prn("*** testform.py ***")

#---------------------------------------------------------------------

FRUIT_CHOICES = [
    ('apple', "Apple"),
    ('banana', "Banana"),
    ('orange', "Orange"),
]
SLOT_CHOICES = [
    ('slotA', "Slot A - Apple"),
    ('slotB', "Slot B - Banana"),
    ('slotC', "Slot C - Carrot"),
    ('slotD', "Slot D - Date"),
]


class TheTestForm(FormDoc):
    aaa = StrField()
    aNumber = IntField(minValue=0, maxValue=100)
    cost = FloatField(title="Cost, £",
         formatStr="{:.2f}")
    tickyBox = BoolField()
    favouriteFruit = ChoiceField(choices=FRUIT_CHOICES,
        showNull=True, allowNull=False)
    slots = MultiChoiceField(choices=SLOT_CHOICES)
    note = TextAreaField()
    dateOfBirth = DateField()

@app.route('/testForm', methods=['POST', 'GET'])
def testForm():
    dpr("- - - in testForm() - - -")
    theTF = TheTestForm()
    theTF.dateOfBirth = BzDate.today()
    dpr("theTF=%r", theTF)
    resultTable = ""
    
    dpr("request=%r", request)
    if request.method=='POST':     
        theTF = theTF.populateFromRequest(request)
        theTF.copyOfAaa = theTF.aaa
        if theTF.isValid():
            resultTable = getResultTable(theTF)
    #//if    
    
    tem = jinjaEnv.get_template("testForm.html")
    h = tem.render(
        theTF = theTF,
        resultTable = resultTable,
    )
    return h


def getResultTable(th: TheTestForm)->str:
    """ return an html table with the contents of (tf) """
    h = """<table class='bz-report-table'>
<tr>
    <th>Field Name</th>
    <th>Type</th>
    <th>Screen Value</th>
    <th>Database Value (repr)</th>
    <th>Value Type</th>
<tr>
"""    
    for fn in th.fieldNames():
        fi = th.getFieldInfo(fn)
        cn = fi.__class__.__name__
        v = th[fn]
        h += form("""<tr>
    <td>{fn}</td>       
    <td><tt>{type}</tt></td>
    <td>{s}</td>      
    <td><code>{r}</code></td>   
    <td><tt>{vt}</tt></td>            
<tr>""",   
            fn = fn,
            type = cn,
            s = th.asReadableH(fn),
            r = htmlEsc(repr(v)),
            vt = htmlEsc(v.__class__.__name__),
        )
    #//for    
    h += "</table>"
    return h

#---------------------------------------------------------------------




#end
