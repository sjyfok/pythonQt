# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:36:32 2017

@author: song
"""
from PyQt4 import QtCore, QtGui

import sys

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class InputDlg(QtGui.QDialog):
    def __init__(self, parent=None):
        super(InputDlg, self).__init__(parent)
        
        label1 = QtGui.QLabel(self.tr("姓名"))
        label2 = QtGui.QLabel(self.tr("性别"))
        label3 = QtGui.QLabel(self.tr("年龄"))
        label4 = QtGui.QLabel(self.tr("身高"))
        
        self.nameLabel = QtGui.QLabel("TengWei")
        self.nameLabel.setFrameStyle(QtGui.QFrame.Panel|QtGui.QFrame.Sunken)
        self.sexLabel = QtGui.QLabel(self.tr("男"))
        self.sexLabel.setFrameStyle(QtGui.QFrame.Panel|QtGui.QFrame.Sunken)
        self.ageLabel = QtGui.QLabel("25")
        self.ageLabel.setFrameStyle(QtGui.QFrame.Panel|QtGui.QFrame.Sunken)
        self.statureLabel=QtGui.QLabel("168")
        self.statureLabel.setFrameStyle(QtGui.QFrame.Panel|QtGui.QFrame.Sunken)
        
        nameButton = QtGui.QPushButton("...")
        sexButton = QtGui.QPushButton("...")
        ageButton = QtGui.QPushButton("...")
        statureButton = QtGui.QPushButton("...")
        
        self.connect(nameButton, QtCore.SIGNAL("clicked()"),self.slotName)
        self.connect(sexButton, QtCore.SIGNAL("clicked()"), self.slotSex)
        self.connect(ageButton, QtCore.SIGNAL("clicked()"), self.slotAge)
        self.connect(statureButton, QtCore.SIGNAL("clicked()"), self.slotStature)
        
        layout = QtGui.QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.nameLabel, 0, 1)
        layout.addWidget(nameButton, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.sexLabel, 1, 1)
        layout.addWidget(sexButton, 1, 2)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.ageLabel, 2, 1)
        layout.addWidget(ageButton, 2, 2)
        layout.addWidget(label3, 3, 0)
        layout.addWidget(self.statureLabel, 3, 1)
        layout.addWidget(statureButton, 3, 2)
        
        self.setLayout(layout)
        self.setWindowTitle(self.tr("资料收集"))
        
    def slotName(self):
        name, ok = QtGui.QInputDialog.getText(self, self.tr("用户名"), self.tr("请输入新名字:"),
                                              QtGui.QLineEdit.Normal, self.nameLabel.text())
        if ok and  name:
            self.nameLabel.setText(name)
            #self.nameLable.setText('ok')
    
    def slotSex(self):
        tlist=[]
        tlist.append(self.tr("男"))
        tlist.append(self.tr("女"))
        sex,ok = QtGui.QInputDialog.getItem(self, self.tr("性别"),
                                            self.tr("请选择性别"), tlist)
        if ok:
            self.sexLabel.setText(sex)
    
    def slotAge(self):
        age, ok = QtGui.QInputDialog.getInteger(self, self.tr("年龄"),
                                                self.tr("请输入年龄:"),
                                                int(self.ageLabel.text()), 0, 150)
        if ok:
            self.ageLabel.setText(str(age))
        
    def slotStature(self):
        stature,ok=QtGui.QInputDialog.getDouble(self, self.tr("身高"),
                                                self.tr("请输入身高:"),
                                                float(self.statureLabel.text()),0,2300.00)
        if ok:
            self.statureLabel.setText(str(stature))
        
                                              
        
    
def main():
    app=QtGui.QApplication(sys.argv) 
    form = InputDlg()
    form.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()