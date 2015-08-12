"""
CS325 - Summer 2015
Project 4
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/20/2015
"""

import sys
import ast
import os
import random
import time
from itertools import izip
from itertools import tee
import annealing


def main():
    lines = []
    infile = ""

    try:
        infile = sys.argv[1]
        with open(infile) as f:
            lines = [line.rstrip() for line in f]  # create list of lines from file without newline characters
            lines = filter(None, lines)  # remove blank lines from list
            lines = [line.split() for line in lines]
    except IndexError:
        print "Error: Missing value for filename."
        print "Please use command: python project4.py <filename>"

    nb_iterations = 1
    nb_cities = -1
    cooling_factor = .95
    temperature_start = 1.0e+10
    temperature_end = .1
    time_begin = time.time()
    cities = [annealing.City(line[0], line[1], line[2]) for line in lines]
    
    annealing.compute_distance_pairs(cities)
    random.seed()
    nb_cities = len(cities) if nb_cities <= 0 else nb_cities

    print 'Starting simulated annealing, type CTRL+C to interrupt...'

    cities = cities[:nb_cities]
    (cities_new, distances_current, distances_best, ids_iteration) = annealing.annealing(cities, temperature_start, temperature_end, cooling_factor, nb_iterations)
    time_end = time.time()

    distance_begin = annealing.total_distance(cities)
    distance_end = annealing.total_distance(cities_new)
    print 'Improvement:          %8.0f %%'  % (100 * (distance_begin - distance_end) / distance_begin)
    print 'Time:                 %8.0f sec' % (time_end - time_begin)
    print 'Initial distance:     %8.0f'  % distance_begin
    print 'Optimal distance:     %8.0f'  % distance_end

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
