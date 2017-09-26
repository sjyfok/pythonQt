# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:59:28 2017

@author: song
"""

from PyQt4 import QtCore, QtGui

import sys  
import os
import cbrtloaderui

import serial
import binascii
import cbrtfrm
import threading
import time
import protocom
from array import array
from threading import Lock

#import espitfconfig
#import espsigctrl
#import defaultbw

g_ser = serial.Serial(timeout = 1)


    
class LoaderDialog(QtGui.QDialog, cbrtloaderui.Ui_CBRTLoader):  
    def __init__(self,parent=None):  
        print("init")
        super(LoaderDialog,self).__init__(parent)          
        self.setupUi(self)
        self.filesize = 0
        self.recvdata = (0).to_bytes(1, byteorder='big')
        
        
    #选串口
    def onComSel(self, idx):
        self.comsel_combox.setItemText(idx, "com"+str(idx+1))
        print(idx)
    


    
    def open(self):
       global g_ser
       print('open')
       idx = self.comsel_combox.currentIndex()
       text = self.comsel_combox.itemText(idx)
      # g_ser = serial.Serial(text, 9600)
       g_ser.setPort(text)
       g_ser.setBaudrate(115200)
       g_ser.open()
     
       print(g_ser.portstr + 'is open')
       readThread = threading.Thread(target=self.serrecv)
       readThread.setDaemon(True)
       readThread.start()
        
        
       # n = g_ser.write(b'hello')
      #  print(g_ser.read(n))
        #g_ser.close()
    #
    def sendbmp(self):
        #self.filelib = open("YF1703-078-03 CBRT-II位图资源 V1.0.bin", "rb")
        #print(self.filesize)
        while self.filesize > 0:
            #print(self.filesize)
            self.lock.acquire()
            data = self.filelib.read(1024)  
            data = self.frmno+data
            if len(data) < 1025:
                self.senddata = cbrtfrm.GenFrame(data, 0x0B)
            else:
                self.senddata = cbrtfrm.GenFrame(data, 0x0A)       
            self.send()
            self.filesize -= 1024
    
    #发送字库文件的线程
    def sendfont(self):
        print(self.filesize)
        while self.filesize > 0:
            self.lock.acquire()
            data = self.filelib.read(1024)  
            data = self.frmno+data
            if len(data) < 1025:
                self.senddata = cbrtfrm.GenFrame(data, 0x03)
            else:
                self.senddata = cbrtfrm.GenFrame(data, 0x02)       
            self.send()
            self.filesize -= 1024
    
    #发送程序文件的进程
    def sendprog(self):
        print(self.filesize)
        while self.filesize > 0:
            self.lock.acquire()
            data = self.filelib.read(1024)  
            data = self.frmno+data
            if len(data) < 1025:
                self.senddata = cbrtfrm.GenFrame(data, 0x06)
            else:
                self.senddata = cbrtfrm.GenFrame(data, 0x05)       
            self.send()
            self.filesize -= 1024
    
    def recvdataproc(self, rvdata):
        if (rvdata[4] == (0x01)):
            #接收的数据为1
            #判断类型 决定创建线程还是唤醒线程
            if (rvdata[1] == (0x89)): 
                #创建位图发送线程  
                self.lock = Lock()
                self.intfrmno = 1              
                self.frmno =self.intfrmno.to_bytes(1, byteorder='big')
                self.threadsend = threading.Thread(target=self.sendbmp)
                self.threadsend.setDaemon(True)
                self.threadsend.start()
            elif (rvdata[1] == (0x8A)):
                self.intfrmno += 1
                self.intfrmno &= 0xFF
                self.frmno = self.intfrmno.to_bytes(1, byteorder='big')
                self.lock.release()
            elif (rvdata[1] == (0x8B)):
                self.lock.release()
                print("位图更新完毕！")
                #self.threadsend.close()
            elif (rvdata[1] == (0x81)):
                #创建字库发送线程
                self.lock = Lock()
                self.intfrmno = 1
                self.frmno = self.intfrmno.to_bytes(1, byteorder='big')
                self.threadsend = threading.Thread(target=self.sendfont)
                self.threadsend.setDaemon(True)
                self.threadsend.start()
            elif (rvdata[1] == (0x82)):
                self.intfrmno += 1
                self.intfrmno &= 0xFF
                self.frmno = self.intfrmno.to_bytes(1, byteorder='big')
                self.lock.release()
            elif (rvdata[1] == (0x83)):
                self.lock.release()
                print("字库更新完毕!")
                #pass
            elif (rvdata[1] == (0x84)):
                 #创建更新程序发送线程
                self.lock = Lock()
                self.intfrmno = 1
                self.frmno = self.intfrmno.to_bytes(1, byteorder='big')
                self.threadsend = threading.Thread(target=self.sendprog)
                self.threadsend.setDaemon(True)
                self.threadsend.start()
            elif (rvdata[1] == (0x85)):
                self.intfrmno += 1
                self.intfrmno &= 0xFF
                self.frmno = self.intfrmno.to_bytes(1, byteorder='big')
                self.lock.release()
            elif (rvdata[1] == (0x86)):
                self.lock.release()
                print("程序更新完毕")
        elif (rvdata[4] == (0x00)):
            pass
        elif (rvdata[4] == (0x02)):
            pass
        elif (rvdata[4] == (0x03)):
            pass
        elif (rvdata[4] == (0x04)):
            pass
                
        
    def serrecv(self):
        while g_ser.isOpen(): 
            num = g_ser.inWaiting()
            if num:
                self.recvdata  += g_ser.read(num)#.decode('utf-8')
                print("recv", end=':')
                print(binascii.b2a_hex(self.recvdata))
                start, end, rsl = protocom.protorx(self.recvdata)
                if rsl == 0:
                    #数据合法
                    tmpdata = self.recvdata[start+2:end-2]
                    self.recvdataproc(tmpdata)
                    self.recvdata = self.recvdata[end:]                   
                elif rsl == 1:
                    #数据需要积累
                    #print("skip end")
                    pass
                    #self.recvdata = self.recvdata[skip:]
                elif rsl == 2:
                    self.recvdata = self.recvdata[start:]
                    
    
                
                
            
        
    def send(self):
        #print("send", end=':')
        #print(binascii.b2a_hex(self.senddata))          
        g_ser.write(self.senddata)


    #打开字库文件
    def onOpenFontLib(self):
        self.filelib = open("YF1703-078-04 CBRT-II字体资源 V1.0.bin", "rb")
        print("YF1703-078-04 CBRT-II字体资源 V1.0.bin")
        
    
     #更新字库
    def onUpdateFont(self):
        #data = self.filefontlib.read(1024)
        self.filesize = os.path.getsize("YF1703-078-04 CBRT-II字体资源 V1.0.bin")
        data = self.filesize
        data = data.to_bytes(4, byteorder='big')
        self.senddata = cbrtfrm.GenFrame(data, 0x01)
        self.send()
    
    #打开位图文件
    def onOpenBmp(self):
        self.filelib = open("YF1703-078-03 CBRT-II位图资源 V1.0.bin", "rb")
        print("YF1703-078-03 CBRT-II位图资源 V1.0.bin")
    
    #更新位图文件
    def onUpdateBmp(self):    
        self.filesize = os.path.getsize("YF1703-078-03 CBRT-II位图资源 V1.0.bin")       
        data = self.filesize
        data = data.to_bytes(4, byteorder='big')
        self.senddata = cbrtfrm.GenFrame(data, 0x09)       
        self.send()
    
    #打开程序文件
    def onOpenPrg(self):
        self.filelib = open("YF1703-078-01 CBRT-II(C型) 嵌入式程序 V1.0.0.bin", "rb")
        print("YF1703-078-01 CBRT-II(C型) 嵌入式程序 V1.0.0.bin")
    
    #更新程序文件
    def onUpdatePrg(self):
        self.filesize = os.path.getsize("YF1703-078-01 CBRT-II(C型) 嵌入式程序 V1.0.0.bin")       
        data = self.filesize
        data = data.to_bytes(4, byteorder='big')
        self.senddata = cbrtfrm.GenFrame(data, 0x04)       
        self.send()
    
    #将list列表转成str 内部包含 16进制串
    def List2StrHex(self, alist):
        text = ''
        for i in alist:
            text = text + ' %02x' %i
        return text     
      
      
def main():
    app=QtGui.QApplication(sys.argv)  
    dialog=LoaderDialog()  
    dialog.setWindowTitle("CbrtLoader V1.0")
    for i in range(1,10):
        dialog.comsel_combox.addItem("com"+str(i))
    dialog.comsel_combox.setItemText(1, "com1")  
    #dialog.monitorid_edit.setText("1")   
   # dialog.itfid_edit.setText("1")
    #dialog.bcmid_edit.setText("1")
    
    dialog.show()  
    g_ser.close()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
