# -*- coding: utf-8 -*-
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
clearFunc()


while True:
  if not tutorial:
    slowPrint('Do you want to start the tutorial? [Y/n]', False, 3)
    ans = keyinput()
    if ans == 'n':
        slowPrint('Skipping the tutorial..', False)
        time.sleep(readtime)
        tutorial = True
        slowPrint('Tutorial skipped!', False)
        time.sleep(readtime)
    else:
        cowPrint('tux', 'Welcome to the tutorial!\nI will be your guide through this game!')
        slowPrint('(Press "enter" to continue)')
        keyinput("enter")
        cowPrint('tux', 'Lets start with the Basics! Here is an apple, try to eat it.')
        slowPrint('(Press "e" to open your inventory)')
        keyinput("e")
        Inventory = inventory(Inventory, 'show')
  


  exit()