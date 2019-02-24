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
    toggleSwitch1 = BoolField(widget='toggleSwitch')
    toggleSwitch2 = BoolField(widget='toggleSwitch')
    showBody = BoolField(widget='toggleSwitch')
    order = BoolField(widget='toggleSwitch',
        showTitle = False,
        onText = "Oldest First",
        offText = "Newest First")
    favouriteFruit = ChoiceField(choices=FRUIT_CHOICES,
        showNull=True, allowNull=False)
    slots = MultiChoiceField(choices=SLOT_CHOICES, required=True)
    note = TextAreaField()
    dateOfBirth = DateField(required=True)

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
    <th colspan=3>Field</th>
    <th colspan=3>Value</th>
</tr>
<tr>
    <th>Py Name</th>
    <th>Screen Name</th>
    <th>Type</th>
    <th>Py Value</th>
    <th>Screen Value</th>
    <th>Type</th>
</tr>
"""    
    for fn in th.fieldNames():
        fi = th.getFieldInfo(fn)
        cn = fi.__class__.__name__
        v = th[fn]
        h += form("""<tr>
    <td><code>{fn}</code></td>
    <td><b>{screenName}</b></td>
    <td><tt>{type}</tt></td>
    <td><code>{r}</code></td>
    <td>{s}</td>
    <td><tt>{vt}</tt></td> 
<tr>""",   
            screenName = fi.title,
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
