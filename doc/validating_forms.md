# Validating Forms

[TOC]

To populate a form with data from a POST request, in Flask (This is a simplified version of the `foo()` view function in [[frambozenapp]]'s `foo.py`):

```py  
@app.route('/foo/<id>', methods=['POST', 'GET'])
def foo(id):
    doc = Foo.getDoc(id)
    msg = ""     
    if request.method=='POST':
        doc = doc.populateFromRequest(request)
        if doc.isValid():
            doc.save()
            msg = "Saved document"     
    tem = jinjaEnv.get_template("foo.html")
    h = tem.render(
        doc = doc,
        id = id,
        msg = ht.goodMessageBox(msg),
    )
    return h
```

Here the form is produced by the `MonDoc` subclass `Van`.

The `populateFromForm()` method doesn't alter its receiver, instead it creates a new object of the same class with the form data. If `doc` is a `FormDoc` you
would typically write:

    doc = doc.populateFromForm(d)

Because you only care about the data in the form. But if `doc` is a `MonDoc`, you might instead write:

    newDoc = doc.populateFromForm(d)

Then you would have both the old value (`doc`) and the new value (`newDoc`).

## Validation

The data in this new object can be validated with:
```py
doc.isValid()
```

whch returns a `bool`.

This works by calling:

* `FieldInfo.errorMsg()` for each field in the form. This returns `""` if there are no errors in the field, and an html string if there are errors
* `FormDoc.formWideErrorMsg()` for the whole form. this picks up errors that apply to the form as a whole -- e.g. if one field has to be greater than another field.

These can be used to compute `FormDoc.isValid()`.

You can also just ask it to a validate certain fields: `newDoc.isValid(['field1', 'field2', 'field3'])`

### Form-wide errors

If there is any form-wide validation that must be done, the method `formWideErrorMessage()` must be over-ridden for the form. For example, in foo.py` we have:
```py

class Foo(MonDoc):
    name = StrField()
    #...other fields...
    dateOfBirth = DateField()
    dateOfDeath = DateField()
```

If both the `dateOfBirth` and `dateOfDeath` are present, the `dateOfDeath` can't be earlier than the `dateOfBirth`. This is exprtessed in a method on `Foo` thus:
```py

    def formWideErrorMessage(self):
        if self.dateOfBirth and self.dateOfDeath:
            if self.dateOfDeath < self.dateOfBirth:
                return "Date Of Death cannot be before Date Of Birth"       
        return "" # no error message, validates OK
```



The method `formWideErrorMessageH()` gets the output from `formWideErrorMessage()` and wraps it up in suitable HTML.

**NB:** `formWideErrorMessageH()` only outputs an error message if `isValid()` has previously been called on the form and there are errors. This is so that the first time the form is displayed (i.e. before any POST request) there are no error messages on the form.

To display form-wide errors your template should look like this (where `doc` is your `FormDoc`):
```html
{{doc.buildForm()}}
{{doc.formWideErrorMessageH()}}
```

## Displaying the form with errors

A form is displayed by calling `doc.buildFormLines()` once to build the whole thing, or by calling `doc.forLine('fieldName')` multiple times to
for each field.

How do these functions know whether to display errors? This is by the `displayErrors` boolean instance variable each `FormDoc` has. When
the `Form` is initialised, this is set to `False` but if it set to `True` when `FormDoc.isValid()` is called.

The reason we use `displayErrors` is that otherwise we would have to pass a parameter to the method that renders the form. This OK for `buildFormLines()`
where you only have to do it once:
```py
h = doc.buildFormLines(displayErrors=True)
```

But rapidly gets annoying if you have to say it individually for each field (in this example in a Jinja2 template, where `doc` and `displayErrors` are parameters passed to it):
```
{{doc.formLine('name', displayErrors)}}
{{doc.formLine('address1', displayErrors)}}
{{doc.formLine('address2', displayErrors)}}
{{doc.formLine('postcode', displayErrors)}}
{{doc.formLine('phone', displayErrors)}}
```

## Writing validation code a a new FieldInfo class

If you create a new `FieldInfo` subclass, how do you write validation code for it?

Do do this, you need to write a `errorMsg()` method for the class. This method takes a parameter `v` which is the value in the field.

NB: the value is *as it will appear in the database*, not as it is input. So for example in an `IntField` if the user enters 345, then `v` would be the int `345` and not the str `"345"`. This is arguably a limitation in the design of monfab, that may be rectified in later versions.


## See also

* [[FormDoc]]
* [[FieldInfo]]
