from django.contrib import admin
from . models import Movie
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'rating', 'year']
    list_editable = ['author', 'year']
    ordering = ['-rating', 'name']
    list_per_page = 10