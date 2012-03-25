from base import *
import os


###############################################
##Local sqlite DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(SRC_ROOT, 'dev.db'),
    }
}
###############################################


###############################################
##TESTING settings

#unclebob settings
#TEST_RUNNER = 'unclebob.runners.Nose'
#import unclebob
#unclebob.take_care_of_my_tests()

#Avoid Lettuce to catch undesired apps
LETTUCE_APPS = PROJECT_APPS

#Django-nose settings
#FIXTURE_DIRS = (os.path.join(SRC_ROOT, 'fixtures'),)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ["--include=^(it|ensure|must|should|specs?|examples?|deve)",
             "--include=(specs?(.py)?|examples?(.py)?)$",
             '--with-spec', '--spec-color']


#Do not hijack the stdout (useful when I want to pdb my tests)
#NOSE_ARGS = ['-sd', '--nologcapture',]

#uncomment this line to enable debug while testing
#NOSE_ARGS.extend(['-v','--debug=nose.plugins.nosedjango',
                  #'--pdb', '--pdb-failures',])

#During tests use only syncdb; do not migrate
SOUTH_TESTS_MIGRATE = False

#Twill settings
#Uncomment to more friedly twill exception display
#DEBUG_PROPAGATE_EXCEPTIONS = True
###############################################


###############################################
##INSTALLED APPS settings
DEVEL_APPS = (
    'django_extensions',
    'debug_toolbar',

    #testing helper apps
    'django_nose',
    'lettuce.django',
)
INSTALLED_APPS += DEVEL_APPS
###############################################


###############################################
#EXTRA SETTINGS

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
###############################################


try:
    from local_settings import *
except:
    pass
