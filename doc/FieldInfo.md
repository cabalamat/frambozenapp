# FieldInfo

A **FieldIno** is an object containing containing a record of the nature of a field in a [[FormDoc]] or [[MonDoc]].

A FieldInfo has a *type* (often a Python  built-in type such as `int` or `str`). Its type is its representation in the Python FormDoc/MonDoc wihch it belongs in. It also has the same type (or JSON equivalent) when saved to a database.

A FieldInfo also has a *form element*. This is the form element it gets rendered to when its FormDoc/MonDoc is rendered as an HTML form.

## FieldInfo subclasses


Implemented in `fieldinfo.py`:

* [[StrField]] = a `str`
* [[TextAreaField]] = like StrField, but rendered in a form using the `<textarea>` control


Implemented in `numberfield.py`

* [[IntField]] = an `int`
* [[FloatField]] = a `float`
* [[BoolField]] = a `bool`



