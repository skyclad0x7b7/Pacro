from lib.constant import REQUIRE_KEY, OP_LIST





def validate(ops):

	pass
"""
def validate_one(op):
	for key in REQUIRE_KEY:
		if key not in op: # if require key not exists in op
			raise ValidateError("Key [%s] not found" % key)

	for target_op in OP_LIST:
		if op['op'] == target_op['op']: # is operation in OP_LIST
			if op['arg'].keys() in target_op['require_arg'].keys(): # if require arg is exists



	else:
		# Nothing Found
		raise ValidateError("Not supported op [%s] in id [%d]" % (op['op'], op['id']))
"""
class ValidateError(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return repr(self.msg)