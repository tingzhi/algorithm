"""
CS325 - Summer 2015
Project 1
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/9/2015
"""

import sys


def enumeration(l):
    n = len(l)
    maximum = l[0]
    start_idx = end_idx = 0

    for i in range(0,n):
        for j in range(i,n):
            summation = 0
            for k in range(i,j):
                if j > i:
                    summation += l[k]
                else:
                    summation = l[i]

            if summation > maximum:
                maximum = summation
                start_idx = i
                end_idx = j
    return dict(subarray=l[start_idx:end_idx], maxsum=maximum)


def linear(l):
    best = cur = cur_idx = start_idx = best_idx = 0

    for i, val in enumerate(l):
        if cur + val > 0:
            cur += val
        else:
            cur = 0
            cur_idx = i + 1

        if cur > best:
            start_idx = cur_idx
            best_idx = i + 1
            best = cur

    return dict(subarray=l[start_idx:best_idx], maxsum=best)


# these are just examples for validating that the methods above don't blow up!
b = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

print "---enumeration---"
res = enumeration(b)
print "subarray: ", res['subarray']
print "max sum: ", res['maxsum']

print "\n---linear---"
res = linear(b)
print "subarray: ", res['subarray']
print "max sum: ", res['maxsum']