from __future__ import absolute_import
import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject', broker='django://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
