from django.db import models

# Create your models here.

class T_ser(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)


class Users(models.Model):
    title = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    add_time = models.DateField(auto_now=True)
    content = models.TextField(30)