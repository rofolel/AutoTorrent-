
import tools.taskforce
import tools.tools
import database.film.imdb as imdb
import tools.log as log
import autotorrent.models as models
class motherShip(object):
    def __init__(self):
        self.log = log.get_log("mothership")
        for _ in  range(0,40):
            tools.taskforce.worker.addWorker()
        self.loadData()

    def loadFilmDB(self,inc=0,val=10000):

        self.log.info("IMDB importation in background {0}%".format(inc/val))
        for stri in imdb.getAllIndex(inc,val):
             tools.taskforce.worker.todo(self.loadID,[stri])
        if inc < val:
            tools.taskforce.worker.todo(self.loadFilmDB,[inc+1,val])

    def loadFilm(self,stri):
        tools.taskforce.worker.todo(self.addFilms,[stri])


    def loadData(self):
        self.films = models.film.objects.all()
        self.series = models.serie.objects.all()

    def loadID(self,ide):
        imdb.getFilmById(ide)

    def workload(self):
        self.log.info("current work load: {0}".format(tools.taskforce.worker.tasks.qsize()))