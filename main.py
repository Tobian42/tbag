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
      spint('tux', 'Welcome to the tutorial!\nI will be your guide through this game!')
      time.sleep(readtime * 3)
      
    
    sprint('tux', f'Hallo Welt: {hp, xp}')
  hp -= 1


clear_console()
time.sleep(1)
sprint('tux', 'Sieht so aus als wärst du gestorben :/ \nVersuch es nochmal!')