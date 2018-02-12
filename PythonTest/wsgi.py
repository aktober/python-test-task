"""
WSGI config for PythonTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PythonTest.settings")

# application = get_wsgi_application()

# for Heroku
application = WhiteNoise(get_wsgi_application())