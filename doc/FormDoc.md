# FormDoc

**FormDoc** is a class representing an HTML form. it contains methods to render the HTML for the form and validate the form from an http POST request.

[TOC]

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

`hasFieldInfo(fieldName:str)->bool` returns whether `fieldName` has a FieldInfo (i.e. is a field)

`fieldNames()->List[str]` returns a list of the field names, in the order they were defined

### Functions on fields

`asReadable(fn:str)->str` returns a string giving a human-readable display value for the contents of the field whose field name is `fn`.

`asReadableH(fn:str)->str` is like `asReadable()` except it returns an HTML-escaped string. 


## Rendering html forms

There are lots of ways to do this. Going from high-level to low-level:

### A whole form

To generate HTML for the form:

    doc.buildForm()

This includes the `name`, `height`, `dob` and `job_id` fields, in that order. 
It includes the enclosing `<table class='bz-form-table'> ... </table>` tags, but not the `<form>`. 

#### A form without an enclosing `<table>` element

You can also use:

    doc.buildFormLines()

This is the same as `doc.buildForm()` except that it doesn't include the `<table>` tags.

### A line in a form

To generate HTML for one line:

    doc.formLine('height')

Inside an HTML template, the `formLine()` method might be used like this:
```
<table class='form-table'>
    {{doc.formLine('height')}}
    {{doc.formLine('width')}}
    {{doc.formLine('mass', readOnly=True)}}
</table>
```

## See also

* [[MonDoc]] is a subclass of `FormDoc` which is associated with a MongoDB collection
* Fields in a `FormDoc` are defined using a [[FieldInfo]] subclass.
* [[Validating forms]]

