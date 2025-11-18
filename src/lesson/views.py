from rest_framework import generics

from src.lesson.models import Lesson
from src.lesson.serializers import LessonSerializer
from src.lesson.tasks import (
    send_notification_start_lesson,
    send_notification_end_lesson,
)


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.select_related("student").all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        lesson = serializer.save()
        send_notification_start_lesson.delay(lesson.student_id, lesson.name)


class LessonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.select_related("student").all()
    serializer_class = LessonSerializer

    def perform_destroy(self, serializer):
        lesson = serializer.save()
        send_notification_end_lesson.delay(lesson.student_id, lesson.name)
