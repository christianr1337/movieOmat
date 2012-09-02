from movies.models import Movie

def latest_movie_list(request):
    latest_movie_list = Movie.objects.all().order_by('-publication')[:5]
    
    return {"latest_movie_list" : latest_movie_list}