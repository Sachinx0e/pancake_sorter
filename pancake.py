class Pancake:
    def __init__(self, id, orientation):
        self.id = id
        self.orientation = orientation

    def from_str(pancake_str):
        id = int(pancake_str[0])
        oritentation = pancake_str[1]
        return Pancake(id,oritentation)

    def switch_orientation(pancake):
        orientation = "w"
        if pancake.orientation == "b":
            orientation = "w"
        elif pancake.orientation == "w":
            orientation = "b"
        
        return Pancake(pancake.id,orientation)

    def flip(position, pancakes):
        pancakes_above_position = pancakes[:position+1]
        if len(pancakes) != 0:
            # reverse the list
            pancakes_above_position.reverse()

            # build a new stack of pancakes
            flipped_pancakes = list(map(Pancake.switch_orientation,pancakes_above_position))
            flipped_pancakes.extend(pancakes[position+1:])
            return flipped_pancakes

        else:
            return pancakes[0:]

    def __eq__(self, other):
        if isinstance(other, Pancake):
            return self.id == other.id and self.orientation == other.orientation
        return False

    def __str__(self):
        return str(self.id)+self.orientation

    def __repr__(self):
        return str(self.id)+self.orientation

    
