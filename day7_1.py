import copy
from pprint import pprint
import statistics
import math

#inputs = open("inputs_day7_test.txt", "r")
inputs = open("inputs_day7.txt", "r")

lines = inputs.readlines()

positions = []
for position in lines[0].split(","):
    positions.append(int(position))

median = statistics.median(positions)
print("Median=", median)

median_cost = 0
for position in positions:
    median_cost += abs(position-median)

print("Median cost:", median_cost)