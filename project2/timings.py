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
    file_name = "project2.csv"

    try:
        if len(sys.argv) < 5:
            raise Exception()

        min = int(sys.argv[1])
        max = int(sys.argv[2])
        inc = int(sys.argv[3])
        coins = ast.literal_eval(sys.argv[4])

        with open(file_name, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['size'] + ['algorithm'] + ['timing'])

            for i in range(min, (max + inc), inc):
                t0 = time.time()
                project2.changegreedy(coins, i)
                t1 = time.time()
                writer.writerow([i] + ['changegreedy'] + [(t1 - t0)*1000])

                t0 = time.time()
                project2.changedp(coins, i)
                t1 = time.time()
                writer.writerow([i] + ['changedp'] + [(t1 - t0)*1000])

                #t0 = time.time()
                #project2.changeslow(coins, i)
                #t1 = time.time()
                #writer.writerow([i] + ['changeslow'] + [(t1 - t0)*1000])

        print "Successfully written to file:", file_name

    except Exception as inst:
        if len(inst.args) > 0:
            print "Error: %s" % inst
        else:
            print "Error: Missing value(s) of: minimum, maximum, increment, or list of coins."

        print "Please use command: python project2.py <min> <max> <inc> \"[ <coins> ]\""


if __name__ == '__main__':
    main()
