from distutils.command.clean import clean
from tokenize import group
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Info(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.f_name
    

class Student(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length =30)
    group = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.f_name