from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=1000)
