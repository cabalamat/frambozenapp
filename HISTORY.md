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
