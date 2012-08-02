'''
Created on Jul 26, 2012

@author: c1337b
'''
from movies.models import Movie, Actor
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information',      {'fields': ['name']}),
        ('Rating',           {'fields': ['rating']}),
        (None,               {'fields': ['actors']}),
        (None,               {'fields': ['publication']}),
    ]
    list_display = ('name', 'rating', 'publication')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        