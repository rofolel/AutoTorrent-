
import tools.taskforce
import tools.tools
import database.film.imdb as imdb
import tools.log as log
import autotorrent.models as models


class motherShip(object):
    def __init__(self):
        self.log = log.get_log("mothership")
        for _ in  range(0,20):
            tools.taskforce.worker.addWorker()
        self.loadData()

    def loadFilmDB(self):
        self.log.info("starting IMDB importation in background")
        for stri in imdb.getAllIndex():
            tools.taskforce.worker.todo(self.loadID,[stri])

    def loadFilm(self,stri):
        tools.taskforce.worker.todo(self.addFilms,[stri])


    def loadData(self):
        self.films = models.film.objects.all()
        self.series = models.serie.objects.all()

    def loadID(self,ide):
        imdb.getFilmById(ide)
