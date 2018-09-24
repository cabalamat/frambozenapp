# testform.py = the /testForm page


from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr
from bozen import FormDoc
from bozen import StrField

prn("*** testform.py ***")

#---------------------------------------------------------------------

class TheTestForm(FormDoc):
    aaa = StrField()
    bbb = StrField()

@app.route('/testForm')
def testForm():
    theTF = TheTestForm()
    
    tem = jinjaEnv.get_template("testForm.html")
    h = tem.render(
        theTF = theTF,
    )
    return h


#---------------------------------------------------------------------




#end
