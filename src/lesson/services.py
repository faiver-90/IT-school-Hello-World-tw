from typing import Dict, Any
from src.lesson.models import Lesson
from src.services.queue.producer import enqueue


def process_lesson(lesson: Lesson) -> None:
    """
    Формирует payload и отправляет событие в очередь.
    """

    payload: Dict[str, Any] = {
        "student_id": lesson.student.id,
        "lesson_name": lesson.name,
        "message": f"Уведомление отправлено студенту {lesson.student.id} по уроку {lesson.name}",
    }

    enqueue.delay("send_notification", payload)
