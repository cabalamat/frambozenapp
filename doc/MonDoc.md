# MonDoc

**MonDoc** is used to describe the schema of a MongoDB collection. MonDoc is a subclass of [[FormDoc]].

[TOC]

## Deleting documents

To delete a single document from the database:
```py
     doc.delete()
```

To delete all the documents in a collection:
```py
     customer.delete_many()
```

You can also delete those documents that satisfy a query, such as all the customers in Edinburgh:
```py
    Customer.delete_many({'city': "Edinburgh"})
```

(The name  `delete_many()` comes from the pymongo collection method `delete_many()`.)


## URLs, logos etc

Some functionality typically happens with many different kinds of documents, so convenience functions are provided:

* `url()` = document's url. NB: if you use [[autopages]] for a collection, don't over-ride `url()` for that collection.
* `classLogo()` = the collection's logo
* `classTitle()` = the collection's title aka [screen name](Database names and screen names)
* `classTitlePlural()` = the collection's title, as a plural
* `logo()` = a document's logo
* `getName()` = short name describing a document
* `getNameH()` = short name describing a document, html-escaped
* `a()` = an html hyperlink for a document

A document has a URL associated with it, given by the `url()` method. This defaults to `"/{colName}/{id}"`, but can be over-ridden if desired
(but **not** if you are using [[autopages]] on that collection).
If a document doesn't have a url, you should over-ride this to return `""`.

A document optionally has a logo associated with it (e.g. using Font Awesome) given by the `logo()` method. To give all documents in a class
the same logo, you should over-ride the `classLogo()` method.

A document has some (hopefully descriptive) text associated with it, got by `getName()`; this defaults to the ascii value of the 1st defined field.

Putting these all together we get `a()` which returns HTML for a link, containing url, logo and name.

## See also

* [Boxen](bozen)
* [[FormDoc]]
