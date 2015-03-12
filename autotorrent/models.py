from django.db import models

class film(models.Model):

    director = models.TextField()
    actors = models.ManyToOneRel()
    year = models.DateField()
    imdbrating = models.IntegerField()
    imdbID = models.TextField()
    tomatoes = models.IntegerField()
    title = models.TextField()
    plot = models.TextField()

class serie(film):
    pass

class actor(models.Model):
    name = models.TextField()


class episode(models.Model):
    date = models.DateField()
    season = models.IntegerField()
    episode = models.IntegerField()



