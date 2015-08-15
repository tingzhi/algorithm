"""
CS325 - Summer 2015
Project 4
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/20/2015
"""

from __future__ import print_function  # compatibility library for print function from Python 3
import math
import random
from anneal import Annealer

import sys
import ast
import os
import random
import time
from itertools import izip
from itertools import tee


def main():
    lines = []
    infile = ''
    first_city = ''
    try:
        infile = sys.argv[1]
        with open(infile) as f:
            lines = [line.rstrip() for line in f]  # remove newline characters & convert to list
            lines = filter(None, lines)  # remove blank lines from list
            lines = [line.split() for line in lines]
            first_city = lines[0][0]
    except IndexError:
        print('Error: Missing value for filename.')
        print('Please use command: python project4.py <filename>')
        exit()

    cities = dict()
    for line in lines:
        if len(line) != 3:
            print('Error: Incorrect input file format')
            exit()
        cities[str(line[0])] = tuple(map(float, line[1:]))  # convert line to dictionary

    # initial state, a randomly-ordered itinerary
    init_state = list(cities.keys())
    random.shuffle(init_state)

    # create a distance matrix
    distance_matrix = {}
    for ka, va in cities.items():
        distance_matrix[ka] = {}
        for kb, vb in cities.items():
            if kb == ka:
                distance_matrix[ka][kb] = 0.0
            else:
                distance_matrix[ka][kb] = distance(va, vb)

    tsp = TravellingSalesmanProblem(init_state, distance_matrix)
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"

    auto_schedule = tsp.auto(minutes=10)
    # {'tmin': ..., 'tmax': ..., 'steps': ...}

    tsp.set_schedule(auto_schedule)
    state, e = tsp.anneal()

    while state[0] != first_city:
        state = state[1:] + state[:1]  # rotate first_city to start
    print("%i mile route:" % e)
    for city in state:
        print("\t", city)

    outfile = infile + ".tour"
    f = open(outfile, 'w')
    f.write(str(e) + '\n')
    for city in state:
        f.write(str(city) + '\n')
    f.close()

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def distance(a, b):
    """Calculate distance between two xy-coordinate locations"""
    x_dist = pow((a[0] - b[0]), 2)
    y_dist = pow((a[1] - b[1]), 2)
    result = math.sqrt(x_dist + y_dist)
    return int(round(result))


class TravellingSalesmanProblem(Annealer):
    """ Annealer for the Traveling Salesman Problem (TSP) """
    
    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TravellingSalesmanProblem, self).__init__(state)  # important! 

    def move(self):
        """Swaps two cities in the route."""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e


if __name__ == '__main__':
    main()
