inputs = open("inputs_day1.txt", "r")

lines = inputs.readlines()

smoothed_lines = []

for i in range(1, len(lines)-1):
    smoothed_lines.append(int(lines[i-1])+int(lines[i])+int(lines[i+1]))

counter = 0

for i in range(1, len(smoothed_lines)):
    if int(smoothed_lines[i]) > int(smoothed_lines[i-1]):
        counter +=1

print(counter)