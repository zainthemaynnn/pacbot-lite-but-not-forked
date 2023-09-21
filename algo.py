# You can modify this file to implement your own algorithm
# The algorithm should return only the next direction in the form of [x, y]

from constants import *

"""
You can use the following values from constants.py to check for the type of cell:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""

def get_next_coordinate(grid, location):
    # modify this algorithm to find the next direction to move in
    # return value in the form of [x, y]
    return location