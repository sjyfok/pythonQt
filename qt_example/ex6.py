# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:36:32 2017

@author: song
"""
from PyQt4 import QtCore, QtGui

import sys

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class MyQQ(QToolBox):
    def __init__(self, parent=None):
        super(MyQQ, self).__init__(parent)
        toolButton1_1=QtGui.QToolButton()
        toolButton1_1.setText(self.tr("朽木"))
        toolButton1_1.setIcon(QIcon("image/9.gif"))
        toolButton1_1.setIconSize(QSize(60,60))
        toolButton1_1.setAutoRaise(True)
        
        toolButton1_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        toolButton1_2 = QToolButton()
        toolButton1_2.setText(self.tr("Cindy"))
        toolButton1_2.setIcon(QIcon("image/8.gif"))
        toolButton1_2.setIconSize(QSize(60,60))
        toolButton1_2.setAutoRaise(True)
        toolButton1_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        toolButton1_3 = QToolButton()
        toolButton1_3.setText(self.tr("了了"))
        toolButton1_3.setIcon(QIcon("image/1.gif"))
        toolButton1_3.setIconSize(QSize(60,60))
        toolButton1_3.setAutoRaise(True)
        toolButton1_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            
        toolButton1_4 = QToolButton()
        toolButton1_4.setText(self.tr("张三虎"))
        toolButton1_4.setIcon(QIcon("image/3.gif"))
        toolButton1_4.setIconSize(QSize(60,60))
        toolButton1_4.setAutoRaise(True)
        toolButton1_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
                                         
        toolButton1_5 = QToolButton()
        toolButton1_5.setText(self.tr("CSDN"))
        toolButton1_5.setIcon(QIcon("image/4.gif"))
        toolButton1_5.setIconSize(QSize(60,60))
        toolButton1_5.setAutoRaise(True)
        toolButton1_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
                                         
        toolButton2_1 = QToolButton()
        toolButton2_1.setText(self.tr("天的另一边"))
        toolButton2_1.setIcon(QIcon("image/5.gif"))
        toolButton2_1.setIconSize(QSize(60,60))
        toolButton2_1.setAutoRaise(True)
        toolButton2_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
               
        toolButton2_2 = QtGui.QToolButton()
        toolButton2_2.setText(self.tr("蓝绿不分"))
        toolButton2_2.setIcon(QtGui.QIcon("image/6.gif"))
        toolButton2_2.setIconSize(QtCore.QSize(60,60))
        toolButton2_2.setAutoRaise(True)
        toolButton2_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
                                              
        toolButton3_1 = QtGui.QToolButton()
        toolButton3_1.setText(self.tr("老牛"))
        toolButton3_1.setIcon(QtGui.QIcon("image/7.gif"))
        toolButton3_1.setIconSize(QtCore.QSize(60,60))
        toolButton3_1.setAutoRaise(True)
        toolButton3_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
         
        toolButton3_2 = QtGui.QToolButton()
        toolButton3_2.setText(self.tr("张三疯"))
        toolButton3_2.setIcon(QtGui.QIcon("image/8.gif"))
        toolButton3_2.setIconSize(QtCore.QSize(60,60))
        toolButton3_2.setAutoRaise(True)
        toolButton3_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        groupbox1=QtGui.QGroupBox()
        vlayout1 = QtGui.QVBoxLayout(groupbox1)
        vlayout1.setMargin(10)                                                        
        vlayout1.setAlignment(QtCore.Qt.AlignCenter)
        vlayout1.addWidget(toolButton1_1)
        vlayout1.addWidget(toolButton1_2)
        vlayout1.addWidget(toolButton1_3)
        vlayout1.addWidget(toolButton1_4)
        vlayout1.addWidget(toolButton1_5)
        vlayout1.addStretch()
        
        groupbox2=QtGui.QGroupBox()
        vlayout2=QtGui.QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(QtCore.Qt.AlignCenter)
        vlayout2.addWidget(toolButton2_1)
        vlayout2.addWidget(toolButton2_2) 
        
        groupbox3=QtGui.QGroupBox()
        vlayout3=QtGui.QVBoxLayout(groupbox3)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(QtCore.Qt.AlignCenter)
        vlayout2.addWidget(toolButton2_1)
        vlayout2.addWidget(toolButton2_2) 
        
        
        
        
                                          
                                          
    
def main():
    app=QtGui.QApplication(sys.argv) 
    myqq = MyQQ()
    myqq.setWindowTitle("My QQ")
    myqq.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()