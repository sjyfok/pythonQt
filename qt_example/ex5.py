# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:36:32 2017

@author: song
"""
from PyQt4 import QtCore, QtGui

import sys

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class MessageBoxDlg(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MessageBoxDlg, self).__init__(parent)
        self.setWindowTitle("Messagebox")
        self.label = QtGui.QLabel("About Qt MessageBox")
        questionButton = QtGui.QPushButton("Question")
        informationButton = QtGui.QPushButton("Infomation")
        warningButton=QtGui.QPushButton("Warning")
        criticalButton=QtGui.QPushButton("Cirtial")
        aboutButton=QtGui.QPushButton("About")
        aboutqtButton=QtGui.QPushButton("About Qt")
        customButton=QtGui.QPushButton("Custom")
        
        gridLayout = QtGui.QGridLayout(self)
        gridLayout.addWidget(self.label, 0, 0, 1, 2)
        gridLayout.addWidget(questionButton, 1, 0)
        gridLayout.addWidget(informationButton, 1, 1)
        gridLayout.addWidget(warningButton, 2, 0)
        gridLayout.addWidget(criticalButton, 2, 1)
        gridLayout.addWidget(aboutButton, 3, 0)
        gridLayout.addWidget(aboutqtButton, 3, 1)
        gridLayout.addWidget(customButton, 4, 0)
        
        self.connect(questionButton, QtCore.SIGNAL("clicked()"), self.slotQuestion)
        self.connect(informationButton, QtCore.SIGNAL("clicked()"), self.slotInformation)
        self.connect(warningButton, QtCore.SIGNAL("clicked()"), self.slotWarning)
        self.connect(criticalButton, QtCore.SIGNAL("clicked()"), self.slotCritical)
        self.connect(aboutButton, QtCore.SIGNAL("clicked()"), self.slotAbout)
        self.connect(aboutqtButton, QtCore.SIGNAL("clicked()"), self.slotAboutQt)
        self.connect(customButton, QtCore.SIGNAL("clicked()"), self.slotCustom)
    
    def slotQuestion(self):
        button = QtGui.QMessageBox.question(self, "Question", self.tr("已达到文件尾,是否从头查找?"),
                                      QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
        if button == QtGui.QMessageBox.Ok:
            self.label.setText("Question button/OK")
        elif button == QtGui.QMessageBox.Cancel:
            self.label.setText("Question button/Cancel")
        else:
            return
    
    def slotInformation(self):
        QtGui.QMessageBox.information(self, "Information",
                                      self.tr("填写任意想告诉于用户的信息!"))
        self.label.setText("Information MessageBox")
    
    def slotWarning(self):
        button = QtGui.QMessageBox.warning(self, "Warning",
                                           self.tr("是否保存对文档的修改?"),
                                            QtGui.QMessageBox.Save|QtGui.QMessageBox.Discard|QtGui.QMessageBox.Cancel,
                                            QtGui.QMessageBox.Save)
        if button==QtGui.QMessageBox.Save:
            self.label.setText("Warning button/Save")
        elif button == QtGui.QMessageBox.Discard:
            self.label.setText("Warning button/Discard")
        elif button == QtGui.QMessageBox.Cancel:
            self.label.setText("Warning button/Cancel")
        else:
            return
    
    def slotCritical(self):
        QtGui.QMessageBox.critical(self, "Critical", 
                                   self.tr("提醒用户一个致命的错误!"))
        self.label.setText("Critical MessageBox")
    
    def slotAbout(self):
        QtGui.QMessageBox.about(self, "About", self.tr("About事例"))
        self.label.setText("About MessageBox")
    
    def slotAboutQt(self):
        QtGui.QMessageBox.aboutQt(self, "About Qt")
        self.label.setText("About Qt MessageBox")
            
    def slotCustom(self):
        customMsgBox = QtGui.QMessageBox(self)
        customMsgBox.setWindowTitle("Custom message box")
        lockButton=customMsgBox.addButton(self.tr("锁定"), QtGui.QMessageBox.ActionRole)
        unlockButton = customMsgBox.addButton(self.tr("解锁"), QtGui.QMessageBox.ActionRole)
        cancelButton=customMsgBox.addButton("cancel", QtGui.QMessageBox.ActionRole)
        customMsgBox.setText(self.tr("这是一个自定义消息框"))
        customMsgBox.exec_()
        button= customMsgBox.clickedButton()
        if button == lockButton:
            self.label.setText("Custom MessageBox/lock")
        elif button == unlockButton:
            self.label.setText("Custom MessageBox/unlock")
        elif button==cancelButton:
            self.label.setText("Custom MessageBox/Cancel")
            
                                      
        
                                              
        
    
def main():
    app=QtGui.QApplication(sys.argv) 
    form = MessageBoxDlg()
    form.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()