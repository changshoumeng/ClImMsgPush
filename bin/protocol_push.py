# -*- coding: utf-8 -*-
#Give wisdom to the machine,By ChangShouMeng


from basepacket import *


class HTTP_POST_METHOD_PUSH_GROUP_OFFLINEMSG(NET_HEAD):
    def __init__(self):
        super(HTTP_POST_METHOD_PUSH_GROUP_OFFLINEMSG,self).__init__()
        self.m_uMainCmd=102
        self.muGroupID=0#uint64
        self.muSenderID=0#uint64
        self.muDeviceType=0#uint16
        self.muFieldSize1=0#uint16
        self.muFieldSize2=0#uint16
        self.message=""#string
        self.memberid=""
        pass
    def pack(self):
        super_data=super(HTTP_POST_METHOD_PUSH_GROUP_OFFLINEMSG,self).pack()         
        fmtstr="QQHHH"
        header_data=struct.pack(fmtstr,self.muGroupID,self.muSenderID,self.muDeviceType,self.muFieldSize1,self.muFieldSize2)
        stringContent=self.message+self.memberid
        assert len(stringContent) == (self.muFieldSize1+self.muFieldSize2)
        stringData=STRING_DATA(stringContent).pack()
        return super_data+header_data+stringData
    
    def unpack(self,data):      
        super_size= NET_HEAD.getSize()
        super_data=data[0:super_size]
        header_size=22
        header_data=data[super_size:super_size+header_size]
        stringData=data[super_size+header_size:]
        
        super(HTTP_POST_METHOD_PUSH_GROUP_OFFLINEMSG,self).unpack(super_data)
        fmtstr="QQHHH"
        self.muGroupID,self.muSenderID,self.muDeviceType,self.muFieldSize1,self.muFieldSize2=struct.unpack(fmtstr,header_data)
        fmtstr  = "%ds%ds"%(self.muFieldSize1,self.muFieldSize2)        
        self.message,self.memberid=struct.unpack(fmtstr,stringData)
       # print "message:",self.message
       # print "memberid:",self.memberid
        
    def getSize(self):
        super_size= NET_HEAD.getSize()
        header_size=22
        return super_size+header_size+self.muFieldSize1+self.muFieldSize2
    
    def getDicData(self):
        dict1=dict()
        dict1["group_id"]=self.muGroupID
        dict1["from_uid"]=self.muSenderID
        dict1["to_uid"]=self.memberid
        dict1["os"]=self.muDeviceType
        dict1["message"]=self.message
        dict1["type"] =0  #from globalres.py
        return dict1
    
if __name__ == '__main__':
    print __file__
    p=HTTP_POST_METHOD_PUSH_GROUP_OFFLINEMSG()



    
