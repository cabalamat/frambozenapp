# allpages.py = stuff relevant to all pages

import os.path
import collections
import cgi

import config

from flask import Flask, request, session
app = Flask(__name__)
app.config["SECRET_KEY"] = "don't tell anyone"
app.config["SESSION_COOKIE_NAME"] = "session_%d" % (config.PORT,)

from monfab import debugdec, butil, termcolours
from monfab.debugdec import printargs, prvars, pr

#---------------------------------------------------------------------
# jinja2 environment

import jinja2
from jinja2 import Template

jinjaEnv = jinja2.Environment()
thisDir = os.path.dirname(os.path.realpath(__file__))
templateDir = butil.join(thisDir, "templates")
jinjaEnv.loader = jinja2.FileSystemLoader(templateDir)


#---------------------------------------------------------------------

#end
