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
        print "Please use command: python project2.py <filename>"

    filename, extension = os.path.splitext(infile)
    outfile = filename + "change" + extension
    f = open(outfile, 'w')

    for i, line in enumerate(lines):
        coins = ast.literal_eval(line)
        amount = ast.literal_eval(next(lines))

        print "\nSet: %d" % (i + 1)
        print "coins: %s, amount: %d\n" % (coins, amount)

        print "---Greedy Algorithm---"
        change, count = changegreedy(coins, amount)
        print change
        print count

        print "---Brute Force Algorithm---"
        change, count = changeslow(coins, amount)
        print change
        print count

        print "---Dynamic Programming---"
        change, count = changedp(coins, amount)
        print change
        print count

        f.write(str(amount) + ":" + str(count) + "\n")

    f.close()


def changeslow(coins, amount):
    m = 0
    n = len(coins)
    change = [0]*n
    minimum = amount

    if amount > 0:
        for i in range(0, n):
            if amount == coins[i]:
                m += 1
                change[i] += 1
                return change, m

        change = [amount] + [0]*(n-1)

        for i in range(1, amount):
            d = [0]*n
            result1, m1 = changeslow(coins, i)
            result2, m2 = changeslow(coins, amount-i)

            for j in range(0, n):
                d[j] = result1[j] + result2[j]
            m = m1 + m2

            if minimum > m:
                minimum = m
                change = d

    return change, minimum


def changegreedy(coins, amount):
    change = []
    total = 0

    for i in reversed(coins):
        count = amount / i
        total += count
        amount = amount % i
        change.append(count)

    change.reverse()
    return change, total


def changedp(coins, amount):
    size = len(coins)
    sub_coins = [[0] * size] * (amount + 1)
    sub_counts = [0] * (amount + 1)

    for sub_amount in range(1, amount + 1):
        d = [0] * size
        sub_coins[sub_amount] = [0] * size  # reset number of coins

        for i in range(size):
            k = sub_amount - coins[i]
            if k >= 0:
                d[i] = sub_counts[k] + 1
            else:
                d[i] = d[i - 1]

        sub_counts[sub_amount] = d[0]
        index = 0

        for i in range(1, size):
            if d[i] < d[i - 1]:
                sub_counts[sub_amount] = d[i]
                index = i

        k = sub_amount - coins[index]

        for i in range(size):
            if i == index:
                sub_coins[sub_amount][i] = sub_coins[k][i] + 1
            else:
                sub_coins[sub_amount][i] = sub_coins[k][i]

    return sub_coins[amount], sub_counts[amount]


if __name__ == '__main__':
    main()
