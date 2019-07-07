from django.db import models
from django.utils.timezone import now
import datetime
# Create your models here.

class Todolist(models.Model):
    task = models.CharField(max_length=60, null=False)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(default=now)
