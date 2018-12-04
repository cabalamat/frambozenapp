# Paginator

[Monfab](home)'s **Paginator** class does pagination. It is build on the Flask's Flask-Paginate but is easier to use.

## Using a Paginator

Creation:
```py
    pag = paginate.Paginator(count, perPage=20)
```

The optional `perPage` parameter is the number of items that will be shown on a page. 

Once we have created a paginator, it knows where it is in the list by looking at the GET request's `page` parameter on the URL (e.g. `/customers?page=4`). This is all 
done transparently so no application code has to be written.

* `pag.skip` = number of items in the list to skip before displaying
* `pag.numShow` = number of items in the list to display
* `pag.links` = HTML for links to other pages
* `pag.info` = String descripting which rows are being displayed, e.g. `"Displaying rows 61-80 of 113."`

## Example

Here the `pag` object is a `Paginator`.

```py
@app.route('/customers')
def customers():
    tem = jinjaEnv.get_template("customers.html")
    count = models.Customer.count()
    pag = paginate.Paginator(count)
    h = tem.render(
        count = count,
        pag = pag,
        table = customersTable(pag),
    )
    return h

def customersTable(pag):
    """ returns an html table of customers """
    h = """<table class='report_table'><tr>
   <th>First Name</th>
   <th>Postcode</th> </tr>"""

    custs = models.Customer.find(
        skip=pag.skip, # skip this number of docs before returning some
        limit=pag.numShow, # max number of docs to return
        sort=['surname','firstName','title'])
    for doc in custs:
        item = form("""<tr>
<td>{firstName}</td>
<td>{surname}</td>
<td>{postcode}</td>
<td><a href='{url}'><i class='fa fa-edit'></i> edit</a></td>
</tr>""",
            firstName = doc.asReadableH('firstName'),
            surname = doc.asReadableH('surname'),
            postcode = doc.asReadableH('postcode'),
            url = doc.url(),
        )
        h += item
    #//for
    h += "</table>\n"
    return h
```

And in the Jinja2 template, `customers.html`:

```html
{% extends "main.html" %}
{% block body %}
<div class='right-pagination'>{{pag.links}}</div>
<h1><i class="fa fa-home"></i> Customers ({{count}})</h1>
<p>{{pag.info}}</p>
{{table}}
<div class='right-pagination'>{{pag.links}}</div>
{% endblock body %}
```



## See also

* [Flask-Paginate on Github](https://github.com/lixxu/flask-paginate)
