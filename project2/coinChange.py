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
        
        print "---Brute Force Algorithm---"
        change, count = changeslow(coins, amount)
        print change
        print count

def changeGreedy():
    change = []
    total = 0
    
    for i in range(len(coins)-1 , -1 , -1):
        count = amount/coins[i]
        total += count
        amount = amount % coins[i]
        change.append({'count': count, 'value': i})
    
    return change, total

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


if __name__ == '__main__':
    main()
