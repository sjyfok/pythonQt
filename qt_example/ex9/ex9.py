# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:36:32 2017

@author: song
"""
from PyQt4 import QtCore, QtGui

import sys
import exui9

class TestDialog(QtGui.QDialog, exui9.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        self.setupUi(self)
        
        
        
                                          
                                          
    
def main():
    app=QtGui.QApplication(sys.argv) 
    dialog = TestDialog()
    #myqq.setWindowTitle("My Table")
    dialog.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()