# -*- coding: utf-8 -*-
#Give wisdom to the machine,By ChangShouMeng

from TcpConnector import *
from basepacket import *


class TcpClient(TcpConnector):
    def __init__(self,connType,ip,port,messageQueue):
        super(TcpClient,self).__init__(connType,ip,port,messageQueue)
        pass
    #How unpack a packet from buffer
    def unpackFromBuffer(self,leftBuffer):
        leftSize=len(leftBuffer)
        if leftSize <NET_HEAD.getSize():
            return 0
        net_head_data=leftBuffer[0:NET_HEAD.getSize()]
        net_head = NET_HEAD()
        net_head.unpack(net_head_data)
        if net_head.m_uPacketSize > 4096 or   net_head.m_uPacketSize <16:
            print "[TcpClient] unpackFromBuffer packetSize:{0} error:".format(net_head.m_uPacketSize)
            return -1
        if leftSize < net_head.m_uPacketSize:
            return 0
        return net_head.m_uPacketSize
        pass
    
    def sendPacket(self,packet):
        data=packet.pack()
        self.sendData(data)
        print "sendPacket->cmd:{0} size:{1}".format(packet.m_uMainCmd,packet.m_uPacketSize)        
            
        
