# testform.py = the /testForm page


from allpages import app, jinjaEnv
from bozen.butil import pr, prn

prn("*** testform.py ***")

#---------------------------------------------------------------------

@app.route('/testForm')
def testForm():
    theTF = None
    
    tem = jinjaEnv.get_template("testForm.html")
    h = tem.render(
        theTF = theTF,
    )
    return h


#---------------------------------------------------------------------




#end
