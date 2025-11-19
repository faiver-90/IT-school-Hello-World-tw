from celery import shared_task


@shared_task
def enqueue(task_name: str, payload: dict):
    from src.services.queue.base_queue import main_queue

    main_queue.put({"task": task_name, "payload": payload, "attempt": 0})
