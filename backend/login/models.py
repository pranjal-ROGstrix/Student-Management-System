from django.db import models

# Create your models here.


class login(models.Model):
    lib_id = models.CharField(max_length=10)
    password = models.CharField(max_length=16, default='student')
    name = models.CharField(max_length=20, default="teacher")


class student(models.Model):
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    lib_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=16, default='student')
    course = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    sec = models.CharField(max_length=5)
    status = models.CharField(max_length=15, default="active")
    email = models.CharField(max_length=30)