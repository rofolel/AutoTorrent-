import json
import unicodedata
class film(object):
    def __init__(self,dic):
        for i in dic:
            self.__dict__[str(i)] = dic[i]
            if i == "imdbID":
                print (len(dic[i]))

    def __str__(self):
        return str(self.__dict__)




class filmDB(object):
    films = dict()
    @classmethod
    def addFilm(cls,_film):
        filmDB.films[_film.Title] = _film

