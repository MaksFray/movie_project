from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "My admin panel"
admin.site.index_title = "My super admin panel"

urlpatterns = [
    path('', views.ShowAllMovies.as_view()),
    path('authors', views.show_all_authors),
    path('actors', views.show_all_actors),
    path('authors/<int:id>', views.show_author, name='author_detail'),
    path('actors/<int:id>', views.show_actor, name='actor_detail'),
    path('<slug:slug_movie>', views.ShowMovie.as_view(), name='movie_detail'),
]