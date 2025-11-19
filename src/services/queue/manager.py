from src.services.notification_service import send_notification

TASKS = {
    "send_notification": send_notification,
}


def execute(task_name: str, payload: dict):
    if task_name not in TASKS:
        raise ValueError("Unknown task: " + task_name)
    return TASKS[task_name](payload)
