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
        MainWindow.resize(329, 96)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_kor = QtGui.QLabel(self.centralwidget)
        self.label_kor.setGeometry(QtCore.QRect(10, 50, 311, 21))
        self.label_kor.setObjectName(_fromUtf8("label_kor"))
        self.label_eng = QtGui.QLabel(self.centralwidget)
        self.label_eng.setGeometry(QtCore.QRect(10, 70, 301, 16))
        self.label_eng.setObjectName(_fromUtf8("label_eng"))
        self.button_start = QtGui.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(10, 10, 311, 41))
        self.button_start.setObjectName(_fromUtf8("button_start"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MakeScript", None))
        self.label_kor.setText(_translate("MainWindow", "마우스 우클릭으로 끝낼 수 있습니다.", None))
        self.label_eng.setText(_translate("MainWindow", "You can finish it by right-clicking", None))
        self.button_start.setText(_translate("MainWindow", "Start", None))

