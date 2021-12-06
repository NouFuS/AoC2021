import copy
from pprint import pprint

def get_nb_fishes(efficient_fishes):
    total = 0
    for cycle, nb in efficient_fishes.items():
        total += nb

    return total

#inputs = open("inputs_day6_test.txt", "r")
inputs = open("inputs_day6.txt", "r")

lines = inputs.readlines()

cycle_base = 8
reset = 6

nb_days = 256

fishes = lines[0].split(",")
for i in range(len(fishes)):
    fishes[i] = int(fishes[i])

efficient_fishes = {}
for i in range(-1,cycle_base+1):
    efficient_fishes.update({i: 0})

for fish in fishes:
    efficient_fishes[fish] = efficient_fishes[fish]+1

for i in range(1, nb_days+1):
    for j in range(cycle_base+1):
        efficient_fishes[j-1] = efficient_fishes[j]
    efficient_fishes[cycle_base] = efficient_fishes[-1]
    efficient_fishes[reset] += efficient_fishes[-1]
    efficient_fishes[-1] = 0
    
print("Fishes after", nb_days, ":", get_nb_fishes(efficient_fishes))