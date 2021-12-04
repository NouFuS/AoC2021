import numpy as np
import copy
from pprint import pprint

inputs = open("inputs_day4.txt", "r")
#inputs = open("inputs_day4_test.txt", "r")
#inputs = open("inputs_day4_test_2.txt", "r")

lines = inputs.readlines()

numbers = lines[0].rstrip().split(",")
for i, nb in enumerate(numbers):
    numbers[i] = int(nb)

values = lines[2].rstrip().split()
grid_size = len(values)

nb_grids = 0
for line in lines[1:]:
    if line == "\n":
        nb_grids +=1

grids = np.zeros([nb_grids, grid_size, grid_size], dtype=np.int8)

new_grid = np.zeros([grid_size, grid_size], dtype=np.int8)
line_index = 0
grid_index = -1
for line in lines[1:]:
    if line == "\n":
        grid_index += 1
        line_index = 0
    else:
        values = line.rstrip().split()
        grids[grid_index, line_index, :] = values
        line_index += 1

validated_numbers = np.zeros(grids.shape)

winner_index = []
score = []
for number in numbers:
    validated_numbers[np.where(grids == number)] = 1
    
    for i in range(0, nb_grids):
        has_line_or_raw= False
        for j in range(0, grid_size):
            if (np.sum(validated_numbers[i, j, :]) == grid_size or np.sum(validated_numbers[i, :, j]) == grid_size) and i not in winner_index:
                winner_index.append(i)
                
                winning_grid = grids[i]
                winning_grid_validated = validated_numbers[i]

                coordinates = np.where(winning_grid_validated == 0)
                sum = np.sum(winning_grid[coordinates])

                score.append( sum*number)


print("Last Winner grid found:")
print(winner_index[-1])
print("With score:")
print(score[-1])