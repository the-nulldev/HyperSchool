from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    about = models.TextField()
    objects = models.Manager()


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=1000)
    duration_months = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    teacher = models.ManyToManyField(Teacher)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)
    objects = models.Manager()

    def __str__(self):
        return self.name

