from django.shortcuts import render, get_object_or_404
from .models import Movie, Author, Actor
from django.db.models import Sum, Avg, Min, Max, Count
# Create your views here.


def show_all_movies(request):
    movies = Movie.objects.order_by('-name')
    for movie in movies:
        movie.save()
    count = movies.count()
    agg = movies.aggregate(Min('rating'), Max('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'movies_agg': agg,
        'movies_count': count,
    })

def show_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
    })

def show_all_authors(request):
    authors = Author.objects.order_by('-last_name')
    return render(request, 'movie_app/all_authors.html',{
        'authors': authors,
    })

def show_author(request, id:int):
    author = get_object_or_404(Author, id=id)
    return render(request, 'movie_app/author.html',{
        'author': author,
    })

def show_all_actors(request):
    pass