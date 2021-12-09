import copy
from pprint import pprint
import itertools
import numpy as np

#inputs = open("inputs_day9_test.txt", "r")
inputs = open("inputs_day9.txt", "r")

lines = inputs.readlines()

size = (len(lines), len(lines[0])-1)

print(size)

terrain = np.zeros(size, dtype=np.int8)
local_minima = np.zeros(size, dtype=np.int8)

for i in range(size[0]):
    for j in range(size[1]):
        terrain[i][j] = int(lines[i][j])

pprint(terrain)

total_risk = 0

for i in range(size[0]):
    for j in range(size[1]):
        found_lower = False
        neighbours = []
        if not found_lower and i > 0:
            found_lower = terrain[i-1][j] <= terrain[i][j]
            neighbours.append(terrain[i-1][j])
        if not found_lower and i < size[0]-1:
            found_lower = terrain[i+1][j] <= terrain[i][j]
            neighbours.append(terrain[i+1][j])
        if not found_lower and j > 0:
            found_lower = terrain[i][j-1] <= terrain[i][j]
            neighbours.append(terrain[i][j-1])
        if not found_lower and j < size[1]-1:
            found_lower = terrain[i][j+1] <= terrain[i][j]
            neighbours.append(terrain[i][j+1])
        
        if not found_lower:
            print("Found low point ", terrain[i][j], "at", i, j, " | ", neighbours)

            total_risk += 1+terrain[i][j]
        
print("Total risk:", total_risk)