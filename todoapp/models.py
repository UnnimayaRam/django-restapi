from datetime import datetime


from django.db import models

import calendar

# Create your models here.
class Todo(models.Model):
    tid=models.IntegerField()
    event = models.CharField(max_length=20)
    date=models.DateField()
    description=models.TextField(max_length=50)