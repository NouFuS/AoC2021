import copy
from pprint import pprint
import itertools

#inputs = open("inputs_day8_test.txt", "r")
#inputs = open("inputs_day8_test2.txt", "r")
inputs = open("inputs_day8.txt", "r")

lines = inputs.readlines()

separated_inputs = []
for line in lines:
    p1 = []
    p2 = []
    full_p1, full_p2 = line.split(" | ")

    for value in full_p1.split():
        p1.append(value)
    
    for value in full_p2.split():
        p2.append(value)
    
    separated_inputs.append([p1, p2])

transcription = {}
transcription.update({"abcefg":0})
transcription.update({"cf":1})
transcription.update({"acdeg":2})
transcription.update({"acdfg":3})
transcription.update({"bcdf":4})
transcription.update({"abdfg":5})
transcription.update({"abdefg":6})
transcription.update({"acf":7})
transcription.update({"abcdefg":8})
transcription.update({"abcdfg":9})

candidate_mappings = []
letters = ["a", "b", "c", "d", "e", "f", "g"]
candidate_mappings = []
permut = itertools.permutations(letters, len(letters))
for comb in permut:
    mapping = {}
    for key, value in zip(comb, letters):
        mapping.update({key:value})
    candidate_mappings.append(mapping)

total = 0

# Test consistency of all mappings
for p1, p2 in separated_inputs:
    valid_mapping = None
    i = 0
    while valid_mapping is None:
        test_mapping = candidate_mappings[i]
        test_transcription = {}
        for key, value in transcription.items():
            new_key = ""
            for digit in key:
                new_key += test_mapping[digit]
            new_key = "".join(sorted(new_key))
            test_transcription.update({new_key:value})


        # Now evaluate the transcription to check that we have the 10 unique numbers
        decoded_numbers = set()
        
        for number in p1:
            input_test = "".join(sorted(number))
            if input_test in test_transcription.keys():
                decoded_numbers.add(test_transcription[input_test])
        
        if len(decoded_numbers) == 10:
            valid_mapping = test_mapping
            
        i += 1
    
    # Inverting the key/values because I messed up above and am too lazy to fix the root issue
    valid_mapping = {v: k for k, v in valid_mapping.items()}
        
    
    full_nb = ""
    for value in p2:
        decoded = ""
        for digit in value:    
            decoded += valid_mapping[digit]
        full_nb += str(transcription["".join(sorted(decoded))])
        
    total += int(full_nb)
    
print("Total:", total)

