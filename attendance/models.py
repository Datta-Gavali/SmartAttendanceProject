from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
