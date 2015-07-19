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
    A = 192
    print l,"\n",A
    res = changegreedy(l, A)
    print "The result array is:\t", res[0], "\nmin number of coins:\t", res[1]
    os.system("pause")

def changegreedy(l, A):
    m = 0
    n = len(l)
    c = [0]*n
    for i in range(0,n-1):
        temp = A
        while temp > 0 :
            temp = temp - l[n-1-i]
            if temp >= 0 :
                A = temp
                c[i] += 1
                m += 1
    return [c,m]

if __name__ == '__main__':
    main()
