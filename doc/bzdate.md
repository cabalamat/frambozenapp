# BzDate

**BzDate** (short for *Bozen Date*) is Bozen's class to handle strings in forms and database fields.

This issue arises because JSON has no native date format. So people have taken to the convention of using [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) string formats. 
But ISO8601 defines lots of string formats, so [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) recommends a subset of them. 

BzDate stores dates as a string in the form *yyyy-mm-dd* for example `"2006-07-09"`.

## Class Methods

`BzDate.today()->BzDate` returns today's date

## Creating a `BzDate`

The `BzDate()` constructor takes an argument that can be:

* a `datetime.date`
* a `datetime.datetime`
* a string beginning with the format *yyyy-mm-dd*, e.g. `"2006-07-09"`
* a string beginning with the format *yyyymmdd*, e.g. `"20060709"`


## Methods for conversion to different formats

`toTuple()->Tuple[int,int,int]` converts to a tuple in the format `(year,month,day)` e.g. `(2006,7,9)`

`to_date()->datetime.date` returns a Python `date` object

`to_datetime()->datetime.datetime` returns a Python `datetime` object

## Methods for date arithmetic

`addDays(numDays:int)->BzDate` adds a number of days to a date. The number can be negative, e.g. `BzDate.today().addDays(-1)` returns yesterday's date.

## See also

* [[BzDateTime]] holds an instant in time
* [[BzTod]] holds a time-of-day
* [[DateField]] is a database or form field holding a date (in `BzDate` format)
* [[DateTimeField]] is a database or form field holding an instant in time(in `BzDateTime` format)
* [[TodField]] is a database or form field holding a time-of-day (in `BzTod` format)



