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
        MainWindow.resize(403, 433)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.list_script = QtGui.QTreeWidget(self.centralwidget)
        self.list_script.setGeometry(QtCore.QRect(10, 10, 281, 381))
        self.list_script.setObjectName(_fromUtf8("list_script"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 10, 91, 381))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.button_open = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.verticalLayout.addWidget(self.button_open)
        self.button_run = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_run.setObjectName(_fromUtf8("button_run"))
        self.verticalLayout.addWidget(self.button_run)
        self.button_stop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_stop.setObjectName(_fromUtf8("button_stop"))
        self.verticalLayout.addWidget(self.button_stop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

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

