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
from PyQt4 import QtCore, QtGui, QtWebKit

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
            return True

        print event.Position
        cur_time = int(time.clock() * 1000)
        if self.prev_time == 0: # If it was first click
            self.prev_time = cur_time
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
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.button_start, QtCore.SIGNAL("clicked()"), self.button_start_clicked)


    def button_start_clicked(self):
        """ When run button clicked """
        execute_thread = Thread(target = self.execute)
        execute_thread.setDaemon(True)
        execute_thread.start()

    def execute(self):
        # Thread Function

        # Disable start button
        self.ui.button_start.setEnabled(False)

        h = Hooker()
        script = h.hook_mouse()
        script = json.dumps(script, sort_keys=True, indent=4)

        # Saving file
        fd = QtGui.QFileDialog(self)
        newFile = fd.getSaveFileName()
        if newFile:
            s = codecs.open(newFile, 'w', 'utf-8')
            s.write(unicode(script))
            s.close();

        # Enable start button
        self.ui.button_start.setEnabled(True)
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pacro_window = MakeScript()
    pacro_window.show()
    sys.exit(app.exec_())

    """
    h = Hooker()
    h.set_file_path("script.json")
    raw_input("Press Enter to Start Hooking")
    h.hook_mouse()"""