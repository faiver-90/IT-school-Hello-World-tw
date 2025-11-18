from django.db import models
from django.db.models import ForeignKey

from src.student.models import Student


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    student = ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.name}"
