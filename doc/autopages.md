# Autopages

**Autopages** are automatically-generated BREAD pages (for Browse Read Edit Add Delete).



## Using autopages

Assume you have a `MonDoc` class `Foo`:
```py
class Foo(MonDoc):
    name = StrField()
    favouriteAnimal = ChoiceField(
        choices=['Cat', 'Dog', 'Spider'])
    notes = TextAreaField()
```

Then to set up autopages:
```py
Foo.autopages("BREAD", showFields=['name', 'favouriteAnimal'])
```

The first argument determines which capabilities to create. Possibilities are:

* **B**, browse = a list of all Foos, in `/foos`
* **R**, read = view a single `Foo` in `/foo/{id}`
* **E**, edit = make the `/foo/{id}` page editable
* **A**, add = add a new Foo by `/foo/NEW`; link to this on the `/foos` page.
* **D**, delete = put a button on the `/foo/{id}` page allowing the user to delete the document

If the first argument is omitted, the value is assumed to be `"BREAD"`.

### Arguments to autopages

The `autopages()` function takes two optional arguments: `showFields` and `sort`. Both affect the "Browse" page (i.e. the list of documents).

* `showFields` determines which fields are shown as columns. This defaults to the first 5 fields defined in the collection's schema.
* `sort` determines what order the documents are shown in. The value for sort works the same way as it does in the [MonDoc.find()](MonDoc#find) function 

### Telling autopages the Flask environment

For autopages to work it needs to know information about the application's Flask environment, in particular it needs:

* `app`, the Flask object
* `jinjaEnv`, the Jinja2 environment, typically got by `jinja2.Environment()`

To inform autopages of these, run this before your first `autopages()` call: 

```py
monfab.notifyFlaskForAutopages(app, jinjaEnv)
```

## Templates

Autopages uses Jinja2 templates, the same as normal pages.

In the `Foo` example, templates `foos.html` and `foo.html` will be used.

The template for a list of documents (i.e. `foos.html`) takes parameters:

* `{{count}}` = the number of documents in the list
* `{{table}}` = the table of documents

The template for one document (i.e. `foo.html`) takes parameters:

* `{{id}}` = the `.id()` of the document in question, or `'NEW'` if we're creating a new one.
* `{{doc}}` = the document, i.e. the instance of `Foo`.
* `{{fwem}}` = if the form is invalid, this contains an html-encoded form-wide error message. Otherwise it is empty.
* `{{msg}}` = if the form has been saved, this is an html-encoded message saying so. Otherwise it is empty.
* `{{autopage}}` = This is the `Autopage` object for this collection class
 
*For an example of how these work, look at `autopage_doc.html`.*

### Default templates

But wait! 

You don't have to write your own templates. If you don't, autopages will attempt to use `autopage_list.html` and `autopage_doc.html`. 

If these don't exist either, you'll get an error message.

## See also

* [[MonDoc]]
