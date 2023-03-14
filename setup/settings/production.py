import environ

from .base import *

# read .env file in this directory.
environ.Env.read_env()

env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # read os.environ['SQLITE_URL']
    'default': env.db('SQLITE_URL')
}
# add a custom name for test database
DATABASES['default'].update({'TEST': {'NAME': 'test_setup_db'}})

# # HTTPS
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# # HTTP Strict Transport Security
# SECURE_HSTS_SECONDS = 3600
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
