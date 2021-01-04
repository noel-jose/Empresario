from django.db import models

# Create your models here.

class Participant(models.Model):
    Year = (('1','First Year'),
            ('2','Second Year'),
            ('3','Third Year'),
            ('4','Fourth Year'))

    name = models.CharField(max_length = 50,blank = False)
    email = models.EmailField(blank = False)
    phone_no = models.CharField(max_length = 12,blank = False)
    college = models.CharField(max_length = 100,blank = False)
    branch = models.CharField(max_length = 50)
    year_of_study = models.CharField(max_length = 1,choices = Year)