from os.path import isfile
import sys
import codecs
import json

from lib.gui.Main import Ui_MainWindow

from PyQt4 import QtCore, QtGui, QtWebKit

class PacroGui(QtGui.QMainWindow):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Set list column
		self.ui.list_script.setColumnWidth(0, 50)
		self.ui.list_script.setColumnWidth(1, 100)
		self.ui.list_script.setColumnWidth(2, 100)

		# Set Signal
		QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.button_open_clicked)

	
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

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	pacro_window = PacroGui()
	pacro_window.show()
	sys.exit(app.exec_())