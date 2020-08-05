# MonDoc database queries

This page details how to do database queries on a [[MonDoc]] collection class.

## Example schema

In the examples that follow, we will be using the following database schema:
```py
class Customer(MonDoc):
    name = StrField(desc="the name of the customer")
    created = DateField(desc="date the account as created on")
    balance = FloatField(desc="balance of the customer's account")
    credit = FloatField(desc="amount of credit the customer is allowed")
```

## Getting a document by its key

The method is `MonDoc.getDoc(id:DbId)->Optional[MonDoc]`.

The key is a [[DbId]] (short for Database id), wihch is a value for the `_id` key in the database.

If the document exists in the database it is returned; if not, `None` is returned.

Example:
```
customerId = "Customer-0a3"
c = Customer.getDoc(customerId) # returns either a Customer or None.
```

## `find` and associated methods

The methods are:

* `MonDoc.count(*args,**kwargs)->int`
* `MonDoc.find(*args,**kwargs)->Iterator[MonDoc]`
* `MonDoc.find_one(*args,**kwargs)->Optional[MonDoc]`
* `MonDoc.delete_many(*args,**kwargs)`

These all take a database query, and optionally other arguments.

### The database query

### other arguments

## See also

* [[MonDoc]]
