## Author: Amal Zouaq
### azouaq@uottawa.ca
### Author: Hadi Abdi Ghavidel
###habdi.cnlp@gmail.com

from operator import attrgetter
import heapq

#Queue - Implementation of the data structure Queue
class Queue:
    # initializes the current data structure
    def __init__(self):
        self.q = []

    # returns the elements of the current data structure
    def show(self):
        return self.q

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return self.q == []

    # add the element item to the current data structure
    def enqueue(self, item):
        self.q.append(item)

    # removes an element from the current data structure
    def dequeue(self):
        first = self.q[0]
        self.q = self.q[1:]
        return first

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.q)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.q


#**Is it okay to use heapq to implement? Or are we to implement it from scratch
#Priority Queue Implementation of the data structure PriorityQueue
class PriorityQueue:
    # initializes the data structure
    def __init__(self, fct):
        self.q = []
        self.priority = fct

    # returns the elements of the current data structure
    def show(self):
        return self.q

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return self.q == []

    # add the element item to the current data structure
    def enqueue(self, item):
        self.q.append(item)

        # heap sort implemented with heapq (is this okay?), so that it will be done in O(logn)
        heap = []
        for node in self.q:
            heapq.heappush(heap, (self.priority(node), node))
        sorted = []
        for i in range(len(heap)):
            sorted.append(heapq.heappop(heap)[1])
        self.q = sorted

    # removes an element from the current data structure
    def dequeue(self):
        first = self.q[0]
        self.q = self.q[1:]
        return first

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.q)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.q

#Stack - Implementation of the data structure Stack
class Stack:
    # initializes the data structure
    def __init__(self):
        self.s = []

    # returns the elements of the current data structure
    def show(self):
        return self.s

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return self.s == []

    # add the element item to the current data structure
    def push(self, item):
        self.s.insert(0, item)

    # removes an element from the current data structure
    def pop(self):
        first = self.s[0]
        self.s = self.s[1:]
        return first

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.s)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.s


#Prints results for search alorithms
def printResults(alg, solution, start, stop, nbvisited):
    try:
        result, depth = solution.extractSolutionAndDepth()
        if result != []:
            print("The Solution is  ", (result))
            print("The Solution is at depth ", depth)
            print("The path cost is ", solution.getcost())
            print('Number of visited nodes:', nbvisited)
            time = stop - start
            print("The execution time is ", time, "seconds.")
            print("Done!")
    except AttributeError:
        print("No solution")
    except MemoryError:
        print("Memory Error!")

def printSolutionVisual(puzzle, solution):
    sol = solution.extractSolution()
    puzzle.show()
    for step in sol:
        puzzle.executeAction(step)
        puzzle.show()