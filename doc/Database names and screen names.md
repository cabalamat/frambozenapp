# Database names and screen names

In Bozen, a **database name** is what something is called in the database, and a **screen name** is the name of the same thing as it is displayed on the screen.

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

In the above example, the collection class is `"DeptNumber"`, the collection name in the database is `"deptNumber"`, 
and the collection's automatically produced screen name is "Dept Number".

