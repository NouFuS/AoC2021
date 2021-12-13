import copy
from os import close
from pprint import pprint
import numpy as np

inputs = open("inputs_day13_test.txt", "r")
#inputs = open("inputs_day13.txt", "r")

lines = inputs.readlines()

points = []
instructions = []

instructions_reached = False

shape = [0, 0]

for line in lines: 
    print("Line:", line)
    if line == "\n":
        instructions_reached = True
        continue
    if not instructions_reached:
        p1, p2 = line.split(",")
        if int(p1) > shape[1]:
            shape[1] = int(p1)
        if int(p2) > shape[0]:
            shape[0] = int(p2)

        points.append( [int(p1), int(p2) ])
    else:
        instructions.append( (line.split("=")[0],  int(line.split("=")[1]) ))

print("Shape=", shape)

for instruction in instructions:
    collapsed_points = np.zeros(shape)
    if instruction[0] == "fold along x":
        for point in points:
            if point[0] > instruction[1]:
                point[0] = point[0] - (point[0] - instruction[1])*2
    if instruction[0] == "fold along y":
        for point in points:
            if point[1] > instruction[1]:
                point[1] = point[1] - (point[1] - instruction[1])*2
for point in points:
    collapsed_points[point[0], point[1]] = 1
# pprint(collapsed_points)
print("After all instructions", instruction, " nb points = ", len(np.where(collapsed_points==1)[0]))

pprint(collapsed_points[0:5, 0:7].T)