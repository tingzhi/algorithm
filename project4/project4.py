"""
CS325 - Summer 2015
Project 4
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/20/2015
"""

import sys
import ast
import os
from annealing import compute_distance
from itertools import izip
from itertools import tee


def main():
    lines = []
    infile = ""

    try:
        infile = sys.argv[1]
        with open(infile) as f:
            #lines = [line for line in f]
            lines = [line.rstrip() for line in f]  # create list of lines from file without newline characters
            lines = filter(None, lines)  # remove blank lines from list
    except IndexError:
            print "Error: Missing value for filename."
            print "Please use command: python project4.py <filename>"

    #outfile = infile + ".tour"
    #f = open(outfile, 'w')

    cities = []
    for line in lines:
        splits = line.split(' ')
        city = {'index': splits[0], 'x': splits[1], 'y': splits[2]}
        cities.append(city)

    for city_x, city_y in pairwise(cities):
        print "city:", city_x['index'],
        print "x:", city_x['x'],
        print "y:", city_x['y']

        print "city:", city_y['index'],
        print "x:", city_y['x'],
        print "y:", city_y['y']

        print "distance:", compute_distance(city_x['x'], city_y['x'], city_x['y'], city_y['y'])
        print ""

    #f.close()

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


if __name__ == '__main__':
    main()
