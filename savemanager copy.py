# -*- coding: utf-8 -*-
import json
import time
from datetime import datetime
from functions import clearFunc

hp = 100
xp = 0


def SetDefaultData():
    global Inventory
    Inventory = {
        "Food": {
            "Apple": 3,
            "Banana": 4
        },
        "Weapons": {
            "Wooden Sword": 300
        }
    },
    SaveGame()
    print('Succsessfully saved default Values')

def SaveGame():
    global Inventory
    global hp
    global xp
    
    Configuration = {
        "game": {
            "last-save": datetime.today().strftime('%d-%m-%Y')
        },
        "inventory": Inventory,
        "player": {
            "hp": 100,
            "xp": 0
        },
        "world": {
            "tutorial": False
        }
    }

    with open(file_name, 'w') as json_file:
         json.dump(Configuration, json_file, sort_keys = True, indent = 4)

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

            Inventory = InventoryData[0]
            hp = PlayerData["hp"]
            xp = PlayerData["xp"]
            tutorial = WorldData["tutorial"]

            return(Inventory, hp, xp, tutorial)
        except FileNotFoundError:
            print('No save file found!')
            time.sleep(readtime)
            clearFunc(log = True)
            ans = input('Do you to create a new save file? [Y/n]\n>>>')
            if ans == 'Y' or ans == 'y':
                SetDefaultData()
            else:
                print('exiting...')
                exit()
