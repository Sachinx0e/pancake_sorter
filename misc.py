from pancake import *
import re

# Decode pancake string and return list of pancakes and the algorithm choice
def decode_input(input_str):
    # split the string every two characters
    input_tokenized = re.findall("..",input_str)

    # splice the string to get pancakes and the algorithm type 
    pancakes_tokens = input_tokenized[:4]
    algorithm = input_tokenized[4].replace("-","")

    pancakes = list(map(Pancake.from_str, pancakes_tokens))
    
    return (pancakes, algorithm)

def is_sorted(pancakes_stack):
    test_sorted_pancake = [
        Pancake(1,"w"),
        Pancake(2,"w"),
        Pancake(3,"w"),
        Pancake(4,"w")
    ]

    return pancakes_stack == test_sorted_pancake


def print_path(state,algorithm):
    path = []

    # walk the path backwards
    ref_node = state
    while ref_node.parent is not None:
        path.append(ref_node)
        ref_node = ref_node.parent

    # now the ref node is root node
    path.append(ref_node)

    # invert the path
    path.reverse()

    # make a path string representation
    state_serialized_list = []
    path_length = len(path)
    for index, state in enumerate(path):
        state_serialized = ""
        # if we are not at the end, get the next the spatula position from the next state
        if index < (path_length - 1):
            next_state = path[index + 1]
            state_serialized = state.serialize(next_state.spatula_position,algorithm)
        
        # if we are at the end spatula postion does not matter
        else:
            state_serialized = state.serialize(-1,algorithm)
        
        state_serialized_list.append(state_serialized)

    # now print everything
    for serialized_state in state_serialized_list:
        print(serialized_state)


