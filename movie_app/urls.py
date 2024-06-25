from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "My admin panel"
admin.site.index_title = "My super admin panel"

urlpatterns = [
    path('', views.ShowAllMovies.as_view()),
    path('authors', views.ShowAllAuthors.as_view()),
    path('actors', views.ShowAllActors.as_view()),
    path('authors/<int:pk>', views.ShowAuthor.as_view(), name='author_detail'),
    path('actors/<int:pk>', views.ShowActor.as_view(), name='actor_detail'),
    path('<slug:slug_movie>', views.ShowMovie.as_view(), name='movie_detail'),
]