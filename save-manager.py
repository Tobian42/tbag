import json

file_name = "gamesave.json"
default_data = {
    "world": {
        "placeholder": 3
    },
    "player": {
        "hp": 10,
        "xp": 0
    },
    "game": {
        "last-save": "01.01.1960"
    }
}

try:
  with open(file_name) as jsonFile:
    Configuration = json.load(jsonFile)
except NameError:
  with open(file_name, 'w') as json_file:
      json.dump(default_data, json_file, indent=4)


# Sort the data
WorldData = Configuration["world"]
PlayerData = Configuration["player"]
GameData = Configuration["game"]

hp = PlayerData["hp"]
xp = PlayerData["xp"]