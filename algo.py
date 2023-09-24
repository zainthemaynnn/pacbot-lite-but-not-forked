# You can modify this file to implement your own algorithm

from constants import *
from grid import grid
import numpy as np
from enum import Enum

Direction = Enum("Direction", ["UP", "DOWN", "LEFT", "RIGHT"])

directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]


def traversible(space):
    """whether a space is traversible"""
    return space == o or space == O or space == e or space == c


def adjacent(grid, x, y):
    """returns traversible adjacent spaces"""
    adj = []
    for d in directions:
        t = dvec(d)
        if traversible(grid[x + t[0]][y + t[1]]):
            adj.append(d)
    return adj


def neg(v):
    """negates tuple vector"""
    return (-v[0], -v[1])


def dvec(direction):
    """converts direction to a tuple vector"""
    if direction == Direction.UP:
        return (0, -1)
    elif direction == Direction.DOWN:
        return (0, 1)
    elif direction == Direction.LEFT:
        return (-1, 0)
    else:
        return (1, 0)


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges


class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight


def construct_graph(grid):
    visited = {}
    nodes = []
    edges = []

    nodes.append((1, 1))
    visited[(1, 1)] = True
    queue = [((1, 1), adjacent(grid, 1, 1))]

    while len(queue) > 0:
        for q in list(queue):
            queue.pop(0)
            o = q[0]
            paths = q[1]

            for d in paths:
                p = o
                t = dvec(d)
                weight = 0

                while weight == 0 or len(adjacent(grid, p[0], p[1])) == 2:
                    if not traversible(grid[p[0] + t[0]][p[1] + t[1]]):
                        t = dvec(
                            next(
                                filter(
                                    lambda nd: t != neg(dvec(nd)),
                                    adjacent(grid, p[0], p[1]),
                                )
                            )
                        )
                    p = (p[0] + t[0], p[1] + t[1])
                    weight += 1

                if weight > 0:
                    if not visited.get(p):
                        visited[p] = True
                        nodes.append(p)
                        queue.append((p, adjacent(grid, p[0], p[1])))
                    # probably a faster way to do this, but eh
                    edges.append(Edge(nodes.index(o), nodes.index(p), weight))

    return Graph(nodes, edges)


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
