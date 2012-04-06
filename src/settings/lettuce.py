# -*- coding: utf-8 -*-
from devel import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(SRC_ROOT, 'lettuce.db'),
    }
}

INSTALLED_APPS += ('lettuce.django',)

#Avoid Lettuce to catch undesired apps
LETTUCE_APPS = PROJECT_APPS

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

INTERNAL_IPS = ('127.0.0.1',)

# Use dummy caching for development.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'KEY_PREFIX': PROJECT_NAME,
        'TIMEOUT': 60
    }
}

# Execute celery tasks locally, so you don't have to be running an MQ
CELERY_ALWAYS_EAGER = True
