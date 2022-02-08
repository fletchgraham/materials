"""Fletcher investigating the Sudoku graph problem."""

from collections import deque

puzzle = """
1 2 3 4
3 4 1 2 
2 1 4 3 
4 3 2 1
"""

puzzle = puzzle.replace('\n', '')
puzzle = puzzle.replace(' ', '')

print(puzzle)

my_graph = {
    0: [1,2,3,4,8,12,5],
    1: [0,2,3,]
}

test_deque = ['hey', 'cool', 'guy']

print(test_deque.pop())