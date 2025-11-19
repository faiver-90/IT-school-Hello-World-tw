from src.services.queue.producer import enqueue


def process_lesson(lesson):
    enqueue.delay(
        "send_notification",
        {
            "student_id": lesson.student_id,
            "lesson_name": lesson.name,
            "message": f"Уведомление отправлено студенту {lesson.student_id} по уроку {lesson.name}",
        },
    )
