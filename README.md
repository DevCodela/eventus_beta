eventus_beta
============
# EVENTUS Beta #

Facilita la búsqueda, promoción de eventos y registro de asistentes. Podrás construir una aplicación funcional, segura y robusta hasta hacer deploy en cualquier servidor.

### Requirements ###

* Virtualenv or virtualenvwrapper
* Django 1.7.0

### Create a virtualenv ###

    $ virtualenv env
    $ source env/bin/activate

### Installing from requirements files

	$ pip install -r requirements/local.txt

### Collectstatics

    $ python manage.py collectstatic --settings=eventus.settings.local

### How to run the project

    $ python manage.py runserver --settings=eventus.settings.local