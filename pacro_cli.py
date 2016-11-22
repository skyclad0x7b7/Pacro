import json
from os.path import exists
from lib.validate import ValidateError
from lib.pacro_core import PacroExecutor


if __name__ == "__main__":
	script_path = raw_input("[*] Please input script file_path : ")
	if not exists(script_path):
		print "Script File Not exists"
		exit(1)

	with open(script_path, "r") as f:
		buf = f.read()
	try:
		op_list = json.loads(buf)
	except Exception as e:
		print "[*] JSON Parse Error : ", e
		exit(1)

	p = PacroExecutor(op_list)
	try:
		p.execute()
	except ValidateError as e:
		print "[*] Error while running script"
		print e.msg