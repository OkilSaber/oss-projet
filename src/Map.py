import glob
from datetime import datetime
from constants.Assets import Assets
import os

SAVES_DIR = ".saves/"
MAP_FILE_EXTENSION = ".map"
DATE_PREFIX = "date="
SIZE = int(40)
    
def list_maps():
    maps = []
    for file in glob.glob("%s*%s" % (SAVES_DIR, MAP_FILE_EXTENSION)):
        map_name = file.removeprefix(SAVES_DIR).removesuffix(MAP_FILE_EXTENSION)
        with open(file, "r") as f:
            date_line = f.readline()
            ts = date_line.removeprefix(DATE_PREFIX)
            date = datetime.fromtimestamp(int(ts))
            maps.append((map_name, date))
    return maps

def load_map(map_name):
    file_path = "%s%s%s" % (SAVES_DIR, map_name, MAP_FILE_EXTENSION)
    map = []
    with open(file_path, "r") as f:
        map = [line[:-1] for line in f] # line[:-1] in order to remove the \n
    return list(map[1:]) # first line contains map timestamp, not useful

def save_map(map_name, map):
    file_path = "%s%s%s" % (SAVES_DIR, map_name, MAP_FILE_EXTENSION)
    timestamp = int(datetime.now().timestamp())
    with open(file_path, "w+") as f:
        f.write("%s%d\n" % (DATE_PREFIX, timestamp))
        for line in map:
            f.write("%s\n" % line)

def delete_map(map_name):
    file_path = "%s%s%s" % (SAVES_DIR, map_name, MAP_FILE_EXTENSION)
    if os.path.exists(file_path):
        os.remove(file_path)