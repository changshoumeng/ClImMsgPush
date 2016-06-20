# -*- coding: utf-8 -*-
#!/usr/bin/env python
import struct

###################################################
class NET_HEAD(object):
    def __init__(self):
        self.m_uPacketSize=0#uint32
        self.m_uMainCmd=0#uint16
        self.m_uSubCmd=0#uint16
        self.m_uMagicID=0#uint32
        self.m_uVersion=1001#uint32        
    def pack(self):        
        format_str="IHHII"
        data=struct.pack(format_str,self.m_uPacketSize,self.m_uMainCmd,self.m_uSubCmd,self.m_uMagicID,self.m_uVersion)
        return data
    def unpack(self,data):
        assert len(data)==16
        format_str="IHHII"
        self.m_uPacketSize,self.m_uMainCmd,self.m_uSubCmd,self.m_uMagicID,self.m_uVersion=struct.unpack(format_str,data)
        pass
    @staticmethod 
    def getSize():
        return 16

    
class STRING_DATA(object):
    def __init__(self,string=""):
        self.string=string
    def pack(self):
        length=len(self.string)        
        formatStr="%ds"%(length) 
        data=struct.pack(formatStr,self.string)
        return data
    def unpack(self,data):
        length=len(data)
        formatStr="%ds"%(length)
        #print formatStr
        self.string,=struct.unpack(formatStr,data)
        return self.string

class UINT64_DATA(object):
    def __init__(self,idv=0):
        self.muId=idv#uint64 
    def pack(self):        
        format_str="Q"
        data=struct.pack(format_str,self.muId)
        return data         
    def unpack(self,data):
        assert len(data)==self.getSize()
        format_str="Q"
        self.muId,=struct.unpack(format_str,data)
        return self.muId
    @classmethod
    def getSize(cls):
        return 8           

