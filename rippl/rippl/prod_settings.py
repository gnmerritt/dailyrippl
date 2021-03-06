import os
from .settings import *  # noqa F403

DEBUG = False
DEBUG_TEMPLATE = False

SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = [".gnmerritt.net", "*vendetta", "*scarab"]

INSTALLED_APPS += [  # noqa F405
    'gunicorn',
]

static_dir = os.environ.get('STATIC_ROOT', None)
if static_dir is not None:
    STATIC_ROOT = static_dir

MIDDLEWARE.remove('querycount.middleware.QueryCountMiddleware')  # noqa F405

RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIV_KEY']
SUNLIGHT_KEY = os.environ['SUNLIGHT_KEY']

SLACK_API_KEY = os.environ['SLACK_API_KEY']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'slack-error': {
            'username': 'rippl django logs',
            'level': 'ERROR',
            'api_key': SLACK_API_KEY,
            'class': 'slacker_log_handler.SlackerLogHandler',
            'channel': '#rippl-logs'
        },
        'slack-info': {
            'username': 'rippl django logs',
            'icon_emoji': 'droplet',
            'level': 'INFO',
            'api_key': SLACK_API_KEY,
            'class': 'slacker_log_handler.SlackerLogHandler',
            'channel': '#rippl-logs'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['slack-error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rippl.general': {
            'handlers': ['slack-info'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
