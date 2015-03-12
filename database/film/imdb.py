import tools.tools
import tools.log
import requests
import database.film as film
import itertools

import json
import time
import random

class FilmImportError(Exception):
    pass

log = tools.log.get_log("imdb")



def getFilmsWith(string):
    _films = list()
    try:
        command = 'http://www.omdbapi.com/?s={0}&y=&plot=short&r=json&plot=full,tomatoes=true'.format(string)
        r = requests.get(command)
        jsonstring =  r.text
        jsonstring = json.loads(jsonstring)

        for i in jsonstring["Search"]:
                _film = film.film(i)
                _films.append(_film)
    except Exception as e :
        print (e)

    return _films



def getAllIndex():
    indexes = list()
    for i in itertools.combinations(["0","1","2","3","4","5","6","7","8","9"],7):
        indexes.append("tt"+"".join(i))
    return indexes




def getFilmById(ide):
    try:
        command = 'http://www.omdbapi.com/?i={0}&y=&plot=short&r=json&plot=full&tomatoes=true'.format(ide)
        print (command)
        r = requests.get(command)
        jsonstring =  r.text

        jsonstring = json.loads(jsonstring)
        _film = film.film(jsonstring)

    except Exception as e :
        print (e)





def getAllSeries():
    pass
def getSeriesEpisodes():
    pass