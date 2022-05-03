from django.db import models

# Create your models here.

class Organizer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Event(models.Model):
    name = models.CharField(max_length=200) 
    place = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    event_datetime = models.DateTimeField('date event')
    price = models.IntegerField(default=0)
    organizer = models.ForeignKey(Organizer, on_delete = models.CASCADE)

