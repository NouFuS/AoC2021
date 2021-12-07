import copy
from pprint import pprint
import statistics
import math

def compute_cost(p1, p2):
    cost = 0
    distance = abs(p1-p2)
    for i in range(0,distance+1):
        cost += i
    return cost


#inputs = open("inputs_day7_test.txt", "r")
inputs = open("inputs_day7.txt", "r")

lines = inputs.readlines()

positions = []
for position in lines[0].split(","):
    positions.append(int(position))

min_position = 9999999
max_position = -999999

for position in positions:
    if position >max_position:
        max_position = position
    if position < min_position:
        min_position = position

min_cost = None
best_position = None
for i in range(min_position, max_position+1):
    cost = 0
    for position in positions:
        cost += compute_cost(position, i)
    
    if min_cost is None or cost < min_cost :
        min_cost = cost
        best_position = i

print("Best position at", best_position, "with cost of:", min_cost)
