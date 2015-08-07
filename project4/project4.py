"""
CS325 - Summer 2015
Project 2
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
            lines = [line.rstrip() for line in f]  # create list of lines from file without newline characters
            lines = filter(None, lines)  # remove blank lines from list
            lines = iter(lines)  # convert list to iterator to allow iterating over two lines at a time
    except IndexError:
        print "Error: Missing value for filename."
        print "Please use command: python project4.py <filename>"

    outfile = infile + ".tour"
    f = open(outfile, 'w')

    for i, line in enumerate(lines):
        coins = ast.literal_eval(line)
        amount = ast.literal_eval(next(lines))

        print "\nSet: %d" % (i + 1)
        print "coins: %s, amount: %d\n" % (coins, amount)

        print "---Brute Force Algorithm---"
        change, count = changeslow(coins, amount)
        print change
        print count

        f.write(str(amount) + ":" + str(count) + "\n")

    f.close()


def changeslow(coins, amount):
    m = 0
    n = len(coins)
    change = [0]*n
    minimum = amount

    return change, minimum


if __name__ == '__main__':
    main()
