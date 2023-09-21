# You can modify this file to implement your own algorithm

from constants import *

"""
You can use the following values from constants.py to check for the type of cell in the grid:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""

def get_next_coordinate(grid, location):

    """
    Calculate the next coordinate for 6ix-pac to move to.
    Check if the next coordinate is a valid move.

    Parameters:
    - grid (list of lists): A 2D array representing the game board.
    - location (list): The current location of the 6ix-pac in the form (x, y).

    Returns:
    - list or tuple: 
        - If the next coordinate is valid, return the next coordinate in the form (x, y) or [x,y].
        - If the next coordinate is invalid, return None.
    """
    
    return location