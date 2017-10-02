## Author: Amal Zouaq
### azouaq@uottawa.ca
### Author: Hadi Abdi Ghavidel
###habdi.cnlp@gmail.com

from operator import attrgetter

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
        if self.q == []:
            return True
        else:
            return False

    # add the element item to the current data structure
    def enqueue(self, item):
        self.q.append(item)

    # removes an element from the current data structure
    def dequeue(self):
        self.q = self.q[1:]

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.q)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.q


#Priority Queue Implementation of the data structure PriorityQueue
class PriorityQueue:
    # initializes the data structure
    def __init__(self, fct):
        print("test")
    # TO COMPLETE

    # returns the elements of the current data structure
    def show(self):
        print("test")
    # TO COMPLETE

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        print("test")
    # TO COMPLETE

    # add the element item to the current data structure
    def enqueue(self, item):
        print("test")
    # TO COMPLETE

    # removes an element from the current data structure
    def dequeue(self):
        print("test")
    # TO COMPLETE

    # returns the size of the current data structure (the number of elements)
    def size(self):
        print("test")
    # TO COMPLETE

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        print("test")
    # TO COMPLETE

#Stack - Implementation of the data structure Stack
class Stack:
    # initializes the data structure
    def __init__(self):
        print("test")
    # TO COMPLETE

    # returns the elements of the current data structure
    def show(self):
        print("test")
    # TO COMPLETE

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        print("test")
    # TO COMPLETE

    # add the element item to the current data structure
    def push(self, item):
        print("test")
    # TO COMPLETE

    # removes an element from the current data structure
    def pop(self):
        print("test")
    # TO COMPLETE

    # returns the size of the current data structure (the number of elements)
    def size(self):
        print("test")
    # TO COMPLETE

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        print("test")
    # TO COMPLETE


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
