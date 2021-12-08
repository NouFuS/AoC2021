import copy
from pprint import pprint


#inputs = open("inputs_day8_test.txt", "r")
inputs = open("inputs_day8.txt", "r")

lines = inputs.readlines()

separated_inputs = []
for line in lines:
    p1 = []
    p2 = []
    full_p1, full_p2 = line.split(" | ")

    for value in full_p1.split():
        p1.append(value)
    
    for value in full_p2.split():
        p2.append(value)
    
    separated_inputs.append([p1, p2])

nb_instances = 0

for p1, p2 in separated_inputs:
    for value in p2:
        if len(value) == 2 or len(value) == 7 or len(value) == 3 or len(value) == 4:
            nb_instances += 1

print("Nb of 1, 4, 7, 8:", nb_instances)