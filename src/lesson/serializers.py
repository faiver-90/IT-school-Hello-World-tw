from src.lesson.models import Lesson
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer[Lesson]):
    class Meta:
        model = Lesson
        fields = "__all__"
