from django.db import models


class actor(models.Model):
    name = models.TextField(blank=True)
    def __str__(self):
        return self.name


class film(models.Model):

    director = models.TextField(blank=True,null=True)
    actors = models.ManyToManyField(actor)
    year = models.DateField(blank=True,null=True)
    imdbrating = models.FloatField(blank=True,null=True)
    imdbID = models.TextField(blank=True)
    title = models.TextField(blank=True,null=True)
    plot = models.TextField(blank=True,null=True)
    genre = models.TextField(blank=True,null=True)
    poster = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title


class serie(models.Model):
    director = models.TextField(blank=True,null=True)
    actors = models.ManyToManyField(actor)
    year = models.DateField(blank=True,null=True)
    imdbrating = models.FloatField(blank=True,null=True)
    imdbID = models.TextField(blank=True)
    title = models.TextField(blank=True,null=True)
    plot = models.TextField(blank=True,null=True)
    genre = models.TextField(blank=True,null=True)
    poster = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title



class episode(models.Model):
    date = models.DateField(blank=True)
    season = models.IntegerField(blank=True)
    episode = models.IntegerField(blank=True)
    title = models.TextField(blank=True,null=True)
    plot = models.TextField(blank=True,null=True)
    actors = models.ManyToManyField(actor)
    serie = models.ForeignKey(serie)
    def __str__(self):
        return "{0}S{1}E{2}"%(self.serie.title,self.season,self.episode)










