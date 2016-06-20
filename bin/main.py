# -*- coding: utf-8 -*-
# Give wisdom to the machine,By ChangShouMeng

from tcpservice import *
from worker import *
from config import *
import signal, sys
import threading
################################################
reload(sys)
sys.setdefaultencoding("utf-8")
################################################
isContinue_event = threading.Event()
is_sigint_up = False
cur_dir = os.path.split(os.path.realpath(__file__))[0]
pidfile = os.path.join(cur_dir, "run/daemon.pid")
################################################
def sigint_handler(signum, frame):
    global is_sigint_up
    global isContinue_event
    is_sigint_up = True
    isContinue_event.set()
    print 'catched interrupt signal!'
################################################
signal.signal(signal.SIGINT, sigint_handler)
################################################
class Server(object):
    def __init__(self, pidfile,bindport,workerNum):
        #super(Server, self).__init__(pidfile)        
        self.pidfile=pidfile
        self.bindport=bindport
        self.workerNum=workerNum
        print "pidfile:",self.pidfile
        print "bindport:",self.bindport
        print "workerNum:",self.workerNum
        syncWriteLine(self.pidfile, str(os.getpid())  )

    def startWorkers(self):
        dump_log("------startWorkers---------")
        self.workers = [Worker(GlobalQueue.taskQueue, GlobalQueue.logQueue, pidfile) for i in range(self.workerNum)]
        for w in self.workers:
            w.start()

    def stopWorker(self):
        for w in self.workers:
            w.stop()

    def startListenService(self):
        dump_log("------startService---------")
        self.tcpServ = TcpAcceptorMgr(self.bindport, 1, GlobalQueue.taskQueue)
        self.tcpServ.start()

    def stopListenService(self):
        pass


    def run(self):
        print "------------run begin-------------"
        self.startWorkers()
        self.startListenService()
        self.serve_forever()
        self.stopListenService()
        self.stopWorker()
        print "------------run end---------------"

    def serve_forever(self):
        global is_sigint_up
        global isContinue_event
        while not is_sigint_up:
            try:
                isContinue_event.clear()
                isContinue_event.wait(timeout=0.01)
            except:
                pass
            if is_sigint_up:
                dump_log( "sys exit-------------")
                break
            self.tcpServ.serve_once()
            output_log()

s = Server(pidfile,5005,1)
################################################
if __name__ == '__main__':
    dump_log(__file__)       
    s.run()





