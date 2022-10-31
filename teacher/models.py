from django.db import models

# Create your models here.

class Teacher(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length =30)
    group = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.f_name
    

class SeniorTeacher(models.Model):
    name = models.CharField(max_length=30)
    possition = models.CharField(max_length=30)
    gread = models.CharField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self):
        return self.gread #represent the admin panel line titel.


class JuniorTeacher(models.Model):
    name = models.CharField(max_length=30)
    senior = models.ForeignKey(SeniorTeacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name