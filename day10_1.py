import copy
from pprint import pprint

#inputs = open("inputs_day10_test.txt", "r")
inputs = open("inputs_day10.txt", "r")

lines = inputs.readlines()

opening = {"<":">", "(":")", "{":"}", "[":"]"}
scores = {")":3, "]":57, "}":1197, ">":25137}

total_score = 0
for line_nb, line in enumerate(lines):
    awaited_closing = []
    print("Line:", line)
    for char in line:
        if char == "\n":
            break
        if char in opening.keys():
            awaited_closing.append(opening[char])
        elif char != awaited_closing[-1]:
            print("Illegal closing:", char, "on line", line_nb)
            total_score += scores[char]
            break
        else:
            del awaited_closing[-1]

print("Total score:", total_score)