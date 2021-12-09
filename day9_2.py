import copy
from pprint import pprint
import itertools
import numpy as np

def explore_bassin(terrain, exploration_terrain, coordinate):
    if terrain[coordinate[0], coordinate[1]] == 9:
        return
    exploration_terrain[coordinate[0], coordinate[1]] = terrain[coordinate[0], coordinate[1]]
    if coordinate[0] > 0 and exploration_terrain[coordinate[0]-1, coordinate[1]] == -1 and terrain[coordinate[0]-1, coordinate[1]] == terrain[coordinate[0], coordinate[1]]+1:
        explore_bassin(terrain, exploration_terrain, [coordinate[0]-1, coordinate[1]])    
    if coordinate[1] > 0 and exploration_terrain[coordinate[0], coordinate[1]-1] == -1 and terrain[coordinate[0], coordinate[1]-1] == terrain[coordinate[0], coordinate[1]]+1:
        explore_bassin(terrain, exploration_terrain, [coordinate[0], coordinate[1]-1])    
    if coordinate[0] < terrain.shape[0]-1 and exploration_terrain[coordinate[0]+1, coordinate[1]] == -1 and terrain[coordinate[0]+1, coordinate[1]] == terrain[coordinate[0], coordinate[1]]+1:
        explore_bassin(terrain, exploration_terrain, [coordinate[0]+1, coordinate[1]])    
    if coordinate[1] < terrain.shape[1]-1 and exploration_terrain[coordinate[0], coordinate[1]+1] == -1 and terrain[coordinate[0], coordinate[1]+1] == terrain[coordinate[0], coordinate[1]]+1:
        explore_bassin(terrain, exploration_terrain, [coordinate[0], coordinate[1]+1])

#inputs = open("inputs_day9_test.txt", "r")
inputs = open("inputs_day9.txt", "r")

lines = inputs.readlines()

size = (len(lines), len(lines[0])-1)

terrain = np.zeros(size, dtype=np.int8)
local_minima = np.zeros(size, dtype=np.int8)

for i in range(size[0]):
    for j in range(size[1]):
        terrain[i][j] = int(lines[i][j])

#pprint(terrain)

total_risk = 0
low_points = []
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
            low_points.append([i, j])
            total_risk += 1+terrain[i][j]

print("Found total risk of", total_risk, "with", len(low_points), "low points")

basins = []
for low_point in low_points:
    exploration_terrain = np.zeros(size, dtype=np.int8)-1
    explore_bassin(terrain, exploration_terrain, low_point)
    basins.append(len(np.where(exploration_terrain > -1)[1]))
    #pprint(exploration_terrain)

sorted_basins = sorted(basins)
print("Nb basins:", len(basins))
print("Basins sizes:", sorted_basins)
print("Result =", sorted_basins[-1]*sorted_basins[-2]*sorted_basins[-3])