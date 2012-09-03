from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     
    url(r'^movies/$', 'movies.views.index'),
    url(r'^movies/alpha/(?P<movie_letter>\w+)/$', 'movies.views.indexLetter'),
    url(r'^movies/search/$', 'movies.views.search'),
    url(r'^movies/(?P<movie_id>\d+)/$', 'movies.views.detail'),
    url(r'^movies/(?P<movie_id>\d+)/results/$', 'movies.views.results'),
    
    url(r'^actors/(?P<actor_id>\d+)/$', 'movies.views.actor'),
)
