from threading import Thread
from Queue import Queue

class worker(Thread):

    class work(object):
        def __init__(self,funct,args):
            self.funct = funct
            self.args = args
        def execute(self):
            self.function(*self.args)

    work_queue = Queue()
    workers  = list()
    @classmethod
    def todo(cls,task,args=[]):
        worker.work_queue.put(worker.work(task,args))

    @classmethod
    def addWorker(cls):
        worker.workers.append(worker().start())

    @classmethod
    def removeWorker(cls):
        worker.work_queue.put("stopstop")



    def __init__(self):
        Thread.__init__(self)
    def run(self):

        while True:
            work = worker.work_queue.get()
            print work
            if work == "stopstop":
                print "Thread stoped"
                worker.workers.remove(self)
                break
            try:
                assert isinstance(work,worker.work)
                work.execute()
            except Exception as e :
                print e

