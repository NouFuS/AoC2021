import copy
from pprint import pprint

#inputs = open("inputs_day6_test.txt", "r")
inputs = open("inputs_day6.txt", "r")

lines = inputs.readlines()

cycle_base = 8
reset = 6

nb_days = 80

fishes = lines[0].split(",")
for i in range(len(fishes)):
    fishes[i] = int(fishes[i])

for i in range(0, nb_days):
    new_fishes = []
    for j in range(len(fishes)):
        fishes[j] -= 1
        if fishes[j] == -1:
            fishes[j] = reset
            new_fishes.append(cycle_base)
    fishes += new_fishes

print("Fishes after", nb_days, ":", len(fishes))