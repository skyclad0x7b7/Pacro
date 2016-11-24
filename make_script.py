import time
import pythoncom
import json
try:
    import pyHook
except:
    print """pyHook not installed.
please download .whl file in \"http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook\"
and type the command like 'pip install pyHook-1.5.1-cp27-none-win32.whl' for 32bit or
'pip install pyHook-1.5.1-cp27-none-win_amd64.whl' for 64bit."""
    exit(1)

class Hooker():
    def __init__(self):
        self.id = 0
        self.prev_time = 0
        self.scripts = []
        self.script_path = None
        self.hook_manager = pyHook.HookManager()
        self.end_flag = False

    def set_file_path(self, script_path):
        self.script_path = script_path

    def hook_mouse(self):
        self.hook_manager.SubscribeMouseAllButtonsDown(self.onclick)
        self.hook_manager.HookMouse()
        while not self.end_flag:
            pythoncom.PumpWaitingMessages()

    def unhook_mouse(self):
        self.hook_manager.UnhookMouse()
    
    def onclick(self, event):
        if "mouse right down" == event.MessageName:
            self.end_flag = True
            self.unhook_mouse()
            self.save_scripts()
            return True

        print event.Position
        cur_time = int(time.clock() * 1000)
        if self.prev_time == 0:
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
            self.id += 1
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

    def save_scripts(self):
        print self.scripts
        dmp = json.dumps(self.scripts, sort_keys=True, indent=4)
        with open(self.script_path, "wb") as f:
            f.write(dmp)


        

if __name__ == "__main__":
    h = Hooker()
    h.set_file_path("script.json")
    raw_input("Press Enter to Start Hooking")
    h.hook_mouse()
