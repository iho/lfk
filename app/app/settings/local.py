from .base import *
INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
        ) 

# SQLite (simplest install)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'db.sqlite3'),
        'timeout': 20,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
