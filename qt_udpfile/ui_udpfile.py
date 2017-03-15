# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udpfile.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_UdpFile(object):
    def setupUi(self, UdpFile):
        UdpFile.setObjectName(_fromUtf8("UdpFile"))
        UdpFile.resize(1134, 729)
        self.btn_openfile = QtGui.QPushButton(UdpFile)
        self.btn_openfile.setGeometry(QtCore.QRect(260, 490, 187, 57))
        self.btn_openfile.setObjectName(_fromUtf8("btn_openfile"))
        self.btn_update = QtGui.QPushButton(UdpFile)
        self.btn_update.setGeometry(QtCore.QRect(560, 490, 187, 57))
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.label = QtGui.QLabel(UdpFile)
        self.label.setGeometry(QtCore.QRect(92, 148, 105, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.edit_localip = QtGui.QLineEdit(UdpFile)
        self.edit_localip.setGeometry(QtCore.QRect(209, 140, 294, 51))
        self.edit_localip.setObjectName(_fromUtf8("edit_localip"))
        self.label_2 = QtGui.QLabel(UdpFile)
        self.label_2.setGeometry(QtCore.QRect(515, 148, 135, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.edit_localport = QtGui.QLineEdit(UdpFile)
        self.edit_localport.setGeometry(QtCore.QRect(662, 140, 294, 51))
        self.edit_localport.setObjectName(_fromUtf8("edit_localport"))
        self.label_3 = QtGui.QLabel(UdpFile)
        self.label_3.setGeometry(QtCore.QRect(92, 230, 105, 30))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.edit_remoteip = QtGui.QLineEdit(UdpFile)
        self.edit_remoteip.setGeometry(QtCore.QRect(209, 220, 294, 51))
        self.edit_remoteip.setObjectName(_fromUtf8("edit_remoteip"))
        self.label_4 = QtGui.QLabel(UdpFile)
        self.label_4.setGeometry(QtCore.QRect(515, 230, 135, 30))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.edit_remoteport = QtGui.QLineEdit(UdpFile)
        self.edit_remoteport.setGeometry(QtCore.QRect(662, 220, 294, 51))
        self.edit_remoteport.setObjectName(_fromUtf8("edit_remoteport"))
        self.bar_sendprogress = QtGui.QProgressBar(UdpFile)
        self.bar_sendprogress.setGeometry(QtCore.QRect(130, 630, 911, 32))
        self.bar_sendprogress.setProperty("value", 24)
        self.bar_sendprogress.setObjectName(_fromUtf8("bar_sendprogress"))

        self.retranslateUi(UdpFile)
        QtCore.QObject.connect(self.btn_openfile, QtCore.SIGNAL(_fromUtf8("clicked()")), UdpFile.slotOpen)
        QtCore.QObject.connect(self.btn_update, QtCore.SIGNAL(_fromUtf8("clicked()")), UdpFile.slotUpdate)
        QtCore.QObject.connect(self.edit_localip, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), UdpFile.slotLocalIP)
        QtCore.QObject.connect(self.edit_localport, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), UdpFile.slotLocalPort)
        QtCore.QObject.connect(self.edit_remoteip, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), UdpFile.slotRemoteIP)
        QtCore.QObject.connect(self.edit_remoteport, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), UdpFile.slotRemotePort)
        QtCore.QMetaObject.connectSlotsByName(UdpFile)

    def retranslateUi(self, UdpFile):
        UdpFile.setWindowTitle(_translate("UdpFile", "Udp-file", None))
        self.btn_openfile.setText(_translate("UdpFile", "打开文件", None))
        self.btn_update.setText(_translate("UdpFile", "更新程序", None))
        self.label.setText(_translate("UdpFile", "本地IP:", None))
        self.label_2.setText(_translate("UdpFile", "本地端口:", None))
        self.label_3.setText(_translate("UdpFile", "远方IP:", None))
        self.label_4.setText(_translate("UdpFile", "远方端口:", None))

