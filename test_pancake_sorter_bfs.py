import pancake_sorter_bfs as bfs
from pancake import *

def test_sort():
    test_pancakes = []
    test_pancakes.append(Pancake(2,"b"))
    test_pancakes.append(Pancake(1,"w"))
    test_pancakes.append(Pancake(4,"b"))
    test_pancakes.append(Pancake(3,"w"))

    sorted_pancake = bfs.sort(test_pancakes)

    test_sorted_pacakes = [
        Pancake(1,"w"),
        Pancake(2,"w"),
        Pancake(3,"w"),
        Pancake(4,"w")
    ]

    assert sorted_pancake == test_sorted_pacakes
