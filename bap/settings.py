# -*- coding: utf-8 -*-
# Django settings for basic pinax project.

import os.path
import posixpath
import pinax
from odict import odict

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# tells Pinax to use the default theme
PINAX_THEME = 'default'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through django.views.static.serve.
SERVE_MEDIA = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

db = 'mysql'
if db == 'sqlite':
    DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
    DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'dev.db')       # Or path to database file if using sqlite3.
    DATABASE_USER = ''             # Not used with sqlite3.
    DATABASE_PASSWORD = ''         # Not used with sqlite3.
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
else:
    DATABASE_ENGINE = 'mysql'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
    DATABASE_NAME = 'bap'       # Or path to database file if using sqlite3.
    DATABASE_USER = 'bap'             # Not used with sqlite3.
    DATABASE_PASSWORD = 'Pass The CPA exam'         # Not used with sqlite3.
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", 'media')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/site_media/media/'

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'static')

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = '/site_media/static/'

# Additional directories which hold static files
STATICFILES_DIRS = (
    ('basic_project', os.path.join(PROJECT_ROOT, 'media')),
    ('pinax', os.path.join(PINAX_ROOT, 'media', PINAX_THEME)),
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=dc&m1jw=0#5=#kab9tebfp^012g==&4oxp*43pa-akzux!8j9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_openid.consumer.SessionConsumer',
    'account.middleware.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'pinax.middleware.security.HideSensistiveFieldsMiddleware',
    # For django-page-cms
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.SetRemoteAddrFromForwardedFor',
)

ROOT_URLCONF = 'bap.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",

    "pinax.core.context_processors.pinax_settings",

    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    "account.context_processors.openid",
    "account.context_processors.account",

    # For django-page-cms
    "pages.context_processors.media",
)

INSTALLED_APPS = (
    # included
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'pinax.templatetags',

    # external
    'notification', # must be first
    'django_openid',
    'emailconfirmation',
    'mailer',
    'announcements',
    'pagination',
    'timezones',
    'ajax_validation',
    'uni_form',

    # internal (for now)
    'basic_profiles',
    'staticfiles',
    'account',
    'signup_codes',
    'about',
    'django.contrib.admin',

    # BAP additions
    'cas_consumer',
    'django_extensions',

    # For cms functionality
    'mptt',
    'tagging',
    'pages',

    # For ads
    'django_generic_flatblocks',
    'generic_ads',

    # For calendering
    'schedule',
    'django_attendance',
    'django_reservations',
)

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'cas_consumer.backends.CASBackend')

MARKUP_FILTER_FALLBACK = 'none'
MARKUP_CHOICES = (
    ('restructuredtext', u'reStructuredText'),
    ('textile', u'Textile'),
    ('markdown', u'Markdown'),
    ('creole', u'Creole'),
)
WIKI_MARKUP_CHOICES = MARKUP_CHOICES

AUTH_PROFILE_MODULE = 'basic_profiles.Profile'
NOTIFICATION_LANGUAGE_MODULE = 'account.Account'

ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
CONTACT_EMAIL = "feedback@example.com"
SITE_NAME = "IU BAP"
LOGIN_URL = "/cas/login/"
LOGOUT_URL = "/cas/logout/"
LOGIN_REDIRECT_URLNAME = "what_next"

# CAS settings
CAS_COMPLETELY_LOGOUT = True
CAS_BASE = 'https://cas.iu.edu/cas/'
CAS_SERVICE = 'http://iubap.org/cas/login/'
CAS_NEXT_DEFAULT = '/'

# Customized weird CAS settings
# A lot of horrible hacks because of IU's implementation: http://kb.iu.edu/data/atfc.html

# They call the service parameter 'casurl' and prepend 'cas' to 'ticket'
CAS_SERVICE_LABEL = 'casurl'
CAS_TICKET_LABEL = 'casticket'
# IU requires cassvc with login and validate requests and they require it to be the first GET variable
CAS_EXTRA_LOGIN_PARAMS = odict((
    ('cassvc', 'IU'),
    (CAS_SERVICE_LABEL, None)))
CAS_EXTRA_VALIDATION_PARAMS = odict((
    ('cassvc', 'IU'),
    (CAS_TICKET_LABEL, None),
    (CAS_SERVICE_LABEL, None)))
# IU doesn't support the urls with slashes after the names
CAS_LOGIN_URL = 'login'
CAS_VALIDATE_URL = 'validate'
CAS_LOGOUT_URL = 'logout'
# IU doesn't support properly urlencoded values
CAS_URLENCODE_PARAMS = False

def update_email(user):
    if not user.email or len(user.email) < 4:
        user.email = '%s@indiana.edu' % user.username
        user.save()

CAS_USERINFO_CALLBACK = update_email

# For django-page-cms
CACHE_BACKEND = "locmem:///?max_entries=5000"
PAGE_PERMISSION = False # Disable advanced hierarchic permissions
PAGE_TAGGING = False # Disable page tagging

LANGUAGES = (('en', 'English'),)
PAGE_HIDE_ROOT_SLUG = True

DEFAULT_PAGE_TEMPLATE = 'pages/base.html'
PAGE_TEMPLATES = (
    ('pages/base.html', 'Standard Info Page'),
)
PAGES_MEDIA_URL = os.path.join(STATIC_URL, 'pages/')

# Settings for the About members list
BAP_MEMBERS_GROUP_NAME = 'BAP Member'
BAP_FACULTY_GROUP_NAME = 'BAP Faculty'

# Settings for django-schedule
# Function to check if a user can edit the given event
def check_cal_edit_permission(ob, user):
        return user.is_authenticated() and 'BAP Content Editor' in [g.name for g in user.groups.all()]
CHECK_PERMISSION_FUNC = check_cal_edit_permission

# django-attendance
ATTENDANCE_HOUR_MULTIPLIER = 1.2 # 50 minutes is 1 hour

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
