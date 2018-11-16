# FKeys

**FKeys** is a [[FieldInfo]] subclass. An `FKeys` field contains a list of foreign keys to MongoDB documents. All the documents must be in the same collection.

In Python, an FKeys field has the type `List[DbId]`.

## Example

Consider an application with books and authors. Each book can have more than one authors, and each author can have more than one books, so there is a many-to-many relation between them. This could be implemented in the following database schema:

```py
class Author(MonDoc):
    name = StrField(desc="name of author")

class Book(MonDoc):
    title = StrField(desc="title of book")
    authors_ids = FKeys(Author)
```

Alternately, you could store the information about which books go with which authors in the `Author` collection:
```py
class AltAuthor(MonDoc):
    name = StrField(desc="name of author")
    books_ids = FKeys('AltBook')

class AltBook(MonDoc):
    title = StrField(desc="title of book")
```
Note that in the `FKeys` constructor, `AltBook` has to be put in quotes as that class hasn't been declared yet.

In the rest of our example, we will use the first way of doing things. Assume you have an author (`au`) and a book (`bk`). Then you can do the following:

Get the database ids of all of the book's authors:
```py
bk.authors_ids # type is List[DbId]
```

Get all of the book's authors, as `Author` objects:
```py
bk.authors # type is List[Author]
```

Get the database ids of all the author's books:
```py
au.getForeignIds('Book', 'authors_ids') # type is Iterable[DbId]
```

Get the author's books, as `Book` objects:
```py
au.getForeignDocs('Book', 'authors_ids') # type is Iterable[Book]
```

The last one is common enough that you could write a convenience method in the Author class for it:
```py
class Author(MonDoc):
    name = StrField(desc="name of author")
    def getBooks(self):
        """ get my books """
        return self.getForeignDocs('Book', 'authors_ids')
```

## Parameters






