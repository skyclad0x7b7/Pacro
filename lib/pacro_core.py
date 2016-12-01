"""
    Core functions of Pacro
"""

from threading import Thread
import json
import time

from PyQt4.QtCore import pyqtSignal, QObject
from lib.validate import ValidateError
from lib.win_event import *

"""
- op_list       = list of operations. parsed json list. [{op1}, {op2}, ...]
- ip            = instruction pointer
- op_len        = length of op_list
- stop_flag     = don't execute next instruction when it's True
"""
class PacroExecutor(QObject):
    # Initialize Signal
    initialize_signal   = pyqtSignal()
    ip_signal           = pyqtSignal(int)
    finished_signal     = pyqtSignal(int)
    error_signal        = pyqtSignal(str)

    def __init__(self, op_list, parent = None): 
        # Initialize PacroExecutor as QObject to emit signals
        super(PacroExecutor, self).__init__(parent)
        self.op_list = op_list
        self.ip = 0
        self.op_len = len(self.op_list)
        self.stop_flag = False

    def execute(self):
        # Initialize
        self.ip = 0
        self.stop_flag = False

        self.initialize_signal.emit()

        while self.ip < self.op_len and not self.stop_flag:
            # Send signal to PacroGui
            self.ip_signal.emit(self.ip)

            op = self.op_list[self.ip]

            if op['op'] == "click":
                # Validate Arguments
                if "x-pos" not in op['arg'] or "y-pos" not in op['arg']:
                    self.error_signal.emit("arguments not found : [%d]" % self.ip)
                    return True

                if op['arg']['x-pos'] < 0 or op['arg']['y-pos'] < 0:
                    self.error_signal.emit("position value should be unsigned integer : [%d]" % self.ip)
                    return True

                # Option
                delay = None
                if "delay" in op['arg']:
                    if op['arg']['delay'] < 0:
                        self.error_signal.emit("delay value should be unsigned integer : [%d]" % self.ip)
                        return True
                    delay = op['arg']['delay']

                # Normal
                click(op['arg']['x-pos'], op['arg']['y-pos'], delay)

            elif op['op'] == "sleep":
                # Validate Arguments
                if "ms" not in op['arg']:
                    self.error_signal.emit("\"ms\" not found : [%d]" % self.ip)
                    return True
                if op['arg']['ms'] < 0:
                    self.error_signal.emit("ms value should be unsigned integer : [%d]" % self.ip) 
                    return True

                # Normal
                time.sleep(op['arg']['ms'] / 1000.0)

            else:
                """ Unknown Operation """
                print "Unknown Operation : %s" % op['op']
                # For Test
                #self.error_signal.emit("Unknown Operation : %s" % op['op'])
                #return True

            self.ip += 1

        self.finished_signal.emit(self.ip - 1) # because it added 1 at the end of while.

        if self.stop_flag:
            return False

        return True

    def stop(self):
        self.stop_flag = True