# Create your views here.
from django.http import HttpResponse, Http404
from movies.models import Movie, Actor
from django.shortcuts import render_to_response
from django.template import RequestContext
import string
from movies.util import get_query

def index(request):
    latest_movie_list = Movie.objects.all().order_by('-publication')[:5]
    
    allTheLetters = string.uppercase
    
    return render_to_response('movies/index.html', {'latest_movie_list': latest_movie_list, 'letters': allTheLetters}, context_instance=RequestContext(request))
    
def indexLetter(request, movie_letter):
    all_movies_with_letter = Movie.objects.filter(name__istartswith=movie_letter)
    allTheLetters = string.uppercase
    
    return render_to_response('movies/indexLetter.html', {'movie_letter': movie_letter, 'all_movies_with_letter': all_movies_with_letter, 'letters': allTheLetters}, context_instance=RequestContext(request))
    
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

#TODO: bessere Suche ueber ALLE Models und attribute einfuegen
def search(request): 
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        movies = Movie.objects.filter(name__icontains=q)
        actors = Actor.objects.filter(lastname__icontains=q)
        first_name_actors =  Actor.objects.filter(firstname__icontains=q) # TODO: besser machen
        return render_to_response('movies/search_results.html',
            {'movies': movies, 'actors': actors, 'first_name_actors': first_name_actors, 'query': q}, context_instance=RequestContext(request))
    else:
        return HttpResponse('Please submit a search term.')
