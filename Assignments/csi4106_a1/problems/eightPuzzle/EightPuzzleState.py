### Author: Amal Zouaq
### azouaq@uottawa.ca
## Author: Hadi Abdi Ghavidel
## habdi.cnlp@gmail.com

import timeit

import numpy as np
import random
import math
from searchdir.blindSearch.breadthfirst_search import *
from searchdir.blindSearch.depthfirst_search import *
from searchdir.heuristicSearch.astar_search import *
from searchdir.state import *


class EightPuzzleState(State):

    #initializes the eight puzzle with the configuration passed in parameter (numbers)
    def __init__(self, numbers):
        self.state = numbers


    #returns a boolean value that indicates if the current configuration is the same as the goal configuration
    def isGoal(self):
        return self.state == [0, 1, 2, 3, 4, 5, 6, 7, 8]


    # returns the set of legal actions in the current state
    def possibleActions(self):
        possibleactions = []
        #depending on where the blank node is, return the possible actions
        if self.state.index(0) < 6:
            possibleactions.append('down')
        if self.state.index(0) > 2:
            possibleactions.append('up')
        if self.state.index(0) not in (2,5,8):
            possibleactions.append('right')
        if self.state.index(0) not in (0,3,6):
            possibleactions.append('left')
        return possibleactions


    # applies the result of the move on the current state
    def executeAction(self, move):
        blankIndex = self.state.index(0) #index of the blank node

        # switch the values of the blank node and the node of its direction
        if move == 'down':
            self.state[blankIndex], self.state[blankIndex + 3] = self.state[blankIndex + 3], self.state[blankIndex]
        elif move == 'up':
            self.state[blankIndex], self.state[blankIndex - 3] = self.state[blankIndex - 3], self.state[blankIndex]
        elif move == 'right':
            self.state[blankIndex], self.state[blankIndex + 1] = self.state[blankIndex + 1], self.state[blankIndex]
        elif move == 'left':
            self.state[blankIndex], self.state[blankIndex - 1] = self.state[blankIndex - 1], self.state[blankIndex]
        # if move == None: #unnecessary?
        #     pass


    # returns true if the current state is the same as other, false otherwise
    def equals(self, other):
        return self.state == other.state


    # prints the grid representing the current state
    # e.g. -----------
        # |   | 1 | 2 |
        # -----------
        # | 3 | 4 | 5 |
        # -----------
        # | 6 | 7 | 8 |
        # -----------
    def show(self):
        print("-----------")
        for index, number in enumerate(self.state):
            if number != 0:
                print("|", number, end=" ")
            else:
                print("|", " ", end=" ")
            if index in (2, 5, 8):
                #print a next line if at end of line
                print("|")
                print("-----------")


    # returns the cost of the action in parameter
    def cost(self, action):
        return 1 # The cost should always be one here?


    # returns the value of the heuristic for the current state
    # note that you can alternatively call heuristic1() and heuristic2() to test both heuristics with A*
    def heuristic(self):
        # Matrix is the (x,y) position values at each 0-8 position within the list.
        # The (x,y) position could also be calculated inside the heuristic function based on the position within the list.
        matrix = [(0,2), (1,2), (2,2), (0,1), (1,1), (2,1), (0,0), (1,0), (2,0)]
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #return self.heuristic1(matrix, goal)
        return self.heuristic2(matrix, goal)


    ## returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic1(self, matrix, goal):
        #Straight line distance. Could have also tried misplaced tiles, but straight line is a closer heuristic
        distance = 0
        # For each element in the list, get the (x,y) position of it provided in matrix.
        # Then get the (x,y) position of where the current tile should be at goal.
        # Use these two positions to get the straight line distance. Add all these distances to get a total distance.
        for i in range(9):
            tilePosition = matrix[i]
            goalPosition = matrix[goal.index(self.state[i])]
            distance += math.sqrt(pow(tilePosition[0] - goalPosition[0], 2) + pow(tilePosition[1] - goalPosition[1], 2))
        return distance

    # returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic2(self, matrix, goal):
        # Manhattan distance
        distance = 0
        #For each element in the list, get the (x,y) position of it provided in matrix.
        #Then get the (x,y) position of where the current tile should be at goal.
        #Use these two positions to get the Manhatten distance. Add all these distances to get a total distance.
        for i in range(9):
            tilePosition = matrix[i]
            goalPosition = matrix[goal.index(self.state[i])]
            distance += abs(tilePosition[0] - goalPosition[0]) + abs(tilePosition[1] - goalPosition[1])
        return distance

    def shuffle_ran(self, board, moves):
        newState = board
        if moves == 100:
            return newState
        else:
            newState.executeAction(random.choice(list(board.possibleActions())))
            moves = moves + 1
            return self.shuffle_ran(newState, moves)

####################### SOLVABILITY ###########################

def issolvable(puzzle):
    puzzle_str = np.array(list(map(int, puzzle)))
    print("Puzzle string: ", puzzle_str)
    if inversions(puzzle_str) % 2:
        return False
    else:
        return True

def inversions(s):
    k = s[s != 0]
    return sum(
        len(np.array(np.where(k[i + 1:] < k[i])).reshape(-1))
        for i in range(len(k) - 1)
    )

def randomize(puzzle):
    puzzle = puzzle.shuffle_ran(puzzle, 1)
    puzzle_choice = []
    for sublist in puzzle.cells:
        for item in sublist:
            puzzle_choice.append(item)
    return puzzle, puzzle_choice

#######  SEARCH ###########################
EIGHT_PUZZLE_DATA = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 8, 7, 6],
                     [4, 0, 6, 1, 2, 8, 7, 3, 5],
                     [1, 2, 8, 7, 3, 4, 5, 6, 0],
                     [5, 1, 3, 4, 0, 2, 7, 6, 8],
                     [1, 2, 5, 7, 6, 8, 0, 4, 3],
                     [4, 6, 0, 7, 2, 8, 3, 1, 5]]

puzzle_choice = EIGHT_PUZZLE_DATA[6]
puzzle = EightPuzzleState(puzzle_choice)
#puzzle, puzzle_choice = randomize(puzzle)
print('Initial Config')
puzzle.show()
if not issolvable(puzzle_choice):
    print("NOT SOLVABLE")
else:
    start = timeit.default_timer()
    solution, nbvisited = breadthfirst_search(puzzle)
    stop = timeit.default_timer()
    printResults('BFS', solution, start, stop, nbvisited)

    start = timeit.default_timer()
    solution, nbvisited = depthfirst_search(puzzle)
    stop = timeit.default_timer()
    printResults('DFS', solution, start, stop, nbvisited)

    start = timeit.default_timer()
    solution, nbvisited = astar_search(puzzle)
    stop = timeit.default_timer()
    printResults('A*', solution, start, stop, nbvisited)

    # Uncomment to print visual of solution. (Called here uses solution from A*)
    # printSolutionVisual(puzzle, solution)

