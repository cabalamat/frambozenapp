# DateField

**DateField** is a [[FieldInfo]] subclass.

## In a form

## Storage

In the database, a `DateField` is stored as a string in a format like *yyyy-mm-dd*. e.g. `"2017-12-31"`. If there is no value, it is stored as the empty string (`""`).

As a Python object, the contents of a `DateField` are stored as a [[BzDate]]. This is a subclass of `str` with extra methods for date related functions. 
*See [[BzDate]] for details.*


## Parameters

`desc:str` = A description of the field. This is used as a comment and is displayed as a tooltip on the field title as it appears on the page (using the HTML `title` attribute)

`title:str` = The text description that will appear against a field on a web form. This defaults to a name based on the field name in the table schema.

`default:Union[str,BzDate]` = the default value that goes in the field. 

`displayInForm:bool` = whether the field is to be rendered in a form built with `doc.buildForm()`  or `doc.buildFormLines()`

`required:bool` = if `True`, this field cannot be empty

`dateFormat:str` = the format the date will be rendered as in a form and in the `doc.asReadble(fn)` and `doc.asReadableH(fn)` methods (in [[FormDoc]])
The format string uses the notation in the [strftime()](https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior) method 
in the Python standard library.
