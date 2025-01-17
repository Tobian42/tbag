import os
import sys
import time
import cowsay
import sshkeyboard

msg_memory = []

def sprint(chr, msg):
   clear_console()
   str = cowsay.get_output_string(chr, msg)
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(.005)

def lprint(action, msg = None):
   global msg_memory
   if action == 'save':
      msg_memory.append(msg)
      return True
   elif action == 'clear':
      msg_memory = []
      return True
   elif action == 'load':
      return("\n".join(msg_memory))
   else:
      return False

def keyinput(target_key):
    def press(key): pass
    while sshkeyboard.listen_keyboard(on_press=press, until=target_key): pass

def clear(scr = False):
   os.system('clear')
   if 


def inventory():
   pass