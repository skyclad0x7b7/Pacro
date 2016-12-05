# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MakeScript.ui'
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
        MainWindow.resize(332, 84)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_start = QtGui.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(10, 10, 161, 41))
        self.button_start.setObjectName(_fromUtf8("button_start"))
        self.button_change_finish_button = QtGui.QPushButton(self.centralwidget)
        self.button_change_finish_button.setGeometry(QtCore.QRect(180, 10, 141, 41))
        self.button_change_finish_button.setObjectName(_fromUtf8("button_change_finish_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_finish_button = QtGui.QLabel(self.centralwidget)
        self.label_finish_button.setGeometry(QtCore.QRect(180, 60, 131, 16))
        self.label_finish_button.setObjectName(_fromUtf8("label_finish_button"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MakeScript", None))
        self.button_start.setText(_translate("MainWindow", "Start", None))
        self.button_change_finish_button.setText(_translate("MainWindow", "Change Finish Button", None))
        self.label.setText(_translate("MainWindow", "Current Finish Button : ", None))
        self.label_finish_button.setText(_translate("MainWindow", "mouse right down", None))

