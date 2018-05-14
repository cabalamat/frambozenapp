# butil.py = basic utilities

from typing import *
import os, os.path
import sys

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
    """ an easier to use version of python's format """
    if args or kwargs:
        r = fs.format(*args, **kwargs)
    else:
        r = fs
    return r    

def pr(fs:str, *args, **kwargs):
    """ print to stdout """
    sys.stdout.write(form(fs, *args, **kwargs))

def prn(fs:str, *args, **kwargs):
    """ print to stdout, with \n at end """
    pr(fs+"\n", *args, **kwargs)


#---------------------------------------------------------------------


#end
