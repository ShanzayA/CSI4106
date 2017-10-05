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
            return node, len(explored)
        node = frontier.dequeue()
        explored.append(node.state)

        #Check the possible child nodes (in other words, the child state is a successor or the possible future states)
        for child in node.expand():
            #Check child state is not in the frontier already (since we want min depth), nor has it already been explored
            if not any(st.state.state == child.state.state for st in frontier.q) and child.state not in explored:
                if child.state.isGoal():
                    return child, len(explored)
                #if the child is not the goal, add to frontier
                frontier.enqueue(child)







