"""
WSGI config for locallibrary project on PythonAnywhere.

This module contains the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/Django-local-library-demo'  # Replace with your actual path
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings_pythonanywhere')

application = get_wsgi_application()
