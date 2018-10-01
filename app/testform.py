# testform.py = the /testForm page

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr
from bozen import FormDoc
from bozen import StrField, ChoiceField

prn("*** testform.py ***")

#---------------------------------------------------------------------

class TheTestForm(FormDoc):
    aaa = StrField()
    bbb = StrField()
    favouriteFruit = ChoiceField(choices=("Apple", "Banana", "Orange"))

@app.route('/testForm', methods=['POST', 'GET'])
def testForm():
    dpr("- - - in testForm() - - -")
    theTF = TheTestForm()
    dpr("theTF=%r", theTF)
    resultTable = ""
    
    dpr("request=%r", request)
    if request.method=='POST':      
        theTF = theTF.populateFromRequest(request)
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
    

#---------------------------------------------------------------------




#end
