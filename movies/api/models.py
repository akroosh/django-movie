from django.db import models
from datetime import date

# Create your models here.
class Genre(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    slug = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField("Title", max_length = 100)
    description = models.TextField("Description", null = True)
    poster = models.ImageField("Постер", upload_to="movies/upload_to", null = True)
    year = models.PositiveSmallIntegerField("Relese date", default=2020, null = True)
    country = models.CharField("Country", max_length=30, null = True)
    world_premiere = models.DateField("Premiere", default=date.today, null = True)
    budget = models.PositiveIntegerField("Budget", default=0, null = True)
    fees_in_world = models.PositiveIntegerField("Fess in the world", default=0, null = True)
    slug = models.CharField(max_length = 100, blank = True)
    genres = models.ManyToManyField(Genre, related_name='movies')

    
    def __str__(self):
        return self.title
