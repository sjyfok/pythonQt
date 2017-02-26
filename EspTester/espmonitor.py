# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:35:21 2017

@author: song
"""
import espcrc16

def DispListHex(alist):
    for item in alist:
        print("%x" %item, end = ' ')
    print(end = '\n')
    
def GenFrame(s_list, m_id, cmd):
    alist = []
    alist.append(0xFE)
    alist.append(0xFE)
    alist.append(0x00)
    alist.append(m_id)   
    #alist.append(0x01)
    alist.append(cmd)
    print(alist)
    if len(s_list) != 0:
        for item in s_list:
            alist.append(item)
   
    alist[2] = len(alist)#.insert(2, len(alist)+1) 
    print(alist)
    crc = espcrc16.GenCrc16(alist[2:]);    
    alist.append(crc>>8)
    alist.append(crc&0xFF)
    alist.append(0xEF)
    alist.append(0xEF)
    DispListHex(alist)
    return alist