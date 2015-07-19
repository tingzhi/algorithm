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
    l = [1,10,15,50]
    A = 20
    
    print l,"\n",A
    
    res = changegreedy(l, A)
    print "By using the Greedy Algorithm, the result array is:\n", res[0], "\nThe number of coins costed is:\n", res[1]

    res = changeslow(l, A)
    print "By using the Brute Force Algorithm, the result array is:\n", res[0], "\nThe number of coins costed is:\n", res[1]

    res = changedp(l, A)
    print "By using the Dynamic Programming Method, the result array is:\n", res[0], "\nthe number of coins costed is:\n", res[1]

    
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
    return [c,minm]
        

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


def changedp(l, A):
    n = len(l)
    c = [0]*n
    cc = [[0]*n]*(A+1)
    T = [0]*(A+1)
    for i in range (1,A+1):
        d = [0]*n
        for j in range (0,n):
            k = i - l[j]
            if k >= 0:
                d[j] = T[k] + 1
            else:
                d[j] = d[j-1]
        T[i] = d[0]
        index = 0
        if cc[i][0] == l[1]:
            cc[i][0] = 0
            cc[i][1] += 1
        for j in range(1,n):
            if d[j] < d[j-1]:
                T[i] = d[j]
                index = j
        k = i - l[index]
        cc[i] = cc[k]
        cc[i][0] += 1
        sum = 0
        for count,array in enumerate(cc[i][0:index]):
            sum += (array)*l[count]
        if sum == l[index]:
            for a in range(0,index):
                cc[i][a] = 0
            cc[i][index] += 1

    return [cc[A], T[A]]


if __name__ == '__main__':
    main()
