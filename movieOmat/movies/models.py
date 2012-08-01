from django.db import models

# Create your models here.
class Actor(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    def __unicode__(self):
        return self.firstname + " " + self.lastname

class Movie(models.Model):
    Actor = models.ManyToManyField(Actor)
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    def __unicode__(self):
        return self.name