from os.path import isfile
from threading import Thread
import sys
import codecs
import json

from lib.gui.Main import Ui_MainWindow
from lib.pacro_core import PacroExecutor
from PyQt4 import QtCore, QtGui, QtWebKit

class PacroGui(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize variable
        self.executor = None
        self.item_list = []

        # Set list column width
        self.ui.list_script.setColumnWidth(0, 40)
        self.ui.list_script.setColumnWidth(1, 80)
        self.ui.list_script.setColumnWidth(2, 140)

        # Set Signal
        QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.button_open_clicked)
        QtCore.QObject.connect(self.ui.button_run, QtCore.SIGNAL("clicked()"), self.button_run_clicked)
        QtCore.QObject.connect(self.ui.button_stop, QtCore.SIGNAL("clicked()"), self.button_stop_clicked)
        QtCore.QObject.connect(self.ui.checkbox_always_on_top, QtCore.SIGNAL("stateChanged(int)"), self.checkbox_always_on_top_clicked)

        # Disable buttons
        self.ui.button_run.setEnabled(False)
        self.ui.button_stop.setEnabled(False)


    def button_open_clicked(self):
        """ When open button clicked """
        fd = QtGui.QFileDialog(self)
        script_file = fd.getOpenFileName()
        if isfile(script_file): # Check the file exists
            script = codecs.open(script_file, 'r', 'utf-8').read()
            try:
                self.script = json.loads(script)
            except:
                # Invalid Json File
                self.show_messagebox('Error', 'Invalid Json File!', QtGui.QMessageBox.Warning)
                return False

            self.update_list_script(self.script)
            self.ui.button_run.setEnabled(True)

    def update_list_script(self, script):
        self.ui.list_script.clear()
        self.item_list = []
        for index, s in enumerate(script):
            new_script = QtGui.QTreeWidgetItem(self.ui.list_script)
            new_script.setText(0, str(index))
            new_script.setText(1, s['op'])
            new_script.setText(2, self.arg_parse(s['arg']))
            self.item_list.append(new_script)

    def show_messagebox(self, msg_title, msg_text, msg_icon, msg_buttons = [], msg_detail = None):
        message = QtGui.QMessageBox(self)
        message.setWindowTitle(msg_title)
        message.setText(msg_text)
        message.setIcon(msg_icon)
        for button in msg_buttons:
            message.addButton(msg_buttons[0], msg_buttons[1])

        if msg_detail != None:
            message.setDetailedText(msg_detail)
        
        message.exec_()
        return message.clickedButton().text()

    def arg_parse(self, dic):
        ret = []
        for i in dic.keys():
            ret.append("{0}={1}".format(i, dic[i]))
        return ",\n".join(ret)

    def button_run_clicked(self):
        """ When run button clicked """
        execute_thread = Thread(target = self.execute)
        execute_thread.setDaemon(True)
        execute_thread.start()

    def execute(self):
        # Thread Function

        # Disable run button, enable stop button
        self.ui.button_run.setEnabled(False)
        self.ui.button_stop.setEnabled(True)

        # Run the script
        self.executor = PacroExecutor(self.script)
        self.executor.ip_signal.connect(self.on_ip_changed)
        self.executor.finished_signal.connect(self.on_finished)
        self.executor.execute()

        # Enable run button, disable stop button
        self.ui.button_run.setEnabled(True)
        self.ui.button_stop.setEnabled(False)

    def button_stop_clicked(self):
        """ When stop button clicked """
        self.executor.stop()

    def checkbox_always_on_top_clicked(self, value):
        
        if value == 2:
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        elif value == 0:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

        self.show()

    @QtCore.pyqtSlot(int)
    def on_ip_changed(self, changed_ip):
        """ When ip changed, it changes the color of row """
        self.item_list[changed_ip].setTextColor(0, QtGui.QColor(255, 0, 0))
        self.item_list[changed_ip].setTextColor(1, QtGui.QColor(255, 0, 0))
        self.item_list[changed_ip].setTextColor(2, QtGui.QColor(255, 0, 0))

        if changed_ip > 0:
            # previous row
            self.item_list[changed_ip-1].setTextColor(0, QtGui.QColor(0, 0, 0))
            self.item_list[changed_ip-1].setTextColor(1, QtGui.QColor(0, 0, 0))
            self.item_list[changed_ip-1].setTextColor(2, QtGui.QColor(0, 0, 0))

    @QtCore.pyqtSlot(int)
    def on_finished(self, final_ip):
        self.item_list[final_ip].setTextColor(0, QtGui.QColor(0, 0, 0))
        self.item_list[final_ip].setTextColor(1, QtGui.QColor(0, 0, 0))
        self.item_list[final_ip].setTextColor(2, QtGui.QColor(0, 0, 0))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pacro_window = PacroGui()
    pacro_window.show()
    sys.exit(app.exec_())