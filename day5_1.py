import numpy as np
import copy
from pprint import pprint

inputs = open("inputs_day5.txt", "r")
#inputs = open("inputs_day5_test.txt", "r")

lines = inputs.readlines()

points = []

for line in lines:
    coords = ((int(line.split(" -> ")[0].split(",")[0]), int(line.split(" -> ")[0].split(",")[1])), (int(line.split(" -> ")[1].split(",")[0]), int(line.split(" -> ")[1].split(",")[1])))
    points.append( coords )

largest_x = 0
largest_y = 0
for point in points:
    p1, p2 = point
    if p1[0] > largest_x or p2[0] > largest_x:
        largest_x = max(p1[0], p2[0])
    if p1[1] > largest_y or p2[1] > largest_y:
        largest_y = max(p1[1], p2[1])

map = np.zeros((largest_x+1, largest_y+1), dtype=np.int8)
for point in points:
    p1, p2 = point
    if p1[0] == p2[0]:
        map[p1[0],min(p1[1],p2[1]):max(p1[1],p2[1])+1 ] += 1
    elif p1[1] == p2[1]:
        map[min(p1[0],p2[0]):max(p1[0],p2[0])+1,p1[1]] += 1

pprint(map.T)
print("Nb of higher than 2 points:", len(np.where(map >=2)[1]))