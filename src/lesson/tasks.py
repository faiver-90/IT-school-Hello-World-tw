from celery import shared_task


@shared_task
def send_notification_start_lesson(student_id, lesson_name):
    return f"Уведомление отправлено студенту {student_id} по уроку {lesson_name} - начало"

@shared_task
def send_notification_end_lesson(student_id, lesson_name):
    return f"Уведомление отправлено студенту {student_id} по уроку {lesson_name} - конец"
