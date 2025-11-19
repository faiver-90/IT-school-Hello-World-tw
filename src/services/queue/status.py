from typing import List
from .base_queue import processing, dead, TaskItem


def get_processing() -> List[TaskItem]:
    """Возвращает список задач, находящихся в обработке."""
    return list(processing.values())


def get_dead() -> List[TaskItem]:
    """Возвращает список задач, упавших после всех ретраев."""
    return dead
