from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    author = models.CharField(max_length=30)
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
    def get_url(self):
        return reverse('movie_detail', args=[self.slug])
    def __str__(self):
        return f"{self.name} by {self.author} - {self.rating}%"