# Issue with Python 3 packaging

Packaging in Python 3 works differently than in Python 2. In particular if you have a package that contains a module you want to run as a script, you can't easily do this in Python 3 (unlike in Python 2).

For now I am fixing the problem by putting the test_... files for bozen in the `app/` directory.

I wrote the repository `~/sproj/p3pack/` to explore this issue. What follows is its README.md file.

# README.md for p3pack

**p3pack** is a short Python program to demonstrate differences in how Python 2 
and Python 3 handle packages.

## Summary

I want to write a Python package and be able to run scripts inside the 
package directly.

I am writing a library as a Python package (in `p3pack/mymodule/`) which 
will be called by my main program (in `p3pack/`). 

The library also contains test scripts which I want to run, using the
test script module (`modb.py`) as the entry point. I can do this in Python 2.7
but not in Python 3.6.

## Structure of application

Here I am using Python 2.7.6 and 3.6.5 to illustrate the difference.

In these tests I have installed `p3pack/` under `~/sproj/`.

    p3pack/
        top.py
        mymodule/
            __init__.py    # this is empty
            moda.py
            modb.py
            
Let's say that `top.py` is the entry point of my main program. 

I have a library in `mymodule/` which is called by `top.py`. Inside `mymodule/`
I also have test code in `modb.py` which tests `moda.py`, so I want to run
`modb.py` as the entry point of my program when testing and debugging the 
library.

This works in Python 2 but not in Python 3.

## Running in Python 2.7

(We don't need to create a virtual environment because Python 2.7 is the 
default python on this system).

Run `p3pack/mymodule/modb.py`:

    ~/sproj/p3pack$ cd mymodule/
    ~/sproj/p3pack/mymodule$ python modb.py
    ----- testing moda.py -----
    Result=124, should be 124
    
This demonstrates that I can run with modb.py as the main module.

Run `p3pack/top.py`:

    ~/sproj/p3pack/mymodule$ cd ..
    ~/sproj/p3pack$ python top.py
    === top.py ===
    result is 17
    r2 is 21

And I can also run with top.py as the main module. This is what I want to
be able to do.

## Running in Python 3.6

Create a a python 3 virtual environment

    ~/sproj/p3pack$ python3 -m venv v3
    ~/sproj/p3pack$ . v3/bin/activate

    
Now run `p3pack/mymodule/modb.py`:


    (v3) ~/sproj/p3pack$ cd mymodule/
    (v3) ~/sproj/p3pack/mymodule$ python modb.py
    ----- testing moda.py -----
    Result=124, should be 124


Run `p3pack/top.py`:

    (v3) ~/sproj/p3pack/mymodule$ cd ..
    (v3) ~/sproj/p3pack$ python top.py
    Traceback (most recent call last):
      File "top.py", line 3, in <module>
        from mymodule import moda, modb
      File "/home/phil/sproj/p3pack/mymodule/modb.py", line 3, in <module>
        import moda
    ModuleNotFoundError: No module named 'moda'

And this is where Python 3 goes wrong. It doesn't let me run `modb.py` both as
the entry point, and also as a module within the package `mymodule`.

I can get it to work by changing line 3 of `modb.py` to:

    from . import moda
    
I get this (correct) output):

    (v3) ~/sproj/p3pack$ python top.py
    === top.py ===
    result is 17

But then, when I try to run with modb.py as the entry point, it falls over:

    (v3) ~/sproj/p3pack$ cd mymodule/
    (v3) ~/sproj/p3pack/mymodule$ python modb.py
    Traceback (most recent call last):
      File "modb.py", line 3, in <module>
        from . import moda
    ImportError: cannot import name 'moda'
 
Now obviously I could get round this my putting all my test scripts in
the top-level directory `p3pack/`. Is this how it is indended to do this in 
Python 3?
    
## Stack Overflow    
    
See this question:

<https://stackoverflow.com/questions/16981921/relative-imports-in-python-3/16985066>
    
    
    
    
    
    
    
    
    
    
    
    
