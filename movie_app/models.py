from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = {
        EUR: 'Euro',
        USD: 'Dollars',
        RUB: 'Rubles',
    }

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    author = models.CharField(max_length=30)
    budget = models.IntegerField(default=1_000_000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
    def get_url(self):
        return reverse('movie_detail', args=[self.slug])
    def __str__(self):
        return f"{self.name} by {self.author} - {self.rating}%"