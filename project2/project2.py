"""
CS325 - Summer 2015
Project 2
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/17/2015
"""

import sys
import re
import ast


def main():
    lines = []
    try:
        with open(sys.argv[1]) as f:
            lines = [line.rstrip() for line in f]  # create list of lines from file without newline characters
            lines = filter(None, lines)  # remove blank lines from list
            lines = iter(lines)  # convert list to iterator to allow iterating over two lines at a time
    except IndexError:
        print "Error: Missing value for filename. Please use command: python project2.py <filename>"

    for i, line in enumerate(lines):
        coins = ast.literal_eval(line)
        amount = ast.literal_eval(next(lines))

        print "Test: %d" % (i + 1)
        print "coins: %s, amount: %d\n" % (coins, amount)

        print "---Greedy Algorithm---"
        change, count = changegreedy(coins, amount)
        print "coins: %s, amount %d\n" % (change, count)


        print "---Dynamic Programming---"
        change, count = changedp(coins, amount)
        print "coins: %s, amount %d\n" % (change, count)

        """
        print "---Brute Force Algorithm---"
        change, count = changeslow(coins, amount)
        for coin in change:
            print "%d coins of %d value" % (coin['count'], coin['value'])
        print "count: %d coins\n" % count
        """

        print "---Brute Force Algorithm---"
        change, count = changeslow(coins, amount)
        print change
        print count


def changeslow(coins, amount):
    min = amount
    change = [0] * len(coins)
    if amount in coins:
        change[coins.index(amount)] += 1
        return change, 1
    else:
        for i in range(1,amount):
            change1, result1 = changeslow(coins, i)
            change2, result2 = changeslow(coins, amount - i)
            result = result1 + result2
            for i in range(0,len(coins)):
                change[i] = change1[i] + change2[i]
            if min > result:
                min = result
    return change, min

'''
    m = 0
    n = len(l)
    c = [0]*n
    minm = A
    if A > 0:
        for i in range(0,n):
            if A == l[i]:
                m += 1
                c[i] += 1
                return [c,m]

        c = [A] + [0]*(n-1)
        for i in range(1,A/2+1):
            d = [0]*n
            m = 0
            result1 = changeslow(l,i)
            for j in range(0,n):
                d[j] += result1[0][j]
            m += result1[1]
            result2 = changeslow(l,A-i)
            for j in range(0,n):
                d[j] += result2[0][j]
            m += result2[1]
            if minm > m:
                minm = m
                c = d
    return c, minm
'''


def changegreedy(coins, amount):
    change = []
    total = 0

    for i in reversed(coins):
        count = amount / i
        total += count
        amount = amount % i
        change.append(count)

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
