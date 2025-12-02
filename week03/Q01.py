#PROJECT 3 WEEK 3 M.S

##1

# print("PARSA PARTOVI PRESENTS".center(100 , "-"))

import itertools
import copy

user_input = input("Enter a sentence or some words(more than one word): ")
words = user_input.split()

def generate_amalgamations(words) :
    for range in [2, 3, 4]:
        for combination in itertools.permutations(words, range):
            yield " ".join(combination)

amalgamations = list(generate_amalgamations(words))
print(" Original amalgamations list:")
print(amalgamations)

shallow_copy = amalgamations.copy()

deep_copy = copy.deepcopy(amalgamations)

amalgamations[0] = "maktab137"

print(" After changing:")
print("Original:", amalgamations)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)