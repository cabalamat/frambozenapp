# Field types in similar projects

This compares field types and they names in similar projects, e.g.:

* Django models
* Django forms
* SQL Alchemy models
* WTForms (forms)

## Ordinary Fields

Python | Monfab     | Django models | Django forms
------ | -------    | ------------- | ------
int    |           IntegerField  |
float  | IntegerField  |
bool   | BooleanField  |
str    | CharField     |
date   | DateField     |

## Relationship Fields


Python | Django models | Django forms
------ | ------------- | ------
       | ForeignKey    |
       | ManyToManyField |
       | OneToOneField |
