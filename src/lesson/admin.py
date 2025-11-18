from django.contrib import admin

from src.lesson.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "start", "end"]
    search_fields = ["name"]
    ordering = ["start"]
