from rest_framework import generics

from src.lesson.models import Lesson
from src.lesson.serializers import LessonSerializer
from src.lesson.services import process_lesson


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.select_related("student").all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        lesson = serializer.save()
        process_lesson(lesson)


class LessonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.select_related("student").all()
    serializer_class = LessonSerializer

    def perform_update(self, serializer):
        old_lesson = self.get_object()
        new_lesson = serializer.save()

        if old_lesson.end != new_lesson.end:
            process_lesson(new_lesson)
