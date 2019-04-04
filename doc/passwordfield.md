# PasswordField

**PasswordField** is a [[FieldInfo]] subclass. Its data type is a `str`. It behaves like a [[StrField]], except the characters entered aren't displayed. This is for security purposes. 

## Parameters

`desc:str` = A description of the field. This is used as a comment and is displayed as a tooltip on the field title as it appears on the page (using the HTML `title` attribute)

`title:str` = The text description that will appear against a field on a web form. This defaults to a name based on the field name in the table schema.

`default:str` = the default value that goes in the field. 

`autocomplete:bool`, defaults to `True` = whether to allow auto-completion for this field

`displayInForm:bool` defaults to `True` = whether the field is to be rendered in a form built with `doc.buildForm()`  or `doc.buildFormLines()`.

`monospaced:bool`, defaults to `False` for most field types. If `True`, text is show in a monospaced font.

`required:bool` = if `True`, this field cannot be empty

`fieldLen:int` default `20` = the length of the field in the HTML form (**NB:** this has no bearing on how long the data in the field can be)

`minLength:int` = the minimum number of characters allowed, for validation.

`maxLength:int` = the maximum number of characters allowed, for validation.

`minValue` and `maxValue` = minimum and maximum values that the field can hold.

`charsAllowed:str` = a list of characters allowed in the field, for validation.
