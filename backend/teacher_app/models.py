from django.db import models

from django.contrib.auth.models import User
from student_app.models import Student

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)

class Course(models.Model):
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    course_title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, null=True, blank=True)
    course_description = models.TextField(max_length=200)

class Assignmet(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

