from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_id = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)



