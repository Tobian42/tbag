print('Loading..')
# imports
from functions import *
from savemanager import LoadGame, readtime
import time

# load game save
time.sleep(readtime)
hp, xp, tutorial = LoadGame()
print('Loaded sucsessffully!')
time.sleep(readtime)
clear_console()


while True:
  if not tutorial:
    ans = input('Do you want to start the tutorial? [Y/n]\n>>>')
    if ans == 'N' or ans == 'n':
        print('Skipping the tutorial..')
        time.sleep(readtime)
        tutorial = True
        print('Tutorial skipped!')
        time.sleep(readtime)
    else:
        sprint('tux', 'Welcome to the tutorial!\nI will be your guide through this game!')
        print('(Press "enter" to continue)')
        keyinput("enter")
        sprint('tux', 'Lets start with the Basics! Here is an apple, try to eat it.')
        print('(Press "e" to open your inventory)')
        keyinput("e")

  


  exit()






clear_console()
time.sleep(1)
sprint('tux', 'Sieht so aus als wärst du gestorben :/ \nVersuch es nochmal!')