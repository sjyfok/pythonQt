# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CBRT.ui'
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

class Ui_CBRTLoader(object):
    def setupUi(self, CBRTLoader):
        CBRTLoader.setObjectName(_fromUtf8("CBRTLoader"))
        CBRTLoader.resize(1496, 1182)
        self.groupBox = QtGui.QGroupBox(CBRTLoader)
        self.groupBox.setGeometry(QtCore.QRect(550, 10, 431, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.splitter_2 = QtGui.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(32, 52, 374, 57))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.pushButton_4 = QtGui.QPushButton(self.splitter_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.set_dev_list_btn = QtGui.QPushButton(self.splitter_2)
        self.set_dev_list_btn.setObjectName(_fromUtf8("set_dev_list_btn"))
        self.groupBox_2 = QtGui.QGroupBox(CBRTLoader)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 491, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.splitter = QtGui.QSplitter(self.groupBox_2)
        self.splitter.setGeometry(QtCore.QRect(12, 42, 435, 57))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.comsel_combox = QtGui.QComboBox(self.splitter)
        self.comsel_combox.setObjectName(_fromUtf8("comsel_combox"))
        self.com_open = QtGui.QPushButton(self.splitter)
        self.com_open.setObjectName(_fromUtf8("com_open"))
        self.layoutWidget = QtGui.QWidget(CBRTLoader)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.layoutWidget1 = QtGui.QWidget(CBRTLoader)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(CBRTLoader)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 170, 431, 121))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.splitter_3 = QtGui.QSplitter(self.groupBox_3)
        self.splitter_3.setGeometry(QtCore.QRect(32, 52, 374, 57))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.pushButton_5 = QtGui.QPushButton(self.splitter_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.set_dev_list_btn_2 = QtGui.QPushButton(self.splitter_3)
        self.set_dev_list_btn_2.setObjectName(_fromUtf8("set_dev_list_btn_2"))
        self.groupBox_4 = QtGui.QGroupBox(CBRTLoader)
        self.groupBox_4.setGeometry(QtCore.QRect(540, 330, 431, 121))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.splitter_4 = QtGui.QSplitter(self.groupBox_4)
        self.splitter_4.setGeometry(QtCore.QRect(40, 50, 374, 57))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.pushButton_6 = QtGui.QPushButton(self.splitter_4)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.set_dev_list_btn_3 = QtGui.QPushButton(self.splitter_4)
        self.set_dev_list_btn_3.setObjectName(_fromUtf8("set_dev_list_btn_3"))

        self.retranslateUi(CBRTLoader)
        QtCore.QObject.connect(self.com_open, QtCore.SIGNAL(_fromUtf8("clicked()")), CBRTLoader.open)
        QtCore.QObject.connect(self.comsel_combox, QtCore.SIGNAL(_fromUtf8("activated(int)")), CBRTLoader.onComSel)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), CBRTLoader.onUpdateFont)
        QtCore.QObject.connect(self.set_dev_list_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CBRTLoader.onOpenFontLib)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), CBRTLoader.onUpdateBmp)
        QtCore.QObject.connect(self.set_dev_list_btn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), CBRTLoader.onOpenBmp)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), CBRTLoader.onUpdatePrg)
        QtCore.QObject.connect(self.set_dev_list_btn_3, QtCore.SIGNAL(_fromUtf8("clicked()")), CBRTLoader.onOpenPrg)
        QtCore.QMetaObject.connectSlotsByName(CBRTLoader)

    def retranslateUi(self, CBRTLoader):
        CBRTLoader.setWindowTitle(_translate("CBRTLoader", "Dialog", None))
        self.groupBox.setTitle(_translate("CBRTLoader", "字库更新", None))
        self.pushButton_4.setText(_translate("CBRTLoader", "更新字库", None))
        self.set_dev_list_btn.setText(_translate("CBRTLoader", "打开字库", None))
        self.groupBox_2.setTitle(_translate("CBRTLoader", "全局设置", None))
        self.label.setText(_translate("CBRTLoader", "串口：", None))
        self.com_open.setText(_translate("CBRTLoader", "打开", None))
        self.groupBox_3.setTitle(_translate("CBRTLoader", "位图更新", None))
        self.pushButton_5.setText(_translate("CBRTLoader", "更新位图", None))
        self.set_dev_list_btn_2.setText(_translate("CBRTLoader", "打开位图", None))
        self.groupBox_4.setTitle(_translate("CBRTLoader", "程序更新", None))
        self.pushButton_6.setText(_translate("CBRTLoader", "更新程序", None))
        self.set_dev_list_btn_3.setText(_translate("CBRTLoader", "打开程序", None))

