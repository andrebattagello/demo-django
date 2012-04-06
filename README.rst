Description
===========

Just a small Django demonstration application.

This is a simple To Do list application,
written intentionally to show up some best Django practices and cool 3rd party apps


How to Run
==========

cd project/requirements
pip install -r base.txt

cd project/src
python manage.py syncdb
python manage.py runserver
Open http://localhost:8000/lista


How to Run the tests
====================

cd project/requirements
pip install -r devel.txt

:Behaviour Unit tests: python manage.py test

:Acceptance tests: python manage.py harvest --settings=settings.lettuce


Tech Stack
==========

Currently using:

Django 1.3.1

Testing stack:
    * Lettuce + Splinter to Acceptance tests
    * Django TestCase to Behaviour unit tests
    * Factory_Boy over traditional fixtures
    * Django Nose to find out my tests
