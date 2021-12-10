import copy
from os import close
from pprint import pprint

#inputs = open("inputs_day10_test.txt", "r")
inputs = open("inputs_day10.txt", "r")

lines = inputs.readlines()

opening = {"<":">", "(":")", "{":"}", "[":"]"}
corrupted_scores = {")":3, "]":57, "}":1197, ">":25137}
complete_scores = {")":1, "]":2, "}":3, ">":4}

total_score_corrupted = 0
scores_complete = []
for line_nb, line in enumerate(lines):
    is_corrupted = False
    awaited_closing = []
    print("Line:", line)
    for char in line:
        if char == "\n":
            break
        if char in opening.keys():
            awaited_closing.append(opening[char])
        elif char != awaited_closing[-1]:
            print("Line", line_nb, "Illegal closing:", char, "on line", line_nb)
            total_score_corrupted += corrupted_scores[char]
            is_corrupted = True
            break
            
        else:
            del awaited_closing[-1]
    
    if is_corrupted:
        continue

    if awaited_closing != []:
        score_complete = 0
        print("Line", line_nb, "Incomplete sequence with:", awaited_closing)
        close_sequence = ""
        for char in reversed(awaited_closing):
            close_sequence += char
            score_complete *= 5
            score_complete += complete_scores[char]
        print("Closing sequence =", close_sequence)
        scores_complete.append(score_complete)
        continue

    print("Line", line_nb, "is valid")

print("Total score corrupted:", total_score_corrupted)
print("Total score completed:", sorted(scores_complete)[int(len(scores_complete)/2)])