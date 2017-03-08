# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:36:32 2017

@author: song
"""
from PyQt4 import QtCore, QtGui

import sys

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


class MyTable(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setColumnCount(5)
        self.setRowCount(2)
        self.setItem(0, 0, QtGui.QTableWidgetItem(self.tr("性别")))
        self.setItem(0, 1, QtGui.QTableWidgetItem(self.tr("姓名")))
        self.setItem(0, 2, QtGui.QTableWidgetItem(self.tr("出生日期")))
        self.setItem(0, 3, QtGui.QTableWidgetItem(self.tr("职业")))
        self.setItem(0, 4, QtGui.QTableWidgetItem(self.tr("收入")))
        lbp1=QtGui.QLabel()
        lbp1.setPixmap(QtGui.QPixmap("image/4.gif"))
        self.setCellWidget(1, 0, lbp1)
        twi1 = QtGui.QTableWidgetItem("Tom")
        self.setItem(1, 1, twi1)
        dte1 = QtGui.QDateTimeEdit()
        dte1.setDateTime(QtCore.QDateTime.currentDateTime())
        dte1.setDisplayFormat("yyyy/mm/dd")
        dte1.setCalendarPopup(True)
        self.setCellWidget(1, 2, dte1)
        cbw= QtGui.QComboBox()
        cbw.addItem("Worker")
        cbw.addItem("Famer")
        cbw.addItem("Doctor")
        cbw.addItem("Lawyer")
        cbw.addItem("Soldier")
        self.setCellWidget(1, 3, cbw)
        sb1= QtGui.QSpinBox()
        sb1.setRange(1000, 10000)
        self.setCellWidget(1, 4, sb1)
                                          
                                          
    
def main():
    app=QtGui.QApplication(sys.argv) 
    myqq = MyTable()
    myqq.setWindowTitle("My Table")
    myqq.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()