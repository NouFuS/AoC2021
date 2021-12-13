import copy
from os import close
from pprint import pprint
import numpy as np

def search_path(current_position, map_dict, current_path, all_paths):
    current_path.append(current_position)
    
    if current_position == "end":
        all_paths.append(current_path)
        return

    possible_continuations = []
    for next_coordinate in map_dict[current_position]:
        if next_coordinate != "start" and (not next_coordinate.islower() or next_coordinate not in current_path):
            possible_continuations.append(next_coordinate)
    
    # cul de sac
    if possible_continuations == []:
        return

    for continuation in possible_continuations:
        search_path(continuation, map_dict, copy.copy(current_path), all_paths)

    

#inputs = open("inputs_day12_test.txt", "r")
#inputs = open("inputs_day12_test2.txt", "r")
#inputs = open("inputs_day12_test3.txt", "r")
inputs = open("inputs_day12.txt", "r")

lines = inputs.readlines()

map_dict = dict()

for line in lines:
    v1, v2 = line.rstrip().split("-")
    if v1 in map_dict:
        map_dict[v1].append(v2)
    else:
        map_dict.update({v1:[v2]})
    if v2 in map_dict:
        map_dict[v2].append(v1)
    else:
        map_dict.update({v2:[v1]})

all_paths = []
current_path = []
current_position = "start"

search_path(current_position, map_dict, current_path, all_paths)

print("All paths (", len(all_paths), "):")
#pprint(all_paths)