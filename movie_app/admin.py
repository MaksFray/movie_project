from django.contrib import admin
from . models import Movie
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'rating', 'year', 'rating_status']
    list_editable = ['author', 'year']
    ordering = ['-rating', 'name']
    list_per_page = 10
    @admin.display(ordering='rating', description='Status')
    def rating_status(self, movie):
        if movie.rating < 50:
            return "Bad"
        elif 50 <= movie.rating < 80:
            return "Good"
        else:
            return "Fascinating"