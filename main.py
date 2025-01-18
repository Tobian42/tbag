print('Loading..')
# imports
from functions import *
from savemanager import LoadGame
from config import readtime
import time

# load game save
time.sleep(readtime)
Inventory, hp, xp, tutorial = LoadGame()
print('Save file loaded sucsessffully!')
time.sleep(readtime)
clear()


while True:
  if not tutorial:
    ans = input('Do you want to start the tutorial? [Y/n]\n>>>').lower()
    if ans == 'n':
        nprint('Skipping the tutorial..')
        time.sleep(readtime)
        tutorial = True
        nprint('Tutorial skipped!')
        time.sleep(readtime)
    else:
        sprint('Welcome to the tutorial!\nI will be your guide through this game!', 'tux')
        nprint('(Press "enter" to continue)')
        keyinput("enter")
        sprint('Lets start with the Basics! Here is an apple, try to eat it.', 'tux')
        nprint('(Press "e" to open your inventory)')
        keyinput("e")
        Inventory = inventory(Inventory, 'show')
  


  exit()