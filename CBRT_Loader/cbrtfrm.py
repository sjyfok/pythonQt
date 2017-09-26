# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:35:21 2017

@author: song
"""
import crc16

def DispListHex(alist):
    for item in alist:
        print("%x" %item, end = ' ')
    print(end = '\n')
    
def GenFrame(s_list, cmd):
    alist =  0xA5.to_bytes(1, byteorder='big')
    alist += 0xA5.to_bytes(1, byteorder='big')
    alist += 0x01.to_bytes(1, byteorder='big')
    alist += cmd.to_bytes(1, byteorder='big')
    length = len(s_list)    
    alist += length.to_bytes(2, byteorder='big')#(length>>8)
    #alist += (length&0xFF)
    alist += s_list
    crc = crc16.GenCrc16(alist[2:])
    alist += crc.to_bytes(2, byteorder='big')#(crc>>8)
    #alist += (crc&0xFF)
    alist += 0x5A.to_bytes(1, byteorder='big')
    alist += 0x5A.to_bytes(1, byteorder='big')
    
    return alist
    '''
  # print(length)
    length = len(s_list)
  #  print(length)
  #  leng = length.to_bytes(2, byteorder='big')
    alist.append(length>>8)   #lenth
    alist.append(length&0xFF)
    print(alist)
    if len(s_list) != 0:
        for item in s_list:
            alist.append(item)
    print(alist)
    crc = crc16.GenCrc16(alist[2:]);    
    alist.append(crc>>8)
    alist.append(crc&0xFF)
    alist.append(0x5A)
    alist.append(0x5A)
    #DispListHex(alist)
    return alist
    '''
    