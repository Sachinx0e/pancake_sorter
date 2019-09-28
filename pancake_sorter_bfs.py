from collections import deque
from treelib import Node, Tree
from state import *
from misc import *

def sort(input_pancakes):
    fringe = deque([])
    tree = Tree()

    # create the root node
    root_state = State(-1,input_pancakes)

    # add the root node to the fringe
    fringe.append(root_state)
    i = 0
    while True:
       i = i + 1
       # if fringe is empty we have failed to find a solution, return None
       if len(fringe) == 0:
           return None
       
       # if fringe is not empty retrieve the latest state node that was inserted
       else:
           #print(",".join(list(map(lambda x: str(x), fringe))))
           state_node = fringe.popleft()
           
           # if the pancakes are sorted return the pancakes
           if is_sorted(state_node.pancakes_stack):
               return state_node.pancakes_stack
           
           # else expand this node
           else:
               child_states  = State.expand(state_node)

               # add child nodes to the fringe
               fringe.extend(child_states)
       

       
     

    
