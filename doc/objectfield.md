# ObjectField

**ObjectField** is a [[FieldInfo]] subclass.

This can contain any JSON value in the Database and the equivalent in Python. It is read-only.

## Parameters

`desc:str` = A description of the field. This is used as a comment and is displayed as a tooltip on the field title as it appears on the page (using the HTML `title` attribute)

`title:str` = The text description that will appear against a field on a web form. This defaults to a name based on the field name in the table schema.

`default:str` = the default value that goes in the field. 

`displayInForm:bool` = whether the field is to be rendered in a form built with `doc.buildForm()`  or `doc.buildFormLines()`.

`monospaced:bool`, defaults to `True`. If `True`, text is shown in a monospaced font.
