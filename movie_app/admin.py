from django.contrib import admin, messages
from django.db.models import QuerySet
from . models import Movie
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'rating', 'year', 'budget', 'currency', 'rating_status']
    list_editable = ['author', 'year', 'budget', 'currency']
    ordering = ['-rating', 'name']
    list_per_page = 10
    actions = ['set_rubles', 'set_euro',]
    @admin.display(ordering='rating', description='Status')
    def rating_status(self, movie):
        if movie.rating < 50:
            return "Bad"
        elif 50 <= movie.rating < 80:
            return "Good"
        else:
            return "Fascinating"

    @admin.action(description="Set currency to rubles")
    def set_rubles(self, request, qs: QuerySet):
        qs.update(currency=Movie.RUB)

    @admin.action(description="Set currency to euro")
    def set_euro(self, request, qs: QuerySet):
        count_updates = qs.update(currency=Movie.RUB)
        self.message_user(
            request,
            f'{count_updates} carts was updated',
            messages.ERROR
        )