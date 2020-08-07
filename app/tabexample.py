# tabexample.py = example showing tabs


from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, form, htmlEsc
from bozen import FormDoc, BzDate
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField,
    DateField)

import tabs

#---------------------------------------------------------------------

TABEX_TABS = [
    ('sea', "<i class='fa fa-ship'></i> Sea"),
    ('car', "<i class='fa fa-car'></i> Car"),
    ('bicycle', "<i class='fa fa-bicycle'></i> Bicycle"),
    ('air', "<i class='fa fa-plane'></i> Air"),
]

def tabexTabLine(tab: str) -> str:
    """ Return HTML for the current tab line
    @return::str containing html
    """
    h = tabs.makeTabLine(TABEX_TABS, tab, "/tabex/{TAB}")
    return h

@app.route('/tabex/<tabId>')
def tabex(tabId):
    
    tem = jinjaEnv.get_template("tabex.html")
    h = tem.render(
        tabLine = tabexTabLine(tabId),
        tabId = tabId,
    )
    return h

#---------------------------------------------------------------------



#end
