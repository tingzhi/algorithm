"""
CS325 - Summer 2015
Project 2
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/20/2015
"""

import project2
import sys
import ast
import time
import csv


def main():
    try:
        if len(sys.argv) < 5:
            raise Exception()

        min = int(sys.argv[1])
        max = int(sys.argv[2])
        inc = int(sys.argv[3])
        coins = ast.literal_eval(sys.argv[4])

        filename = "test" + time.strftime("%Y%m%d%-H%M%S") + ".txt"
        f = open(filename, 'w')

        for i in range(min, (max + inc), inc):
            f.write(str(coins) + "\n")
            f.write(str(i) + "\n")

        f.close()

        print "Successfully written to file:", filename

    except Exception as inst:
        if len(inst.args) > 0:
            print "Error: %s" % inst
        else:
            print "Error: Missing value(s) of: minimum, maximum, increment, or list of coins."

        print "Please use command: python project2.py <min> <max> <inc> \"[ <coins> ]\""


if __name__ == '__main__':
    main()
