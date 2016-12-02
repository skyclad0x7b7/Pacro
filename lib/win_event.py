"""
	Windows events such as click
"""


import time
import os
import win32api
import win32con
import json

from lib.constant import *

def click(pos_x, pos_y, delay = None):
    """ Simple Click Function """
    win32api.SetCursorPos((pos_x, pos_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos_x, pos_y, 0, 0)
    if delay != None:
        time.sleep(delay / 1000.0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos_x, pos_y, 0, 0)

def keyboard_updown(key, delay = 0.05):
	try:
		win32api.keybd_event(VK_CODE[key], 0, 0, 0)
		time.sleep(delay)
		win32api.keybd_event(VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
	except KeyError as e:
		print "Unknown || Undefined Keyboard Event!!" # Temp Message