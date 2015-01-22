from django.db import models

# Create your models here.
class stretch_tasks(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200,null=True)
    date = models.DateTimeField()
    text = models.CharField(max_length=1000)
    answerN = models.DecimalField(max_digits=10, decimal_places=3,null=True )
    answerL = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    answerS = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    imagelink = models.CharField(max_length=200)


class stretch_attempts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200,null=True)
    taskid = models.IntegerField()
    date = models.DateTimeField()
    answerN = models.CharField(max_length=1000,default="false")
    answerL = models.CharField(max_length=1000,default="false")
    answerS = models.CharField(max_length=1000,default="false")
#python manage.py makemigrations testsystem - for each change here
####python manage.py sqlmigrate testsystem 0001
#python manage.py migrate