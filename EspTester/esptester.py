# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:59:28 2017

@author: song
"""

from PyQt4 import QtCore, QtGui

import sys  
import espui

import serial
import binascii
import espmonitor
import threading
import time
import espitfconfig
import espsigctrl
import defaultbw

g_ser = serial.Serial(timeout = 1)


    
class EspDialog(QtGui.QDialog,espui.Ui_EspTester):  
    def __init__(self,parent=None):  
        print("init")
        super(EspDialog,self).__init__(parent)          
        self.setupUi(self)
    
    #获得监测模块的ID
    def GetMonitorID(self):
        tstr = self.monitorid_edit.text()
        m_id = int(tstr)
        return m_id
    
    #获得接口模块ID
    def GetItfID(self):
        tstr = self.itfid_edit.text()
        itf_id = int(tstr)
        return itf_id
        
    def serrecv(self):
        while True: 
            num = g_ser.inWaiting()
            #print(num)
            if num == 0:
                time.sleep(1)  
            else:
                text = self.recv_edit.text()
                tmp = g_ser.read(num)#.decode('utf-8')
                tmp = binascii.b2a_hex(tmp)
                tmp = str(tmp, encoding = 'utf-8')
                temp_data = ''
                for index,value in enumerate(tmp): 
                    temp_data += value
                    if len(temp_data) == 2:
                        text = text + ' ' + temp_data
                        temp_data = ''
                print(text)
                self.recv_edit.setText(text)
            
        
    def send(self):
        print("send")
        text = self.sendedit.text()
        #toHtml("UTF-8");
        
        txt = text.replace(' ', '')
        print(txt)
        text = binascii.a2b_hex(txt)
        print(text)
        g_ser.write(text)
        self.recv_edit.setText('')
            #g_ser.write(hex(item))
        
    def open(self):
        global g_ser
        print('open')
        idx = self.comsel_combox.currentIndex()
        text = self.comsel_combox.itemText(idx)
       # g_ser = serial.Serial(text, 9600)
        g_ser.setPort(text)
        g_ser.setBaudrate(9600)
        g_ser.open()
        print(g_ser.portstr + 'is open')
        readThread = threading.Thread(target=self.serrecv)
        readThread.setDaemon(True)
        readThread.start()
        
        
       # n = g_ser.write(b'hello')
      #  print(g_ser.read(n))
        #g_ser.close()
    
       
    def onComSel(self, idx):
        self.comsel_combox.setItemText(idx, "com"+str(idx+1))
        print(idx)
          
    #生成旧版状态查询帧 并显示到编辑框中
    def onSta0BtnClicked(self):
        m_id = self.GetMonitorID()
        alist = espmonitor.GenFrame([], m_id, 0x00)
        #espmonitor.DispListHex(alist)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
   # def onInEditChange(self):
    #    pass
    
    #监测模块ID编辑框改变 回调函数
    def OnMonitorIDChange(self, text):
        self.monitorid_edit.setText(text)
    
    #设置接口模块ID 回调函数
    def OnItfIDChange(self, text):
        self.itfid_edit.setText(text)
        print(text)
        

    
    
    #生成设备列表帧并显示到 发送编辑框中
    def OnSetDevListBtn(self):
        m_id = self.GetMonitorID()
        itf_id = self.GetItfID()      
        dlist = [0x01] #接口模块个数
        dlist.append(itf_id) #接口模块ID
        print(dlist)
        alist = espmonitor.GenFrame(dlist, m_id, 0x20)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
        #espmonitor.DispListHex(alist)
        #text = ''
        #for i in alist:
         #  text = text + ' %02x' %i
        #self.sendedit.setText(text)
    
    #生成旧版广播查询帧 并显示到编辑框中
    def OnBcQueryBtnDown(self):
        m_id = 0x0
        alist = espmonitor.GenFrame([], m_id, 0x00)
        
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    
    #生成旧版报文状态查询帧 并显示到编辑框中
    def OnBWQuery0BtnDown(self):
        m_id = self.GetMonitorID()   
        dlist = []
        itf_id = self.GetItfID()
        dlist.append(itf_id)
        alist = espmonitor.GenFrame(dlist, m_id, 0x10)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
      
        
    def GetBcmID(self):
        tstr = self.bcmid_edit.text()
        bcm_id = int(tstr)
        return bcm_id
        
    #报文传输模块ID设置
    def OnBcmIDChange(self, text):
        self.bcmid_edit.setText(text)
    
    #新版状态广播查询
    def OnBcQuery1BtnDown(self):
        bcm_id = self.GetBcmID()
        m_id = 0x0 
        dlist = []
        dlist.append(bcm_id)
        alist = espmonitor.GenFrame(dlist, m_id, 0x01)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    #将list列表转成str 内部包含 16进制串
    def List2StrHex(self, alist):
        text = ''
        for i in alist:
            text = text + ' %02x' %i
        return text
    
    #新版状态查询
    def onSta1Query1BtnDown(self):
        bcm_id = self.GetBcmID()
        m_id = self.GetMonitorID()
        dlist = []
        dlist.append(bcm_id)
        alist = espmonitor.GenFrame(dlist, m_id, 0x01)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    #新版报文状态查询
    def OnBWQuery1BtnDown(self):
        bcm_id = self.GetBcmID()
        m_id = self.GetMonitorID()
        dlist = []
        dlist.append(bcm_id)
        alist = espmonitor.GenFrame(dlist, m_id, 0x11)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    #测试时读取电压
    def OnVoltageQueryBtnDown(self):
         m_id = self.GetMonitorID()
         alist = espmonitor.GenFrame([], m_id, 0x30)
         text = self.List2StrHex(alist)
         self.sendedit.setText(text)
    
    #设置接口模块编辑框内容改变
    def OnSetItfIDChange(self, text):
        self.itfid_set_edit.setText(text)
    
    #设置报文传输模块个数编辑框内容改变
    def OnBcmCntChange(self, text):
        self.bcmcnt_edit.setText(text)
        
    #获得设定的接口模块ID
    def GetSetItfID(self):
        tstr = self.itfid_set_edit.text()
        setitf_id = int(tstr)
        print(setitf_id)
        return setitf_id
        
    #获得报文传输模块个数
    def GetBCMCnt(self):
        tstr = self.bcmcnt_edit.text()
        bcm_cnt = int(tstr)
        print(bcm_cnt)
        return bcm_cnt
        
   
    
    
        
    #生成信号配置帧
    def OnGenSigBtnDown(self):
        itmp = 0
        if self.sig1_chkBox.isChecked():
            itmp = itmp | (1<<0)
        else:
            itmp = itmp & ~(1<<0)
        if self.sig2_chkBox.isChecked():
            itmp = itmp | (1<<1)
        else:
            itmp = itmp & ~(1<<1)
        if self.sig3_chkBox.isChecked():
            itmp = itmp | (1<<2)
        else:
            itmp = itmp & ~(1<<2)
        print(itmp)
        dlist = []
        dlist.append(itmp)
        alist = espsigctrl.GenFrame(dlist, 0x07)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    #保存bcmidset 编辑框的修改
    def OnSetBcmIDChange(self, text):
        self.setbcmid_edit.setText(text)  
        
    #获得设定的接口模块ID
    def GetSetBCMID(self):
        tstr = self.setbcmid_edit.text()
        setbcm_id = int(tstr)
        return setbcm_id
    
     #生成配置报文传输模块个数和接口模块ID的帧
    def OnBcmCNTConfigBtnDown(self):
        dlist = [0x00]
        dlist.append(self.GetBCMCnt()) 
        alist = espitfconfig.GenFrame(dlist, 0x04)       
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
        
        #设置接口模块ID
    def OnItfIDConfig(self):
        dlist = [0x00]
        dlist.append(self.GetSetItfID())
        alist = espitfconfig.GenFrame(dlist, 0x00)       
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
        
    #生成配置报文传输模块ID的帧
    def OnSetBcmIDBtnDown(self):
        dlist = []
        dlist.append(self.GetSetBCMID())
        alist = espitfconfig.GenFrame(dlist, 0x02)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    #配置接口模块和应答器的报文
    def OnSetibBWBtnDown(self):
        dlist = defaultbw.RetDefaultBw()
        alist = espitfconfig.GenFrame(dlist, 0x10)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
        
    
    #配置接口模块报文
    def OnSetIBwBtnDown(self):
        dlist = defaultbw.RetDefaultBw()
        alist = espitfconfig.GenFrame(dlist, 0x12)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    #配置应答器报文
    def OnSetbBwBtnDown(self):
        dlist = defaultbw.RetDefaultBw()
        alist = espitfconfig.GenFrame(dlist, 0x11)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    #查看接口模块ID
    def OnCheckItfID(self):
        alist = espitfconfig.GenFrame([], 0x01)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    
    #查看报文传输模块数量
    def OnCheckBcmCnt(self):
        alist = espitfconfig.GenFrame([], 0x05)
        text = self.List2StrHex(alist)
        self.sendedit.setText(text)
    
    
        
        
            
        
        
      
   
      
def main():
    app=QtGui.QApplication(sys.argv)  
    dialog=EspDialog()  
    dialog.setWindowTitle("ESPTester V1.0")
    for i in range(1,10):
        dialog.comsel_combox.addItem("com"+str(i))
    dialog.comsel_combox.setItemText(1, "com1")  
    dialog.monitorid_edit.setText("1")   
    dialog.itfid_edit.setText("1")
    dialog.bcmid_edit.setText("1")
    
    dialog.show()  
    g_ser.close()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
