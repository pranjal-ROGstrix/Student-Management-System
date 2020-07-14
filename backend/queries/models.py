from django.db import models
from login.models import student
# Create your models here.


class queries(models.Model):
    query = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    key = models.ForeignKey('login.student', on_delete=models.CASCADE)
    status = models.CharField(default="active", max_length=10)
