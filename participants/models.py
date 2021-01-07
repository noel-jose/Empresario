from django.db import models

from events.models import Event

# Create your models here.

class Participant(models.Model):

    Year = (('1','First Year'),
            ('2','Second Year'),
            ('3','Third Year'),
            ('4','Fourth Year'))
     
    Branch = (('CSE','Computer Science Engineering'),
              ('ECE','Elelctronics and Communication'),
              ('EEE','Electrical Engineering'),
              ('MECH','Mechanical Engineering'),
              ("CIVIL","Civil Engineering"),
              ("IT",'Information Technology'),
              ("AUTO",'Automobile Engineering'),
              ("CHM","Chemical Engineering"))

    name = models.CharField(max_length = 50,blank = False)
    email = models.EmailField(blank = False)
    phone_no = models.CharField(max_length = 12,blank = False)
    college = models.CharField(max_length = 100,blank = False)
    department = models.CharField(max_length = 50,choices = Branch)
    year_of_study = models.CharField(max_length = 1,choices = Year)
    registered_event = models.ForeignKey(Event, on_delete=models.PROTECT,null = True)

    def __str__(self):
            return self.name
