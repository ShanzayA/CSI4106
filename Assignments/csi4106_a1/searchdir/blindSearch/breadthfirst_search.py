from searchdir.node import *
from searchdir.util import *

## This method must implement Breadth-first search (BFS)
## It must return the solution node and the number of visited nodes
def breadthfirst_search(initialState):
    print('BFS------------------------------')
    node = Node(initialState)
    if node.state.isGoal():
        return node.extractSolutionAndDepth()
    frontier = Queue()
    frontier.enqueue(node)
    explored = []
    while True:
        if frontier.isEmpty():
            return node.extractSolutionAndDepth()
        node = frontier.dequeue()
        explored.append(node.state)
        for child in node.expand():
            if not any(st.state.state == child.state for st in frontier.q) and child.state not in explored:
                if child.state.isGoal():
                    return child.extractSolutionAndDepth()
                frontier.enqueue(child)







