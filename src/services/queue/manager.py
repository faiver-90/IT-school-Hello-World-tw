from typing import Dict, Callable, Any

from src.services.notification_service import send_notification


TaskHandler = Callable[[Dict[str, Any]], None]

TASKS: Dict[str, TaskHandler] = {
    "send_notification": send_notification,
}


def execute(task_name: str, payload: Dict[str, Any]) -> None:
    """
    Выполняет задачу по имени. Бросает ValueError, если задача не зарегистрирована.
    """
    if task_name not in TASKS:
        raise ValueError(f"Unknown task: {task_name}")
    handler = TASKS[task_name]
    handler(payload)
