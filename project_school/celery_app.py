from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_school.settings")

app = Celery("project_school")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect
def start_inmemory_worker(sender, **kwargs):
    from src.services.queue.worker import Worker

    w = Worker()
    w.start()
    print(">>> In-memory queue worker running inside Celery worker")
