"""
    Automatic script making.
    It might be added to Pacro.py
"""


import time
import pythoncom
import sys
import codecs
import json
try:
    import pyHook
except:
    print """pyHook not installed.
please download .whl file in \"http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook\"
and type the command like 'pip install pyHook-1.5.1-cp27-none-win32.whl' for 32bit or
'pip install pyHook-1.5.1-cp27-none-win_amd64.whl' for 64bit."""
    exit(1)

from threading import Thread
from lib.gui.MakeScript import Ui_MainWindow
from PyQt4 import QtCore, QtGui

class Hooker():
    def __init__(self):
        self.prev_time = 0
        self.scripts = []
        self.hook_manager = pyHook.HookManager()
        self.end_flag = False

    def set_file_path(self, script_path):
        self.script_path = script_path

    def hook_mouse(self):
        self.hook_manager.SubscribeMouseAllButtonsDown(self.onclick)
        self.hook_manager.HookMouse()
        while not self.end_flag:
            pythoncom.PumpWaitingMessages()
        return self.scripts

    def unhook_mouse(self):
        self.hook_manager.UnhookMouse()
    
    def onclick(self, event):
        if "mouse right down" == event.MessageName:
            self.end_flag = True
            self.unhook_mouse()
            return False

        print event.Position
        cur_time = int(time.clock() * 1000)
        print self.prev_time
        if self.prev_time == 0: # If it was first click
            print "Cur : ", cur_time
            self.prev_time = cur_time
            print "prev : ", self.prev_time
        else:
            self.scripts.append(
                {
                    "op":"sleep",
                    "arg":{
                        "ms": cur_time - self.prev_time
                    }
                }
            )
            self.prev_time = cur_time

        self.scripts.append(
            {
            "op":"click",
            "arg":{
                "x-pos":event.Position[0],
                "y-pos":event.Position[1]
            }
            }
        )
        return True

class MakeScript(QtGui.QMainWindow):
    # Initialize Signal
    execute_started_signal  = QtCore.pyqtSignal()
    execute_ended_signal    = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set Signal
        QtCore.QObject.connect(self.ui.button_start, QtCore.SIGNAL("clicked()"), self.button_start_clicked)

        self.execute_started_signal.connect(self.execute_started)
        self.execute_ended_signal.connect(self.execute_ended)


    def button_start_clicked(self):
        """ When run button clicked """
        execute_thread = Thread(target = self.execute)
        execute_thread.setDaemon(True)
        execute_thread.start()

    def execute(self):
        # Thread Function
        self.execute_started_signal.emit()  # Start Signal

        h = Hooker()
        script = h.hook_mouse()
        self.script = json.dumps(script, sort_keys=True, indent=4)

        self.execute_ended_signal.emit()    # End Signal

    @QtCore.pyqtSlot() # Slot for MakeScript
    def execute_started(self):
        # Disable Start button
        self.ui.button_start.setEnabled(False)

    @QtCore.pyqtSlot() # Slot for MakeScript
    def execute_ended(self):
        # Enable Start button
        self.ui.button_start.setEnabled(True)
        # Saving file
        fd = QtGui.QFileDialog(self)
        newFile = fd.getSaveFileName()
        if newFile:
            s = codecs.open(newFile, 'w', 'utf-8')
            s.write(unicode(self.script))
            s.close();


if __name__ == "__main__":
    time.clock()
    app = QtGui.QApplication(sys.argv)
    pacro_window = MakeScript()
    pacro_window.show()
    sys.exit(app.exec_())

    """
    h = Hooker()
    h.set_file_path("script.json")
    raw_input("Press Enter to Start Hooking")
    h.hook_mouse()"""