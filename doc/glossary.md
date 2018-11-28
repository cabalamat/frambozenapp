# Glossary

This **glossary** is a list of some terms used in [[Bozen]].

**Screen Value** or **Display Value** = a value as it is displayed on the screen

**Database Value** = a value as it is stored in the database.

**Python Value** or **Py Value** = a value as it is stored in a python object. This is especially used of a the value of a *field* in a *document*.

**Document** = an instance of a [[FormDoc]] or [[MonDoc]] subclass, or a document in a MongoDB database. 

## Terms relating to MongoDB databases

MongoDB uses **collection** to mean a table in a database, and **document** to mean a record in a database.

A MongoDB document is a JSON data structure which when read into Python by pymongo as a `dict`; its keys are called **field names** and its values are **field values**.

**Table** and **collection** are synonyms: they refer to a MongoDB collection.

**Document**, **record** and **row** are synonyms: they refer to a MongoDB document.

**Field** and **column** are synonyms: they refer to a field in a MongoDB document.

**Table definition** and **table schema** both mean a definition of a table in a `MonDoc` subclass. Another name for a MonDoc subclass is **collection class**.

A **database schema** means all the tables in a database; in an applicaiton, this might be defined in a file called `models.py`.

