from django.db import models

from users.models import TaskUser

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(TaskUser,on_delete=models.CASCADE)
