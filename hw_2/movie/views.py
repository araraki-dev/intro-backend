from django.shortcuts import render
from .models import Movie


def get_index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movie/index.html', {'movies': movies})

def get_movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie/details.html', {'movie': movie})