from .models import Movie

def slider_movie(request):
    movies = Movie.objects.all().order_by('created')[0:3]
    return {'slider_movie': movies}