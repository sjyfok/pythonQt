# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:12:12 2017

@author: song
"""
import os
import struct

filenames = ['应答器.bmp', 'leu.bmp', '数据查看.bmp', '数据删除.bmp',
            '设置.bmp', '帮助.bmp', '主页s.bmp', '应答器s.bmp', 'leus.bmp', '数据查看s.bmp', '数据删除s.bmp',
            '设置s.bmp', '帮助s.bmp']
file_wr = open('cbrtbmp.bin', 'wb')
for name in filenames:
    filesize = os.path.getsize(name)
    print(filesize)
    filesize = struct.pack('<L', filesize)
    print(filesize)
    file_wr.write(filesize)

filecnt = len(filenames)
print(filecnt)
for pak in range(filecnt, 128):
    filesize = struct.pack('<L', 0)
    file_wr.write(filesize)
    
for name in filenames:
    with open(name, 'rb') as file_rd:
        contents = file_rd.read()
        file_wr.write(contents)
    

file_wr.close()


#with  as file_wr:
#   file_wr.write(filesize)
    #file_wr.write(contents)

    
#with open('cbrtpng.bin', 'wb') as file_wr:
#   file_wr.write(filesize)
#  file_wr.write(contents)
    
#filesize = os.path.getsize(r'应答器.png')
#print(filesize);
#filesize = struct.pack('<L', filesize)
#print(filesize)

#with open("应答器.png", "rb") as file_object:
#    contents = file_object.read()

#with open('cbrtpng.bin', 'wb') as file_wr:
#    file_wr.write(filesize)
#    file_wr.write(contents)
    