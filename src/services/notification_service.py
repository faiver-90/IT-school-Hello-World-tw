from typing import Dict, Any


def send_notification(payload: Dict[str, Any]) -> None:
    """
    Обработчик задачи уведомления.
    """
    print("[NOTIFY]", payload)
