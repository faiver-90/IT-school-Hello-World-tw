from rest_framework import generics
from drf_spectacular.utils import extend_schema, extend_schema_view

from src.lesson.models import Lesson
from src.lesson.serializers import LessonSerializer
from src.lesson.services import process_lesson


@extend_schema_view(
    get=extend_schema(
        summary="Список занятий",
        description="Возвращает список всех занятий вместе с данными студента.",
        tags=["Lessons"],
    ),
    post=extend_schema(
        summary="Создать занятие",
        description="Создаёт новое занятие и запускает процессинг (process_lesson).",
        tags=["Lessons"],
    ),
)
class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.select_related("student").all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        lesson = serializer.save()
        process_lesson(lesson)


@extend_schema_view(
    get=extend_schema(
        summary="Получить занятие",
        tags=["Lessons"],
    ),
    patch=extend_schema(
        summary="Изменить занятие",
        description="Если поле end изменилось — запускается process_lesson.",
        tags=["Lessons"],
    ),
    delete=extend_schema(
        summary="Удалить занятие",
        tags=["Lessons"],
    ),
    put=extend_schema(
        summary="Изменить частично занятие",
        tags=["Lessons"],
    ),
)
class LessonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.select_related("student").all()
    serializer_class = LessonSerializer

    def perform_update(self, serializer):
        old_lesson = self.get_object()
        new_lesson = serializer.save()
        if old_lesson.end != new_lesson.end:
            process_lesson(new_lesson)
