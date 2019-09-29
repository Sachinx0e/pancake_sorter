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

    def heuristic_cost(self):
        largest_out_of_place_id = 0
        number_of_burnt_pancakes = 0
        for index,pancake in enumerate(self.pancakes_stack):
            # find largest id
            if pancake.id != (index+1) and pancake.id > largest_out_of_place_id:
                largest_out_of_place_id = pancake.id

            # count number of burnt pancakes
            if pancake.orientation == "b":
                number_of_burnt_pancakes = number_of_burnt_pancakes + 1

        return max(largest_out_of_place_id, number_of_burnt_pancakes)

    def flipping_cost(self):
        return self.spatula_position + 1

    def backwards_cost(self):
        # loop and sum actual cost until you reach root node
        flipping_cost_sum = 0
        ref_state = self
        while ref_state.parent is not None:
            flipping_cost_sum =  flipping_cost_sum + ref_state.flipping_cost()
            ref_state = ref_state.parent

        # now ref state is root node, cost is going to be zero, 
        # but we still add this statement for clarity
        flipping_cost_sum = flipping_cost_sum + ref_state.flipping_cost()

        return flipping_cost_sum 

    def total_cost(self):
        return self.backwards_cost() + self.heuristic_cost(); 

    def tie_braking_id(self):
        id_string = "".join(list(map(lambda x: x.tie_braking_id(), self.pancakes_stack)))
        return int(id_string)

    def __lt__(self, other):
        # if both total cost are equal
        if self.total_cost() == other.total_cost():
            # break the tie
            return self.tie_braking_id() < other.tie_braking_id()
        else:
            return self.total_cost() < other.total_cost()
    
    def __eq__(self, other):
        return self.serialize(self.spatula_position,"a") == other.serialize(other.spatula_position,"a")

    def __str__(self):
        #pancakes = list(map(lambda x: str(x), self.pancakes_stack))
        #return "".join(pancakes) + " | p = {}".format(self.spatula_position)
        return self.serialize(self.spatula_position,"a")

    def __repr__(self):
        #pancakes = list(map(lambda x: str(x), self.pancakes_stack))
        #return "".join(pancakes) + " | p = {}".format(self.spatula_position)
        return self.serialize(self.spatula_position,"a")

    def serialize(self,spatula_position, algorithm):
        pancakes = list(map(lambda x: str(x), self.pancakes_stack))
        if spatula_position != -1:
            pancakes.insert(spatula_position+1,"|")
        if algorithm == "a":
            return "".join(pancakes) + " g={}, h={}, f={}".format(self.backwards_cost(), self.heuristic_cost(), self.total_cost())
        else:
            return "".join(pancakes)

