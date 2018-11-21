# FormDoc

**FormDoc** is a class representing an HTML form. it contains methods to render the HTML for the form and validate the form from an http POST request.

## Example

```py
class MyForm(FormDoc):
    name = StrField()
    height = IntField(desc="height to nearest inch",
        title="Height, inches")
    dob = DateField(title="Date of Birth")
```

## Functions

### Misc utility functions

`getFieldInfo(fn:str)->FieldInfo` given a field name, gets the [[FieldInfo]] instance (this contains information about the type of the field)

