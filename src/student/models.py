from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    student_id = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.student_id})"