from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Actor(models.Model):
    MALE = "M"
    FEMALE = "F"

    GENDERS = {
        (MALE, 'Man'),
        (FEMALE, 'Woman'),
    }
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    def get_url(self):
        return reverse('actor_detail', args=[self.id])
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    def get_url(self):
        return reverse('author_detail', args=[self.id])

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
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='movies')
    budget = models.IntegerField(default=1_000_000, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(default='', null=False)
    actors = models.ManyToManyField(Actor)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])
    def __str__(self):
        return f"{self.name} by {self.author} - {self.rating}%"