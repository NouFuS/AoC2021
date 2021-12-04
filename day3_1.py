from pprint import pprint

inputs = open("inputs_day3.txt", "r")
#inputs = open("inputs_day3_test.txt", "r")

lines = inputs.readlines()

gamma_binary = [0]*len(lines[0].rstrip())
epsilon_binary = [0]*len(lines[0].rstrip())

ones_occurences = [0]*len(lines[0].rstrip())

for line in lines:
    for i, bit in enumerate(line.rstrip()):
        if bit == "1":
            ones_occurences[i] += 1

for digit, occurences in enumerate(ones_occurences):
    if occurences > len(lines)/2:
        gamma_binary[digit] = 1
        epsilon_binary[digit] = 0
    else:
        gamma_binary[digit] = 0
        epsilon_binary[digit] = 1

gamma_binary_str = ""
epsilon_binary_str = ""

for gamma_digit, epsilon_digit in zip(gamma_binary, epsilon_binary):
    gamma_binary_str += str(gamma_digit)
    epsilon_binary_str += str(epsilon_digit)

gamma = int(gamma_binary_str, 2)
epsilon = int(epsilon_binary_str, 2)

consumption = gamma*epsilon

print("Consumption=", consumption)