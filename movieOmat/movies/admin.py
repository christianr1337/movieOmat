'''
Created on Jul 26, 2012

@author: c1337b
'''
from movies.models import Movie, Actor, Comment, Language, Regisseur
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information',      {'fields': ['name']}),
        ('Rating',           {'fields': ['rating']}),
        (None,               {'fields': ['actors']}),
        (None,               {'fields': ['regisseur']}),
        (None,               {'fields': ['publication']}),
        (None,               {'fields': ['seen']}),
        (None,               {'fields': ['description']}),
        (None,               {'fields': ['length']}),
        (None,               {'fields': ['languages']}),
    ]
    list_display = ('name', 'rating', 'publication')
    
class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Language)
admin.site.register(Regisseur)

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        