inputs = open("inputs_day1.txt", "r")

lines = inputs.readlines()


counter = 0

for i in range(1, len(lines)):
    if int(lines[i]) >int(lines[i-1]):
        counter +=1

print(counter)