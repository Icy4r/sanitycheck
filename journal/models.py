import datetime

from django.db import models

# Create your models here.
class Interaction(models.Model):
    title = models.CharField(max_length=30)
    conversations = models.TextField()
    time = models.DateField(default=datetime.date.today)