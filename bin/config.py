# -*- coding: utf-8 -*-
#Give wisdom to the machine,By ChangShouMeng

import multiprocessing as mp
import Queue
import time

def GetNowTime():
    return time.strftime("%Y%m%d",time.localtime(time.time()))


class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance        


#################################################
class GlobalQueue(Singleton):
    taskQueue=mp.JoinableQueue()
    logQueue=mp.JoinableQueue()
    logDir="/data/imlog/msgpush"    
    logFlag="msgpush"
    logDate=GetNowTime()
    logFile="{0}/{1}_{2}.log".format( logDir,logFlag,logDate )
    f=open(logFile,"a")        
    
    @staticmethod
    def dumpLog(info): 
        GlobalQueue.logQueue.put(info)

    @staticmethod
    def outputLog():
        if GlobalQueue.logQueue.qsize() == 0:
            return
        try:
            t = GlobalQueue.logQueue.get()
            print "log>>:",t
            GlobalQueue.f.write(t)
            GlobalQueue.f.write("\n")
            GlobalQueue.f.flush()
            if GlobalQueue.logDate !=  GetNowTime() :
                    GlobalQueue.f.close()
                    logFile="{0}/{1}_{2}.log".format( GlobalQueue.logDir,GlobalQueue.logFlag,GlobalQueue.logDate )
                    GlobalQueue.f = open( logFile,"a")
                    GlobalQueue.logDate=GetNowTime()
        except Queue.Empty:
            print "queue is empty"

def dump_log(info):
    GlobalQueue.dumpLog(info)

def output_log():
    GlobalQueue.outputLog()

            

