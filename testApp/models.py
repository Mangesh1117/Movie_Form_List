from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=15)
    genre = models.CharField(max_length=10)
    director = models.CharField(max_length=20)
    actor = models.CharField(max_length=20)
    actress = models.CharField(max_length=20)
    rdate = models.DateField()
    language = models.CharField(max_length=10)
    rating = models.CharField(max_length=1)
