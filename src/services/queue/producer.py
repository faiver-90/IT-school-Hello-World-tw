from typing import Dict, Any
from celery import shared_task


@shared_task
def enqueue(task_name: str, payload: Dict[str, Any]) -> None:
    """
    Кладёт задачу в in-memory очередь.
    """
    from src.services.queue.base_queue import main_queue, TaskItem

    item: TaskItem = {
        "task": task_name,
        "payload": payload,
        "attempt": 0,
    }

    main_queue.put(item)
