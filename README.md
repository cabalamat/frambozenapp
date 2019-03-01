# Frambozenapp

**Frambozenapp** is a Python web application that showcases the
**frambozen** library.

## About Bozen

## Installation

Requirements: Python 3.6, MongoDB, Git (to clone repository).

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

## Documentation

Documentation is available in the `./doc/` directory. It's in the 
extended markdown format that 
[CatWiki](https://github.com/cabalamat/catwiki) uses 
(and was created in CatWiki), so is best viewed with CatWiki.

## Screenshots


![](doc/test_form.png)