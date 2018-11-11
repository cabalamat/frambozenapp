# FieldInfo

**FieldInfo** is the abstract superclass for fields in [forms](FormDoc) and [database tables](MonDoc).

A FieldInfo has a *type* (often a Python  built-in type such as `int` or `str`). Its type is its representation in the Python FormDoc/MonDoc wihch it belongs in. It also has the same type (or JSON equivalent) when saved to a database.

A FieldInfo also has a *form element*. This is the form element it gets rendered to when its FormDoc/MonDoc is rendered as an HTML form.

## FieldInfo subclasses


Implemented in `fieldinfo.py`:

* [[StrField]] = a `str`
* [[TextAreaField]] = like StrField, but rendered in a form using the `<textarea>` control


Implemented in `numberfield.py`:

* [[IntField]] = an `int`
* [[FloatField]] = a `float`
* [[BoolField]] = a `bool`

Implemented in `keychoicefield.py`:

* [[ChoiceField]] = a `str`, being one of a series of choices
* [[FK]] = a foreign key to a MongoDB document

## Parameters

Some parameters are common to many `FieldInfo` subclasses. For each parameter we give its type after ":", where relevant.

`desc`:`str` = A description of the field. This is used as a comment and is displayed as a tooltip on the field title as it appears on the page (using the HTML `title` attribute)

`title`:`str` = The text description that will appear against a field on a web form. This defaults to a name based on the field name in the table schema.

`default` = the default value that goes in the field. The type of this depends on the type of field in question. The default value is what goes into the field in a newly created `MonDoc` record, unless over-ridden.

`displayInForm`:`bool`, defaults to `True`. There are two ways to render a Form: render the whole thing in one go with `doc.buildForm()`  or `doc.buildFormLines()`,
or render each field separately (see [[FormDoc]] for details).
If we are rendering the whole form in one go, then it only includes fields for which this parameter is `True`.
This is useful when a form is being created from a `MonDoc` and we don't want to display some fields in a form relating to the document.

`monospaced`:`bool`, defaults to `False` for most field types. If `True`, text is show in a monospaced font.

`minLength`:`int` (`StrField` and `TextAreaField`) = the minimum number of characters allowed,
for validation.

`minValue` and `maxValue` (all field types, but they only make sense for `DateField`, `DatetimeField`, `HhmmField`, `IntField`, `FloatField`) = minimum and maximum values
that the field can hold.

`maxLength`:`int` (`StrField` and `TextAreaField`) = the maximum number of characters allowed,
for validation.

`charsAllowed`:`str` (`StrField` and `TextAreaField`) = a list of characters allowed in the
field, for validation.



