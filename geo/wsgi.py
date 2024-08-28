"""
WSGI config for geo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('/Users/manoel.dantas/Documents/curso_django/geo_root/geo')
sys.path.append('/Users/manoel.dantas/Documents/curso_django/geo_root')

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('PYTHONPATH','/Users/manoel.dantas/miniforge3/lib/python3.10/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geo.settings')

application = get_wsgi_application()
