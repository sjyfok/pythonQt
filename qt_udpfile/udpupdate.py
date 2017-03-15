# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:21:55 2017

@author: song
"""

from PyQt4 import QtCore, QtGui

import sys

import ui_udpfile
import socket

import genfrm
import os

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class updateDlg(QtGui.QDialog, ui_udpfile.Ui_UdpFile):
    def __init__(self, parent=None):
        super(updateDlg, self).__init__(parent)
        self.setupUi(self)
        self.bytestr=b''
        self.f_name = ''
        self.local_ip = '192.168.0.21'
        self.local_port = 20001
        self.edit_localip.setText(self.local_ip)
        self.edit_localport.setText(str(self.local_port))
        
        self.remote_ip = '192.168.0.22'
        self.remote_port = 5555
        self.edit_remoteip.setText(self.remote_ip)
        self.edit_remoteport.setText(str(self.remote_port))
        
        self.bar_sendprogress.setMinimum(0)
        self.bar_sendprogress.setValue(0)
      
        
        
     
    def slotOpen(self):
        self.f_name = QtGui.QFileDialog.getOpenFileName()
        
        #if f_name:
         #   f = open(f_name, 'rb')
          #  self.bytestr = f.read()            
           
 
        
    def slotUpdate(self):
        if self.f_name:
            file_len = os.path.getsize(self.f_name)
            d_addr = self.remote_pc
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(self.local_pc)
            retflag = True
            if file_len:
                head = genfrm.CreatFrmHead(0x03, 7)
                s.sendto(head, d_addr)
                head = genfrm.CreatFrmStart(file_len)
                end = genfrm.CreatFrmEnd()
                s.sendto(head, d_addr)
                s.sendto(end, d_addr)
                retflag = False                
            else:
                QtGui.QMessageBox.information(self, "Error",
                                      self.tr("文件为空!"))
                return 
                
            data, addr = s.recvfrom(100)
            print(data)
            print(addr)  
            
            self.bar_sendprogress.setMinimum(0)
            self.bar_sendprogress.setMaximum(file_len)  
            self.bar_sendprogress.setValue(0)
            f = open(self.f_name, 'rb')
            size = 0
            while retflag == False:
                bytestr = f.read(1024)
                if bytestr:
                    length = len(bytestr)
                    if length < 1024:
                        head = genfrm.CreatFrmHead(0x05, length+3)
                        retflag = True
                    else:
                        head = genfrm.CreatFrmHead(0x04, length+3)                        
                    end = genfrm.CreatFrmEnd()
                    s.sendto(head, d_addr)
                    s.sendto(bytestr, d_addr)
                    s.sendto(end, d_addr)
                    data, addr = s.recvfrom(100)    
                    print(data)
                    print(addr)
                    size += length
                    print(size)
                    self.bar_sendprogress.setValue(size)
                    QtCore.QThread.msleep(100)
                    
            QtGui.QMessageBox.information(self, "更新完成",
                                      self.tr("更新完成!!"))
        else:
            QtGui.QMessageBox.information(self, "Error",
                                      self.tr("需要先打开文件!!"))
        
        f.close()

    
    def slotLocalIP(self, text):
        self.local_ip = text
        self.local_pc = (self.local_ip, self.local_port)
        print(self.local_pc)
    
    def slotLocalPort(self, text):
        self.local_port = int(text)
        self.local_pc = (self.local_ip, self.local_port)
        print(self.local_pc)
    
    def slotRemoteIP(self, text):
        self.remote_ip = text
        self.remote_pc = (self.remote_ip, self.remote_port)
        print(self.remote_pc)
    
    def slotRemotePort(self, text):
        self.remote_port = int(text)
        self.remote_pc = (self.remote_ip, self.remote_port)   
        print(self.remote_pc)
                                    

        
          
                                     
    
    
def main():
    app=QtGui.QApplication(sys.argv) 
    form = updateDlg()
    form.show()
    sys.exit(app.exec_())
    
     
    
    
if __name__ == '__main__':
    main()