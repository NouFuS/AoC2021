inputs = open("inputs_day2.txt", "r")

lines = inputs.readlines()

x = 0
z = 0

for line in lines:
    word, value = line.split()
    if word == "forward":
        x += int(value)
    if word == "down":
        z += int(value)
    if word == "up":
        z -= int(value)

print("x=", x, " | ", "z=", z)
print("Result=",  x*z)