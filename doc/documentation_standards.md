# Documentation Standards

This page lists the **documentation standards and conventions** that are used in this Frambozen documentation.

## Python source code

### The value of an expression

Example:
```py
a = 6
b = 3
a+b #=> 9
```

### Types

When denoting a Python type, such as a field or a parameter to a function, the format used in the python `typing` module is used. E.g.:

```py
List[Tuple[str,str]]
```

denotes a list of tuples, wioth each tuple consisting of 2 string. An example of a value conforming to this type is:
```py
SLOT_CHOICES = [
    ('slotA', "Slot A - Apple"),
    ('slotB', "Slot B - Banana"),
    ('slotC', "Slot C - Carrot"),
    ('slotD', "Slot D - Date"),
]
```

## See also

* [[Coding Standards]]