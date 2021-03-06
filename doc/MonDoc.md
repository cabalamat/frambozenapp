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

## Saving to the database

### Hooks on saving to the database

In your MonDoc subclass you can define hooks, i.e. method that will be triggered on a specific event. the hooks are:

* `preSave()` = called before saving
* `postSave()` = called after saving
* `preCreate()` = call before creating
* `postLoad()` = called after loading from the database

See [[MonDoc hook functions]] for details.

### `mongoDict()->dict`

The `mongoDict()` method returns a `dict` of the document suitable for putting in a MongoDB database.

## Querying the database

*See also [[MonDoc database queries]]*.

Querying the database is done by the `MonDoc.find()` class method which is analogous to the `find()` method in `pymongo`. 

Imagine you have a `Customer` table:

```py
class Customer(MonDoc):
    name = StrField(desc="the name of the customer")
    created = DateTimeField(desc="when the customer account was created")
    balance = FloatField(desc="the customer's balance")
    #...other fields...
```

You want all customers created since the start of 2019, in the order of when they were created. This is:

```py
recentCustomers = CustomerFind({'name': {'$gte': "2019-01-01"}}, sort='created')
```

If you want the most recent first (i.e. in decreasing order of `created`), this would be:
```py
recentCustomers = CustomerFind({'name': {'$gte': "2019-01-01"}}, sort=('created',-1))
```

If you want the 20 customers with the lowest balances, in order of increasing balance, this would be:
```py
lowBalCusts = CustomerFind(sort='balance', max=20)
```

## Low-level database access

### `col()->pymongo.collection.Collection`

The `col()` method returns the underlying pymongo Collection object.

## See also

* [[Bozen]]
* [[FormDoc]]
* [[MonDoc database queries]]
* [[MonDoc collection class]]
