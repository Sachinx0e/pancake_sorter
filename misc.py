from pancake import *
import re

# Decode pancake string and return list of pancakes and the algorithm choice
def decode_input(input_str):
    # split the string every two characters
    input_tokenized = re.findall("..",input_str)

    # splice the string to get pancakes and the algorithm type 
    pancakes_tokens = input_tokenized[:4]
    algorithm = input_tokenized[4].replace("-","")

    pancakes = list(map(pancake.Pancake.from_str, pancakes_tokens))
    
    return (pancakes, algorithm)

def is_sorted(pancakes_stack):
    test_sorted_pancake = [
        Pancake(1,"w"),
        Pancake(2,"w"),
        Pancake(3,"w"),
        Pancake(4,"w")
    ]

    return pancakes_stack == test_sorted_pancake


