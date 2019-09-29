from state import *
from pancake import *

def test_heuristic_cost_1():
    state = State(-1, [
        Pancake(2,"b"),
        Pancake(3,"w"),
        Pancake(1,"b"),
        Pancake(4,"w"),
    ])

    heuristic_cost = state.heuristic_cost()

    assert heuristic_cost == (3)

def test_heuristic_cost_2():
    state = State(-1, [
        Pancake(1,"b"),
        Pancake(2,"b"),
        Pancake(3,"b"),
        Pancake(4,"b"),
    ])

    heuristic_cost = state.heuristic_cost()

    assert heuristic_cost == 4


def test_total_cost():
    root_state = State(-1, [
        Pancake(2,"b"),
        Pancake(3,"w"),
        Pancake(1,"b"),
        Pancake(4,"w"),
    ])

    state_1 = State(0, [
        Pancake(2,"b"),
        Pancake(3,"w"),
        Pancake(1,"b"),
        Pancake(4,"w"),
    ],parent=root_state)

    state_2 = State(2, [
        Pancake(2,"b"),
        Pancake(3,"w"),
        Pancake(1,"b"),
        Pancake(4,"w"),
    ],parent=state_1)


    state_3 = State(3, [
        Pancake(2,"b"),
        Pancake(3,"w"),
        Pancake(1,"b"),
        Pancake(4,"w"),
    ],parent=state_2)

    total_cost = state_3.total_cost()

    assert total_cost == 11


def test_state_sort():
    states = []
    root_state = State(-1, [
        Pancake(4,"b"),
        Pancake(2,"w"),
        Pancake(3,"b"),
        Pancake(4,"w"),
    ])
    print(root_state.total_cost())
    states.append(root_state)

    state_1 = State(-1, [
        Pancake(4,"b"),
        Pancake(3,"w"),
        Pancake(1,"b"),
        Pancake(2,"w"),
    ])
    states.append(state_1)

    state_2 = State(-1, [
        Pancake(1,"b"),
        Pancake(2,"w"),
        Pancake(3,"b"),
        Pancake(4,"w"),
    ])
    print(state_2.total_cost())
    states.append(state_2)

    states.sort()

    assert states[0] == state_2




