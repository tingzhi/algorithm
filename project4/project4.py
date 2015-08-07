"""
CS325 - Summer 2015
Project 4
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/20/2015
"""

import sys
import ast
import os


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

    outfile = infile + ".tour"
    f = open(outfile, 'w')

    cities = []
    for line in lines:
        splits = line.split(' ')
        city = {'name': splits[0], 'x': splits[1], 'y': splits[2]}
        cities.append(city)

    for city in cities:
        print "name:", city['name'],
        print "x:", city['x'],
        print "y:", city['y']

    f.close()


def changeslow(coins, amount):
    m = 0
    n = len(coins)
    change = [0]*n
    minimum = amount

    return change, minimum


if __name__ == '__main__':
    main()
