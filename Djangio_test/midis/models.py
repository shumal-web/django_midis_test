from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    year_of_exp = models.IntegerField()
    working_field = models.CharField(max_length=100)

