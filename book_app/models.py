from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=70)
    rating = models.IntegerField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} - {self.rating}%"