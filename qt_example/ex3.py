# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:26:47 2017

@author: song
"""

from PyQt4 import QtCore, QtGui

import sys

class Geometry(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Geometry, self).__init__(parent)
        self.setWindowTitle("Geometry")
        Label1 = QtGui.QLabel("x0:")
        Label2 = QtGui.QLabel("y0:")
        Label3 = QtGui.QLabel("frameGeometry():")
        Label4 = QtGui.QLabel("pos():")
        Label5 = QtGui.QLabel("Geometry():")
        Label6 = QtGui.QLabel("width():")
        Label7 = QtGui.QLabel("height():")
        Label8 = QtGui.QLabel("rect():")
        Label9 = QtGui.QLabel("size():")
        self.xLabel = QtGui.QLabel()
        self.yLabel = QtGui.QLabel()
        self.frameGeometryLabel = QtGui.QLabel()
        self.posLabel = QtGui.QLabel()
        self.geometryLabel = QtGui.QLabel()
        self.widthLabel = QtGui.QLabel()
        self.heightLabel = QtGui.QLabel()
        self.rectLabel = QtGui.QLabel()
        self.sizeLabel = QtGui.QLabel()
        
        layout = QtGui.QGridLayout()
        layout.addWidget(Label1, 0, 0)
        layout.addWidget(self.xLabel, 0, 1)
        layout.addWidget(Label2, 1, 0)
        layout.addWidget(self.yLabel, 1, 1)
        layout.addWidget(Label3, 2, 0)
        layout.addWidget(self.frameGeometryLabel, 2, 1)
        layout.addWidget(Label4, 3, 0)
        layout.addWidget(self.posLabel, 3, 1)
        layout.addWidget(Label5, 4, 0)
        layout.addWidget(self.geometryLabel, 4, 1)
        layout.addWidget(Label6, 5, 0)
        layout.addWidget(self.widthLabel, 5, 1)
        layout.addWidget(Label7, 6, 0)
        layout.addWidget(self.heightLabel, 6, 1)
        layout.addWidget(Label8, 7, 0)
        layout.addWidget(self.rectLabel, 7, 1)
        layout.addWidget(Label9, 8, 0)
        layout.addWidget(self.sizeLabel, 8, 1)
        
        self.setLayout(layout)
        self.updateLabel()
    
    def moveEvent(self, event):
        self.updateLabel()
        
    def resizeEvent(self, event):
        self.updateLabel()
        
    def updateLabel(self):
        self.xLabel.setText(str(self.x()))
        self.yLabel.setText(str(self.y()))
                
        self.frameGeometryLabel.setText(str(self.frameGeometry().x())
        +","+str(self.frameGeometry().y())+","
        + str(self.frameGeometry().width())+","
        + str(self.frameGeometry().height()))
        
        self.posLabel.setText(str(self.pos().x())+","
        +str(self.pos().y()))
        
        self.geometryLabel.setText(str(self.geometry().x())+","
        +str(self.geometry().y())+"," +
        str(self.geometry().width())+","+str(self.geometry().height()))
        
        self.widthLabel.setText(str(self.width()))
        self.heightLabel.setText(str(self.height()))
        
        self.rectLabel.setText(str(self.rect().x())
        +","+str(self.rect().y())+","+str(self.rect().width())+","
        +str(self.height()))
        
        self.sizeLabel.setText(str(self.size().width()) +","+
        str(self.size().height()))
        
        
        
        

        
        
    
        
def main():
    app=QtGui.QApplication(sys.argv) 
    form = Geometry()
    form.show()
    sys.exit(app.exec_())
    
  
      
     
    
    
    
if __name__ == '__main__':
    main()