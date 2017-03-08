# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:36:32 2017

@author: song
"""
from PyQt4 import QtCore, QtGui

import sys

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))


class Progess(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Progess, self).__init__(parent)
        self.setWindowTitle(self.tr("使用进度条"))
        numLabel = QtGui.QLabel(self.tr("文件数目"))
        self.numLabelEdit = QtGui.QLineEdit("10")
        typeLabel = QtGui.QLabel(self.tr("显示类型"))
        self.typeComboBox = QtGui.QComboBox()
        self.typeComboBox.addItem(self.tr("进度条"))
        self.typeComboBox.addItem(self.tr("进度对话框"))
        
        self.progressBar = QtGui.QProgressBar()
        startPushButton = QtGui.QPushButton(self.tr("开始"))
        
        layout = QtGui.QGridLayout()
        layout.addWidget(numLabel, 0, 0)
        layout.addWidget(self.numLabelEdit, 0, 1)
        layout.addWidget(typeLabel, 1, 0)
        layout.addWidget(self.typeComboBox, 1, 1)
        layout.addWidget(self.progressBar, 2, 0, 1, 2)
        layout.addWidget(startPushButton, 3, 1)
        layout.setMargin(15)
        layout.setSpacing(10)
        
        self.setLayout(layout)
        
        self.connect(startPushButton, QtCore.SIGNAL("clicked()"), self.slotStart)
        
    def slotStart(self):
        num = int(self.numLabelEdit.text())
        if self.typeComboBox.currentIndex() == 0:
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(num)
            
            for i in range(num):
                self.progressBar.setValue(i)
                QtCore.QThread.msleep(100)
        elif self.typeComboBox.currentIndex() == 1:
            progressDialog = QtGui.QProgressDialog(self)
            progressDialog.setWindowModality(QtCore.Qt.WindowModal)
            progressDialog.setMinimumDuration(5)
            progressDialog.setWindowTitle("请等待")
            progressDialog.setLabelText(self.tr("拷贝..."))
            progressDialog.setCancelButtonText(self.tr("取消"))
            progressDialog.setRange(0, num)
            
            for i in range(num):
                progressDialog.setValue(i)
                QtCore.QThread.msleep(100)
                if progressDialog.wasCanceled():
                    return
            
        
                                          
                                          
    
def main():
    app=QtGui.QApplication(sys.argv) 
    progess = Progess()
    #myqq.setWindowTitle("My Table")
    progess.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()