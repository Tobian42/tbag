import json, time, datetime
import config, functions

Inventory = {}
hp = None
xp = None

def SaveGame(Default):
    if Default: 
        global Inventory, hp, xp
        

def LoadGame():
    while True:
        # Open the file
        try:
            with open(config.saveFile) as jsonFile:
                rawSave = json.load(jsonFile)
            
            # Sort the data
            global readTime
        except FileNotFoundError:
            functions.slowPrint('No save file found!')
            time.sleep(config.readTime)
            functions.clearFunc(log = True)
            functions.slowPrint('Do you want to create a save file? [Y/n]')
            ans = functions.keyinput()
            if ans == 'n':
                functions.slowPrint('exiting.....', False, 10)
                time.sleep(config.readTime)
                exit()
            else:
                SaveGame(Default = True)