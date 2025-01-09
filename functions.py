import sys
import os
import time
import cowsay

def sprint(chr, msg):
   str = cowsay.get_output_string(chr, msg)
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(.005)

def clear_console():
   os.system('clear')