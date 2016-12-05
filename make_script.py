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
from lib.constant import *
from lib.gui.MakeScript import Ui_MainWindow
from PyQt4 import QtCore, QtGui

class Hooker():
    def __init__(self):
        self.finish_button = 'mouse right down'
        self.prev_time = 0
        self.scripts = []
        self.hook_manager = pyHook.HookManager()
        self.end_flag = False

    def set_file_path(self, script_path):
        self.script_path = script_path

    def hooking(self):
        self.end_flag = False # Initialize

        # Mouse Hook
        self.hook_manager.SubscribeMouseAllButtonsDown(self.onClick)
        self.hook_manager.HookMouse()

        # Keyboard Hook
        self.hook_manager.KeyDown = self.onKeyboardEvent
        self.hook_manager.HookKeyboard()

        while not self.end_flag:
            pythoncom.PumpWaitingMessages()
        return self.scripts

    def unhooking(self):
        self.end_flag = True
        self.hook_manager.UnhookMouse()
        self.hook_manager.UnhookKeyboard()
    
    def onClick(self, event):
        
        if self.finish_button == event.MessageName:
            
            self.unhooking()
            return True

        print event.Position
        print event.Time
        print "======================"

        if self.prev_time == 0: # If it was first event
            self.prev_time = event.Time
        else:
            self.scripts.append(
                {
                    "op":"sleep",
                    "arg":{
                        "ms": event.Time - self.prev_time
                    }
                }
            )
            self.prev_time = event.Time

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

    def onKeyboardEvent(self, event):
        
        if self.finish_button == event.Key:
            self.unhooking()
            return False

        print event.Key
        print event.Time
        print event.KeyID
        print "======================"

        if self.prev_time == 0: # If it was first event
            self.prev_time = event.Time
        else:
            self.scripts.append(
                {
                    "op":"sleep",
                    "arg":{
                        "ms": event.Time - self.prev_time
                    }
                }
            )
            self.prev_time = event.Time

        self.scripts.append(
            {
                "op":"keyboard",
                "arg":{
                    "key":event.Key
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
        self.hooker = Hooker()

        # Set Signal
        QtCore.QObject.connect(self.ui.button_start, QtCore.SIGNAL("clicked()"), self.button_start_clicked)
        QtCore.QObject.connect(self.ui.button_change_finish_button, QtCore.SIGNAL("clicked()"), self.button_change_finish_button_clicked)

        self.execute_started_signal.connect(self.execute_started)
        self.execute_ended_signal.connect(self.execute_ended)


    def button_start_clicked(self):
        """ When run button clicked """
        execute_thread = Thread(target = self.execute)
        execute_thread.setDaemon(True)
        execute_thread.start()

    def button_change_finish_button_clicked(self):
        """ When Change Finish Button Clicked """
        # Get Keys of Possible keyboard events
        possible_items = VK_CODE.keys() 

        # Append mouse events
        possible_items.append("mouse right down")
        possible_items.append("mouse left down")
        possible_items.sort()

        new_finish_button, ok = QtGui.QInputDialog.getItem(self, "Please select new finish button", "List of possible events", possible_items, 0, False)
        if ok and new_finish_button:
            self.ui.label_finish_button.setText(new_finish_button)
            self.hooker.finish_button = new_finish_button

    def execute(self):
        # Thread Function
        self.execute_started_signal.emit()  # Start Signal

        script = self.hooker.hooking()
        self.script = json.dumps(script, sort_keys=True, indent=4)

        self.execute_ended_signal.emit()    # End Signal

    @QtCore.pyqtSlot() # Slot for MakeScript
    def execute_started(self):
        # Disable Start button / Change Finish Button
        self.ui.button_start.setEnabled(False)
        self.ui.button_change_finish_button.setEnabled(False)

    @QtCore.pyqtSlot() # Slot for MakeScript
    def execute_ended(self):
        # Enable Start button / Change Finish Button
        self.ui.button_start.setEnabled(True)
        self.ui.button_change_finish_button.setEnabled(True)
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