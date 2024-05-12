from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('<slug:slug_movie>', views.show_movie, name='movie_detail'),
]