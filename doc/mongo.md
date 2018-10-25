# mongo

`mongo` is a module in [Bozen](bozen). It does some communication with [[MongoDB]] via pymongo.

## Functions

### setDefaultDatabase(dbName)

The default database is the one that all collections belong to, unless set otherwise. Generally, all the collections that a Bozen program is interacting with will belong to the same database.

This function sets that database.

### getDefaultDatabase()

Returns whatever the default database was set as.