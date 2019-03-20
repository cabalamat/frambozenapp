# MonDoc hook functions

The **hook functions** are:

* `preSave()` = called before saving
* `postSave()` = called after saving
* `preCreate()` = call before creating
* `postLoad()` = called after loading from the database

## Definitions in MonDoc

In `MonDoc` they have empty definitions:

```py    
    def preSave(self):
        """ The user can over-ride this with a method to be called
        immediately before the document is saved.
        """
        pass

    def postSave(self):
        """ The user can over-ride this with a method to be called
        immediately after the document is saved.
        """
        pass

    def preCreate(self):
        """ The user can over-ride this with a method to be called
        immediately before the document is created in the database
        (but just after its future _id has been assigned).
        """
        pass
    
    def postLoad(self):
        """ The user can over-ride this with a method to be called
        immediately after the document is loaded.
        """
        pass
```

## Caveat on `preCreate()`

`preCreate()` uses the existence of the `_id` instance varialbe to determine whether the document already exists in the database (objects in the database always have a value for this).

So if you create a new instance of your `MonDoc` subclass, and set its `_id`, then `MonDoc` with think ity already exists in the database and not call `preCreate()`.



## See also

* [[MonDoc]]