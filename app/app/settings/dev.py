from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATIC_ROOT = join(PROJECT_ROOT, '..', 'public', 'static')
MEDIA_ROOT = join(PROJECT_ROOT, '..', 'public', 'media')

try:
    from .local import *
except ImportError:
    pass
