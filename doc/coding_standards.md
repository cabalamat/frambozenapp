# Coding Standards

This page lists coding standards and conventions that Bozen will conform to.

[TOC]

## Python

Python code will require Python 3.6 or later and will conform with [PEP 8](https://www.python.org/dev/peps/pep-0008/), with the following clarifications and exceptions:

### Indentation

Use 4 spaces. No tabs. Hanging indents are fine and should be indented by 4 characters from the previous level, e.g. this is OK:
```py
def longFunctionName(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

Compound if statements:
```py
if (thisIsOneThing 
    and foo(xyz)):
    doSomething()
```

Closing lines of lists line up with line containing the start of the construct:
```py
myList = [
    1, 2, 3,
    4, 5, 6,
]
myDict = {
   'foo': 6,
   'bar'; 897,
}
```

### Identifiers

Use CamelCase, e.g. `theFunctionName` not `the_function_name`. Classes and types start in upper case: e.g. `MonDoc`. System-wide constants in all upper case with "_" to delimit words e.g.:
```py
APP_LOGO = "<i class='icon-noun_162884_cc'></i> "
```

Where part of an identifier is an initialism, letters after the first go in lower case, e.g. `theHtmlEditor`, `cssClassList`.

Don't use non-ascii characters in identifiers.

### Misc

In quoted strings, use single quotes for what would bve a Symbol in Smalltalk (i.e. short strings that are valid identifiers and have symbolic meaning), otherwise use double quotes. 

```py
FRUIT_CHOICES = [
    ('apple', "Apple"),
    ('banana', "Banana"),
    ('orange', "Orange"),
]
class myForm(FormDoc):
    favouriteFruit = ChoiceField(choices=FRUIT_CHOICES,
        default='banana')
```

Trailing commas outside brackets to form a tuple of 1 value are not allowed:

Yes:
```py
FILES = ('setup.cfg',)
```
No:
```py
FILES = 'setup.cfg',
```

Where types are declared, do it in a way consistent with [PEP 484](https://www.python.org/dev/peps/pep-0484/), the `typing` module and mypy.
```py
from typing import *

def getDefaultDatabase()->Optional[pymongo.collection.Collection]:
    """ return the default database, if this has been set """
    return defaultDB
```
## HTML

## CSS

*See also [[Bozen CSS]].*

Bozen code outputs HTML. This HTML contains CSS classes. The file `bozen.css` contains definitions of the CSS classes used by Bozen.

These CSS classes begin with `bz-` where they define the type of an element, but not not when they merely define a characteristic of it.

Example. This Python:
```py
class TheTestForm(FormDoc):
    bbb = StrField(monospaced=True)
```
Might, when rendering the form, produce HTML like this:
```html
<input class="bz-input monospace" 
    id="id_bbb" name="bbb"
    type="text" value="" size=20>
```

This includes the CSS classes `bz-input` (which means it is a Bozen input element in a form) tells you wta it is, 
and `monospace` (which means the text in the form is displayed in a monospace font) describes something about what it looks like.

## See also

* [[Documentation Standards]]



