# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:35:18 2017

@author: song
"""

from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
b = QtGui.QPushButton("hello")
b.show()
app.connect(b, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
sys.exit(app.exec_())
    