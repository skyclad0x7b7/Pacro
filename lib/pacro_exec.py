import json
import time

from lib.validate import ValidateError
from lib.win_event import *

class PacroExecutor():
	def __init__(self, op_list):
		self.op_list = op_list
		self.ip = 0
		self.op_len = len(self.op_list)

	def execute(self):
		while self.ip < self.op_len:
			op = self.op_list[self.ip]

			if op['op'] == "goto":
				# Validate Arguments
				if "target_id" not in op['arg']:
					raise ValidateError("\"target_id\" not found : [%d]" % op['id'])
				if not (0 < op['arg']['target_id'] <= self.op_len):
					raise ValidateError("target_id [%d] out of range : [%d]" % op['id'])
				# Normal
				self.ip = op['arg']['target_id']
				continue

			elif op['op'] == "click":
				# Validate Arguments
				if "x-pos" not in op['arg'] or "y-pos" not in op['arg']:
					raise ValidateError("arguments not found : [%d]" % op['id'])
				if op['arg']['x-pos'] < 0 or op['arg']['y-pos'] < 0:
					raise ValidateError("position value should be unsigned integer : [%d]" % op['id'])

				# Option
				delay = None
				if "delay" in op['arg']:
					if op['arg']['delay'] < 0:
						raise ValidateError("delay value should be unsigned integer : [%d]" % op['id'])
					delay = op['arg']['delay']

				# Normal
				click(op['arg']['x-pos'], op['arg']['y-pos'], delay)

			elif op['op'] == "sleep":
				# Validate Arguments
				if "ms" not in op['arg']:
					raise ValidateError("\"ms\" not found : [%d]" % op['id'])
				if op['arg']['ms'] < 0:
					raise ValidateError("ms value should be unsigned integer : [%d]" % op['id']) 

				# Normal
				time.sleep(op['arg']['ms'] / 1000.0)

			self.ip += 1