import sys
import misc
import pancake_sorter

def main(input_str):
    pancakes, algorithm = misc.decode_input(input_str)  
    if algorithm == "a":
        state = pancake_sorter.sort_a_star(pancakes)
        misc.print_path(state, algorithm)
    elif algorithm ==  "b":
        state = pancake_sorter.sort_bfs(pancakes)
        misc.print_path(state, algorithm)
    else:
        print("Unknown algorithm {}".format(algorithm))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input string in the format : 1w3b4w2a-a")
    else:
        main(sys.argv[1])