from pancake import *

def test_flip():
    pancakes = []
    pancakes.append(Pancake(2,"b"))
    pancakes.append(Pancake(1,"w"))
    pancakes.append(Pancake(4,"b"))
    pancakes.append(Pancake(3,"w"))

    flipped_panckaes = Pancake.flip(2,pancakes)

    test_flipped_pancakes = [
        Pancake(4,"w"),
        Pancake(1,"b"),
        Pancake(2,"w"),
        Pancake(3,"w")
    ]

    assert flipped_panckaes == test_flipped_pancakes


