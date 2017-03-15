# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:44:51 2017

@author: song
"""

import binascii

#将list列表转成str 内部包含 16进制串
def List2StrHex(alist):
    text = ''
    for i in alist:
        text = text + ' %02x' %i
    return text
        
def CreatFrmHead(cmd, length):
      head = []
      head.append(0xB5)
      head.append(0xB5)
      head.append(0x0)
      head.append(0x0)
      head.append(0x00)
      head.append(0x01)
      head.append(cmd)
      head[2] = length>>8#(length&0xFF)
      head[3] = (length&0xFF)
      text = List2StrHex(head)   
      txt = text.replace(' ', '')
      text = binascii.a2b_hex(txt)
                    
      return text

def CreatFrmEnd():
    end = []
    end.append(0x5B)
    end.append(0x5B)
    text = List2StrHex(end)   
    txt = text.replace(' ', '')
    text = binascii.a2b_hex(txt)
    return text

def CreatFrmStart(file_len):
    con = []
    con.append(0x00)
    con.append(0x00)
    con.append(0x00)
    con.append(0x00)
    con[0] = (file_len>>24)&0xFF;
    con[1] = (file_len>>16)&0xFF;
    con[2] = (file_len>>8)&0xFF;
    con[3] = (file_len&0xFF)
    text = List2StrHex(con)
    txt = text.replace(' ', '')
    text = binascii.a2b_hex(txt)
    return text