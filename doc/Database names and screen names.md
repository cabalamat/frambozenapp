# Database names and screen names

In Bozen, a **database name** is what something is called in the database, and a **screen name** is the name of the same thing as it is displayed on the screen.

[TOC]

## Database name versus screen name of fields

For example, consider this [[MonDoc]] subclass `DeptNumber`:
```py
class DeptNumber(MonDoc):
    phoneNumber = StrField(
        required=True)
    dept = StrField(title="Department",
        required=True)
    notes = TextAreaField()
```

The first field has a database name of `"phoneNumber"`, and its corresponding screen name of "Phone Number" is automatically generated from this. 

The second field's database name is `"dept"`, and its screen name is defined as "Department". Note that **title** means the same as screen name. 

## Collection classes have screen names too

In the above example, the collection class (in Python) is `DeptNumber`, the collection name in the database is also `DeptNumber`, 
and the collection's automatically produced screen name is "Dept Number".

## Database format versus screen format

A related concept is how data is stored in the database (the **datebase format**) versus how it appears on the screen (the **screen format**). 

### ChoiceField

Choices are given as database format first, then screen format. For example, if we have:
```py
FRUIT_CHOICES = [
    ('apple', "An Apple"),
    ('banana', "A Banana"),
    ('orange', "An Orange"),
]
class MyForm(FormDoc):
    favouriteFruit = ChoiceField(choices=FRUIT_CHOICES)
```

Then if ther value in the database is `'apple'`, that value would appear as "An Apple" on the screen.

### DateField

A date is stored like `"2017-12-31"` in the database. when it appears on the screen the format looks like "2017-Dec-31". See [[DateField]].


