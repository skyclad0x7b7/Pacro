from os.path import isfile
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

		# Set list column
		self.ui.list_script.setColumnWidth(0, 40)
		self.ui.list_script.setColumnWidth(1, 80)
		self.ui.list_script.setColumnWidth(2, 140)

		# Set Signal
		QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.button_open_clicked)
		QtCore.QObject.connect(self.ui.button_run, QtCore.SIGNAL("clicked()"), self.button_run_clicked)

	
	def button_open_clicked(self):
		fd = QtGui.QFileDialog(self)
		script_file = fd.getOpenFileName()
		if isfile(script_file):
			script = codecs.open(script_file, 'r', 'utf-8').read()
			try:
				self.script = json.loads(script)
			except:
				# Invalid Json File
				self.show_messagebox('Error', 'Invalid Json File!', QtGui.QMessageBox.Warning)
				return False

			self.update_list_script(self.script)

	def update_list_script(self, script):
		for s in script:
			new_script = QtGui.QTreeWidgetItem(self.ui.list_script)
			new_script.setText(0, str(s['id']))
			new_script.setText(1, s['op'])
			new_script.setText(2, self.arg_parse(s['arg']))

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
		# should be thread
		executor = PacroExecutor(self.script)
		executor.execute()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	pacro_window = PacroGui()
	pacro_window.show()
	sys.exit(app.exec_())

# @ Todo : MultiThreading