# -*- coding: utf-8 -*-
#Give wisdom to the machine,By ChangShouMeng

from TcpClient import *
from protocol_push import *

tcpClient=TcpClient(0,"127.0.0.1",1989,None)
def main():  
    global tcpClient
    if not tcpClient.start():
        print "tcpClient start failed"
        return
    print "start succ"
    req=HTTP_POST_METHOD_PUSH_GROUP_OFFLINEMSG()
    req.m_uMainCmd=1
    req.muGroupID=11
    req.muSenderID=22
    req.muDeviceType=2
    text="HELLOWORLD"
    req.muFieldSize1=len(text)
    ids="11,22"
    req.muFieldSize2=len(ids)    
    req.message = text
    req.memberid=ids
    req.m_uPacketSize=req.getSize()
    tcpClient.sendPacket(req)     
    print "send req"


if __name__ == '__main__':
    print __file__
    main()
    input("wait..")
    
