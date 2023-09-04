from django.db import models
class student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    school = models.CharField(max_length=200)

# Create your models here.
