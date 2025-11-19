from rest_framework import generics
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Student
from .serializers import StudentSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Список студентов",
        description="Возвращает всех студентов.",
        tags=["Students"],
    ),
    post=extend_schema(
        summary="Создать студента",
        description="Добавляет нового студента.",
        tags=["Students"],
    ),
)
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@extend_schema_view(
    get=extend_schema(summary="Получить данные студента", tags=["Students"]),
    patch=extend_schema(summary="Изменить данные студента", tags=["Students"]),
    delete=extend_schema(summary="Удалить данные студента", tags=["Students"]),
    put=extend_schema(
        summary="Изменить данные студента",
        tags=["Lessons"],
    ),
)
class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
