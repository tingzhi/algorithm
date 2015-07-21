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
    import argparse

    parser = argparse.ArgumentParser(description='Project 2 generator, tester, results aggregation, and timings.')
    parser.add_argument('-t', '--timing', action='store_true',
                        help='execute timings for changegreedy and changedp algorithms.')
    parser.add_argument('-o', '--output', action='store_true',
                        help='execute algorithms and output results to screen.')
    parser.add_argument('-s', '--save', action='store_true',
                        help='execute algorithms and output results to CSV files.')
    args = parser.parse_args()

    coins1 = [1, 5, 10, 25, 50]  # coins for Problem 4 - V
    coins2 = [1, 2, 6, 12, 24, 48, 60]  # coins for Problem 5 - V1
    coins3 = [1, 6, 13, 37, 150]  # coins for Problem 5 - V2
    coins4 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]  # coins for Problem 6 = V
    amounts1 = [x for x in range(2010, 2205, 5)]
    amounts2 = [x for x in range(2000, 2201, 1)]

    if args.output:
        for amount in amounts1:
            print "\nProblem 4"
            print "coins: %s, amount: %d\n" % (coins1, amount)
            print "---Greedy Algorithm---"
            change, count = project2.changegreedy(coins1, amount)
            print change
            print count
            """
            print "---Brute Force Algorithm---"
            change, count = project2.changeslow(coins1, amount)
            print change
            print count
            """
            print "---Dynamic Programming---"
            change, count = project2.changedp(coins1, amount)
            print change
            print count

        for amount in amounts2:
            print "\nProblem 5, V1"
            print "coins: %s, amount: %d\n" % (coins2, amount)
            print "---Greedy Algorithm---"
            change, count = project2.changegreedy(coins2, amount)
            print change
            print count
            """
            print "---Brute Force Algorithm---"
            change, count = project2.changeslow(coins2, amount)
            print change
            print count
            """
            print "---Dynamic Programming---"
            change, count = project2.changedp(coins2, amount)
            print change
            print count

        for amount in amounts2:
            print "\nProblem 5, V2"
            print "coins: %s, amount: %d\n" % (coins3, amount)
            print "---Greedy Algorithm---"
            change, count = project2.changegreedy(coins3, amount)
            print change
            print count
            """
            print "---Brute Force Algorithm---"
            change, count = project2.changeslow(coins3, amount)
            print change
            print count
            """
            print "---Dynamic Programming---"
            change, count = project2.changedp(coins3, amount)
            print change
            print count

        for amount in amounts2:
            print "\nProblem 6"
            print "coins: %s, amount: %d\n" % (coins4, amount)
            print "---Greedy Algorithm---"
            change, count = project2.changegreedy(coins4, amount)
            print change
            print count
            """
            print "---Brute Force Algorithm---"
            change, count = project2.changeslow(coins4, amount)
            print change
            print count
            """
            print "---Dynamic Programming---"
            change, count = project2.changedp(coins4, amount)
            print change
            print count

    if args.timing:
        with open('timings.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['set'] + ['size'] + ['algorithm'] + ['timing'])


            for i, amount in enumerate(amounts1):
                print "\nProblem 4"
                print "coins: %s, amount: %d\n" % (coins1, amount)
                print "---Greedy Algorithm---"
                t0 = time.time()
                project2.changegreedy(coins1, amount)
                t1 = time.time()
                writer.writerow([i] + [amount] + ['changegreedy'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Brute Force Algorithm---"
                t0 = time.time()
                project2.changeslow(coins1, amount)
                t1 = time.time()
                writer.writerow([i] + ['changeslow'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Dynamic Programming---"
                t0 = time.time()
                project2.changedp(coins1, amount)
                t1 = time.time()
                writer.writerow([i] + ['changedp'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000

            for i, amount in enumerate(amounts2):
                print "\nProblem 5, V1"
                print "coins: %s, amount: %d\n" % (coins2, amount)
                print "---Greedy Algorithm---"
                t0 = time.time()
                project2.changegreedy(coins2, amount)
                t1 = time.time()
                writer.writerow([i] + [amount] + ['changegreedy'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Brute Force Algorithm---"
                t0 = time.time()
                project2.changeslow(coins2, amount)
                t1 = time.time()
                writer.writerow([i] + ['changeslow'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Dynamic Programming---"
                t0 = time.time()
                project2.changedp(coins2, amount)
                t1 = time.time()
                writer.writerow([i] + ['changedp'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000

            for i, amount in enumerate(amounts2):
                print "\nProblem 5, V2"
                print "coins: %s, amount: %d\n" % (coins3, amount)
                print "---Greedy Algorithm---"
                t0 = time.time()
                project2.changegreedy(coins3, amount)
                t1 = time.time()
                writer.writerow([i] + [amount] + ['changegreedy'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Brute Force Algorithm---"
                t0 = time.time()
                project2.changeslow(coins3, amount)
                t1 = time.time()
                writer.writerow([i] + ['changeslow'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Dynamic Programming---"
                t0 = time.time()
                project2.changedp(coins3, amount)
                t1 = time.time()
                writer.writerow([i] + ['changedp'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000

            for i, amount in enumerate(amounts2):
                print "\nProblem 6"
                print "coins: %s, amount: %d\n" % (coins4, amount)
                print "---Greedy Algorithm---"
                t0 = time.time()
                project2.changegreedy(coins4, amount)
                t1 = time.time()
                writer.writerow([i] + [amount] + ['changegreedy'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Brute Force Algorithm---"
                t0 = time.time()
                project2.changeslow(coins4, amount)
                t1 = time.time()
                writer.writerow([i] + ['changeslow'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000
                """
                print "---Dynamic Programming---"
                t0 = time.time()
                project2.changedp(coins4, amount)
                t1 = time.time()
                writer.writerow([i] + ['changedp'] + [(t1 - t0)*1000])
                print "Time: %d" % (t1 - t0)*1000

        print "Timings successfully written to file: timings.csv"

    if args.save:
        with open('results.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['set'] + ['size'] + ['algorithm'] + ['coins'])

            for i, amount in enumerate(amounts1):
                change, count = project2.changegreedy(coins1, amount)
                writer.writerow([i] + [amount] + ['changegreedy'] + [count])
                """
                change, count = project2.changeslow(coins1, amount)
                writer.writerow([i] + [amount] + ['changeslow'] + [count])
                """
                change, count = project2.changedp(coins1, amount)
                writer.writerow([i] + [amount] + ['changedp'] + [count])

            for i, amount in enumerate(amounts2):
                change, count = project2.changegreedy(coins2, amount)
                writer.writerow([i] + [amount] + ['changegreedy'] + [count])
                """
                change, count = project2.changeslow(coins2, amount)
                writer.writerow([i] + [amount] + ['changeslow'] + [count])
                """
                change, count = project2.changedp(coins2, amount)
                writer.writerow([i] + [amount] + ['changedp'] + [count])

            for i, amount in enumerate(amounts2):
                change, count = project2.changegreedy(coins3, amount)
                writer.writerow([i] + [amount] + ['changegreedy'] + [count])
                """
                change, count = project2.changeslow(coins3, amount)
                writer.writerow([i] + [amount] + ['changeslow'] + [count])
                """
                change, count = project2.changedp(coins3, amount)
                writer.writerow([i] + [amount] + ['changedp'] + [count])

            for i, amount in enumerate(amounts2):
                change, count = project2.changegreedy(coins4, amount)
                writer.writerow([i] + [amount] + ['changegreedy'] + [count])
                """
                change, count = project2.changeslow(coins4, amount)
                writer.writerow([i] + [amount] + ['changeslow'] + [count])
                """
                change, count = project2.changedp(coins4, amount)
                writer.writerow([i] + [amount] + ['changedp'] + [count])

        print "Results successfully written to file: results.csv"


if __name__ == '__main__':
    main()
