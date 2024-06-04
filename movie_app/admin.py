from django.contrib import admin, messages
from django.db.models import QuerySet
from . models import Movie, Author, Actor
# Register your models here.

admin.site.register(Author)
admin.site.register(Actor)

class RatingFilter(admin.SimpleListFilter):
    title = 'Rating filter'
    parameter_name = 'rating'
    def lookups(self, request, model_admin):
        return [
            ('<40','Low'),
            ('40-80', 'Medium'),
            ('>80', 'High')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value()=='<40':
            return queryset.filter(rating__lt=40)
        if self.value()=='40-80':
            return queryset.filter(rating__gte=40).filter(rating__lt=80)
        if self.value()=='>80':
            return queryset.filter(rating__gte=80)
        return queryset

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ['name', 'rating']
    #exclude = ['slug']
    #readonly_fields = ['budget']
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'rating', 'year', 'budget', 'currency', 'rating_status']
    list_editable = [ 'year', 'budget', 'currency']
    filter_horizontal = ['actors']
    ordering = ['-rating', 'name']
    list_per_page = 10
    actions = ['set_rubles', 'set_euro',]
    search_fields = ['name', 'rating']
    list_filter = ['name', RatingFilter, 'year']
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