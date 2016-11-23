# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(430, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.list_script = QtGui.QTreeWidget(self.centralwidget)
        self.list_script.setGeometry(QtCore.QRect(10, 10, 281, 381))
        self.list_script.setObjectName(_fromUtf8("list_script"))
        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(300, 10, 121, 23))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.button_run = QtGui.QPushButton(self.centralwidget)
        self.button_run.setGeometry(QtCore.QRect(300, 40, 121, 23))
        self.button_run.setObjectName(_fromUtf8("button_run"))
        self.button_stop = QtGui.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(300, 90, 121, 23))
        self.button_stop.setObjectName(_fromUtf8("button_stop"))
        self.checkbox_always_on_top = QtGui.QCheckBox(self.centralwidget)
        self.checkbox_always_on_top.setGeometry(QtCore.QRect(300, 370, 111, 16))
        self.checkbox_always_on_top.setObjectName(_fromUtf8("checkbox_always_on_top"))
        self.checkbox_repeat = QtGui.QCheckBox(self.centralwidget)
        self.checkbox_repeat.setGeometry(QtCore.QRect(300, 70, 81, 16))
        self.checkbox_repeat.setObjectName(_fromUtf8("checkbox_repeat"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pacro", None))
        self.list_script.headerItem().setText(0, _translate("MainWindow", "Id", None))
        self.list_script.headerItem().setText(1, _translate("MainWindow", "Operation", None))
        self.list_script.headerItem().setText(2, _translate("MainWindow", "Arguments", None))
        self.button_open.setText(_translate("MainWindow", "Open", None))
        self.button_run.setText(_translate("MainWindow", "Run", None))
        self.button_stop.setText(_translate("MainWindow", "Stop", None))
        self.checkbox_always_on_top.setText(_translate("MainWindow", "Always On Top", None))
        self.checkbox_repeat.setText(_translate("MainWindow", "Repeat", None))

