from django.db import models

class Actor(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    birthday = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return self.firstname + " " + self.lastname
    
class Regisseur(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    birthday = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return self.firstname + " " + self.lastname
    
class Language (models.Model):
    language = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.language

class Movie(models.Model):
    regisseur = models.ForeignKey(Regisseur)
    actors = models.ManyToManyField(Actor)
    name = models.CharField(max_length=50)
    rating = models.IntegerField(blank=True, null=True)
    publication = models.DateTimeField(blank=True, null=True)
    seen = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True) #TODO besser anderes format
    languages = models.ManyToManyField(Language)
    
    def __unicode__(self):
        return self.name
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
