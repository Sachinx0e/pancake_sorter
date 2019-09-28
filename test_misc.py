import misc
from pancake import *

def test_decode_input():
    input_str = "2b1w4b3w-a"
    pancakes, algorithm = misc.decode_input(input_str)  

    test_pancakes = []
    test_pancakes.append(Pancake(2,"b"))
    test_pancakes.append(Pancake(1,"w"))
    test_pancakes.append(Pancake(4,"b"))
    test_pancakes.append(Pancake(3,"w"))

    # assert that pancakes are decoded properly
    assert len(pancakes) == 4
    assert pancakes == test_pancakes

    # assert that algorithm is decoded properly
    assert algorithm == "a"
    