# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:57:08 2017

@author: song
"""

import espcrc16

def DispListHex(alist):
    for item in alist:
        print("%x" %item, end = ' ')
    print(end = '\n')
    
def GenFrame(s_list, cmd):
    alist = []
    alist.append(0xA5)
    alist.append(0xA5)
    alist.append(0x04)
    alist.append(0x01)
    alist.append(cmd) #cmd = 0x07 切换信号  
    alist.append(0x00) #长度
    alist.append(0x00)
    #alist.append(0x01)
    #alist.append(cmd)   
    if len(s_list) != 0:
        for item in s_list:
            #alist.append(0x00)
            alist.append(item)
    length = len(s_list)
    alist[5] = (length>>8)
    alist[6] = (length&0xFF)#.insert(2, len(alist)+1)    
    #print(alist)
    crc = espcrc16.GenCrc16(alist[2:]);    
    alist.append(crc>>8)
    alist.append(crc&0xFF)
    alist.append(0x5A)
    alist.append(0x5A)
    
    return alist