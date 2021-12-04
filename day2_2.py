inputs = open("inputs_day2.txt", "r")

lines = inputs.readlines()

aim = 0
x = 0
z = 0

for line in lines:
    word, value = line.split()
    if word == "forward":
        x += int(value)
        z += int(value)*aim
    if word == "down":
        aim += int(value)
    if word == "up":
        aim -= int(value)

print("x=", x, " | ", "z=", z)
print("Result=",  x*z)