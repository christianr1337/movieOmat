from django.db import models

#Actor
class Actor(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    birthday = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return self.firstname + " " + self.lastname

#Director
class Regisseur(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    birthday = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return self.firstname + " " + self.lastname
    
#Language
class Language (models.Model):
    language = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.language

#Joint Model Movie
class Movie(models.Model):
    name = models.CharField(max_length=50)
    imdb_name = models.CharField(max_length=50)
    in_folder = models.CharField(max_length=200)
    languages = models.CharField(max_length=50) #TODO zu model languages mappen
    quality = models.CharField(max_length=50)
    imdb_rating = models.IntegerField(blank=True, null=True)  # TODO: float
    rating = models.IntegerField(blank=True, null=True)  # TODO: float
    seen = models.DateTimeField(blank=True, null=True)
    regisseur = models.ForeignKey(Regisseur, blank=True, null=True)
    actors = models.ManyToManyField(Actor, blank=True, null=True)
    publication = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True) #laenge in min

    def __unicode__(self):
        return self.name

#Comment
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
