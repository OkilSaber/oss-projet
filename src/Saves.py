import glob
from datetime import datetime
from constants.Assets import Assets
import os
import json
import platform

SAVES_DIR = ".saves/"
SAVE_FILE_EXTENSION = ".save.json"


def list_saves():
    saves = []
    for file in glob.glob("%s*%s" % (SAVES_DIR, SAVE_FILE_EXTENSION)):
        save_name = file.removeprefix(
            SAVES_DIR).removesuffix(SAVE_FILE_EXTENSION)
        with open(file, "r") as f:
            data = json.load(f)
            ts = data["date"]
            date = datetime.fromtimestamp(ts)
            saves.append((save_name, date))
    return saves


def load_save(save_name):
    if (platform.system() == "Windows"):
        file_path = "%s%s" % (save_name, SAVE_FILE_EXTENSION)
    else:
        file_path = "%s%s%s" % (SAVES_DIR, save_name, SAVE_FILE_EXTENSION)
    with open(file_path, "r") as f:
        data = json.load(f)
        return data


def save(save_name, snake, fruit, direction):
    file_path = "%s%s%s" % (SAVES_DIR, save_name, SAVE_FILE_EXTENSION)
    timestamp = int(datetime.now().timestamp())
    if (os.path.isdir(SAVES_DIR) != True):
        os.mkdir(SAVES_DIR)
    with open(file_path, "w") as f:
        json.dump(
            {
                "date": int(timestamp),
                "snake": snake,
                "direction": direction,
                "fruit": {
                    "x": fruit[0],
                    "y": fruit[1]
                }
            },
            f
        )


def delete_save(save_name):
    if (platform.system() == "Windows"):
        file_path = "%s%s" % (save_name, SAVE_FILE_EXTENSION)
    else:
        file_path = "%s%s%s" % (SAVES_DIR, save_name, SAVE_FILE_EXTENSION)
    if os.path.exists(file_path):
        os.remove(file_path)
