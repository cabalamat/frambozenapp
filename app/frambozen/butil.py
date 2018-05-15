# butil.py = basic utilities

from typing import *
import os, os.path
import sys
import html

#---------------------------------------------------------------------

def normalizePath(p: str, *pathParts: List[str]) -> str:
    """ Normalize a file path, by expanding the user name and getting
    the absolute path.
    :param p: a path to a file or directory
    :param pathParts: optional path parts
    :return the same path, normalized
    """
    p1 = os.path.abspath(os.path.expanduser(p))
    if len(pathParts)>0:
        allPathParts = [ p1 ]
        allPathParts.extend(pathParts)
        p1 = os.path.join(*allPathParts)
    p2 = os.path.abspath(p1)
    return p2
normalisePath=normalizePath # alternate spelling
join=normalizePath # it works like os.path.join, but better

#---------------------------------------------------------------------
# formatting functions

def form(fs:str, *args, **kwargs)->str:
    """ an easier to use version of python's format(). It works the same
    except that %s is converted to {} and %r is converted to {!r}
    """
    if args or kwargs:
        fs2 = fs.replace("%s", "{}").replace("%r", "{!r}")
        r = fs2.format(*args, **kwargs)
    else:
        r = fs
    return r    

def pr(fs:str, *args, **kwargs):
    """ print to stdout """
    sys.stdout.write(form(fs, *args, **kwargs))

def prn(fs:str, *args, **kwargs):
    """ print to stdout, with \n at end """
    sys.stdout.write(form(fs, *args, **kwargs))
    sys.stdout.write("\n")


def htmlEsc(s: str) -> str:
    return html.escape(s)



#---------------------------------------------------------------------


#end
