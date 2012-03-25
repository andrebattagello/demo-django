import os
import django

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

SITE_ID = 1

# Make this unique, and don't share it with anybody.
#With django-extensions generate a new one using `manage.py generate_secret_key`
SECRET_KEY = 'your-secret-key'

ROOT_URLCONF = 'urls'


###############################################
##General Project information
PROJECT_NAME = 'your-project-name'
PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..')
SRC_ROOT = os.path.join(PROJECT_ROOT, 'src')
DOCS_ROOT = os.path.join(PROJECT_ROOT, 'docs')
PUBLIC_ROOT = os.path.join(PROJECT_ROOT, 'public')
TEMPLATES_ROOT = os.path.join(PROJECT_ROOT, 'templates')
###############################################


###############################################
##Language support settings
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'America/Sao_Paulo'
#LANGUAGE_CODE = 'pt-br'
#LANGUAGES = (
    #('pt-br',_('Brazilian Portuguese')),
#)
###############################################


###############################################
##Media assets (user-uploaded content) settings
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')
MEDIA_URL = '/media/'
###############################################


###############################################
##Static assets settings
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static') #collect to this directory
STATIC_URL = '/static/' #serve them from this URL
#ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
#search them from this directories
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
    #uncomment the next line if using the admin django contrib app
    ('admin', os.path.join(os.path.dirname(django.__file__), 'contrib', 'admin', 'media')),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]
###############################################


###############################################
##Template settings
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#   'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATES_ROOT.replace('\\', '/'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)
###############################################


###############################################
##INSTALLED APPS SETTINGS
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    #put external 3rd-party installed apps here
    'south',
    #'compressor',
    #'mailer',


)

PROJECT_APPS = (
    #put your internal project apps here
    'lista',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
###############################################


###############################################
##Email settings::

DEFAULT_FROM_EMAIL = 'xyz@xyz.com'
SERVER_EMAIL = 'xyz@xyz.com'

##Email Hosting settings (smtp Gmail example)::
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'xyz@xyz.com'
EMAIL_HOST_PASSWORD = 'your-email-password-here'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#If using django-mailer
if 'mailer' in INSTALLED_APPS:
    EMAIL_BACKEND = 'mailer.backend.DbBackend'
    #what django-mailer will actually use
    MAILER_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    #MAILER_EMAIL_BACKEND = 'django_ses.SESBackend'

#You can also use the Python SMTP debugging server. Run it with:
#python -m smtpd -n -c DebuggingServer localhost:1025
#EMAIL_PORT = 1025
###############################################


###############################################
#EXTRA SETTINGS

###############################################
