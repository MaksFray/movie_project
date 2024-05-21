from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "My admin panel"
admin.site.index_title = "My super admin panel"

urlpatterns = [
    path('', views.show_all_movies),
    path('<slug:slug_movie>', views.show_movie, name='movie_detail'),
]