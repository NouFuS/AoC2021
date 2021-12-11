import copy
from os import close
from pprint import pprint
import numpy as np

def charge(terrain, coord):
    
    i, j = coord
    
    if i < 0 or j < 0 or i >= len(terrain) or j >= len(terrain[0]):
        return

    if terrain[i][j] != -1:
            terrain[i][j] += 1
            if terrain[i][j] == 10:
                terrain[i][j] = -1
                charge(terrain, (i-1, j-1))
                charge(terrain, (i-1, j))
                charge(terrain, (i-1, j+1))
                charge(terrain, (i, j-1))
                charge(terrain, (i, j))
                charge(terrain, (i, j+1))
                charge(terrain, (i+1, j-1))
                charge(terrain, (i+1, j))
                charge(terrain, (i+1, j+1))
    return


#inputs = open("inputs_day11_test1.txt", "r")
#inputs = open("inputs_day11_test2.txt", "r")
inputs = open("inputs_day11.txt", "r")

lines = inputs.readlines()

size = (len(lines), len(lines[0])-1)
print("Terrain of size:", size)

terrain = np.zeros(size, dtype=np.int8)
local_minima = np.zeros(size, dtype=np.int8)

for i in range(size[0]):
    for j in range(size[1]):
        terrain[i][j] = int(lines[i][j])

t = 1

sync = None

while sync is None:
    for i in range(size[0]):
        for j in range(size[1]):
            charge(terrain, (i,j))

    if len(np.where(terrain == -1)[1]) == size[0]*size[1]:
        sync = t

    terrain[np.where(terrain == -1)] = 0
    t += 1

print("First sync:", sync)