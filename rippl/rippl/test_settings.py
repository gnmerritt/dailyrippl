import os
from .settings import *  # noqa F403

DATABASES = {  # noqa F405
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa F405
    }
}
