# front.py = front page

from allpages import app, jinjaEnv
from bozen.butil import pr, prn

import config

prn("*** front.py ***")

#---------------------------------------------------------------------

@app.route('/')
def front():
    tem = jinjaEnv.get_template("front.html")
    h = tem.render(
        adminSiteExists = config.CREATE_ADMIN_SITE
    )
    return h


# end
