# Bozen CSS

**Bozen CSS** is the CSS classes and identifiers included in HTML rendered by [[Bozen]].

The layout for these classes and identifiers is defined in `static/bozen.css` in the Flask app.

## CSS classes

In the below "Old class name" refers to the equivalent class name in [[Monfab]], Bozen's predecessor.

### Forms


Class name      | Old class name | Meaning / notes
------          | ------         | ------
`bz-form-table` | `form-table`   | goes in `<table>` element inside `<form>`
`bz-field-title`| `form-title`   | the title for the field in a form
`bz-input`      | `gin`          | input element in a form
`bz-read-only`  | `roin`         | read only input
`bz-read-only`  | `read-only`    | 
`bz-form-error-line` | `form-error-line` | line containing an error message in a form
`bz-form-error` | `form-error`   | an error message in a form
`bz-form-warning-line` | `form-warning-line` | line containing an error message in a form
`bz-form-warning`| `form-warning`| an error message in a form
`bz-DateField`  | `DateField`    | says it is a [[DateField]] form element
`bz-DateTimeField` | `DateTimeField` | says it is a [[DateTimeField]] form element

### Visual display of forms

Class name      | Old class name | Meaning / notes
------          | ------         | ------
`monospace`     | `monospace`    | uses a monspaced font

### Report tables

This is used to contain tabular information, e.g. a list of documents in [[autopages]].

Class name       | Old class name | Meaning / notes
------           | ------         | ------
`bz-report-table`| `report_table` | goes in `<table>` element 

## Font Awesome

Bozen-produced HTML includes Font Awesome 4.5 icons, which are implemented as CSS classes. The ones used are:


Icon   | Class name   | Used for 
------ | ------       | -----
<i class='fa fa-exclamation-triangle'></i> | `fa-exclamation-triangle` | accompanies error messages



## See Also

* [[Coding standards]]