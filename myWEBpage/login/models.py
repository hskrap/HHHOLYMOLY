from django.db import models

# Create your models here.
class Info(models.Model):
    no = models.CharField(max_length=7)
    name = models.CharField(max_length=10)