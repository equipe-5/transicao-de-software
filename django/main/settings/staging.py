import os

from main.settings.main import *

DEBUG = False


# HTTPS

ALLOWED_HOSTS = [
    os.getenv('PUBLIC_IP', '0.0.0.0'),
    os.getenv('PUBLIC_URL', 'localhost'),
]

CSRF_TRUSTED_ORIGINS = [
    'http://django:80',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True


# Static and media files

STATIC_ROOT = os.getenv('STATIC_ROOT')

MEDIA_ROOT = os.getenv('MEDIA_ROOT')
