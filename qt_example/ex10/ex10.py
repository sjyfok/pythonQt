# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:36:32 2017

@author: song
"""
from PyQt4 import QtCore, QtGui

import sys
import ex10_1, ex10_2, ex10_3 

class TestDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        firstUi = ex10_1.Ui_Dialog()
        secondUi = ex10_2.Ui_Dialog()
        self.thirdUi = ex10_3.Ui_Dialog()
        
        tabWidget = QtGui.QTabWidget(self)
        w1 = QtGui.QWidget()
        firstUi.setupUi(w1)
        w2 = QtGui.QWidget()
        secondUi.setupUi(w2)
        tabWidget.addTab(w1, "First")
        tabWidget.addTab(w2, "Second")
        tabWidget.resize(380, 380)
        self.connect(firstUi.childPushButton, QtCore.SIGNAL("clicked()"), self.slotChild)
        self.connect(secondUi.closePushButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))
        
    def slotChild(self):
        dlg = QtGui.QDialog()
        self.thirdUi.setupUi(dlg)
        dlg.exec_()
    
    
        
        
        
                                          
                                          
    
def main():
    app=QtGui.QApplication(sys.argv) 
    dialog = TestDialog()
    #myqq.setWindowTitle("My Table")
    dialog.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()