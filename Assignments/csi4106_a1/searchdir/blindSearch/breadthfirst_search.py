from searchdir.node import *
from searchdir.util import *

## This method must implement Breadth-first search (BFS)
## It must return the solution node and the number of visited nodes
def breadthfirst_search(initialState):
    print('BFS------------------------------')

    # Create a start node from the given problem's initial state.
    node = Node(initialState)

    # Check this node is not already the goal and return it if yes.
    if node.state.isGoal():
        return node, 0

    # Create a frontier queue that will hold the successor nodes.
    # Add the start node to the frontier to start exploring.
    # Create an empty set to hold the closed nodes (already explored nodes).
    frontier = Queue()
    frontier.enqueue(node)
    explored = set()

    try:
        # Enter a loop to explore the successor nodes until the goal state is found or no more nodes can be produced.
        while not frontier.isEmpty():
            # Make the current node the first in line from the frontier queue. (Will be the shallowest node).
            # Add it to the closed list.
            node = frontier.dequeue()
            explored.add(node.state)

            # Generate the successor nodes (possible states from possible actions from current node).
            for child in node.expand():
                # Check if each successor node is not already in the frontier (since we want min depth)
                # nor in the already explored (closed nodes) list to prevent endless loops.
                if not any(child.state.equals(nd.state) for nd in frontier.show()) and not any(child.state.equals(s) for s in explored):
                    if child.state.isGoal():
                        return child, len(explored)
                    # If the successor was not the goal, add it to the frontier to possibly explore later.
                    frontier.enqueue(child)
    except MemoryError:
        print("Out of memory. Could not continue")

    # Could not find solution. (Left loop because no more successors)
    return False, -1







