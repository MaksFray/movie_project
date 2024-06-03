from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "My admin panel"
admin.site.index_title = "My super admin panel"

urlpatterns = [
    path('', views.show_all_movies),
    path('authors', views.show_all_authors),
    path('/actors', views.show_all_actors),
    path('authors/<int:id>', views.show_author, name='author_detail'),
    path('<slug:slug_movie>', views.show_movie, name='movie_detail'),
]