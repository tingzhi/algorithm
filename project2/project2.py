"""
CS325 - Summer 2015
Project 2
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/17/2015
"""

import sys
import re
import ast
import os

def main():
    l = [1,5,10,25,50]
    A = 41
    print l,"\n",A
    
    res = changegreedy(l, A)
    print "By using the Brute Force Algorithm, the result array is:\n", res[0], "\nThe number of coins costed is:\n", res[1]

    res = changeslow(l, A)
    print "By using the Greedy Algorithm, the result array is:\n", res[0], "\nThe number of coins costed is:\n", res[1]

    
def changeslow(l, A):
    m = 0
    n = len(l)
    c = [0]*n
    for i in range(0,n):
        if A == l[i]:
            m += 1
            c[i] += 1
            return [c,m]
    minm = A
    d = [A] + [0]*(n-1)
    for i in range(0,A/2):
        result1 = changeslow(l,i)
        for j in range(0,n):
            d[j] += result1[0][j]
        m += result1[1]
        result2 = changeslow(l,A-i)
        for k in range(0,n):
            d[k] += result2[0][k]
        m += result2[1]
        if minm > m:
            m = minm
            c = d
    return [c,m]
        

def changegreedy(l, A):
    m = 0
    n = len(l)
    c = [0]*n
    for i in range (0,n):
        temp = A
        while temp > 0:
            temp = temp - l[n-1-i]
            if temp >= 0:
                A = temp
                c[n-1-i] += 1
                m += 1
    return [c,m]


if __name__ == '__main__':
    main()
