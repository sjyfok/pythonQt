# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:26:47 2017

@author: song
"""

from PyQt4 import QtCore, QtGui
import sys

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class StandardDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        super(StandardDialog, self).__init__(parent)
        self.setWindowTitle("Standard Dialog")
        filePushButton = QtGui.QPushButton(self.tr("文件对话框"))
        colorPushButton = QtGui.QPushButton(self.tr("颜色对话框"))
        fontPushButton = QtGui.QPushButton(self.tr("字体对话框"))
        self.fileLineEdit = QtGui.QLineEdit()
        self.colorFrame = QtGui.QFrame(self)
        self.colorFrame.setFrameShape(QtGui.QFrame.Box)
        self.colorFrame.setAutoFillBackground(True)
        self.fontLineEdit = QtGui.QLineEdit("Hello World!")
        layout = QtGui.QGridLayout()
        layout.addWidget(filePushButton, 0, 0)
        layout.addWidget(self.fileLineEdit, 0, 1)
        layout.addWidget(colorPushButton, 1, 0)
        layout.addWidget(self.colorFrame, 1, 1)
        layout.addWidget(fontPushButton, 2, 0)
        layout.addWidget(self.fontLineEdit, 2, 1)
        self.setLayout(layout)
        self.connect(filePushButton, QtCore.SIGNAL("clicked()"), self.openFile)
        self.connect(colorPushButton, QtCore.SIGNAL("clicked()"), self.openColor)
        self.connect(fontPushButton, QtCore.SIGNAL("clicked()"), self.openFont)

    def openFile(self):
        s = QtGui.QFileDialog.getOpenFileName(self, "Open file dialog", "/", "python files(*.py)")
        self.fileLineEdit.setText(str(s))
        
    def openColor(self):
        c = QtGui.QColorDialog.getColor()#(QtCore.Qt.blue)
        if c.isValid():
            #print(c)
            self.colorFrame.setPalette(QtGui.QPalette(c))
           # self.colorFrame.setStyleSheet("QWidget { background-color: %s }" % c.name())
    
    def openFont(self):
        f,ok = QtGui.QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(f)
            
        
        
    
        
def main():
    app=QtGui.QApplication(sys.argv) 
    form = StandardDialog()
    form.show()
    
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()