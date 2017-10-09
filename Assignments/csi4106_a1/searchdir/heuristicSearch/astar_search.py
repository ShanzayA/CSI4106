
from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue

## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
    print('A* ------------------------------------')

    # Create a start node from the given problem's initial state.
    node = Node(initialState)

    # Check this node is not already the goal and return it if yes.
    if node.state.isGoal():
        return node, 0

    #Create a frontier priority queue that will hold the successor nodes.
    #Add the start node to the frontier to start exploring.
    #Create an empty list to hold the closed nodes (already explored nodes).
    frontier = PriorityQueue()
    frontier.enqueue(node)
    closed = []