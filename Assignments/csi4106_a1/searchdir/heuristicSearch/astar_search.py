
from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue

## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
    print('A* ------------------------------------')

    # Create a start node from the given problem's initial state.
    node = Node(initialState)

    #Create a frontier priority queue that will hold the successor nodes.
    #Add the start node to the frontier to start exploring.
    #Create an empty list to hold the closed nodes (already explored nodes).
    frontier = PriorityQueue(priority)
    frontier.enqueue(node)
    explored = []

    try: #**To move this try inside, when adding to frontier
        # Enter a loop to explore the successor nodes until the goal state is found or no more nodes can be produced.
        while not frontier.isEmpty():
            # Make the current node the next one in the frontier
            node = frontier.dequeue()
            if node.state.isGoal():
                return node, len(explored)
            explored.append(node.state)
            # Generate the successor nodes (possible states from possible actions from current node).
            for child in node.expand():
                for nd in frontier.q:
                    if child.state.state == nd.state.state and child.f < nd.f:
                        frontier.q.remove(nd)
                if not any(nd.state.state == child.state.state for nd in frontier.q) and child.state not in explored:
                    frontier.enqueue(child)
    except MemoryError:
        print("Out of memory. Could not continue")


#Used for determining how to sort priority queue
def priority(item):
    # the priority is the f value: i.e. the cost of the node so far (g) + the estimate distance to the goal (h)
    return item.f
