from collections import deque
from treelib import Node, Tree
from state import *
from misc import *

def sort_bfs(input_pancakes):
    fringe = deque([])
    tree = Tree()

    # create the root node
    root_state = State(-1,input_pancakes)

    # add the root node to the fringe
    fringe.append(root_state)

    while True:
       # if fringe is empty we have failed to find a solution, return None
       if len(fringe) == 0:
           return None
       
       # if fringe is not empty retrieve the latest state node that was inserted
       else:
           #print(",".join(list(map(lambda x: str(x), fringe))))
           state_node = fringe.popleft()
           
           # if the pancakes are sorted return the pancakes
           if is_sorted(state_node.pancakes_stack):
               return state_node
           
           # else expand this node
           else:
               child_states  = State.expand(state_node)

               # add child nodes to the fringe
               fringe.extend(child_states)


def sort_a_star(input_pancakes):
    fringe = deque([])
    tree = Tree()

    closed_set = []

    # create the root node
    root_state = State(-1,input_pancakes)

    # add the root node to the fringe
    fringe.append(root_state)

    pops = 0

    while True:
       # if fringe is empty we have failed to find a solution, return None
       if len(fringe) == 0:
           return None
       
       # if fringe is not empty retrieve the left most node
       else:
           #print(",".join(list(map(lambda x: str(x), fringe))))
           state_node = fringe.popleft()
           pops = pops + 1
           print ("Number of poped nodes: {}".format(pops), end="\r")
           # if the pancakes are sorted return the pancakes
           if is_sorted(state_node.pancakes_stack):
               return state_node
           
           # else expand this node
           else:
               child_states  = State.expand(state_node)

               # add the note to closed set
               closed_set.append(state_node)
               
               # loop over the children
               for child_state in child_states:
                   # if the child is already in closed set, do nothing
                   if child_state in closed_set:
                       continue
                   else:
                       # if child is not in closed set then add it to the fringe
                       fringe.append(child_state)

                       # sort the fringe according to costs
                       fringe_as_list = list(fringe)
                       fringe_as_list.sort()

                       # turn it back to deque
                       fringe = deque(fringe_as_list)
       

       
     

    
