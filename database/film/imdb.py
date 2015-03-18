import random
import json
import time
from datetime import datetime
from math import floor, ceil
import requests

import tools.tools
import tools.log
import autotorrent.models as models


class FilmImportError(Exception):
    pass

log = tools.log.get_log("imdb")


def getAllIndex(incr,div):
    indexes = list()
    min = (99999999/div)*incr
    max = (99999999/div)*(incr+1)
    for i in range(floor(min),ceil(max)):
        indexes.append("tt"+str(i).zfill(8))
    random.shuffle(indexes)
    return indexes




def getFilmById(ide):
        if models.film.objects.all().filter(imdbID=ide):
            return
        command = 'http://www.omdbapi.com/?i={0}&y=&plot=short&r=json&plot=full'.format(ide)
        r = requests.get(command)
        jsonstring =  r.text.replace("N/A" , "")
        if 'Error' in jsonstring:
            return
        filmdic = json.loads(jsonstring)


        if filmdic["Type"] == "movie":
            _film = loadFilm(filmdic)
        elif filmdic["Type"] == 'series' :
            _film = loadSerie(filmdic)
        elif filmdic["Type"] == 'serie' :
            _film = loadSerie(filmdic)
        else:
            _film = loadEpisode(filmdic)
        _film.save()
        actors = filmdic["Actors"].split(',')
        for act in actors:
            _actor = loadActor(act)
            _actor.save()
            _film.actors.add(_actor)
        print ('added %s'%(_film.title))
        _film.save()
        time.sleep(random.randint(0,5)/7)

def loadActor(actor):
    actor = actor.strip()
    tab = models.actor.objects.all().filter(name=actor)
    if len(tab) > 0:
        return tab[0]
    else:
        act = models.actor()
        act.name = actor
        return act





def loadFilm(filmdic):
        _film = models.film()
        _film.title = filmdic['Title']
        _film.director = filmdic['Director']
        _film.imdbID = filmdic['imdbID']
        try:
            _film.imdbrating = filmdic['imdbRating']
        except:
            _film.imdbrating = None
            pass

        try:
            _film.year = datetime.strptime( filmdic['Year'],"%Y")
        except:
            _film.year = None
            pass
        _film.genre = filmdic['Genre']
        _film.plot = filmdic['Plot']
        return _film

def loadSerie(filmdic):
        _serie = models.serie()
        _serie.title = filmdic['Title']
        _serie.director = filmdic['Director']
        _serie.imdbID = filmdic['imdbID']
        try:
            _serie.imdbrating = filmdic['imdbRating']
        except:
            _serie.imdbrating = None
            pass
        try:
            _serie.year = datetime.strptime( filmdic['Year'],"%Y")
        except:
            _serie.year = None
            pass
        _serie.genre = filmdic['Genre']
        _serie.plot = filmdic['Plot']
        return _serie

def loadEpisode(filmdic):
    _episode = models.episode()
    if filmdic['seriesID'] != '':
        tab = models.serie.objects.all().filter(imdbID=filmdic['seriesID'])
        if len(tab) > 0:
            _episode.serie = tab[0]
        else:
            tab = models.serie.objects.all().filter(imdbID=filmdic['seriesID'])
            getFilmById(filmdic['seriesID'])
            _episode.serie = tab[0]
    else:
        return
    try:
        _episode.date = datetime.strptime(filmdic['Released'],"%d %b %Y").strftime("%Y-%m-%d")
    except:
        _episode.date = None

    _episode.plot = filmdic['Plot']
    _episode.title = filmdic['Title']
    _episode.episode = filmdic['Episode']
    _episode.season = filmdic['Season']
    return _episode

    pass



def getAllSeries():
    pass
def getSeriesEpisodes():
    pass