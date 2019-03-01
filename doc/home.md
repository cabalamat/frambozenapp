# Frambozen and Frambozenapp

**Frambozen** is a Python ORM for MongoDB, integrated with a web forms 
layer for Flask. **Frambozenapp** is an application to show off the 
features of Frambozen.

Frambozen has a logo:

![Frambozen Logo](frambozen_logo.png)

[TOC]

## About this documentation

This documentation is stored in the `doc/` directory in frambozenapp. 

The documentation was written using my **CatWiki** wiki software, available from <https://github.com/cabalamat/catwiki>.

The documentation files are stored in the expanded form of Markdown used by CatWiki. 
They are best viewed in catWiki; alternately you can view them in a text editor or other Markdown software (with some limitations).

## Frambozen

Is known as **bozen** inside the repository (it's shorter). See [[Bozen]].

## Frambozenapp

To start, first clone the repository locally.

    $ git clone git@github.com:cabalamat/frambozenapp.git
    $ cd frambozenapp
    
Create a virtual environment called `v3`:

    $ python3 -m venv v3
    
Go into your virtual environment:

    $ . v3/bin/activate
    
Install the requirements:

    $ pip install -r requirements.txt

Finally, go into the `app/` directory and run the program. The
`--debug` flag denotes that you are running it in debugging mode.
    
    $ cd app
    $ python main.py --debug

Now you can point your web browser at <http://127.0.0.1:9033> to
view the site.

### Screenshots

Screenshots of some Frambozenapp pages [are available](screenshots).

## See also

* [[Field types in similar projects]]
* [[Issue with Python 3 packaging]]
* [[To-do]] list