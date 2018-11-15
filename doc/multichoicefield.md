# MultiChoiceField

**MultiChoiceField** is a [[FieldInfo]] subclass.

In Python, the field's datatype is `List[str]`; the JSON equivalent in the database is an array of strings.

In a form it appears as a list of tick boxes; the user can tick as many or as few as they like.

## Example

```py
SLOT_CHOICES = [
    ('slotA', "Slot A - Apple"),
    ('slotB', "Slot B - Banana"),
    ('slotC', "Slot C - Carrot"),
    ('slotD', "Slot D - Date"),
]
class MyForm(FormDoc):
    slots = MultiChoiceField(choices=SLOT_CHOICES)
```

## Parameters

`choices:List[Tuple[str,str]]` **compulsory** = the choices in the tick boxes. For each tuple, the database value is defined followed by the display value.

`desc:str` = A description of the field. This is used as a comment and is displayed as a tooltip on the field title as it appears on the page (using the HTML `title` attribute)

`title:str` = The text description that will appear against a field on a web form. This defaults to a name based on the field name in the table schema.

`default:List[str]` = the default value that goes in the field. 

`displayInForm:bool` = whether the field is to be rendered in a form built with `doc.buildForm()`  or `doc.buildFormLines()`.
