# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:14:33 2017

@author: song
"""
import crc16

'''
返回packet_s, packet_e, rsl
一包数据的开始位置和结束位置和帧是否合法 
rsl = 0  本报数据合法
rsl = 1  没有处理需要积累数据
rsl = 2  需要跳过一包数据的packet_s个字符 
'''
def protorx(data):   
    if len(data) < 4:
        return 0, 0, 1
    head = 0
    while data[head] != (0xA5):  #去掉非头部分数据
        head += 1
  
    if (data[head] == (0xA5)) & (data[head+1] == (0xA5)):  #找到头
        #寻找尾
        length = len(data)
        tail = head+2
        while tail < length:
            if data[tail] != (0x5A):
                tail += 1
            else:
                if (tail+1) < length: 
                    if  (data[tail+1] == (0x5A)): #找到尾     
                        #校验
                        if crc16.GenCrc16(data[head+2:tail]) == 0:
                            #校验成功
                            return head, tail+2, 0                        
                        else:
                            #校验错
                            return tail+2, 0, 2                  
                    else:
                        tail += 1
                else:
                    tail += 1
        else:
            return head, 0, 1
    
    return head+1, 0, 2