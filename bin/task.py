# -*- coding: utf-8 -*-
#Give wisdom to the machine,By ChangShouMeng

from protocol_push import *
import urllib
import urllib2
from urllib2 import URLError, HTTPError
import socket
import time,random
import traceback


urllib2.socket.setdefaulttimeout(3)
iplist=['192.168.1.2']

class Task(object):
    def __init__(self,taskName,taskData):
        self.taskName=taskName
        self.taskData=taskData
    def doTask(self): 
        info="doTask>>name={0} size:{1} data:{2}".format(self.taskName,len(self.taskData)  ,self.taskData )
        return info
    def __str__(self):    
        return self.taskName   

class HttpTask(Task):
    def __init__(self,taskName,taskData):
        super(HttpTask,self).__init__(taskName,taskData)
        self.logQueue=None
        self.workerid=0
    def dump_log(self,info):
        if self.logQueue:
            text="worker[{0}][{1}] {2}".format(self.workerid,self.taskName,info)
            self.logQueue.put(text)
    def doTask(self):
        try:
            p=HTTP_POST_METHOD_PUSH_GROUP_OFFLINEMSG()
            p.unpack(self.taskData)
            data=p.getDicData()
            content = urllib.urlencode(data)       
            url="http://%s/im/forward"%(random.choice(iplist))
            self.doPost(url,content)
            return
            pass
        except:
            info= "{0} doTask Except:{1}".format( self.taskName,traceback.format_exc() )
            self.dump_log( info )
            
    def doPost(self,url,content):
        try:
            self.dump_log("doPost:{0}".format(url))
            self.dump_log( "content:{0}".format(content) )
            request = urllib2.Request(url, content)
            response = urllib2.urlopen(request)
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.add_header('Host', 'chelun.eclicks.cn')
        except URLError,e:   
            if hasattr(e, 'code'):
                info="couldn\'t fulfill the request.url:{0}".format(url)
                self.dump_log( info)
            elif hasattr(e, 'reason'): 
                info='failed to reach a server. url:{0}'.format(url)
                self.dump_log( info )
        else:        
            page = response.read()       
            if page.strip()=="{\"code\":1}" :
                pass
                #return
            info=' done response:{0}'.format(page.decode("utf-8") )
            self.dump_log( info)
            #self.sendResponse(0)           
        pass               
                