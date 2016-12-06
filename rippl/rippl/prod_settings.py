import os
from .settings import *  # noqa F403

DEBUG = False
DEBUG_TEMPLATE = False

SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = [".gnmerritt.net", "*vendetta", "*scarab"]

INSTALLED_APPS += [  # noqa F405
    'gunicorn',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rippl',
        'USER': 'rippluser',
        'PASSWORD': os.environ['RIPPL_PG_PASS'],
        'HOST': 'localhost',
        'PORT': '',
    }
}
CONN_MAX_AGE = 30

SLACK_API_KEY = os.environ['SLACK_API_KEY']

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
