'''
Created on Jul 26, 2012

@author: c1337b
'''
from movies.models import Movie, Actor, Comment, Language, Regisseur
from django.contrib import admin

admin.site.register(Comment)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Language)
admin.site.register(Regisseur)
