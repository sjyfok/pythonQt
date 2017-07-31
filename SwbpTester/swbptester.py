# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:57:08 2017

@author: song
"""

from PyQt4 import QtCore, QtGui
import sys
import swbpui
import serial
import binascii
import threading
import time
import swbpframe
g_ser = serial.Serial(timeout = 1)


class SwbpDialog(QtGui.QDialog,swbpui.Ui_SwbpTester):
    
    def __init__(self, parent = None):
        print('init')
        super(SwbpDialog, self).__init__(parent)
        self.setupUi(self)

    
    def serrecv(self):
        while True:
            num = g_ser.inWaiting()
            if num == 0:
                time.sleep(1)
                continue
            text = self.recv_edit.text()
            tmp = g_ser.read(num)
            tmp = binascii.b2a_hex(tmp)
            tmp = str(tmp, encoding = 'utf-8')
            temp_data = ''
            for (index, value) in enumerate(tmp):
                temp_data += value
                if len(temp_data) == 2:
                    text = text + ' ' + temp_data
                    temp_data = ''
            self.recv_edit.setText(text)

    
    def send(self):
        print('send')
        text = self.sendedit.text()
        txt = text.replace(' ', '')
        print(txt)
        text = binascii.a2b_hex(txt)
        print(text)
        g_ser.write(text)
        self.recv_edit.setText('')

    
    def open(self):
        text = self.m_ComSellineEdit.text()
        print('open '+text)
        #idx = self.comsel_combox.currentIndex()
        #text = self.comsel_combox.itemText(idx)
        g_ser.setPort(text)
        g_ser.setBaudrate(115200)
        g_ser.open()
        print(g_ser.portstr + 'is open')
        readThread = threading.Thread(target = self.serrecv)
        readThread.setDaemon(True)
        readThread.start()

    


    
    def List2StrHex(self, alist):
        text = ''
        for i in alist:
            text = text + ' %02x' % i
        
        return text

    
    def OnVoltageQueryBtnDown(self):
        alist = swbpframe.GenFrame([], 3)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)

    
    def OnGenPwrStaBtnDown(self):
        itmp = 0
        if self.LeuPwr_chkBox.isChecked():
            itmp = itmp | 2
        else:
            itmp = itmp & ~3
        if self.BrmPwr_chkBox.isChecked():
            itmp = itmp | 1
        else:
            itmp = itmp & ~2
        print(itmp)
        dlist = []
        dlist.append(itmp)
        alist = swbpframe.GenFrame(dlist, 1)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)

    
    def OnReadPwrStaBtnDown(self):
        alist = swbpframe.GenFrame([], 2)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)

    
    def OnRestoreBtnDown(self):
        alist = swbpframe.GenFrame([], 5)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)

    
    def OnGenClibraBtnDown(self):
        dlist = []

        tstr = self.m_lineEdit_1.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        tstr = self.m_lineEdit_2.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)

        tstr = self.m_lineEdit_3.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        tstr = self.m_lineEdit_4.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        tstr = self.m_lineEdit_5.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        tstr = self.m_lineEdit_6.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)

        tstr = self.m_lineEdit_7.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)

        tstr = self.m_lineEdit_8.text()        
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        tstr = self.m_lineEdit_9.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        tstr = self.m_lineEdit_10.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        tstr = self.m_lineEdit_11.text()
        tmp = int(tstr)
        tmp &= 0xFFFF
        dlist.append(tmp >> 8)
        dlist.append(tmp & 0xFF)
        
        alist = swbpframe.GenFrame(dlist, 0x04)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)




def main():
    app = QtGui.QApplication(sys.argv)
    dialog = SwbpDialog()
    dialog.setWindowTitle('SwbpTester V1.0')
    dialog.m_ComSellineEdit.setText("COM1")
    '''  
    for i in range(1, 9):
        dialog.comsel_combox.addItem('com' + str(i))
   
    dialog.comsel_combox.setItemText(1, 'com1')
    ''' 
    dialog.m_lineEdit_1.setText('3300')
    dialog.m_lineEdit_2.setText('3300')
    dialog.m_lineEdit_3.setText('3300')
    dialog.m_lineEdit_4.setText('3300')
    dialog.m_lineEdit_5.setText('3300')
    dialog.m_lineEdit_6.setText('3300')
    dialog.m_lineEdit_7.setText('3300')
    dialog.m_lineEdit_8.setText('3300')
    dialog.m_lineEdit_9.setText('3300')
    dialog.m_lineEdit_10.setText('3300')
    dialog.m_lineEdit_11.setText('3300')

    dialog.show()
    g_ser.close()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()