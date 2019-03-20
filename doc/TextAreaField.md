# TextAreaField

**TextAreaField** is a [[FieldInfo]] subclass. It is similar to a [[StrField]] except that it appears as a multi-line input box instead of as single line one.

## Parameters


`desc:str` = A description of the field. This is used as a comment and is displayed as a tooltip on the field title as it appears on the page (using the HTML `title` attribute)

`title:str` = The text description that will appear against a field on a web form. This defaults to a name based on the field name in the table schema.

`default:str` = the default value that goes in the field. 

`displayInForm:bool` defaults to `True` = whether the field is to be rendered in a form built with `doc.buildForm()`  or `doc.buildFormLines()`.

`monospaced:bool` defaults to `False` = If `True`, text is show in a monospaced font.

`required:bool` = if `True`, this field cannot be empty

`rows:int` default `2` = number of rows visible in the textarea

`cols:int` default `30` = number of columns visible in the textarea

`minLength:int` = the minimum number of characters allowed, for validation.

`maxLength:int` = the maximum number of characters allowed, for validation.

`minValue` and `maxValue` = minimum and maximum values that the field can hold.

`charsAllowed:str` = a list of characters allowed in the field, for validation.
