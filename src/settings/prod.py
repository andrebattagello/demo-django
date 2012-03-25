from base import *


#redefinition of debug settings from base
DEBUG = False
TEMPLATE_DEBUG = False


###############################################
##Production DB
#Simple PostgreSQL + pgBouncer example::
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'your-db-name',
       'USER': 'user-with-access-to-db',
       'PASSWORD': '',
       'HOST': '',
       'PORT': '6432', #pgBouncer port on the web server
   }
}
###############################################


###############################################
##Cache settings
#Simple Memcache example::
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['cacheserver:11211',],
        'KEY_PREFIX': 'your-key-prefix',
    }
}
CACHE_MIDDLEWARE_SECONDS = 600
###############################################

###############################################
##INSTALLED APPS settings
PROD_APPS = (
    'gunicorn',
)
INSTALLED_APPS += PROD_APPS
###############################################


###############################################
##Logging settings
# See http://docs.djangoproject.com/en/dev/topics/logging for more details
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
###############################################


###############################################
##STATIC/MEDIA assets settings
#You probably want to redefine STATIC_URL and MEDIA_URL
#to match some server configuration.
STATIC_URL = ''
MEDIA_URL = ''
###############################################


###############################################
#EXTRA SETTINGS


#Sessions settings
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
#SESSION_COOKIE_DOMAIN = '.yoursite.com'

#Bazooka caching approach: Cache the entire site.
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware', #Always first
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', #Always last
)
###############################################

try:
    from secret import *
except:
    pass
