import pancake_sorter
from pancake import *

def test_sort_bfs():
    test_pancakes = []
    test_pancakes.append(Pancake(1,"b"))
    test_pancakes.append(Pancake(2,"w"))
    test_pancakes.append(Pancake(4,"b"))
    test_pancakes.append(Pancake(3,"w"))

    sorted_pancake = pancake_sorter.sort_bfs(test_pancakes)

    test_sorted_pacakes = [
        Pancake(1,"w"),
        Pancake(2,"w"),
        Pancake(3,"w"),
        Pancake(4,"w")
    ]

    assert sorted_pancake.pancakes_stack == test_sorted_pacakes


def test_sort_a_star_1():
    test_pancakes = []
    test_pancakes.append(Pancake(2,"b"))
    test_pancakes.append(Pancake(1,"w"))
    test_pancakes.append(Pancake(4,"b"))
    test_pancakes.append(Pancake(3,"w"))

    sorted_pancake = pancake_sorter.sort_a_star(test_pancakes)

    test_sorted_pacakes = [
        Pancake(1,"w"),
        Pancake(2,"w"),
        Pancake(3,"w"),
        Pancake(4,"w")
    ]

    assert sorted_pancake.pancakes_stack == test_sorted_pacakes
