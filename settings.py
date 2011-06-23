# Django settings for Frodi project.

import os
here = lambda x: os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), x))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'curr.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = here('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'osu&z3#^x_n7)m0kjl-4uo%ql_tkwhuwute!rn-iab7k64!%&8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    here('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "site_structure.context_processors.generate_menu",
    "site_structure.context_processors.generate_highlights",
    "site_structure.context_processors.random_header",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    #"django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'site_structure',
    'secondary_schools',
    'secondary_schools.courses',
    'management',
    'community',
    'secondary_schools.schools',
    'iceland',
    'feedzilla',	#vm.19.05.2011 - Feedzilla stillingar
    'tagging',		#vm.19.05.2011 - Feedzilla stillingar
    'common',		#vm.19.05.2011 - Feedzilla stillingar

)

#vm.19.05.2011 - Feedzilla stillingar
FEEDZILLA_PAGE_SIZE = 25
FEEDZILLA_SUMMARY_SIZE = 2000
FEEDZILLA_SITE_TITLE = 'Yet another feedzilla site'
FEEDZILLA_SITE_DESCRIPTION = 'Edit your settings to change that line'
FEEDZILLA_CLOUD_STEPS = 4
FEEDZILLA_CLOUD_MIN_COUNT = 2
FEEDZILLA_TAGS_LOWERCASE = True
FEEDZILLA_POST_PROCESSORS = (
    'feedzilla.processors.ContentFilterProcessor',
)
