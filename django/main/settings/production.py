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


# Logging

LOGFILE_ROOT = pathlib.Path(os.getenv('LOGS_ROOT', BASE_DIR / 'logs'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(pathname)s:%(lineno)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'django.debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE_ROOT / 'django_debug.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
            'filters': ['debug'],
        },
        'django.info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE_ROOT / 'django_info.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
            'filters': ['info'],
        },
        'django.error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE_ROOT / 'django_error.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
            'filters': ['error'],
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['django.debug', 'django.info', 'django.error'],
            'propagate': True,
        },
        'main': {
            'level': 'DEBUG',
            'handlers': ['django.debug', 'django.info', 'django.error'],
            'propagate': True,
        },
    },
}

logging.config.dictConfig(LOGGING)
