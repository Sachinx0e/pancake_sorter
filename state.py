from pancake import *

class State:
    
    def __init__(self,spatula_position, pancakes_stack, parent=None):
        self.parent = parent
        self.spatula_position = spatula_position
        self.pancakes_stack = pancakes_stack
 
    def expand(state):
        
        expanded_states = []

        for spatula_position in range(0,4):
            if spatula_position != state.spatula_position:
                flipped_pancakes = Pancake.flip(spatula_position,state.pancakes_stack)
                new_state = State(spatula_position, flipped_pancakes, parent=state)
                expanded_states.append(new_state)

        return expanded_states

    def __str__(self):
        pancakes = list(map(lambda x: str(x), self.pancakes_stack))
        if self.spatula_position == -1:
            return '|' + "".join(pancakes)
        else:
            pancakes.insert(self.spatula_position + 1, "|")
            return "".join(pancakes)

    def __repr__(self):
        pancakes = list(map(lambda x: str(x), self.pancakes_stack))
        if self.spatula_position == -1:
            return '|' + "".join(pancakes)
        else:
            pancakes.insert(self.spatula_position + 1, "|")
            return "".join(pancakes)