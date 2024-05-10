from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} by {self.author} - {self.rating}%"