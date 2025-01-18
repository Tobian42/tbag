import json
import time
from datetime import datetime
from functions import clear

file_name = "gamesave.json"
readtime = 1


def SetDefaultData():
    hp = 100
    xp = 0
    SaveGame(hp, xp)

def SaveGame(hp, xp):
    Configuration = {
        "world": {
            "placeholder": 3
        },
        "player": {
            "hp": hp,
            "xp": xp
        },
        "inventory": {
            "Food": {
                "Banana": 4,
                "Apple": 3
            },
            "Weapons": {
                "Wooden Sword": 300
            }
        },
        "game": {
            "tutorial": False,
            "last-save": datetime.today().strftime('%d-%m-%Y')
        }
    }
    with open(file_name, 'w') as json_file:
        json.dump(Configuration, json_file, indent=4)

def LoadGame():
    while True:
        #try to open the file
        try:
            with open(file_name) as jsonFile:
                Configuration = json.load(jsonFile)

            # Sort the data
            WorldData = Configuration["world"]
            PlayerData = Configuration["player"]
            InventoryData = Configuration["inventory"]
            GameData = Configuration["game"]

            hp = PlayerData["hp"]
            xp = PlayerData["xp"]
            tutorial = GameData["tutorial"]

            return(hp, xp, tutorial)
        except FileNotFoundError:
            print('No save file found!')
            time.sleep(readtime)
            clear(log = True)
            ans = input('Do you to create a new save file? [Y/n]\n>>>')
            if ans == 'Y' or ans == 'y':
                SetDefaultData()
            else:
                print('exiting...')
                exit()

def SaveGame():
    pass