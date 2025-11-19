import os

from django.apps import AppConfig


class ProjectSchoolConfig(AppConfig):
    name = "project_school"

    def ready(self):
        # Запускать воркер только в дочернем процессе (реальном Django)
        if os.environ.get("RUN_MAIN") != "true":
            return

        from src.services.queue.worker import Worker

        worker = Worker()
        worker.start()
