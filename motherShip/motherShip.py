
import tools.taskforce
import tools.tools
import database.film.film as film
import database.film.imdb as imdb
import tools.log as log
class motherShip(object):
    def __init__(self):
        self.log = log.get_log("mothership")
        for _ in  range(0,20):
            tools.taskforce.worker.addWorker()
        self.films = film.filmDB.films

    def loadFilmDB(self):
        self.log.info("starting IMDB importation in background")
        for stri in imdb.getAllIndex():
            tools.taskforce.worker.todo(self.loadID,[stri])

    def loadFilm(self,stri):
        tools.taskforce.worker.todo(self.addFilms,[stri])

    def addFilms(self,stri):
        f = imdb.getFilmsWith(stri)
        for i in f :
            film.filmDB.addFilm(i)


    def loadID(self,ide):
        imdb.getFilmById(ide)
