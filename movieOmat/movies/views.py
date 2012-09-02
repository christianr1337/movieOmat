# Create your views here.
from django.http import HttpResponse, Http404
from movies.models import Movie, Actor
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    latest_movie_list = Movie.objects.all().order_by('-publication')[:5]
    
    return render_to_response('movies/index.html', {'latest_movie_list': latest_movie_list})
    
def detail(request, movie_id):

    try:
        m = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404
    return render_to_response('movies/detail.html', {'movie': m}, context_instance=RequestContext(request))

def results(request, movie_id):
    return HttpResponse("You're looking at the results of movie %s." % movie_id)

def actor(request, actor_id):
    try:
        a = Actor.objects.get(pk=actor_id)
        #a = Movie.objects.filter(pk=actor_id)
    except Movie.DoesNotExist:
        raise Http404
    return render_to_response('movies/actor.html', {'actor': a}, context_instance=RequestContext(request))