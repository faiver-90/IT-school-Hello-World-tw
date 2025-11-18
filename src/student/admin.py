from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "student_id"]
    search_fields = ["name", "student_id"]
    ordering = ["id"]
