# FK

An `FK` is a foreign key to a MongoDB document. As a field, it is a subclass of [[FieldInfo]].

`FK` is defined in `keychoicefield.py`.

## Example

Consider an app with *Books* and *Authors*. Each book has at most one author. 

```py
class Author(MonDoc):
    name = StrField()

class Book(MonDoc):
    title = StrField()
    yearPublished = IntField()
    author_id = FK(Author)
```    

Now let's create an author and a book:
```py
a = Author(name="George Orwell")
a.save()
b = Book(title="Animal Farm", yearPublished=1945)
b.save()
```

At this point we haven't set the book's author, and the value of the `b.author_id` field in the Python `b` object is `None`. In the database the corresponding value is `null` (the JSON equivalent of Python's `None`). Let's give the book an author:
```py
b.author_id = a._id
b.save()
```
The `b.author_id` field is now the primary key for the author. In the database, `b` might now look like this:
```json
{
    "_id" : "Book-092",
    "title" : "Animal Farm",
    "yearPublished" : 1945,
    "author_id" : "Author-08z"
}
```
With the author record looking like this:
```json
{
    "_id" : "Author-08z",
    "name" : "George Orwell"
}
```

### Dereferencing a foreign key

Later on in the program, you load a copy of the book, `bCopy`, from the database:
```py
bCopy = find_one({'title': "Animal Farm"})
```
You could get the author_id by: `bCopy.author_id`. You can get the author document from its `_id`, i.e.:
```py
theAuthor = Author.getDoc(bCopy.author_id)
```
But the usual way is `bCopy.author`. From here you can access the author's fields, e.g.:
```py
bCopy.author.name #=> "George Orwell"
```

## Parameters

The `FK` constructor takes one compulsory parameter, the name of the collection it is a reference to. If this collection hasn't been defined you, you can use a string, e.g. `FK(Author)` and `FK('Author')` mean the same thing.
