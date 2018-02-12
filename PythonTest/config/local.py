from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eqmlgfusosv-kx8*%-yh=7h*ux^z*)bo(lx596l&17uv%$2pi1'


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pythontest',
        'USER': 'postgres',
        'PASSWORD': '',
    }
}

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))