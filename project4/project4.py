"""
CS325 - Summer 2015
Project 4
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/20/2015
"""

import sys
import ast
import os
from annealing import City
from annealing import compute_distance_pairs
from itertools import izip
from itertools import tee


def main():
    lines = []
    infile = ""

    try:
        infile = sys.argv[1]
        with open(infile) as f:
            lines = [line.rstrip() for line in f]  # create list of lines from file without newline characters
            lines = filter(None, lines)  # remove blank lines from list
            lines = [line.split(' ') for line in lines]
    except IndexError:
        print "Error: Missing value for filename."
        print "Please use command: python project4.py <filename>"

    cities = [City(line[0], line[1], line[2]) for line in lines]
    compute_distance_pairs(cities)

    for a, b in pairwise(cities):
        print a
        print b
        print 'distance: %d' % (a.distance_to_city(b))
        print ""

    #outfile = infile + ".tour"
    #f = open(outfile, 'w')
    # put code for processing and writing out to file here
    #f.close()


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


if __name__ == '__main__':
    main()
