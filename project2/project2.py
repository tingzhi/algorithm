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
        for coin in change:
            print "%d coins of %d value" % (coin['count'], coin['value'])
        print "count: %d coins\n" % count


        print "---Dynamic Programming---"
        change, count = changedp(coins, amount)
        for coin in change:
            print "%d coins of %d value" % (coin['count'], coin['value'])
        print "count: %d coins\n" % count

        """
        print "---Brute Force Algorithm---"
        change, count = changeslow(coins, amount)
        for coin in change:
            print "%d coins of %d value" % (coin['count'], coin['value'])
        print "count: %d coins\n" % count
        """
    

def changeslow(l, A):

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


def changegreedy(coins, amount):
    coins.sort()
    coins.reverse()
    change = []
    total = 0

    for i in coins:
        count = amount/i
        total += count
        amount = amount%i
        change.append({'count': count, 'value': i})

    return change, total


def changedp(coins, amount):
    coins.sort()
    coins.reverse()
    cache = {0: []}

    print "cache[0]: %s, %d" % (cache[0], sum(cache[0]))

    for i in range(1, amount):
        print i

    for i in coins:
        print i

    """
    n = len(l)
    c = [0]*n
    cc = [[0]*n]*(A+1)
    T = [0]*(A+1)
    for i in range (1,A+1):
        d = [0]*n
        cc[i] = [0]*n
        for j in range (0,n):
            k = i - l[j]
            if k >= 0:
                d[j] = T[k] + 1
            else:
                d[j] = d[j-1]
        T[i] = d[0]
        index = 0
        for x in range(1,n):
            if d[x] < d[x-1]:
                T[i] = d[x]
                index = x
        k = i - l[index]
        for a in range(0,n):
            if a == index:
                cc[i][a] = cc[k][a] + 1
            else:
                cc[i][a] = cc[k][a]
    return cc[A], T[A]
    """

    return [], 0


if __name__ == '__main__':
    main()
