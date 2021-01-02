from django.db import models

# Create your models here.

class Event(models.Model):
    EVENT_TYPES = (('S','Single'),('T','Team'))

    name = models.CharField(max_length = 50,blank = False)
    desc = models.CharField(max_length = 150,blank = False)
    event_date = models.DateField()
    event_type = models.CharField(max_length=1,choices = EVENT_TYPES)

