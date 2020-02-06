# Utility Functions

[[Bozen]]'s **utility functions** are mostly implemented in `butil.py`.

[TOC]

## String formatting functions

### `form()`

`form(fs:str,*args,**kwargs)->str` is similar to Python's `aString.format(fmtSpec, *args, *kwargs)`, except that the old-style format specificers `%s` and `%r` are also understood. For example:

```py
i = 1
arr = [44,55,66]
x = form("arr[%r]==%r", i, arr[i])
```

`x` has the value `"arr[1]=55"`.

### Printing functions

These work by calling `form()`, potentially adding a `"\n"` at the end and then sending to the relevant output stream:

* `pr(fs:str,*args,**kwargs)` = print to stdout
* `epr(fs:str,*args,**kwargs)` = print to stderr
* `prn(fs:str,*args,**kwargs)` = print to stdout, with `"\n"` at end    
* `eprn(fs:str,*args,**kwargs)` = print to stderr, with `"\n"` at end    


## Debugging functions

`dpr(formatStr:str,*args,**kwargs)` works like the `eprn()` function above but prefixes the output with the function name and line number it was called from.

`@printargs` is a decorator. It prints out the input parameters to a function and its return value. Example:

```py
from typing import List, Union
from bozen.butil import *

@printargs
def flatSum(a:Union[List,int])->int:
    if isinstance(a, list):
        fs = sum(flatSum(e) for e in a)
        return fs
    return a

prn("result=%r", flatSum([2, [7,99,88], 3000]))
```

This returns:

```
flatSum([2, [7, 99, 88], 3000])
| flatSum(2)
| flatSum(2) => 2
| flatSum([7, 99, 88])
| | flatSum(7)
| | flatSum(7) => 7
| | flatSum(99)
| | flatSum(99) => 99
| | flatSum(88)
| | flatSum(88) => 88
| flatSum([7, 99, 88]) => 194
| flatSum(3000)
| flatSum(3000) => 3000
flatSum([2, [7, 99, 88], 3000]) => 3196
result=3196
```



`pretty(ob, indent:int=4)->str` prettyprints an object.

## HTML functions

These function help in writing web apps.

`htmlEsc(str)->str` escapes a string for HTML, e.g. `htmlEsc("6>5")` return s `"6gt;5"`.

## Others
