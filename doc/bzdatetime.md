# BzDateTime

**BzDateTime** (short for *Bozen Date and Time*) is Bozen's class to handle date-and-time strings in forms and database fields.


## Creating a `BzDateTime`

The `BzDateTime()` constructor takes an argument that can be:

* a `BzDate`, in which case the date is copied and the time set to `"00:00:00"`
* a `BzDateTime`, in which case it is copied
* a `datetime.date`
* a `datetime.datetime`
* a string in any of the formats:
    * `"2017-11-28"` (date only)
    * `"2017-11-28T13:45"` (date followed by hour:minute)
    * `"2017-11-28T13:45:07"` (date followed hour:minute:second)
    * `"20171128"` (date only)
    * `"2017112813"` (date and hour)
    * `"201711281345"` (date, hour, minute)
    * `"20171128134507"` (date, hour, minute, second)
* an `int` where 1970-Jan-01 is day 0. The time is set to `"00:00:00"`

### Note on construction from string

Where `BzDateTime` is constructed from a string, if the string is in any of these formats:

* `"2017-11-28"` (date only)
* `"2017-11-28T13:45"` (date followed by hour:minute)
* `"2017-11-28T13:45:07"` (date followed hour:minute:second)

then after the date part, the separators can be any non-digit characters.

Example. In this code:
```py
bzdt1 = BzDateTime("2017-11-28T13:45:07")
bzdt2 = BzDateTime("2017-11-28 hello world 13 45 07")
```

then `bzdt1` and `bzdt2` will have the same value.


## Methods for conversion to different formats

`toTuple_ymd()->Tuple[int,int,int]` converts to a tuple in the format `(year,month,day)` e.g. `(2006,7,9)`

`toTuple_ymdhms()->Tuple[int,int,int,int,int,int]` converts to a tuple in the format `(year,month,day,hours,minutes,seconds)` e.g. `(2006,7,9,23,58,57)`

`to_date()->datetime.date` returns a Python `date` object

`to_datetime()->datetime.datetime` returns a Python `datetime` object

`to_dayInt()->int` returns an `int`. This converts a day to an integer where 1-Jan-1970 is day zero, and each succeeding day adds 1.



## See also

* [[BzDate]]
