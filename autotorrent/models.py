from django.db import models


class actor(models.Model):
    name = models.TextField()

class film(models.Model):

    director = models.TextField()
    actors = models.ManyToManyField(actor)
    year = models.DateField()
    imdbrating = models.IntegerField()
    imdbID = models.TextField()
    tomatoes = models.IntegerField()
    title = models.TextField()
    plot = models.TextField()

class serie(film):
    pass


class episode(models.Model):
    date = models.DateField()
    season = models.IntegerField()
    episode = models.IntegerField()
    serie = models.ForeignKey(serie)










