import os, sys, time, math, cowsay, sshkeyboard
from config import readtime, itemmap

index = 0
msg_memory = []

def sprint(msg, chr = None, clearcons = True): # Print text slowly (and with cowsay)
   if clearcons: clear(log = True)
   if chr: str = cowsay.get_output_string(chr, msg)
   else: str = msg
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(.005)

def nprint(msg): # Print text and log it
   termlog('save', msg)
   print(msg)

def bprint(msg, title = ''): # Print text inside a box
   global index
   content = '' 
   size = 20
   addtitlel = max(math.ceil((size - len(title)) / 2 ), 2)
   addtitler = max(math.floor((size - len(title)) / 2 ), 2)
   sort = sorted(msg.items())
   for item, quantity in sort:
      addspace = max(size - (3 + len(item) + len(str(quantity))), 2)
      content = content + f'│ [{index}] │ {item}: {quantity}{' '*addspace}│\n'
      index += 1

   sprint((
     f'┌─────┬{'─'*addtitlel}{title}{'─'*addtitler}┐\n' +
     content +
     f'└─────┴{'─'*(addtitlel + len(title) + addtitler)}┘'
   ), None, False)


def termlog(action, msg = None):
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

def clear(log = False):
   os.system('clear')
   if log: termlog('clear')


def inventory(Inventory, action, item = None):
   if action == 'show':
      step = 1
      clear()
      while True:
         if step == 1:
            global index; index = 1
            items = []
            for category in Inventory.keys():
               bprint(Inventory[category], category)
               sort = sorted(Inventory[category].items())
               for item, quantity in sort:
                  items.append(item)
            try:
               choosen = input('\nChoose an Item\n>>>')
               item = items[int(choosen) - 1]
               itemtype = itemmap[item]
               step = 2
            except:
               print('Please enter a valid number')
               time.sleep(readtime)
               clear()
         elif step == 2:
            print(f'Choose an action for {item}:')
            if itemtype == 'Food':
               print('[E]at [D]elete')
            elif itemtype == 'Weapons':
               print('[A]ttack [D]elete')
            use = input('>>>').lower()
            if use == 'a':
               pass
            elif use == 'd':
               pass
            elif use == 'e':
               pass
            
   else:
      print(f'an invalid action was called! "{action}"')
   return Inventory