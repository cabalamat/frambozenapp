# Bozen

**Bozen** is the Form library and MongoDB ORM of Frambozen.

[TOC]

## Overview of Bozen's structure and documentation

The most important classes in Bozen are:

* **[[FormDoc]]**, which handles HTML forms
* **[[MonDoc]]**, a subclass of `FormDoc` which knows how to get data into and out of a MongoDB database. 
  Once you have defined your [MonDoc collection classes](MonDoc collection class), you can do [database queries](MonDoc database queries) on them.
* the **[[FieldInfo]]** classes. Every field has an instance of a subclass of FieldInfo describing what data type it is and how it behaves in a form.

Other Bozen features:

* For a MonDoc, automatically generated **[[autopages]]** can perform BREAD (Browse, Read, Edit, Add, Delete) functionality for it.
* There is an automatically generated **[[Admin Site]]** wihch allows users to view and edit the database. 
* The **[[Paginator]]** class enables a table to be paginated so that only a certain number of rows appear on each page.
* There are various **[[utility functions]]**.
* Bozen's **[[date and time handling]]** facilities

### Utility modules

Packaged with Bozen, but not strictly part of it, are some utility modules I've written:

* [[lintest]] is a replacement for Python's *unittest* test framework.

## Modules

The [[mongo]] module interacts with [[MongoDB]] using the pymongo library.

## See also

* [[Coding standards]] and [[documentation standards]]
* [[Bozen CSS]]
* [[Glossary]]
