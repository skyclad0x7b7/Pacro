"""
	Windows events such as click
"""


import time
import os
import win32api
import json
from win32con import *


def click(pos_x, pos_y, delay = None):
    """ Simple Click Function """
    win32api.SetCursorPos((pos_x, pos_y))
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, pos_x, pos_y, 0, 0)
    if delay != None:
        time.sleep(delay / 1000.0)
    win32api.mouse_event(MOUSEEVENTF_LEFTUP, pos_x, pos_y, 0, 0)
