#!/usr/bin/env python
from django.core.management import execute_manager

import os

DJANGO_ENVIRON = os.environ.get('DJANGO_ENVIRON', None)

try:
    if DJANGO_ENVIRON == 'PROD':
        import settings.prod as settings
    elif DJANGO_ENVIRON == 'DEVEL':
        import settings.devel as settings
    else:
        import settings  #let what it is in __init__ handle
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)


if __name__ == "__main__":
    execute_manager(settings)
