# login.py = pages for logging in and users 

"""
Contains pages:

  / = for logging in
  /logout = log out the current user
  /users = show all users
  /user = show a user's data

See also <userdb.py> which contains the database model for users.

"""

import time
import string

from flask import request, redirect, abort
from flask.ext.login import login_user, logout_user, current_user
import pymongo

from monfab.debugdec import printargs, prvars, pr
import monfab
from monfab import (MonDoc, FormDoc,
    ObjectField, StrField, TextAreaField,
    PostcodeField, EmailField,
    ChoiceField, FK, FKeys, MultiChoiceField,
    DateField, DateTimeField, HhmmField,
    IntField, FloatField, BoolField,
    FileField, ImageField)

import allpages
from allpages import *
from permission import *

import userdb
import models


#---------------------------------------------------------------------
# Front page (/)

# page to go to, on login, if the user is an engineer
ENG_ON_LOGIN_PAGE = "/startday"

class LoginForm(monfab.FormDoc):
    userName = monfab.StrField()
    password = monfab.PasswordField()


@app.route('/', methods=['POST', 'GET'])
def front():
    frontPageTem = jinjaEnv.get_template("front_page.html")
    doc = LoginForm()
    msg = ""

    if request.method=='POST':

        #>>>>> CSRF handling
        pr("@@@ session=%r @@@", session)
        token = session.pop('_csrf_token', None)
        pr("@@@ token=%r @@@", token)
        #if not token or token != request.form.get('_csrf_token'):
        #    pass
        #    #abort(403)

        #d = monfab.toDict(request.form)
        #doc = doc.populateFromForm(d)
        doc = doc.populateFromRequest(request)
        u = userdb.User.find_one({'userName': doc.userName})

        ok = u and userdb.verifyPassword(u.hashedPassword,
                                         doc.password)
        pr("doc.password=%r ok=%r", doc.password, ok)
        #notifyLoginAttempt(doc, ok)
        if ok:
            login_user(u)
            eng = models.Engineer.getDoc(doc.userName)
            if eng:
                # user is an engineer
                return redirect(ENG_ON_LOGIN_PAGE)
        else:
            msg = ("<p><span style='color:#800; background:#fee;'>"
                   "<i class='fa fa-times-circle'></i> "
                   "login failed</span></p>")

    canAutocomplete = ("Linux" in platform.platform())
    autocomplete = ("autocomplete=on" if canAutocomplete
                    else "autocomplete=off")
    h = frontPageTem.render(
        doc = doc,
        msg = msg,
        autocomplete = autocomplete,
    )
    return h



#---------------------------------------------------------------------

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")

#---------------------------------------------------------------------

@app.route('/users')
@needPerm('userPages')
def users():
    tem = jinjaEnv.get_template("users.html")
    h = tem.render(
        table = usersTable(),
        count = userdb.User.count(),
    )
    return h

def usersTable():
    """ returns an html table of users """
    h = """<table class='report_table'>
<tr>
   <th class=debug>(id)</th>
   <th>User name</th>
   <th>Email</th>
</tr>
"""
    for doc in userdb.User.find(sort=[('userName',pymongo.ASCENDING)]):

        item = form("""<tr>
<td class="debug unemphasized">{id}</td>
<td><a href="/user/{id}">{userName}</a></td>
<td>{email}</td>
</tr>""",
            id = doc.id(),
            userName = doc.asReadableH('userName'),
            email = doc.asReadableH('email'),
        )
        h += item
    #//for
    h += "</table>\n"
    return h

def yn(b):
    if b:
        return "Yes"
    else:
        return "No"

def orNone(s):
    if s:
        return htmlEsc(s)
    else:
        return "<span class='unemphasized'>None</span>"

#---------------------------------------------------------------------


@app.route('/user/<id>', methods=['POST', 'GET'])
@needPerm('userPages')
def user(id):
    if id=='NEW':
        doc = userdb.User()
        prvars("doc")
    else:
        doc = userdb.User.getDoc(id)
        prvars("doc")
    msg = ""

    if request.method=='POST' and canEd:
        doc = doc.populateFromRequest(request)
        if doc.isValid():
            if request.form['delete']=="1":
                doc.delete()
                msg = "Deleted user"
            else:    
                doc.save()
                msg = "Saved user"
    #//if

    tem = jinjaEnv.get_template("user.html")
    h = tem.render(
        doc = doc,
        id = htmlEsc(id),
        msg = ht.goodMessageBox(msg),
    )
    return h


#---------------------------------------------------------------------


#end