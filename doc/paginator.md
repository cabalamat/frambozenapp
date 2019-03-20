# Paginator

[[Bozen]]'s **Paginator** class does pagination. It is build on the Flask's Flask-Paginate but is easier to use.

## Using a Paginator

Creation:
```py
    pag = paginate.Paginator(count, perPage=20)
```

The optional `perPage` parameter is the number of items that will be shown on a page. 

Once we have created a paginator, it knows where it is in the list by looking at the GET request's `page` parameter on the URL (e.g. `/foos?page=4`). This is all 
done transparently so no application code has to be written.

* `pag.skip` = number of items in the list to skip before displaying
* `pag.numShow` = number of items in the list to display
* `pag.total` = the total number of items in the list
* `pag.fromIx` = the index of the first item to be displayed, indexing from 1
* `pag.toIx` = the index of the last item to be displayed, indexing from 1
* `pag.links` = HTML for links to other pages
* `pag.info` = String descripting which rows are being displayed, e.g. `"Displaying rows 61-80 of 113."`

## Example

Here the `pag` object is a `Paginator`, from `foo.py`:

```py
@app.route('/foos')
def foos():
    count = Foo.count()
    pag = paginate.Paginator(count)
    tem = jinjaEnv.get_template("foos.html")
    h = tem.render(
        count = count,
        pag = pag,
        table = foosTable(pag),
    )
    return h

def foosTable(pag: paginate.Paginator) -> str:
    """ a table of foos """
    h = """<table class='bz-report-table'>
<tr>
    <th>Id</th>
    <th>Name</th>
    <th>Description</th>
    <th>Favourite<br>Drink</th>
    <th>Fruits<br>Liked</th>
    <th>Ticky<br>Box</th>
</tr>    
    """
    fs = Foo.find(
        skip=pag.skip, # skip this number of docs before returning some
        limit=pag.numShow, # max number of docs to return
        sort='name')
    for f in fs:
        h += form("""<tr>
     <td style='background:#fed'><tt>{id}</tt></td>      
     <td>{name}</td>       
     <td>{description}</td>       
     <td>{favouriteDrink}</td>    
     <td>{fruitsLiked}</td>       
     <td>{tickyBox}</td>                  
</tr>""",
            id = htmlEsc(f.id()),
            name = f.a(),
            description = f.asReadableH('description'),
            favouriteDrink = f.asReadableH('favouriteDrink'),
            fruitsLiked = f.asReadableH('fruitsLiked'),
            tickyBox = f.asReadableH('tickyBox'),
        )     
    #//for f
    h += "</table>"
    return h
```

Note how we modify the `Foo.find()` call to only fetch the documents we need, based on the status of `pag`.

And in the Jinja2 template, `foos.html`:

```html
{% block body %}
<div class='right-pagination'>{{pag.links}}</div>
<h1><i class='fa fa-star'></i> Foos ({{count}})</h1>
<p>{{pag.info}}</p>
{{table}}
<div class='right-pagination'>{{pag.links}}</div>
{% endblock body %}
```

Note that:

* `{{pag.info}}` outputs a text discription of which rows we are displaying, e.g.: "Displaying rows 1-20 of 22."
* `{{pag.links}}` contains links to other pages of the pagination

## See also

* [Flask-Paginate on Github](https://github.com/lixxu/flask-paginate)
