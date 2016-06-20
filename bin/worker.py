# -*- coding: utf-8 -*-:

import os,time
from syncfile import *
from task import * 
import Queue
import multiprocessing as mp
import traceback
from config import *

class Worker(mp.Process):    
    def __init__(self, task_queue, logQueue,pidfile):
        mp.Process.__init__(self)
        self.task_queue=task_queue
        self.logQueue=logQueue
        self.pidfile=pidfile
        self.isStop=False
        self.ownerpid=""

    def dump_log(self,info):
        text="Worker[{0}] {1}".format(self.ownerpid,info)
        self.logQueue.put(text)
        
    def stop(self):
        self.isStop=True

    def run(self):
        self.ownerpid = str(os.getpid())
        self.dump_log( "start.." )
        syncWriteLine(self.pidfile,self.ownerpid)
        proc_name = self.name
        while not self.isStop:           
            try:
                t = self.task_queue.get()
                if  isinstance(t, Task):
                    t.logQueue=self.logQueue
                    t.workerid=self.ownerpid
                    t.doTask()                
                else:
                    info= "Worker run,but TypeError:{0}".format( type(t) )
                    self.dump_log(info)
                    #print traceback.format_exc()
            except Queue.Empty:
                #print 'queue empty'
                time.sleep(0.01)
                pass
        self.dump_log( "worker end..")

            
 
        #return       
        
#class MyTask(Task):
#    def doTask(self):    
#        print ("taskName={0} taskData_data={1}".format(self.taskName ,self.taskData) )    
#
#
#def test():
#    tasks = multiprocessing.JoinableQueue()
#    results = multiprocessing.Queue()
#    workerNum=2
#    workers = [ Worker(tasks, results) for i in range(workerNum) ]
#    for w in workers:
#        w.start()
#
#    t=MyTask("action111","11111112222222 23")
#    tasks.put(t)
#        
#    t=MyTask("action22","ssssss2222 AA dd")
#    tasks.put(t)    
#    pass
#
#
#test()        
