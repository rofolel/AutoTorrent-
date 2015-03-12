from threading import Thread
from queue import Queue
import tools.log as log
class worker(Thread):
    log = log.get_log("Taskforce")
    class work(object):
        def __init__(self,funct,args):
            self.funct = funct
            self.args = args
        def execute(self):
            self.funct(*self.args)

    tasks = Queue()
    taskforce  = list()
    @classmethod
    def todo(cls,task,args=[]):
        worker.tasks.put(worker.work(task,args))

    @classmethod
    def addWorker(cls):
        worker.taskforce.append(worker().start())

    @classmethod
    def removeWorker(cls):
        worker.tasks.put("stopstop")



    def __init__(self):
        Thread.__init__(self)
    def run(self):

        while True:
            work = worker.tasks.get()
            if work.funct == "stopstop":
                break
            try:
                work.execute()
            except Exception as e :
                worker.log.warning(str(e))


        worker.taskforce.remove(self)
