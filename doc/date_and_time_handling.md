# Date and Time Handling

There are [[FieldInfo]] subclasses containing dates and times:

* [[DateField]] holds a date in a form like `"2017-12-31"` 
* [[DateTimeField]] holds a date and time in a form like `"2017-12-31T23:31:53"`
* [[TodField]] holds a time-of-day in a form like `"17:30:00"`

These fields all hold their data as strings. Whe the data is read into a Python object, it is stored as the relevant Bozen class:

FieldInfo class   | Example string          | Data class
------------------|-------------------------|-----------
[[DateField]]     | `"2017-12-31"`          | [[BzDate]]
[[DateTimeField]] | `"2017-12-31T23:31:53"` | [[BzDateTime]]
[[TodField]]      | `"17:30:00"`            | [[BzTod]]