from django.shortcuts import render, get_object_or_404
from .models import Movie, Author, Actor
from django.db.models import Sum, Avg, Min, Max, Count
from django.views.generic import ListView, DetailView
# Create your views here.

class ShowAllMovies(ListView):
    model = Movie
    template_name = 'movie_app/all_movies.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = super().get_queryset()
        sorted_movies = queryset.order_by('name')
        return sorted_movies

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_count'] = context['movies'].count()
        context['movies_agg'] = context['movies'].aggregate(Min('rating'), Max('rating'))
        return context

class ShowMovie(DetailView):
    template_name = 'movie_app/one_movie.html'
    model = Movie
    slug_url_kwarg = 'slug_movie'


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
    actors = Actor.objects.order_by('-last_name')
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors,
    })

def show_actor(request, id:int):
    actor = get_object_or_404(Actor, id=id)
    return render(request, 'movie_app/actor.html',{
        'actor': actor,
    })