import os

from django.utils.version import get_version


# Settings

MODE = os.getenv('MODE')

if MODE == 'production':
    from main.settings.production import *
elif MODE == 'staging':
    from main.settings.staging import *
else:
    from main.settings.development import *

# Secret key

SECRET_KEY = os.getenv('SECRET_KEY', '')
if not SECRET_KEY:
    if not (BASE_DIR / '..' / 'SECRET_KEY').exists():
        from django.core.management.utils import get_random_secret_key
        SECRET_KEY = get_random_secret_key()
        with open(BASE_DIR / '..' / 'SECRET_KEY', 'w') as file:
            file.write(SECRET_KEY)
    with open(BASE_DIR / '..' / 'SECRET_KEY', 'r') as file:
        SECRET_KEY = file.read().strip()


# Applications

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
