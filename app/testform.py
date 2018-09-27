# testform.py = the /testForm page


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

@app.route('/testForm')
def testForm():
    dpr("- - - in testForm() - - -")
    theTF = TheTestForm()
    dpr("theTF=%r", theTF)
    
    tem = jinjaEnv.get_template("testForm.html")
    h = tem.render(
        theTF = theTF,
    )
    return h


#---------------------------------------------------------------------




#end
