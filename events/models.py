from django.db import models

# Create your models here.

class Event(models.Model):
    EVENT_TYPES = (('S','Single'),('T','Team'))

    name = models.CharField(max_length = 50,blank = False)
    description = models.CharField(max_length = 500,blank = False)
    event_start_date = models.DateTimeField(auto_now=False )
    event_end_date = models.DateTimeField(auto_now=False)
    event_type = models.CharField(max_length=1,choices = EVENT_TYPES)
    registration_fee = models.IntegerField(blank = False,default = 100)
    prize_amount = models.IntegerField(blank = False,default = 1000)
    event_image = models.FileField(blank = True,max_length =100,upload_to ='static/images',null = True)

    def __str__(self):
        return self.name

    




