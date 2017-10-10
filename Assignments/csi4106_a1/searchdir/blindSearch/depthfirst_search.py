from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):
    print('DFS ----------------------------------')

    # Create a start node from the given problem's initial state.
    node = Node(initialState)

    # Create a frontier stack that will hold the successor nodes.
    # Add the start node to the frontier to start exploring.
    # Create an empty list to hold the closed nodes (already explored nodes).
    frontier = Stack()
    frontier.push(node)
    explored = []

    try: 
        # Enter a loop to explore the successor nodes until the goal state is found or no more nodes can be produced.
        while not frontier.isEmpty():
            # Make the current node the next one on the same path,
            # or if reached the end, the node on the next branch
            node = frontier.pop()
            if node.state.isGoal():
                return node, len(explored)
            explored.append(node.state)
            # Generate the successor nodes (possible states from possible actions from current node).
            for child in node.expand():
                if child.state not in explored:
                    frontier.push(child)
    except MemoryError:
        print("Out of memory. Could not continue")

    # Could not find solution. (Left loop because no more successors)
    return False, -1