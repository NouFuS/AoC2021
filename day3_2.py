import copy

def filter_by_criterion(numbers, position, filter_type):
    occurences = 0
    for number in numbers:
        if number[position] == "1":
                occurences += 1

    if filter_type == "most_common":
        if occurences >= len(numbers)/2:
            criterion = "1"
        else:
            criterion = "0"

    elif filter_type == "least_common":
        if occurences < len(numbers)/2:
            criterion = "1"
        else:
            criterion = "0"
    else:
        raise Exception("Unknown filter type")

    filtered_numbers = []
    for number in numbers:
        if number[position] == criterion:
            filtered_numbers.append(number)

    return filtered_numbers, criterion

def get_unique_number(numbers, filter_type):
    filtered_numbers = copy.copy(numbers)
    position = 0
    while len(filtered_numbers) != 1 and position < len(numbers[0]):
        filtered_numbers, _ = filter_by_criterion(filtered_numbers, position, filter_type)
        position += 1

    if len(filtered_numbers) > 1:
        raise Exception("Did not find unique value for O2...")

    return filtered_numbers[0]

inputs = open("inputs_day3.txt", "r")
#inputs = open("inputs_day3_test.txt", "r")

lines = inputs.readlines()

numbers = []
for line in lines:
    numbers.append(line.rstrip())

O2_rating = int(get_unique_number(numbers, "most_common"), 2)
CO2_rating = int(get_unique_number(numbers, "least_common"), 2)

print("Life support rating=", O2_rating*CO2_rating)