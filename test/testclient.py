# -*- coding: utf-8 -*-
import SocketServer
import os
import sys
from SocketServer import StreamRequestHandler as SRH

import struct
import urllib
import urllib2
from urllib2 import URLError, HTTPError
import socket
import time
import traceback
import random
import threading
import globalres
from   globalres import logger
from   daemon import Daemon
import Queue


def main():
     reload(sys)    
     sys.setdefaultencoding( "utf-8" )	
     dict1=dict()
     dict1["group_id"]=0
     dict1["from_uid"]=1530883
     #dict1["to_uid"]='1464851'
     dict1["to_uid"]='162790'
     dict1["os"]=2
     #dict1["message"]='{"type":"4","text":"长安cx20","content":"我刚申请创建了《长安cx20》车轮会，求支持！","userLat":"44.065113","url":"http://chelun.eclicks.cn/web/invite?fid=31897","userLng":"131.133362"}'
     dict1["message"]='{"type":"0","text":"chagnan","content":"hello","userLat":"44.065113","url":"http://chelun.eclicks.cn/web/invite?fid=31897","userLng":"131.133362"}'
     #dict1["message"]='{"userLng":"121.510436","type":"0","text":"255555","userLat":"31.188116"}'	
     dict1["type"] =0


     
     srcdata="" 

     content = urllib.urlencode(dict1)

     srcdata = content
     urllib2.socket.setdefaulttimeout(5)
     url="http://%s/im/forward"%('192.168.1.118')
    
     request = urllib2.Request(url, content)
     request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')
     request.add_header('Content-Type', 'application/x-www-form-urlencoded')
     request.add_header('Host','chelun.eclicks.cn')
        #request.add_header('Referer', 'http://chelun.eclicks.cn')
     logger.debug('[Thread:{0} url:{1} ] request-data:{2}'.format(1, url,srcdata)    )       
     try:
            response = urllib2.urlopen(request)  
     except URLError,e:   
            if hasattr(e, 'code'):    
                logger.debug('[Thread:{0} url:{1} result] The server couldn\'t fulfill\
                        the request. urlencode:{2} errorcode:{3}'.format(
                        1, 
                        url,
                        srcdata,
                        e.code ))    
                  
            elif hasattr(e, 'reason'): 
                logger.debug('[Thread:{0} url:{1} result] We failed to reach a server.\
                        urlencode:{2} reason:{3}'.format(
                       1, 
                        url,
                        srcdata,
                        e.reason ))   
                        
     else:        
            page = response.read()       
            if page.strip()=="{\"code\":1}" :
                pass
                #return
               
            logger.warning( "[Thread:{0} url:{1} result] urlencode:{2} response:{3}".format(
                        1, 
                        url,
                        srcdata, 
                        page.decode("utf-8") 
                        )  )  
               
                    
    

main()
