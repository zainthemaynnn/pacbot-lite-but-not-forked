# You can modify this file to implement your own algorithm

from constants import *
from grid import grid
import numpy as np
from enum import Enum
import networkx as nx
import matplotlib.pyplot as plt

START_COORD = (14, 7)
# whether the eulerian tour includes empty intersections.
# I'm trying both. whichever value I submitted was better.
# there's probably a faster way than both though.
WALK_EMPTY_PATHS = False

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


def linear_path(p0, p1):
    """returns all points from p0 to p1"""
    path = []
    direction = (p1[0] - p0[0], p1[1] - p0[1])
    dist = 1e7
    if abs(direction[0]) > 0:
        direction = (abs(direction[0]) / direction[0], 0)
        dist = abs(direction[0])
    else:
        direction = (0, abs(direction[1]) / direction[1])
        dist = abs(direction[1])

    while p0 != p1:
        p0 = (p0[0] + direction[0], p0[1] + direction[1])
        path.append(p0)

    return path


def construct_graph(grid):
    """
    creates a graph based on every point with a turn/intersection
    """

    graph = g = nx.Graph()

    # bfs for graph nodes
    graph.add_node(START_COORD)
    queue = [(START_COORD, adjacent(grid, START_COORD[0], START_COORD[1]))]

    while len(queue) > 0:
        for q in list(queue):
            queue.pop(0)

            o = q[0]
            paths = q[1]

            for d in paths:
                p = o
                t = dvec(d)
                weight = 0

                # update the path length (weight) until it hits a wall/intersection
                while (
                    weight == 0
                    or len(adjacent(grid, p[0], p[1])) == 2
                    and traversible(grid[p[0] + t[0]][p[1] + t[1]])
                ):
                    p = (p[0] + t[0], p[1] + t[1])
                    weight += 1

                if weight == 0 or not WALK_EMPTY_PATHS and grid[p[0]][p[1]] == e:
                    continue

                if not graph.has_node(p):
                    graph.add_node(p)
                    queue.append((p, adjacent(grid, p[0], p[1])))
                graph.add_edge(o, p, weight=weight)

    return graph


def generate_path(graph):
    euler_graph = nx.euler.eulerize(graph)
    euler_path = nx.euler.eulerian_path(euler_graph, source=START_COORD, keys=True)
    return ((int(x), int(y)) for (p, o, _) in euler_path for (x, y) in linear_path(p, o))


"""
You can use the following values from constants.py to check for the type of cell in the grid:
I = 1 -> Wall
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""


def get_next_coordinate(path_gen):
    """
    Calculate the next coordinate for 6ix-pac to move to.
    Check if the next coordinate is a valid move.
    """

    return next(path_gen, None)
