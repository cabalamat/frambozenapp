# HISTORY.md

This is the HISTORY file for frambozenapp.

New entries go at the end.

## 2018-Sep-12

Subgoal is to write a simple version of FormDoc with two field types,
StrField and IntField.

Created /testForm page

Wrote stub of formdoc, fieldinfo, test_fieldinfo pages.

Next steps: write some tests in test_fieldinfo, write the StrField
class to implement the tests.

## 2018-Oct-28

Currently 23 assertions in 8 test functions

Next steps: MonDoc functions for loading documents (`getDoc()`)
and acting on groups of documents (`find()`, `find_one()` etc). --DONE

Deleting documents.  --DONE

Adding a(), url() etc functions  --DONE

## 2018-Nov-11 

Currently 52 assertions in 16 test functions

3286 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-12

Passed 59 assertions in 17 test functions
3342 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-13

Add NullDoc (for when FK cannot be dereferenced)
Passed 70 assertions in 19 test functions
3447 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-14

Add MultiChoiceField
3546 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-17

Working on FKeys
Passed 83 assertions in 22 test functions
3808 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-17

FKeys reverse lookups
Passed 91 assertions in 24 test functions
3864 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-21

Tidy up FKeys/FK
Passed 99 assertions in 28 test functions
3955 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-24

Doing BzDate, BzDateTime, DateField, etc...
Passed 123 assertions in 37 test functions
4126 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-29

BzDate date picker working, misc tidying up and documentation
Passed 130 assertions in 38 test functions 
4351 lines of Python (from `wc *.py */*.py`)

Started Foo class, associated /foos, /foo pages
4591 lines of Python (from `wc *.py */*.py`)

## 2018-Nov-30

Done /foos, /foo pages
4603 lines of Python (from `wc *.py */*.py`)

## 2018-Dec-01

Working on BzDateTime...
Passed 144 assertions in 42 test functions
4792 lines of Python (from `wc *.py */*.py`)

Passed 170 assertions in 48 test functions
4926 lines of Python (from `wc *.py */*.py`)


## 2018-Dec-02

Finished BzDateTime
Passed 182 assertions in 49 test functions
4944 lines of Python (from `wc *.py */*.py`)

Done DateTimeField.
5064 lines of Python (from `wc *.py */*.py`)

Added <paginate.py>, paginating /foos
Added autopages
5501 lines of Python (from `wc *.py */*.py`)

## 2018-Dec-05

Issues with FKeys not updating from form POST request...
fixed
5542 lines of Python (from `wc *.py */*.py`)
1468 lines of documentation (`wc ../doc/*.md`)











