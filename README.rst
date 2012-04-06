Description
===========

Just a small Django demonstration application.

This is a simple To Do list application,
written intentionally to show up some best Django practices and cool 3rd party apps


How to Run
==========

* cd project/requirements
* pip install -r devel.txt
 
* cd project/src
* python manage.py syncdb
* python manage.py runserver
* Open http://localhost:8000/lista


How to Run the tests
====================

* cd project/requirements
* pip install -r devel.txt

Behaviour Unit tests
~~~~~~~~~~~~~~~~~~~~

python manage.py test

Acceptance tests
~~~~~~~~~~~~~~~~

* pip install splinter
* pip install lettuce
* python manage.py harvest --settings=settings.lettuce


Tech Stack
==========

Currently using:

Django
Bootstrap CSS

Testing stack:
    * Lettuce + Splinter to Acceptance tests
    * Django TestCase to Behaviour unit tests
    * Factory_Boy over traditional fixtures
    * Django Nose to find out my tests


Common issues
=============

Sometimes, lxml can be tricky to install

:Windows: http://pypi.python.org/pypi/lxml/2.3
:Linux: 
    * sudo apt-get install libxml2-dev
    * sudo apt-get install libxslt1-dev
    * sudo apt-get install python2.7-dev
