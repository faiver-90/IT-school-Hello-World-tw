import os
from celery_app import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_school.settings")

app = Celery("project_school")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
