import database.film.imdb as imdb
import tools.workers as w
import datetime,time

def printTime():
    time.sleep(0.5)
    print datetime.datetime.now()
for i in range(0, 20):
    w.worker.work_queue.put(printTime)

for e in range(0,15):
    w.worker.addWorker()

#imdb.getAllFilms()


