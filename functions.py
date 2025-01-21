# -*- coding: utf-8 -*-
import os, sys, time, math, cowsay, sshkeyboard
from config import *

msg_memory = []
index = 1

# Print a dict in a box with indexes
def boxPrint(content, title = None, slow = True, save = True, clear = 'all'):
   global index
   formatedContent = ''
   size = 20
   addtitlel = max(math.ceil((size - len(title)) / 2 ), 2)
   addtitler = max(math.floor((size - len(title)) / 2 ), 2)
   sort = sorted(content.items())

   for item, quantity in sort:
      addspace = max(size - (3 + len(item) + len(str(quantity))), 2)
      formatedContent = formatedContent + f'│ [{index}] │ {item}: {quantity}{" " * addspace}│\n'

      index += 1

      content = (f'┌─────┬{"─" * addtitlel}{title}{"─" * addtitler}┐\n' +
      formatedContent +
      f'└─────┴{"─" * (addtitlel + len(title) + addtitler)}┘')

   if clear:
      if clear == 'all': clearFunc(True)
      elif clear == 'console': clearFunc()
      elif clear == 'log': savePrint('clear')
   if slow: slowPrint(content, False)
   else:
      print(content)
      if save: savePrint('save', content)

# Print a text using cowsay
def cowPrint(character, content, slow = True, save = True, clear = 'all'):
   content = cowsay.get_output_string(character, content)
   
   if clear:
      if clear == 'all': clearFunc(True)
      elif clear == 'console': clearFunc()
      elif clear == 'log': savePrint('clear')
   if slow:
      slowPrint(content, slow)
   else:
      print(content)
      if save: savePrint('save', content)

# Save text and print it
def savePrint(action, content = None, slow = False):
   global msg_memory

   if action == 'save' and content:
      msg_memory.append(content)
   elif action == 'clear':
      msg_memory = []
   elif action == 'load':
      if content == 'clear': clearFunc()
      slowPrint("\n".join(msg_memory), False)
   else:
      return False
   return True

# Print text slowly
def slowPrint(content, save = True, speed = 1):
   global readtime
   sleeptime = readtime * speed
   if save: savePrint('save', content)

   for c in content + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(sleeptime / 200)

# clear console
def clearFunc(log = False):
   if log: savePrint('clear')
   os.system('clear')

# Wait for a specif key pressed or return pressed key
def keyinput(targetKey = None):
   if targetKey:
      def press(key): pass
      while sshkeyboard.listen_keyboard(on_press=press, until=targetKey): pass
   else:
      pressedKey = None
      def press(key):
         nonlocal pressedKey
         pressedKey = key
         sshkeyboard.stop_listening()
      sshkeyboard.listen_keyboard(on_press=press)
      return pressedKey

# Inventory actions
def inventory(Inventory, action, item = None):
   if action == 'show':
      step = 1
      clearFunc()
      while True:
         if step == 1:
            global index; index = 1
            items = []
            slowPrint('Inventory:', False, 5)
            for category in Inventory.keys():
               boxPrint(Inventory[category], category, True, False, False)
               sort = sorted(Inventory[category].items())
               for item, quantity in sort:
                  items.append(item)
            choosen = input('\nChoose an item (choose 0 to exit)\n>>>')
            try:
               choosen = int(choosen)
               if choosen == 0:
                  step = 0
                  savePrint('load', 'clear')
                  return 'exited'
               item = items[(choosen -1)]
               itemtype = itemmap[item]
               step = 2
            except ValueError:
               clearFunc()
               print('Please input a Number')      
            except IndexError:
               clearFunc()
               print("This Item doesn't exist")
            except KeyError:
               clearFunc()
               print(f'>{item}< does not exist in the itemmap [config.py]\nError(204)')
               exit('Invalid Item Found')
         elif step == 2:
            clearFunc()
            slowPrint(f'Choose what to do with {item};')
            if itemtype == 'Food':
               slowPrint('[e]at, [d]rop')
            action = keyinput()
            if action == 'e':
               gain = foodmap[item]
               slowPrint(f'You gained {gain} hp')